"""Captura diapositivas con Playwright para revisión visual.

Uso:  python3 slides/shoot.py 4:1 6:3 19:0
      (diapositiva:pasos  -> cuántas veces se avanza con la flecha dentro de la diapositiva)

Requiere:  pip install playwright && playwright install chromium
Las capturas quedan en slides/shots/ (ignorado por git).
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
deck = (HERE / "dist" / "index.html").as_uri()
out = HERE / "shots"
out.mkdir(exist_ok=True)
shots = [tuple(map(int, s.split(":"))) for s in sys.argv[1:]] or [(1, 0)]

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1600, "height": 900})
    errors = []
    pg.on("pageerror", lambda e: errors.append(str(e)))
    for sl, st in shots:
        pg.goto("about:blank")
        pg.goto(f"{deck}#{sl}")
        pg.wait_for_timeout(300)
        for _ in range(st):
            pg.keyboard.press("ArrowRight")
        pg.wait_for_timeout(1600)
        pg.screenshot(path=str(out / f"shot-{sl:02d}-{st}.png"))
    b.close()
print("capturas en", out, "| errores JS:", errors or "ninguno")
