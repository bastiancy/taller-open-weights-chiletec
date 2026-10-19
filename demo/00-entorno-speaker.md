# Entorno del PC de la demo (verificado el 18 oct 2026)

Solo para el speaker (rama `develop`).

## Hardware

| Componente | Detalle |
|---|---|
| GPU | NVIDIA GeForce RTX 3090, 24 GB VRAM (driver 595.99.02, CUDA 13.2) |
| CPU | Intel Core i9-12900K, 24 hilos |
| RAM | 61 GiB (+14 GiB swap) |
| Disco | 696 GB libres |
| Escritorio en reposo | ~0,45 GB de VRAM ocupados (GNOME, Firefox, etc.) |

## Software

| Programa | Versión | Notas |
|---|---|---|
| Ollama | 0.31.2 | Servicio systemd. **Escucha en `127.0.0.1:1234`** (no en el estándar 11434), modelos en `/opt/ollama/models`, `OLLAMA_KEEP_ALIVE=-1` (los modelos nunca se descargan solos de la VRAM) |
| LM Studio | 0.4.26 | Datos en `/opt/ai/lmstudio`, CLI `lms` en `/opt/ai/lmstudio/bin`. Servidor apagado |
| Python | 3.12.13 (pyenv) | Entorno en `.venv/` creado con `uv`, dependencias en `requirements.txt` |
| Monitor de GPU | `nvitop` (en `.venv`) | Reemplaza a `nvtop`, que no está instalado (requiere `sudo apt install nvtop`) |

## Modelos disponibles

**LM Studio** (GGUF):
- Qwen3.8-27B Q4_K_M (16,8 GB) + mmproj (multimodal)
- Qwen3-30B-A3B Q4_K_M (18,6 GB) — MoE
- gemma-4-26B-A4B-it QAT Q4_0 (14,4 GB) + mmproj — MoE, multimodal
- gemma-4-12B-it Q4_K_M (7,4 GB) + mmproj
- DeepSeek-R1-0528-Qwen3-8B Q4_K_M (5,0 GB) — destilado
- Meta-Llama-3.1-8B-Instruct Q4_K_M (4,9 GB)

**Ollama:** `gemma4:26b` (17 GB), `google/gemma-4-26b-a4b-qat` (17 GB), `llama3.2:3b` (2,0 GB), `nomic-embed-text` (274 MB, embeddings para el RAG).

## Medición rápida (Ollama, contexto 4096, 200 tokens de salida)

Medido en caliente (con el modelo ya cargado una vez).

| Modelo | GPU completa | Parcial | Solo CPU |
|---|---|---|---|
| llama3.2:3b (denso, 3B) | 239 tok/s | 57 tok/s (14 capas) | 27 tok/s |
| gemma4:26b (MoE, 4B activos) | 125 tok/s | 41 tok/s (15 capas) | 19 tok/s |

Observaciones útiles para la charla:
- **Arranque en frío:** la primera petición después de cargar tardó 15 s (3B) y 36 s (26B). **Precalentar cada modelo antes del taller.**
- El MoE de 26B corre en CPU a 19 tok/s porque solo activa ~4B parámetros por token: buen ejemplo para "denso vs MoE".
- Con `gemma4:26b` y `llama3.2:3b` cargados a la vez, la VRAM llega a ~21 GB.

## Problemas detectados (a resolver antes del taller)

1. **Choque de puertos:** Ollama usa `1234`, que es el puerto por defecto del servidor de LM Studio. Además, el contenido del taller y los asistentes esperan `localhost:11434`. Para volver al estándar (requiere sudo):
   ```bash
   sudo systemctl edit ollama
   # en el bloque [Service] dejar:  Environment="OLLAMA_HOST=127.0.0.1:11434"
   sudo systemctl restart ollama
   ```
2. **VRAM compartida entre programas:** con `OLLAMA_KEEP_ALIVE=-1`, un modelo de Ollama queda ocupando la GPU indefinidamente. Antes de la demo de LM Studio: `ollama stop <modelo>` (o `ollama ps` para ver qué hay cargado). Y al revés: expulsar el modelo en LM Studio antes de la demo de Ollama.
3. `nvtop` y `qrencode` no están instalados (`sudo apt install nvtop qrencode`). Alternativas sin sudo: `.venv/bin/nvitop` y el paquete `qrcode` de Python.
