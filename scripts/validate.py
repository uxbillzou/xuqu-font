#!/usr/bin/env python3
"""Meaningful regression checks for the Google Fonts conversion.

Checks approved A/B, all retained glyphs, coverage, real weight progression,
HarfBuzz mark positioning and tnum, every encoded glyph's FreeType raster,
and equivalence of TTF/WOFF2 outlines. Does not claim OS GUI installation QA.
"""
from pathlib import Path
import json,unicodedata,hashlib
from collections import Counter
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.areaPen import AreaPen
from PIL import ImageFont
from export_sources import geometry,STYLES,ROOT

def shape(font,text,features=None,language=None):
    h=hb.Font(hb.Face(font));h.scale=(1000,1000)
    b=hb.Buffer();b.add_str(text);b.guess_segment_properties()
    if language:b.language=language
    hb.shape(h,b,features or {})
    return [(i.codepoint,p.x_advance,p.y_advance,p.x_offset,p.y_offset) for i,p in zip(b.glyph_infos,b.glyph_positions)]

def main():
    cfg=json.loads((ROOT/'project.json').read_text());prefix=cfg['family_name'].replace(' ','')
    req=json.loads((ROOT/'sources/data/GF_Latin_Core.json').read_text())
    expected={r['unicode'] for r in req if r['unicode'] is not None}
    reports=[];areas={};failures=[]
    expected_changes={0x31,0x10F,0x13D,0x13E,0x165,0x122,0x123,0x136,0x137,0x13B,0x13C,0x145,0x146,0x156,0x157}
    for style,weight in STYLES:
        p=ROOT/'fonts/ttf'/f'{prefix}-{style}.ttf';data=p.read_bytes();f=TTFont(p)
        web=TTFont(ROOT/'fonts/webfonts'/f'{prefix}-{style}.woff2')
        old=TTFont(ROOT/'reference/v1.3'/f'XUQU-{style}.ttf')
        cm=f.getBestCmap();ocm=old.getBestCmap()
        assert expected<=set(cm)
        required_unencoded={r['name'] for r in req if r['unicode'] is None}
        assert required_unencoded<=set(f.getGlyphOrder()),required_unencoded-set(f.getGlyphOrder())
        assert set(ocm)<=set(cm)
        assert web.getBestCmap()==cm
        assert f['OS/2'].usWeightClass==weight
        assert len(shape(data,'XUQU ABC xyz 0123456789'))>0
        changes=[];equal=0;rendered=0;outside=[];shape_fails=[];areas[style]={}
        pil=ImageFont.truetype(str(p),96)
        for cp,gn in cm.items():
            g=geometry(f,gn);wg=geometry(web,gn)
            assert g.symmetric_difference(wg).area<.001,(style,cp,'format mismatch')
            assert f['hmtx'][gn][0]==web['hmtx'][gn][0]
            areas[style][cp]=g.area
            if not g.is_empty:
                if g.bounds[1]<-350 or g.bounds[3]>1150:outside.append(f'U+{cp:04X}')
                pil.getmask(chr(cp));rendered+=1
            if cp in ocm:
                og=geometry(old,ocm[cp]);diff=g.symmetric_difference(og).area
                advance_change=f['hmtx'][gn][0]-old['hmtx'][ocm[cp]][0]
                if diff>.001 or advance_change:
                    changes.append({'codepoint':f'U+{cp:04X}','outline_difference_area':round(diff,4),'advance_delta':advance_change})
                    if cp not in expected_changes:failures.append(f'{style}: unexpected retained-glyph change U+{cp:04X}')
                else:equal+=1
        for ch in 'AB':
            assert geometry(f,cm[ord(ch)]).symmetric_difference(geometry(old,ocm[ord(ch)])).area<.001,(style,ch)
            assert f['hmtx'][cm[ord(ch)]][0]==old['hmtx'][ocm[ord(ch)]][0]
        sample=['XUQUTECH','Design the next.','Aa Bb Gg Qq 0123456789','Șș Țț Ẁẁ Ẃẃ Ẅẅ Ỳỳ ẞ','A\u0301 x\u0301 i\u0301 j\u0301 į\u0301','d\u030C l\u030C L\u030C t\u030C','a\u0301\u0308 A\u0326\u0301','Ģģ Ķķ Ļļ Ņņ']
        for s in sample:
            shaped=shape(data,s)
            if any(x[0]==0 for x in shaped):shape_fails.append(s)
        marks=shape(data,'x\u0301')
        assert len(marks)==2 and marks[1][1]==0 and (marks[1][3]!=0 or marks[1][4]!=0),(style,'mark positioning')
        dotted=shape(data,'į\u0301')
        assert any(f.getGlyphOrder()[x[0]]=='i.ogonek.dotless' for x in dotted),(style,'soft dot removal')
        tnum=shape(data,'0123456789',{'tnum':1})
        assert len({x[1] for x in tnum})==1,(style,'tnum')
        prop=shape(data,'0123456789')
        assert len({x[1] for x in prop})>1,(style,'proportional')
        for pair in ['AV','To','WA','YA']:
            assert sum(x[1] for x in shape(data,pair))==sum(x[1] for x in shape((ROOT/'reference/v1.3'/f'XUQU-{style}.ttf').read_bytes(),pair)),(style,pair)
        cats=shape(data,'l·l L·L',language='ca')
        assert any('loclCAT' in f.getGlyphOrder()[x[0]] for x in cats)
        assert not outside,outside
        assert not shape_fails,shape_fails
        reports.append({'style':style,'weight':weight,'encoded_characters':len(cm),'glyphs':len(f.getGlyphOrder()),'gf_latin_core_encoded_required':len(expected),'gf_latin_core_missing':[],'original_encoded_retained':len(ocm),'original_glyphs_unchanged':equal,'intentional_changes':changes,'A_B_approved_outlines_and_advance':'exact match','rasterized_nonempty_glyphs':rendered,'TTF_WOFF2_equivalence':'pass','shaping_samples':sample,'shaping':'pass','mark_positioning':'pass','soft_dot_removal':'pass','catalan_locl':'pass','tnum':'pass','proportional_digits':'pass','retained_kerning_samples':'pass'})
    nonincreasing=[]
    common=set.intersection(*(set(x) for x in areas.values()))
    for cp in sorted(common):
        values=[areas[s][cp] for s,_ in STYLES]
        if any(values) and any(b<=a for a,b in zip(values,values[1:])):nonincreasing.append({'codepoint':f'U+{cp:04X}','areas':values})
    if nonincreasing:failures.append('Some visible glyphs lack strictly increasing ink area')
    result={'status':'pass' if not failures else 'fail','checks':reports,'weight_progression':{'nonincreasing':nonincreasing,'checked_codepoints':len(common)},'failures':failures,'limitations':['No macOS/Windows GUI installation acceptance test','No Adobe/Figma GUI testing','Fontspector network checks are disabled','Google design review and name acceptance remain pending; owner has approved the family-wide OFL grant']}
    (ROOT/'documentation/qa/regression.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'failures':failures,'styles':len(reports),'characters_each':reports[0]['encoded_characters'],'weight_anomalies':nonincreasing},ensure_ascii=False,indent=2))
    assert not failures,failures
if __name__=='__main__':main()
