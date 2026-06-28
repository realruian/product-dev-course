"""26 页逐页截图 + 联络表，肉眼自检对齐 / 溢出。"""
from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image
import math

ROOT = Path(__file__).parent
DECK = ROOT / "deck.html"
SHOTS = ROOT / "shots"
SHOTS.mkdir(exist_ok=True)
TOTAL = 29

with sync_playwright() as p:
    browser = p.chromium.launch()
    ctx = browser.new_context(viewport={"width": 1920, "height": 1080}, device_scale_factor=1)
    page = ctx.new_page()
    page.goto(DECK.as_uri())
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(400)
    for i in range(TOTAL):
        page.evaluate(f"show({i})")
        page.wait_for_timeout(400)
        # 含 reveal 的页 → 按对应的 step 数（多按会翻页！）
        # 又拆出"套回本案例"独立一页后：第 5 页 6 个 step、第 11 页 4 条差异
        reveal_steps = {5: 6, 11: 4}
        if i in reveal_steps:
            for _ in range(reveal_steps[i]):
                page.keyboard.press("ArrowRight"); page.wait_for_timeout(120)
            page.wait_for_timeout(280)
        page.screenshot(path=str(SHOTS / f"{i:02d}.png"))
        print(f"  shot {i:02d}")
    browser.close()

# 4×2 联络表
COLS, ROWS = 4, 2
THUMB_W, THUMB_H = 480, 270
PER = COLS * ROWS
sheets = math.ceil(TOTAL / PER)
for s in range(sheets):
    sheet = Image.new("RGB", (COLS * THUMB_W, ROWS * THUMB_H), "white")
    for k in range(PER):
        idx = s * PER + k
        if idx >= TOTAL: break
        t = Image.open(SHOTS / f"{idx:02d}.png").resize((THUMB_W, THUMB_H))
        sheet.paste(t, ((k % COLS) * THUMB_W, (k // COLS) * THUMB_H))
    sheet.save(SHOTS / f"sheet_{s+1:02d}.png")
print("done")
