"""Build the order page from design/ parts.
python3 build.py demo  -> ../demo/index.html (orders/slips simulated, red ribbon, noindex)
python3 build.py main  -> ../index.html      (the real page)
Page logic lives in app.js — edit it there, then rebuild."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
mode = sys.argv[1] if len(sys.argv) > 1 else 'demo'
read = lambda n: open(os.path.join(HERE, n), encoding='utf-8').read()
img = '../img/' if mode == 'demo' else 'img/'
css = read('style.css').replace('url(../img/', 'url(' + img)
body = read('body.html').replace('IMG/', img)
ribbon = '<div class="demo-ribbon">หน้าตัวอย่างดีไซน์ (Demo) · กดลองได้ทุกปุ่ม แต่ไม่บันทึกคำสั่งซื้อและสลิปจริง</div>' if mode == 'demo' else ''
body = body.replace('<!--RIBBON-->', ribbon)
title = 'สั่งเสื้อรุ่น 21 · ตัวอย่างดีไซน์' if mode == 'demo' else 'สั่งเสื้อ NO limit 21'
meta = ('<meta name="robots" content="noindex, nofollow">' if mode == 'demo' else
        '<meta property="og:title" content="สั่งเสื้อ Hood · เสื้อยืด · ร่ม — NO limit รุ่น 21">\n'
        '<meta property="og:description" content="เห็นราคาทุกไซส์ คิดยอดให้อัตโนมัติ และแนบสลิปโอนเงินได้ · ปิดรับ 30 ต.ค. 69">\n'
        '<meta property="og:image" content="https://mahantapon.github.io/wsc21-order/img/hood.jpg">')
scripts = '<script>\n' + read('app.js') + '</script>\n<script>\n' + read('extra.js') + '</script>\n'
if mode == 'demo':
    scripts += '<script>\n' + read('demo.js') + '</script>\n'
html = f"""<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="สั่งเสื้อ Hood เสื้อยืดผู้ปกครอง และร่ม พร้อมราคาทุกไซส์ คิดยอดให้อัตโนมัติ และแนบสลิปโอนเงินได้">
{meta}
<link rel="icon" href="{img}school-logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@400;500;600;700&family=Kanit:wght@600;700;800&display=swap">
<style>
{css}</style>
</head>
<body>
{body}
{scripts}</body>
</html>
"""
out = os.path.join(HERE, '..', 'demo' if mode == 'demo' else '', 'index.html')
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, 'w', encoding='utf-8').write(html)
print('wrote', os.path.normpath(out), len(html), 'chars')
