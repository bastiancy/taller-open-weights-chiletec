"""Compila slides/deck.src.html -> slides/dist/index.html.

Reemplaza los marcadores:
  __QR__   -> contenido de assets/qr.b64 (PNG en base64)
  __SHIP__ -> contenido de assets/ship.svg (nave original de las líneas de tiempo)

Uso:  python3 slides/build.py
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
src = (HERE / "deck.src.html").read_text(encoding="utf-8")
qr = (HERE / "assets" / "qr.b64").read_text(encoding="utf-8").strip()
ship = (HERE / "assets" / "ship.svg").read_text(encoding="utf-8").strip()

out = src.replace("__QR__", qr).replace("__SHIP__", ship)
assert "__QR__" not in out and "__SHIP__" not in out
dist = HERE / "dist"
dist.mkdir(exist_ok=True)
(dist / "index.html").write_text(out, encoding="utf-8")
print(f"OK -> {dist / 'index.html'} ({len(out):,} bytes)")
