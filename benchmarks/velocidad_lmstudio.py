"""Benchmark rápido de velocidad y consumo en LM Studio (uso interno, rama develop).

Para cada modelo y cada reparto GPU/CPU: carga el modelo con `lms load --gpu`, envía la misma
pregunta por el API local de LM Studio, mide tokens/s (stats del API) y muestrea el consumo de la
GPU con nvidia-smi durante la generación. Escribe benchmarks/resultados/velocidad_lmstudio.csv.

Uso:  .venv/bin/python benchmarks/velocidad_lmstudio.py
"""
import csv, json, statistics, subprocess, threading, time, urllib.request
from pathlib import Path

LMS = "/opt/ai/lmstudio/bin/lms"
PORT = 1235
URL = f"http://127.0.0.1:{PORT}/api/v0/chat/completions"
MODELOS = ["google/gemma-4-26b-a4b-qat", "qwen/qwen3.8-27b"]
REPARTOS = [("GPU completa", "max"), ("Mitad GPU", "0.5"), ("Solo CPU", "off")]
PROMPT = "Explica en tres frases qué es un modelo de lenguaje open weights."
OUT = Path(__file__).resolve().parent / "resultados" / "velocidad_lmstudio.csv"


def sh(*a, timeout=600):
    return subprocess.run(a, capture_output=True, text=True, timeout=timeout)


def watts(stop, samples):
    while not stop.is_set():
        r = sh("nvidia-smi", "--query-gpu=power.draw", "--format=csv,noheader,nounits", timeout=10)
        try:
            samples.append(float(r.stdout.strip()))
        except ValueError:
            pass
        time.sleep(0.25)


def pedir(model, n_tokens):
    body = json.dumps({"model": model, "messages": [{"role": "user", "content": PROMPT}],
                       "temperature": 0, "max_tokens": n_tokens, "stream": False}).encode()
    req = urllib.request.Request(URL, body, {"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req, timeout=1800))


def main():
    sh(LMS, "server", "start", "-p", str(PORT))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    filas = []
    for m in MODELOS:
        for nombre, gpu in REPARTOS:
            sh(LMS, "unload", "--all")
            r = sh(LMS, "load", m, "--gpu", gpu, "-c", "4096", "--identifier", "bench", "-y", timeout=900)
            if r.returncode:
                print("no se pudo cargar", m, gpu, r.stderr[-300:]); continue
            pedir("bench", 8)                                   # precalentar
            idle = float(sh("nvidia-smi", "--query-gpu=power.draw", "--format=csv,noheader,nounits").stdout.strip())
            stop, samples = threading.Event(), []
            t = threading.Thread(target=watts, args=(stop, samples)); t.start()
            res = pedir("bench", 300 if gpu != "off" else 150)
            stop.set(); t.join()
            st = res.get("stats", {})
            fila = {"modelo": m, "reparto": nombre, "gpu_offload": gpu,
                    "tok_s": round(st.get("tokens_per_second", 0), 1),
                    "ttft_s": round(st.get("time_to_first_token", 0), 2),
                    "tokens": res.get("usage", {}).get("completion_tokens"),
                    "gpu_w_prom": round(statistics.mean(samples), 0) if samples else None,
                    "gpu_w_reposo": idle}
            print(fila); filas.append(fila)
    sh(LMS, "unload", "--all")
    with OUT.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0])); w.writeheader(); w.writerows(filas)
    print("->", OUT)


if __name__ == "__main__":
    main()
