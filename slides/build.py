"""Compila slides/deck.src.html -> slides/dist/index.html.

Reemplaza los marcadores:
  __QR__              -> contenido de assets/qr.b64 (PNG en base64)
  __SHIP__            -> contenido de assets/ship.svg (nave original de las líneas de tiempo)
  __ASSET:ruta__      -> data URI del archivo assets/ruta (para usar en <img src="...">),
                         así dist/index.html queda autocontenido

Uso:  python3 slides/build.py
"""
import base64
import mimetypes
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
src = (HERE / "deck.src.html").read_text(encoding="utf-8")
qr = (HERE / "assets" / "qr.b64").read_text(encoding="utf-8").strip()
ship = (HERE / "assets" / "ship.svg").read_text(encoding="utf-8").strip()


def data_uri(m):
    path = HERE / "assets" / m.group(1)
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


out = src.replace("__QR__", qr).replace("__SHIP__", ship)
out = re.sub(r"__ASSET:([^_\s\"']+(?:_[^_\s\"']+)*)__", data_uri, out)
assert "__QR__" not in out and "__SHIP__" not in out and "__ASSET:" not in out
dist = HERE / "dist"
dist.mkdir(exist_ok=True)
(dist / "index.html").write_text(out, encoding="utf-8")
print(f"OK -> {dist / 'index.html'} ({len(out):,} bytes)")
