#!/usr/bin/env python3
"""Render exact font specimens with FreeType (no synthetic weights)."""
from pathlib import Path
import json,subprocess
from PIL import Image,ImageDraw,ImageFont
from fontTools.ttLib import TTFont
from export_sources import ROOT,STYLES

BG='#101714';FG='#F4F5ED';LIME='#B8F568';MUTED='#90A093'
def main():
    cfg=json.loads((ROOT/'project.json').read_text());prefix=cfg['family_name'].replace(' ','')
    out=ROOT/'documentation/specimens';out.mkdir(parents=True,exist_ok=True)
    system=subprocess.check_output(['fc-match','sans-serif','-f','%{file}'],text=True)
    label=lambda size:ImageFont.truetype(system,size)
    def font(style,size):return ImageFont.truetype(str(ROOT/'fonts/ttf'/f'{prefix}-{style}.ttf'),size)
    im=Image.new('RGB',(1820,1600),BG);d=ImageDraw.Draw(im)
    d.text((80,52),'XUQU / GOOGLE FONTS PREPARATION',font=label(28),fill=LIME)
    d.text((80,103),'Five real weights. Approved A & B retained.',font=label(24),fill=MUTED)
    for idx,(style,w) in enumerate(STYLES):
        y=195+idx*270;d.line((80,y-24,1740,y-24),fill='#33473A',width=2)
        d.text((80,y+8),str(w),font=label(39),fill=LIME)
        d.text((80,y+60),style,font=label(24),fill=MUTED)
        d.text((285,y),'XUQUTECH  Aa Bb',font=font(style,90),fill=FG)
        d.text((285,y+120),'Design the next. 0123456789',font=font(style,54),fill=FG)
    d.text((80,1540),f"Xuqu v{cfg['version']} • 400 encoded characters • 5 static styles • SIL OFL 1.1 • Xu Zou",font=label(21),fill=MUTED)
    im.save(out/'01-Five-Weights.png')
    im=Image.new('RGB',(1820,1570),BG);d=ImageDraw.Draw(im)
    d.text((80,50),'LATIN CORE / EXTENDED PROOF',font=label(30),fill=LIME)
    texts=['Șș Țț Ẁẁ Ẃẃ Ẅẅ Ỳỳ ẞ','Ģģ Ķķ Ļļ Ņņ  Ďď Ľľ Ťť','A\u0301 x\u0301 i\u0301 j\u0301 į\u0301  a\u0301\u0308']
    for idx,(style,w) in enumerate(STYLES):
        y=150+idx*274
        d.text((80,y+4),f'{w}',font=label(34),fill=LIME);d.text((80,y+51),style,font=label(22),fill=MUTED)
        for j,t in enumerate(texts):d.text((280,y+j*78),t,font=font(style,55),fill=FG)
        d.line((80,y+241,1740,y+241),fill='#33473A',width=2)
    d.text((80,1518),'Actual font rendering • New Core glyphs, detached commas, side carons and combining marks',font=label(21),fill=MUTED)
    im.save(out/'02-Latin-Core-Proof.png')
    im=Image.new('RGB',(1820,1214),BG);d=ImageDraw.Draw(im)
    d.text((80,58),'BOLD / EXTRABOLD DETAIL',font=label(30),fill=LIME)
    d.text((80,115),'Same size. Different outline weight. Approved A and B unchanged.',font=label(25),fill=MUTED)
    for x,style,w in [(80,'Bold',700),(950,'ExtraBold',800)]:
        d.text((x,220),f'{style} / {w}',font=label(30),fill=LIME)
        d.text((x,280),'AB',font=font(style,350),fill=FG)
        d.text((x,700),'Aa Bb ẞ',font=font(style,126),fill=FG)
        d.text((x,900),'Șș Țț',font=font(style,120),fill=FG)
    d.line((905,215,905,1090),fill='#33473A',width=2)
    d.text((80,1138),f"Rendered from the actual v{cfg['version']} TTF files. Actual font outlines; no synthetic weight.",font=label(23),fill=MUTED)
    im.save(out/'03-AB-Weight-Detail.png')
    print('Rendered 3 exact-font proof images.')
if __name__=='__main__':main()
