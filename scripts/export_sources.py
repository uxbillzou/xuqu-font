#!/usr/bin/env python3
"""Convert approved v1.3 outlines to editable UFO, add GF Latin Core glyphs.

This importer is only needed to recreate the initial source conversion. Normal
builds use the committed UFO files directly, so designers' edits are preserved.
No outlines from another typeface are used.
"""
from pathlib import Path
import json, math, unicodedata, argparse
from copy import deepcopy
import ufoLib2
from fontTools.ttLib import TTFont
from fontTools.agl import UV2AGL
from fontTools.pens.recordingPen import DecomposingRecordingPen
from shapely.geometry import Polygon, GeometryCollection, LineString, box
from shapely.ops import unary_union
from shapely.affinity import translate, scale
from shapely.geometry.polygon import orient

ROOT = Path(__file__).resolve().parents[1]
STYLES = [('Thin',100),('Light',300),('Regular',400),('Bold',700),('ExtraBold',800)]
MARKS = [0x300,0x301,0x302,0x303,0x304,0x306,0x307,0x308,0x30A,0x30B,0x30C,0x326,0x327,0x328]
BELOW = {0x326,0x327,0x328}
SCALE = {'Thin':.60,'Light':.78,'Regular':1.,'Bold':1.12,'ExtraBold':1.26}
STEM = {'Thin':28,'Light':58,'Regular':100,'Bold':148,'ExtraBold':190}

def name(cp): return UV2AGL.get(cp, f'uni{cp:04X}')
def polygons(s):
    if s.is_empty:return []
    return [s] if s.geom_type=='Polygon' else [p for p in s.geoms if p.geom_type=='Polygon']
def geometry(tt, gn):
    pen=DecomposingRecordingPen(tt.getGlyphSet());tt.getGlyphSet()[gn].draw(pen)
    s=GeometryCollection();pts=[]
    for op,args in pen.value:
        if op=='moveTo':pts=[args[0]]
        elif op=='lineTo':pts.append(args[0])
        elif op in ('closePath','endPath'):
            if len(pts)>2:s=s.symmetric_difference(Polygon(pts).buffer(0))
            pts=[]
        else:raise ValueError(f'Unexpected curve in polygon master: {gn}: {op}')
    return s.buffer(0)
def clean_points(coords):
    a=[]
    for x,y in list(coords)[:-1]:
        p=(round(x),round(y))
        if not a or p!=a[-1]:a.append(p)
    if len(a)>1 and a[0]==a[-1]:a.pop()
    while len(a)>3:
        keep=[]
        for i,b in enumerate(a):
            p,c=a[i-1],a[(i+1)%len(a)]
            cross=(b[0]-p[0])*(c[1]-b[1])-(b[1]-p[1])*(c[0]-b[0])
            dot=(b[0]-p[0])*(c[0]-b[0])+(b[1]-p[1])*(c[1]-b[1])
            if cross!=0 or dot<0:keep.append(b)
        if len(keep)==len(a) or len(keep)<3:break
        a=keep
    return a
def draw(g,s):
    p=g.getPen()
    for poly in polygons(s):
        poly=orient(poly,1) # UFO convention; fontmake reverses for TrueType.
        for ring in [poly.exterior,*poly.interiors]:
            pts=clean_points(ring.coords)
            if len(pts)<3:continue
            p.moveTo(pts[0])
            for pt in pts[1:]:p.lineTo(pt)
            p.closePath()
def line(points,t):return LineString(points).buffer(t/2,cap_style=2,join_style=2,mitre_limit=3)
def octave(w,h,c=20):
    c=min(c,w/3,h/3)
    return Polygon([(0,c),(0,h-c),(c,h),(w-c,h),(w,h-c),(w,c),(w-c,0),(c,0)])
def mark_shape(cp,sty):
    if cp==0x300:s=Polygon([(-165,150),(-60,150),(80,0),(-15,0)])
    elif cp==0x301:s=Polygon([(-80,0),(15,0),(165,150),(60,150)])
    elif cp==0x302:s=Polygon([(-210,0),(-95,0),(0,80),(95,0),(210,0),(40,155),(-40,155)])
    elif cp==0x303:s=line([(-190,35),(-110,105),(-45,105),(50,35),(115,35),(185,105)],55)
    elif cp==0x304:s=box(-180,30,180,95)
    elif cp==0x306:s=line([(-165,130),(-90,40),(90,40),(165,130)],60)
    elif cp==0x307:s=translate(octave(90,90,14),-45,25)
    elif cp==0x308:s=unary_union([translate(octave(85,85,14),-160,0),translate(octave(85,85,14),75,0)])
    elif cp==0x30A:s=translate(octave(195,160,40).difference(translate(octave(95,70,15),50,45)),-97,0)
    elif cp==0x30B:s=unary_union([translate(mark_shape(0x301,'Regular'),-105,0),translate(mark_shape(0x301,'Regular'),105,0)])
    elif cp==0x30C:s=Polygon([(-210,155),(-95,155),(0,75),(95,155),(210,155),(40,0),(-40,0)])
    elif cp==0x326:s=Polygon([(-45,-45),(45,-45),(45,-110),(-15,-185),(-60,-185),(-15,-105),(-45,-105)])
    elif cp==0x327:s=line([(10,8),(10,-35),(70,-85),(70,-135),(20,-175),(-85,-175)],65)
    elif cp==0x328:s=line([(85,12),(0,-75),(0,-130),(55,-175),(155,-175)],65)
    else:raise ValueError(cp)
    return scale(s,SCALE[sty],SCALE[sty],origin=(0,0))

def metadata(u,style,weight,cfg):
    i=u.info;fam=cfg['family_name'];i.familyName=fam;i.styleName=style
    i.unitsPerEm=1000;i.ascender=970;i.descender=-260;i.capHeight=700;i.xHeight=530
    i.versionMajor,i.versionMinor=map(int,cfg['version'].split('.'))
    i.openTypeHeadCreated='2026/09/13 00:00:00'
    i.openTypeOS2WeightClass=weight;i.openTypeOS2WidthClass=5
    i.openTypeOS2Type=[];i.openTypeOS2Selection=[7,8]
    i.openTypeOS2VendorID='XUQU'
    i.openTypeOS2CodePageRanges=[0,1,4,7,29]
    i.openTypeOS2Panose=[2,11,{'Thin':2,'Light':3,'Regular':5,'Bold':8,'ExtraBold':9}[style],5,2,2,2,2,2,4]
    i.openTypeOS2TypoAscender=970;i.openTypeOS2TypoDescender=-260;i.openTypeOS2TypoLineGap=0
    i.openTypeHheaAscender=970;i.openTypeHheaDescender=-260;i.openTypeHheaLineGap=0
    i.openTypeOS2WinAscent=1150;i.openTypeOS2WinDescent=350
    i.postscriptUnderlinePosition=-150;i.postscriptUnderlineThickness=70
    i.openTypeNameDesigner=cfg['author_display']
    from finalize_metadata import apply_project_metadata
    apply_project_metadata(u,cfg)
    i.styleMapFamilyName=fam if style in ('Regular','Bold') else fam+' '+style
    i.styleMapStyleName='bold' if style=='Bold' else 'regular'
    i.openTypeNamePreferredFamilyName=fam;i.openTypeNamePreferredSubfamilyName=style
    i.postscriptFontName=fam.replace(' ','')+'-'+style

def export(style,weight,cfg,overwrite=False):
    path=ROOT/'sources'/f'Xuqu-{style}.ufo'
    if path.exists() and not overwrite:raise SystemExit(f'{path.name} exists; use --overwrite only to regenerate.')
    tt=TTFont(ROOT/'reference/v1.3'/f'XUQU-{style}.ttf');cmap=dict(tt.getBestCmap())
    u=ufoLib2.Font();metadata(u,style,weight,cfg)
    shapes={}; widths={}; changes=[]
    skip={'.null','nonmarkingreturn'}
    for gn in tt.getGlyphOrder():
        if gn in skip:continue
        shapes[gn]=geometry(tt,gn);widths[gn]=tt['hmtx'][gn][0]
    def put(cp,s,w,gn=None):
        gn=gn or cmap.get(cp) or name(cp)
        if cp is not None:cmap[cp]=gn
        shapes[gn]=s; widths[gn]=w
        return gn
    def get(cp):return shapes[cmap[cp]]
    def nfd_shape(base,cp):
        bs=get(base)
        if base in (ord('i'),ord('j')):
            bs=unary_union([p for p in polygons(bs) if p.bounds[1]<530])
        cx=(bs.bounds[0]+bs.bounds[2])/2
        ms=mark_shape(cp,style)
        if cp in BELOW:return unary_union([bs,translate(ms,cx,0)]).buffer(0)
        if widths[cmap[base]]<400:ms=scale(ms,.6,1,origin=(0,0))
        ms=translate(ms,cx,bs.bounds[3]+55-ms.bounds[1])
        return unary_union([bs,ms]).buffer(0)
    # GF Latin Core: 14 zero-advance combining marks.
    for cp in MARKS:put(cp,mark_shape(cp,style),0)
    # Standalone accents use the same design as the combining forms.
    for cp,m in [(0x2C6,0x302),(0x2C7,0x30C),(0x2D8,0x306),(0x2D9,0x307),(0x2DA,0x30A),(0x2DB,0x328),(0x2DC,0x303),(0x2DD,0x30B)]:
        s=mark_shape(m,style);w=max(300,round(s.bounds[2]-s.bounds[0])+116)
        s=translate(s,w/2-(s.bounds[0]+s.bounds[2])/2,0 if m in BELOW else 600-s.bounds[1])
        put(cp,s,w)
    # Dotless j, Romanian comma-below, and Welsh grave/acute/dieresis forms.
    put(0x237,unary_union([p for p in polygons(get(ord('j'))) if p.bounds[1]<530]),widths[cmap[ord('j')]])
    core=json.loads((ROOT/'sources/data/GF_Latin_Core.json').read_text())
    for rec in core:
        cp=rec['unicode']
        if cp is None or cp in cmap or cp==0x1E9E:continue
        seq=unicodedata.normalize('NFD',chr(cp))
        if len(seq)==2 and ord(seq[0]) in cmap and ord(seq[1]) in MARKS:
            put(cp,nfd_shape(ord(seq[0]),ord(seq[1])),widths[cmap[ord(seq[0])]])
        else:raise ValueError(f'No design recipe for {rec}')
    # Capital sharp S: a distinct cap-height open lower bowl, not two S glyphs.
    t=STEM[style]; w=840
    sharp=unary_union([box(58,0,58+t,580),line([(58+t/2,530),(58+t/2,600),(158,700-t/2),(520,700-t/2),(615,575),(480,430),(750,270),(790,130),(700,t/2),(375,t/2)],t*.90)])
    x0,y0,x1,y1=sharp.bounds
    sharp=translate(scale(sharp,(w-58)/(x1-x0),700/(y1-y0),origin=(x0,y0)),0,-y0)
    put(0x1E9E,sharp,898)
    # Latvian and historical R comma forms need detached commas, not cedilla hooks.
    for cp in [0x122,0x123,0x136,0x137,0x13B,0x13C,0x145,0x146,0x156,0x157]:
        base=ord(unicodedata.normalize('NFD',chr(cp))[0]);bs=get(base)
        cx=(bs.bounds[0]+bs.bounds[2])/2;ms=mark_shape(0x326,style)
        if base==ord('g'):
            ms=scale(ms,-1,-1,origin=(0,0));ms=translate(ms,cx,bs.bounds[3]+55-ms.bounds[1])
        else:ms=translate(ms,cx,0)
        put(cp,unary_union([bs,ms]),widths[cmap[base]])
        changes.append({'codepoint':f'U+{cp:04X}','reason':'detached comma accent; Latvian g uses turned comma above'})
    # Required unencoded glyphs, reachable through locl and contextual ccmp.
    for gn,y in [('periodcentered.loclCAT',265),('periodcentered.loclCAT.case',350)]:
        s=get(0xB7);cx=(s.bounds[0]+s.bounds[2])/2;cy=(s.bounds[1]+s.bounds[3])/2
        put(None,translate(s,130-cx,y-cy),260,gn)
    put(None,deepcopy(get(ord('i'))),widths[cmap[ord('i')]],'idotaccent')
    put(None,unary_union([p for p in polygons(get(0x12F)) if p.bounds[1]<530]),widths[cmap[0x12F]],'i.ogonek.dotless')
    alt=scale(get(ord("'")),.65,.7,origin=(0,0))
    put(None,translate(alt,-alt.bounds[0],-alt.bounds[3]),0,'caroncomb.alt')
    # Side carons for Czech/Slovak tall letters are not wide accents above stems.
    for cp in [0x10F,0x13D,0x13E,0x165]:
        seq=unicodedata.normalize('NFD',chr(cp));base=ord(seq[0]);s=get(base)
        a=translate(alt,s.bounds[2]+35-alt.bounds[0],700-alt.bounds[3])
        put(cp,unary_union([s,a]),max(widths[cmap[base]],round(a.bounds[2])+45))
        changes.append({'codepoint':f'U+{cp:04X}','reason':'side caron for tall Czech/Slovak letter'})
    # Auxiliary controls, dotted circle for displaying a detached combining mark.
    for cp,w in [(0x2028,0),(0x2029,0),(0x200B,0),(0x200C,0),(0x200D,0),(0xFEFF,0)]:put(cp,GeometryCollection(),w)
    dots=[]
    for k in range(12):
        a=k*math.pi/6;size={'Thin':32,'Light':40,'Regular':50,'Bold':64,'ExtraBold':78}[style]
        dots.append(translate(octave(size,size,8),400+260*math.cos(a)-size/2,350+260*math.sin(a)-size/2))
    put(0x25CC,unary_union(dots),800)
    # Default proportional numbers, with existing tabular design preserved by tnum.
    for cp in range(48,58):
        gn=cmap[cp];put(None,deepcopy(shapes[gn]),widths[gn],gn+'.tf')
        if cp==49:
            s=shapes[gn];put(cp,translate(s,58-s.bounds[0],0),round(s.bounds[2]-s.bounds[0])+116)
    # Shape and encoding data into the UFO.
    byname={}
    for cp,gn in cmap.items():byname.setdefault(gn,[]).append(cp)
    categories={}
    for gn,s in shapes.items():
        g=u.newGlyph(gn);g.width=widths[gn];g.unicodes=sorted(byname.get(gn,[]));draw(g,s)
        cp=g.unicode
        if cp in MARKS or gn=='caroncomb.alt':
            categories[gn]='mark'
            if gn=='caroncomb.alt':
                g.appendAnchor({'name':'_caron','x':0,'y':0})
            elif cp in BELOW:
                g.appendAnchor({'name':'_bottom','x':0,'y':0});g.appendAnchor({'name':'bottom','x':0,'y':round(s.bounds[1]-40)})
            else:
                g.appendAnchor({'name':'_top','x':0,'y':0});g.appendAnchor({'name':'top','x':0,'y':round(s.bounds[3]+45)})
        elif (cp is not None and (unicodedata.category(chr(cp)).startswith('L') or cp==0x25CC)) or gn in ('idotaccent','i.ogonek.dotless'):
            categories[gn]='base'
            if not s.is_empty:
                cx=round((s.bounds[0]+s.bounds[2])/2)
                g.appendAnchor({'name':'top','x':cx,'y':round(s.bounds[3]+55)})
                g.appendAnchor({'name':'bottom','x':cx,'y':min(0,round(s.bounds[1]))})
                if cp in [ord(x) for x in 'dlLt']:
                    g.appendAnchor({'name':'caron','x':round(s.bounds[2]+35),'y':700})
        else:categories[gn]='base'
    u.lib['public.openTypeCategories']=categories
    # Keep side-caron forms as editable components, also enabling automatic
    # caron-placement checks; geometry is identical to the proofed construction.
    for cp in [0x10F,0x13D,0x13E,0x165]:
        base=ord(unicodedata.normalize('NFD',chr(cp))[0]);g=u[cmap[cp]]
        g.clearContours();g.getPen().addComponent(cmap[base],(1,0,0,1,0,0))
        g.getPen().addComponent('caroncomb.alt',(1,0,0,1,round(get(base).bounds[2]+35),700))
    u.lib['public.glyphOrder']=list(shapes)
    u.lib['public.postscriptNames']={g:g for g in shapes}
    # Existing kerning remains identical except for newly added forms inheriting it.
    pairs=tt['kern'].kernTables[0].kernTable
    u.kerning.update({k:v for k,v in pairs.items() if k[0] in shapes and k[1] in shapes})
    for rec in core:
        cp=rec['unicode']
        if cp is None or cp in tt.getBestCmap():continue
        seq=unicodedata.normalize('NFD',chr(cp))
        if len(seq)>1 and ord(seq[0]) in cmap:
            gn=cmap[cp];bn=cmap[ord(seq[0])]
            for (l,r),v in list(u.kerning.items()):
                if l==bn:u.kerning[(gn,r)]=v
                if r==bn:u.kerning[(l,gn)]=v
    marknames=' '.join(cmap[x] for x in MARKS if x not in BELOW)
    feats=['languagesystem DFLT dflt;','languagesystem latn dflt;','languagesystem latn CAT;','languagesystem latn TRK;','languagesystem latn AZE;']
    feats += [f'@AboveMarks = [{marknames}];','lookup RemoveDots {',f"sub {cmap[105]}' @AboveMarks by {cmap[0x131]};",f"sub {cmap[106]}' @AboveMarks by {cmap[0x237]};",f"sub {cmap[0x12F]}' @AboveMarks by i.ogonek.dotless;",'} RemoveDots;','feature ccmp { lookup RemoveDots; } ccmp;']
    feats += ['feature locl {','script latn;','language CAT;',"sub l periodcentered' l by periodcentered.loclCAT;","sub L periodcentered' L by periodcentered.loclCAT.case;",'language TRK;',f'sub {cmap[105]} by idotaccent;','language AZE;',f'sub {cmap[105]} by idotaccent;','} locl;']
    feats += ['feature tnum {']+[f'sub {cmap[cp]} by {cmap[cp]}.tf;' for cp in range(48,58)]+['} tnum;']
    # caron alternate is accessible when directly combining with tall letters.
    feats += ['feature ccmp {',f"sub [d l L t] {cmap[0x30C]}' by caroncomb.alt;",'} ccmp;']
    u.features.text='\n'.join(feats)+'\n'
    u.save(path,overwrite=True)
    missing=[x for x in core if x['unicode'] is not None and x['unicode'] not in cmap]
    assert not missing,missing
    return {'style':style,'weight':weight,'encoded_characters':len(cmap),'glyphs':len(u),'added_codepoints':[f'U+{x:04X}' for x in sorted(set(cmap)-set(tt.getBestCmap()))],'intentional_design_changes':changes,'ufo':path.relative_to(ROOT).as_posix()}

def main():
    p=argparse.ArgumentParser();p.add_argument('--overwrite',action='store_true');a=p.parse_args()
    cfg=json.loads((ROOT/'project.json').read_text());reports=[]
    for s,w in STYLES:
        r=export(s,w,cfg,a.overwrite);reports.append(r);print(s,r['glyphs'],'glyphs',flush=True)
    (ROOT/'documentation/qa/source-conversion.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':main()
