#!/usr/bin/env python3
"""OGP 5案を生成する。1200x630。"""
from PIL import Image, ImageDraw, ImageFont, ImageOps
import os

BASE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(BASE, "img")
OUT = os.path.join(BASE, "og")
os.makedirs(OUT, exist_ok=True)
W, H = 1200, 630
BOLD = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
TEAL = (14, 107, 92)
TEAL_D = (8, 62, 53)
CREAM = (246, 241, 230)
INK = (18, 18, 18)
GOLD = (201, 162, 39)
WHITE = (255, 255, 255)

def font(size):
    return ImageFont.truetype(BOLD, size, index=0)

def cover(path, w, h):
    im = Image.open(path).convert("RGB")
    return ImageOps.fit(im, (w, h), Image.LANCZOS)

def save(im, name):
    im.save(os.path.join(OUT, name), quality=88)
    print("made", name)

TITLE = "水戸で薬屋づくしの一日"
SUB = "展示 ＋ 映画 ＋ あんこう鍋"

# 案1: あんこう鍋フルブリード＋下帯
im = cover(os.path.join(IMG, "ankou.jpg"), W, H)
d = ImageDraw.Draw(im, "RGBA")
d.rectangle([0, H - 190, W, H], fill=(8, 62, 53, 235))
d.text((56, H - 168), TITLE, font=font(72), fill=WHITE)
d.text((58, H - 74), SUB + "　｜　水戸日帰りプラン", font=font(34), fill=(180, 230, 220))
save(im, "og1.jpg")

# 案2: 京成百貨店（左）＋クリーム地に大タイトル（右）
im = Image.new("RGB", (W, H), CREAM)
ph = cover(os.path.join(IMG, "keisei.jpg"), 520, H)
im.paste(ph, (0, 0))
d = ImageDraw.Draw(im)
d.rectangle([520, 0, 536, H], fill=TEAL)
d.text((580, 120), "水戸で", font=font(84), fill=INK)
d.text((580, 216), "薬屋づくし", font=font(84), fill=TEAL)
d.text((580, 312), "の一日", font=font(84), fill=INK)
d.text((584, 452), "『薬屋のひとりごと』展 × 劇場版", font=font(30), fill=(93, 90, 84))
d.text((584, 496), "会期 12/19 – 1/12　京成百貨店（水戸）", font=font(30), fill=(93, 90, 84))
save(im, "og2.jpg")

# 案3: 3枚コラージュ＋上帯
im = Image.new("RGB", (W, H), INK)
im.paste(cover(os.path.join(IMG, "keisei.jpg"), 400, 470), (0, 160))
im.paste(cover(os.path.join(IMG, "ankou.jpg"), 400, 470), (400, 160))
im.paste(cover(os.path.join(IMG, "mito-station.jpg"), 400, 470), (800, 160))
d = ImageDraw.Draw(im)
d.text((48, 34), TITLE, font=font(64), fill=WHITE)
d.text((W - 48, 58), "MITO DAY TRIP", font=font(30), fill=GOLD, anchor="ra")
save(im, "og3.jpg")

# 案4: 深緑ベタ＋タイポのみ
im = Image.new("RGB", (W, H), TEAL_D)
d = ImageDraw.Draw(im)
d.rectangle([36, 36, W - 36, H - 36], outline=GOLD, width=4)
d.text((W // 2, 150), "薬屋づくし", font=font(150), fill=WHITE, anchor="ma")
d.text((W // 2, 330), "展示と映画と、あんこう鍋。", font=font(46), fill=(180, 230, 220), anchor="ma")
d.text((W // 2, 440), "2026.12.19 – 2027.1.12　水戸", font=font(38), fill=GOLD, anchor="ma")
save(im, "og4.jpg")

# 案5: 水戸駅南口（COMBOX）フルブリード＋左上タイトル帯
im = cover(os.path.join(IMG, "combox.jpg"), W, H)
d = ImageDraw.Draw(im, "RGBA")
d.rectangle([0, 0, W, 168], fill=(246, 241, 230, 242))
d.text((52, 30), TITLE, font=font(66), fill=INK)
d.text((54, 112), "『薬屋のひとりごと』展 × 劇場版『亡妃の秘宝』", font=font(30), fill=TEAL)
save(im, "og5.jpg")
print("done")
