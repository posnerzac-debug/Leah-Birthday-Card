#!/usr/bin/env python3
"""Make an unrevealing, static social preview matching the birthday countdown."""
from pathlib import Path
import sys
from PIL import Image, ImageDraw, ImageFont

output = Path(sys.argv[1] if len(sys.argv) > 1 else 'birthday-preview.png')
output.parent.mkdir(parents=True, exist_ok=True)
W, H = 1200, 630
image = Image.new('RGB', (W, H), '#f1e6df')
draw = ImageDraw.Draw(image)
# Warm stationery styling matches the existing countdown, not the gift artwork.
draw.ellipse((-220, -310, 610, 460), fill='#f9f1ea')
draw.ellipse((765, 280, 1470, 950), fill='#ead7d2')
draw.rounded_rectangle((93, 69, 1111, 589), radius=17, fill='#e2d0c9')
draw.rounded_rectangle((82, 55, 1100, 577), radius=17, fill='#fffbf7', outline='#decac0', width=2)
draw.rounded_rectangle((98, 71, 1084, 561), radius=12, outline='#eedfd7', width=2)
fonts = '/usr/share/fonts/truetype/dejavu/'
serif = fonts + 'DejaVuSerif.ttf'
sans = fonts + 'DejaVuSans.ttf'
bold = fonts + 'DejaVuSans-Bold.ttf'

def center(text, cy, size, color, face=serif):
    font = ImageFont.truetype(face, size)
    box = draw.textbbox((0, 0), text, font=font)
    draw.text(((W-(box[2]-box[0]))/2, cy-box[1]), text, font=font, fill=color)

center('A LITTLE SOMETHING FOR YOU', 88, 19, '#94736a', bold)
center('A BIRTHDAY SURPRISE', 157, 20, '#aa7470', bold)
center('Nuh-uh-uh.', 203, 72, '#43352e')
center("Come back when you're a bit older and wiser.", 307, 25, '#785f56')
draw.line((562, 362, 638, 362), fill='#d9bcb3', width=2)
center('UNLOCKS SEPTEMBER 24  ·  12:00 A.M. TORONTO TIME', 382, 17, '#94736a', bold)
for x, label in zip((277, 444, 611, 778), ('DAYS', 'HOURS', 'MINUTES', 'SECONDS')):
    draw.rounded_rectangle((x, 423, x+146, 521), radius=7, fill='#f6ece6', outline='#e9d8cf', width=2)
    font = ImageFont.truetype(serif, 46)
    number = '--'
    tb = draw.textbbox((0, 0), number, font=font)
    draw.text((x+73-(tb[2]-tb[0])/2, 434-tb[1]), number, font=font, fill='#674b43')
    labelfont = ImageFont.truetype(bold, 13)
    lb = draw.textbbox((0, 0), label, font=labelfont)
    draw.text((x+73-(lb[2]-lb[0])/2, 494-lb[1]), label, font=labelfont, fill='#a28479')
center('Love, Zac.', 531, 19, '#ab8280')
image.save(output, 'PNG', optimize=True)
print(f'Generated {output}: {image.size}, {output.stat().st_size} bytes')
