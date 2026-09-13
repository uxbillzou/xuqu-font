"""Build five real static outline weights, including the approved B refinement.

Uses the original vector master, component-aware offsets, topology protection,
and optical normalization. This does not rely on faux bold in the renderer.
"""
from pathlib import Path
import json, math, unicodedata
from shapely.geometry import GeometryCollection
from shapely.ops import unary_union
from shapely.affinity import affine_transform
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.t2CharStringPen import T2CharStringPen
from fontTools.ttLib import TTFont, newTable
from fontTools.ttLib.tables._k_e_r_n import KernTable_format_0
from fontTools.feaLib.builder import addOpenTypeFeaturesFromString
import base_regular as b

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'fonts';OUT.mkdir(exist_ok=True)
STYLES=[('Thin','极细',100,-34),('Light','细体',300,-22),('Regular','常规',400,0),('Bold','粗体',700,27),('ExtraBold','特粗',800,55)]
ADJUSTMENTS=[]
APPROVED_B=json.loads((ROOT/'source'/'b-approved-outlines.json').read_text())['styles']

def components(s):
    if s.is_empty:return []
    if s.geom_type=='Polygon':return [s]
    return [p for p in s.geoms if p.geom_type=='Polygon' and p.area>1]
def holes(s):return sum(len(p.interiors) for p in components(s))
def valid_transform(original,changed,min_hole_ratio=.12):
    if not (not changed.is_empty and changed.is_valid and len(components(changed))==len(components(original)) and holes(changed)==holes(original) and changed.area>original.area*.06):return False
    old_holes=sorted([b.Polygon(r).area for p in components(original) for r in p.interiors])
    new_holes=sorted([b.Polygon(r).area for p in components(changed) for r in p.interiors])
    return all(n>=o*min_hole_ratio for o,n in zip(old_holes,new_holes))

def local_offset(p,delta):
    # Punctuation, small counters, and diacritics need less movement than capitals.
    actual=delta
    if delta<0:
        # A local scale prevents a 65-unit accent from disappearing when the main
        # 100-unit stem is reduced to the thin master.
        radius=p.area/max(p.length,1)
        actual=-min(abs(delta),radius*(.84 if delta<-25 else .57))
    result=p.buffer(actual,join_style=2,mitre_limit=3)
    if valid_transform(p,result):return result,actual
    lo,hi=0.,1.
    for _ in range(24):
        t=(lo+hi)/2
        q=p.buffer(actual*t,join_style=2,mitre_limit=3)
        if valid_transform(p,q):lo=t
        else:hi=t
    actual*=lo*.94
    return p.buffer(actual,join_style=2,mitre_limit=3),actual

def weight_shape(name,s,delta):
    if s.is_empty or delta==0:return s
    parts=[]; used=[]
    for p in components(s):
        q,actual=local_offset(p,delta)
        parts.append(q);used.append(actual)
    result=unary_union(parts)
    # Protect gaps between diacritics and stems and between neighboring elements.
    if not valid_transform(s,result):
        lo,hi=0.,1.
        for _ in range(24):
            k=(lo+hi)/2
            q=unary_union([p.buffer(a*k,join_style=2,mitre_limit=3) for p,a in zip(components(s),used)])
            if valid_transform(s,q):lo=k
            else:hi=k
        used=[a*lo*.94 for a in used]
        result=unary_union([p.buffer(a,join_style=2,mitre_limit=3) for p,a in zip(components(s),used)])
    # Keep cap height, x-height, baseline, advance, and the outside ink box stable.
    x0,y0,x1,y1=s.bounds;u0,v0,u1,v1=result.bounds
    sx=(x1-x0)/(u1-u0);sy=(y1-y0)/(v1-v0)
    result=affine_transform(result,[sx,0,0,sy,x0-u0*sx,y0-v0*sy]).buffer(0)
    assert valid_transform(s,result,.04),(name,delta)
    if any(abs(a-delta)>2 for a in used):ADJUSTMENTS.append({'glyph':name,'target_offset':delta,'local_offsets':[round(a,2) for a in used]})
    return result

def shapes_for(style,delta):
    shapes={n:weight_shape(n,s,delta) for n,s in b.SHAPES.items()}
    t={'Thin':28,'Light':58,'Regular':100,'Bold':148,'ExtraBold':190}[style]
    h=min(t*.9,140)
    custom={}
    def put(ch,s):custom[ch]=b.shift(s,b.SB,0)
    # Draw diagonal stems directly: a fixed counter-area safeguard had nearly
    # frozen A between Bold and ExtraBold. Cap height and advance stay fixed.
    slope=(420-.65*t)/700
    inset=t*math.sqrt(1+slope*slope)
    apex=(420-inset)/slope
    outer=b.poly([(0,0),(420-.65*t,700),(420+.65*t,700),(840,0)])
    legs=b.poly([(0,0),(420-.65*t,700),(420+.65*t,700),(840,0),(840-inset,0),(420,apex),(inset,0)])
    put('A',b.union(legs,b.rect(0,270-t*.45,840,270+t*.45).intersection(outer)))
    put('&',b.line([(735,520),(230,50),(95,50),(45,100),(45,260),(460,590),(460,645),(405,700),(220,700),(155,645),(155,570),(750,0)],t*.9))
    put('#',b.union(b.line([(155,0),(275,700)],t*.85),b.line([(460,0),(580,700)],t*.85),b.rect(0,235-t*.4,720,235+t*.4),b.rect(40,465-t*.4,760,465+t*.4)))
    def bowl(w=680,H=530,right_square=True):
        c=max(25,95-t*.55)
        outer=b.poly([(0,95),(0,H-95),(95,H),(w,H),(w,0),(95,0)])
        inner=b.poly([(t,h+c),(t,H-h-c),(t+c,H-h),(w-t,H-h),(w-t,h),(t+c,h)])
        result=outer.difference(inner)
        return result if right_square else b.shift(b.scaled(result,-1,1),w,0)
    put('Q',b.union(b.ring(820,700,t,t*.9),b.poly([(635-1.25*t,255),(635,255),(850,-35),(850-1.25*t,-35)])))
    put('0',b.union(b.ring(760,700,t,t*.9),b.diag((170,120),(590,580),t*.65)))
    for ch,w,H in [('Z',820,700),('z',670,530)]:
        if delta<0:
            a=b.line([(0,H-t/2),(w-t/2,H-t/2),(t/2,t/2),(w,t/2)],t)
            put(ch,a)
    for ch,w,H in [('K',835,700),('k',685,530)]:
        stemH=700
        a=b.union(b.rect(0,0,t,stemH),b.line([(t/2,H*.47),(w-t/2,H-t/2)],t),b.line([(t/2,H*.47),(w-t/2,t/2)],t))
        put(ch,a)
    # Three horizontal strokes must fit within the lowercase x-height.
    put('s',b.sform(640,530,132 if style=='Bold' else 152 if style=='ExtraBold' else t))
    eh=min(t*.75,140);mid=min(t*.65,120)
    upper_y=265+mid/2
    corner=min(max(25,95-t*.55),(530-eh-upper_y)/2.1)
    upper=b.octagon(680-2*t,530-eh-upper_y,corner,t,upper_y)
    lower=b.poly([(t,eh+corner),(t,265-mid/2),(700,265-mid/2),(700,eh),(t+corner,eh)])
    put('e',b.octagon(680,530,95).difference(upper).difference(lower))
    put('a',bowl())
    put('d',b.union(bowl(),b.rect(680-t,0,680,700)))
    put('q',b.union(bowl(),b.rect(680-t,-205,680,530)))
    put('b',b.union(bowl(right_square=False),b.rect(0,0,t,700)))
    put('p',b.union(bowl(right_square=False),b.rect(0,-205,t,530)))
    gh=min(t*.82,155)
    gbase=bowl()
    tail=b.line([(680-t/2,80),(680-t/2,-80),(560,-205+gh/2),(120,-205+gh/2)],gh)
    put('g',b.union(gbase,tail))
    dotw={'Thin':42,'Light':65,'Regular':105,'Bold':135,'ExtraBold':160}[style]
    put('i',b.union(b.rect(50-t/2,0,50+t/2,530),b.dot(50-dotw/2,714-dotw,dotw)))
    put('j',b.union(b.line([(210,530),(210,-80),(145,-205+t/2),(0,-205+t/2)],t),b.dot(210-dotw/2,714-dotw,dotw)))
    put('l',b.line([(t/2,700),(t/2,100),(100,t/2),(230,t/2)],t))
    put('!',b.union(b.rect(50-t/2,200,50+t/2,700),b.dot(50-dotw/2,0,dotw)))
    put('ı',b.rect(50-t/2,0,50+t/2,530))
    put('|',b.rect(40-t/2,-90,40+t/2,790))
    put('¦',b.union(b.rect(40-t/2,-90,40+t/2,260),b.rect(40-t/2,440,40+t/2,790)))
    for ch,w,cy in [('-',440,335),('‐',440,335),('‑',440,335),('\u00ad',440,335),('−',440,335),('–',720,335),('—',1080,335),('_',780,-130),('¯',430,665)]:put(ch,b.rect(0,cy-t*.45,w,cy+t*.45))
    put('.',b.dot(52.5-dotw/2,0,dotw))
    put('·',b.dot(52.5-dotw/2,342.5-dotw/2,dotw))
    bulletw={'Thin':95,'Light':135,'Regular':185,'Bold':220,'ExtraBold':255}[style]
    put('•',b.dot(92.5-bulletw/2,332.5-bulletw/2,bulletw))
    put(':',b.union(b.dot(52.5-dotw/2,0,dotw),b.dot(52.5-dotw/2,452.5-dotw/2,dotw)))
    comma=b.union(b.dot(87.5-dotw/2,0,dotw),b.poly([(87.5-dotw*.3,dotw*.4),(87.5+dotw/2,dotw*.4),(87.5+dotw*.02,-125),(87.5-dotw*.62,-125)]))
    put(',',comma)
    put(';',b.union(comma,b.dot(87.5-dotw/2,452.5-dotw/2,dotw)))
    put('…',b.union(*(b.dot(52.5+230*i-dotw/2,0,dotw) for i in range(3))))
    for ch,count in [("'",1),('"',2)]:
        pieces=[b.rect(42.5+185*i-t*.42,490,42.5+185*i+t*.42,700) for i in range(count)]
        put(ch,b.union(*pieces))
    # Normalize redesigned bowl/diagonal glyphs to the existing widths and metrics.
    keep_bearing=set('ij!ı|¦.\'"-_,;:·•…')|set('‐‑\u00ad−–—¯')
    for ch,s in custom.items():
        n=b.CMAP[ord(ch)]
        if ch not in keep_bearing:
            ref=b.SHAPES[n];x0,y0,x1,y1=ref.bounds;u0,v0,u1,v1=s.bounds
            sx=(x1-x0)/(u1-u0);sy=(y1-y0)/(v1-v0)
            s=affine_transform(s,[sx,0,0,sy,x0-u0*sx,y0-v0*sy]).buffer(0)
        shapes[n]=s
    if style=='Regular':shapes=dict(b.SHAPES)
    # Approved B: one shared middle stroke and a short flat waist. Import exact
    # integer contours from the approved proof, including the Regular master.
    br=APPROVED_B[style]['contours']
    shapes[b.CMAP[ord('B')]]=b.Polygon(br[0],br[1:])
    # Recompose derived letters from the same weighted bases; never offset the
    # combined glyph, where a small symbol can limit the whole letter's weight.
    def get(ch):return b.shift(shapes[b.CMAP[ord(ch)]],-b.SB,0)
    def derived(ch,s):shapes[b.CMAP[ord(ch)]]=b.shift(s,b.SB,0)
    derived('Æ',b.union(b.scaled(get('A'),.75,1),b.shift(get('E'),540,0)))
    def joined_bowl(joint,H,stem,hh):
        c=95;ci=max(25,c-stem*.55)
        outer=b.poly([(0,c),(0,H-c),(c,H),(joint+stem,H),(joint+stem,0),(c,0)])
        inner=b.poly([(stem,hh+ci),(stem,H-hh-ci),(stem+ci,H-hh),(joint,H-hh),(joint,hh),(stem+ci,hh)])
        return outer.difference(inner)
    # A shared square stem avoids tiny enclosed triangles where two cut-corner
    # bowls previously overlapped, particularly in the Thin ligatures.
    ejouter=b.poly([(0,0),(0,530),(585,530),(680,435),(680,95),(585,0)])
    ci=max(25,95-t*.55)
    ejupper=b.poly([(t,upper_y),(t,530-eh),(680-t-ci,530-eh),(680-t,530-eh-ci),(680-t,upper_y)])
    ejlower=b.rect(t,eh,700,265-mid/2)
    ejoined=ejouter.difference(ejupper).difference(ejlower)
    derived('æ',b.union(joined_bowl(480,530,t*.82,min(t*.9,140)),b.shift(ejoined,480,0)))
    derived('œ',b.union(joined_bowl(512,530,t*.9,min(t*.9,140)),b.shift(ejoined,512,0)))
    ehcap=t*.85
    ej=b.union(b.rect(638,0,638+t,700),b.rect(638,700-ehcap,1418,700),b.rect(638,355-ehcap/2,1343,355+ehcap/2),b.rect(638,0,1418,ehcap))
    derived('Œ',b.union(joined_bowl(638,700,t*.9,ehcap),ej))
    derived('ĸ',b.scaled(get('K'),.83,.757))
    derived('Ħ',b.union(get('H'),b.rect(-60,515-t*.35,880,515+t*.35)))
    derived('Ĳ',b.union(get('I'),b.shift(get('J'),440,0)))
    derived('ĳ',b.union(get('i'),b.shift(get('j'),210,0)))
    derived('Ŀ',b.union(get('L'),b.shift(get('·'),350,15)))
    derived('ŀ',b.union(get('l'),b.shift(get('·'),250,10)))
    for ch,base in [('ª','a'),('º','o')]:
        derived(ch,b.union(b.shift(b.scaled(get(base),.55,.55),0,410),b.rect(0,340-t*.25,374,340+t*.25)))
    for ch,num in [('¹','1'),('²','2'),('³','3')]:derived(ch,b.shift(b.scaled(get(num),.53,.53),0,330))
    for ch,top,bottom in [('¼','1','4'),('½','1','2'),('¾','3','4')]:
        derived(ch,b.union(b.shift(b.scaled(get(top),.47,.47),0,371),b.shift(b.scaled(get(bottom),.47,.47),485,0),b.diag((300,0),(595,700),t*.65)))
    for ch,base in [('≤','<'),('≥','>')]:derived(ch,b.union(b.shift(b.scaled(get(base),1,.8),0,100),b.rect(0,0,630,t*.65)))
    derived('¡',b.shift(b.scaled(get('!'),1,-1),0,530))
    derived('¿',b.shift(b.scaled(get('?'),-1,-1),665,530))
    derived('‰',b.union(b.scaled(get('%'),.85,1),b.shift(b.ring(270,300,min(t*.58,110),min(t*.58,110),50),730,0)))
    derived('™',b.union(b.shift(b.scaled(get('T'),.43,.43),0,400),b.shift(b.scaled(get('M'),.43,.43),425,400)))
    yh=80 if style=='Regular' else t*.65
    derived('¥',b.union(get('Y'),b.rect(145,245-yh/2,695,245+yh/2),b.rect(145,110-yh/2,695,110+yh/2)))
    derived('≠',b.union(get('='),b.diag((190,50),(460,650),t*.75)))
    arrow=b.union(b.rect(60,350-t*.4,760,350+t*.4),b.line([(330,630),(50,350),(330,70)],t*.85))
    derived('↔',b.union(arrow,b.shift(b.scaled(arrow,-1,1),820,0)))
    punctscale={'Thin':.60,'Light':.78,'Regular':1,'Bold':1.15,'ExtraBold':1.32}[style]
    for ch in '‘’‚“”„′″`´¨¸':
        ref=b.G[ch];x0,y0,x1,y1=ref.bounds;cx=(x0+x1)/2;cy=(y0+y1)/2
        derived(ch,affine_transform(ref,[punctscale,0,0,punctscale,cx*(1-punctscale),cy*(1-punctscale)]))
    # The separate brand mark has three disconnected strokes. Weight them
    # independently without allowing their spacing to cap the whole symbol.
    logo_name=b.CMAP[0xE000]
    shapes[logo_name]=b.union(*(weight_shape(logo_name+str(i),p,delta) for i,p in enumerate(components(b.SHAPES[logo_name]))))
    # All precomposed accents inherit the exact base from this weight. Scale
    # accent groups independently so they cannot make the base thinner.
    markscale={'Thin':.60,'Light':.78,'Regular':1,'Bold':1.12,'ExtraBold':1.26}[style]
    for cp,n in b.CMAP.items():
        ch=chr(cp);nfd=unicodedata.normalize('NFD',ch)
        if len(nfd)>1 and ord(nfd[0]) in b.CMAP and all(m in '\u0300\u0301\u0302\u0303\u0304\u0306\u0307\u0308\u030a\u030b\u030c\u0327\u0328' for m in nfd[1:]):
            base=nfd[0];bn=b.CMAP[ord(base)]
            if '\u0327' in nfd or '\u0328' in nfd:
                base_shape=shapes[bn]
                ct={'Thin':24,'Light':40,'Regular':65,'Bold':82,'ExtraBold':99}[style]
                if base=='g':
                    # Standard Latvian lowercase g uses a turned comma above.
                    mark=b.scaled(get(','),-.65,-.65)
                    x0,y0,x1,y1=mark.bounds
                    mark=b.shift(mark,b.SB+340-(x0+x1)/2,585-y0)
                elif '\u0328' in nfd:
                    cut=base_shape.intersection(b.LineString([(-1000,5),(3000,5)]))
                    segs=[cut] if cut.geom_type=='LineString' else [p for p in cut.geoms if p.geom_type=='LineString']
                    right=max(segs,key=lambda p:p.bounds[2])
                    anchor=right.bounds[2]-min(ct*.5,(right.bounds[2]-right.bounds[0])*.5)
                    mark=b.line([(anchor,12),(anchor-70,-60),(anchor-70,-120),(anchor-20,-175),(anchor+80,-175)],ct)
                else:
                    anchor=(base_shape.bounds[0]+base_shape.bounds[2])/2
                    mark=b.line([(anchor,12),(anchor,-35),(anchor+60,-85),(anchor+60,-135),(anchor+10,-175),(anchor-95,-175)],ct)
                shapes[n]=b.union(base_shape,mark)
                continue
            if base in 'ij':
                without_dot=b.SHAPES[bn].difference(b.rect(-500+b.SB,590,500+b.SB,1000))
                extra=b.SHAPES[n].difference(without_dot)
                base_shape=b.union(*(p for p in components(shapes[bn]) if p.bounds[1]<530))
            else:
                extra=b.SHAPES[n].difference(b.SHAPES[bn]);base_shape=shapes[bn]
            if not extra.is_empty:
                x0,y0,x1,y1=extra.bounds;cx=(x0+x1)/2;cy=(y0+y1)/2
                mark=affine_transform(extra,[markscale,0,0,markscale,cx*(1-markscale),cy*(1-markscale)])
                if y0>=530:
                    low=base_shape.bounds[3]+32
                    if mark.bounds[1]<low:mark=b.shift(mark,0,low-mark.bounds[1])
                    if mark.bounds[3]>970:mark=b.shift(mark,0,970-mark.bounds[3])
                elif mark.bounds[1]<-240:mark=b.shift(mark,0,-240-mark.bounds[1])
                shapes[n]=b.union(base_shape,mark)
    return shapes

def build(style,zh,weight,shapes,is_ttf):
    fb=FontBuilder(1000,isTTF=is_ttf)
    fb.setupGlyphOrder(b.ORDER);fb.setupCharacterMap(b.CMAP)
    if is_ttf:
        glyphs={}
        for n in b.ORDER:
            pen=TTGlyphPen(None);b.draw(pen,shapes[n]);glyphs[n]=pen.glyph()
        fb.setupGlyf(glyphs)
    else:
        charstrings={}
        for n in b.ORDER:
            pen=T2CharStringPen(b.METRICS[n][0],None);b.draw(pen,shapes[n]);charstrings[n]=pen.getCharString()
        fb.setupCFF('XUQU-'+style,{'FullName':'XUQU '+style,'FamilyName':'XUQU','Weight':style,'version':'1.300','Notice':'Custom XUQU outline family.'},charstrings,{})
    metrics={n:(b.METRICS[n][0],round(s.bounds[0]) if not s.is_empty else 0) for n,s in shapes.items()}
    fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=960,descent=-250,lineGap=0)
    # Legacy RIBBI grouping plus typographic family/subfamily naming.
    legacy_family='XUQU体' if style in ('Regular','Bold') else 'XUQU体 '+style
    legacy_style='Bold' if style=='Bold' else 'Regular'
    fb.setupNameTable({'familyName':legacy_family,'styleName':legacy_style,'uniqueFontIdentifier':'XUQUTECH:XUQU-'+style+':1.300','fullName':'XUQU体 '+style,'psName':'XUQU-'+style,'version':'Version 1.300','copyright':'XUQU typeface. Created for XUQUTECH, 2026.','designer':'XUQUTECH / AI-assisted custom type design','description':'Wide geometric Latin display family. '+style+' weight.','licenseDescription':'Custom font asset delivered to XUQUTECH. No third-party font outlines incorporated.'},mac=False)
    names=fb.font['name']
    names.setName('XUQU体',16,3,1,0x409);names.setName(style,17,3,1,0x409)
    names.setName('XUQU体',16,3,1,0x804);names.setName(zh,17,3,1,0x804)
    names.setName('XUQU体' if style in ('Regular','Bold') else 'XUQU体 '+zh,1,3,1,0x804)
    names.setName('粗体' if style=='Bold' else '常规',2,3,1,0x804)
    names.setName('XUQU体 '+zh,4,3,1,0x804)
    for nid,val in [(1,'XUQU' if style in ('Regular','Bold') else 'XUQU '+style),(2,legacy_style),(4,'XUQU '+style),(6,'XUQU-'+style)]:names.setName(val,nid,1,0,0)
    fs=0x80|(0x20 if style=='Bold' else 0x40)
    fb.setupOS2(version=4,sTypoAscender=960,sTypoDescender=-250,sTypoLineGap=0,usWinAscent=980,usWinDescent=260,sxHeight=530,sCapHeight=700,usWeightClass=weight,usWidthClass=7,fsType=0,fsSelection=fs,achVendID='XUQU')
    fb.setupPost(underlinePosition=-150,underlineThickness=max(30,round(70*weight/400)))
    fb.setupMaxp()
    fb.font['head'].macStyle=1 if style=='Bold' else 0
    fb.font['head'].fontRevision=1.3
    if is_ttf:
        gasp=newTable('gasp');gasp.gaspRange={65535:15};fb.font['gasp']=gasp
    fea='languagesystem DFLT dflt;\nlanguagesystem latn dflt;\nfeature kern {\n'+'\n'.join(f'pos {l} {r} {v};' for (l,r),v in sorted(b.PAIRS.items()) if v)+'\n} kern;'
    addOpenTypeFeaturesFromString(fb.font,fea)
    if is_ttf:
        kt=newTable('kern');kt.version=0;st=KernTable_format_0();st.version=0;st.coverage=1;st.kernTable={k:v for k,v in b.PAIRS.items() if v};kt.kernTables=[st];fb.font['kern']=kt
    path=OUT/f'XUQU-{style}.{"ttf" if is_ttf else "otf"}'
    fb.font.save(path)
    return path

if __name__=='__main__':
    result=[]
    for style,zh,weight,delta in STYLES:
        shapes=shapes_for(style,delta)
        ttf=build(style,zh,weight,shapes,True)
        build(style,zh,weight,shapes,False)
        web=TTFont(ttf);web.flavor='woff2';web.save(OUT/f'XUQU-{style}.woff2')
        result.append({'style':style,'chinese_style':zh,'weight_class':weight,'characters':len(b.CMAP),'new':bool(delta)})
    report={'family':'XUQU体','family_release':'1.3','styles':result,'regular_primary_letterforms_preserved_except':['B'],'approved_B_source':'b-approved-outlines.json','outline_method':'approved shared-stroke B; drawn diagonal and punctuation masters; independent accent composition; component-aware offsets; full-character weight regression','optical_adjustments':ADJUSTMENTS}
    (ROOT/'source'/'family-build.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print(json.dumps({'family':report['family'],'styles':result,'optical_adjustments':len(ADJUSTMENTS)},ensure_ascii=False,indent=2))
