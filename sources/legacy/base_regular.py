#!/usr/bin/env python3
"""XUQU体 1.000 — original geometric outlines derived from the supplied wordmark.

Run: python source/build_font.py
Requires: fonttools, shapely, brotli, pillow, uharfbuzz.
All coordinates and Latin letter outlines are authored in this file.
"""
from pathlib import Path
import json, math, unicodedata
from shapely.geometry import Polygon, LineString, box, GeometryCollection
from shapely.ops import unary_union
from shapely.affinity import translate, scale
from shapely.geometry.polygon import orient
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.t2CharStringPen import T2CharStringPen
from fontTools.ttLib import TTFont, newTable
from fontTools.ttLib.tables._k_e_r_n import KernTable_format_0
from fontTools.feaLib.builder import addOpenTypeFeaturesFromString
from fontTools.agl import UV2AGL

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'fonts'
OUT.mkdir(exist_ok=True)
UPM, CAP, XH, T, TH, SB = 1000, 700, 530, 100, 90, 58
G, WIDTH = {}, {}

def poly(points): return Polygon(points)
def rect(x0,y0,x1,y1): return box(x0,y0,x1,y1)
def union(*items): return unary_union([x for x in items if not x.is_empty]).buffer(0)
def shift(s,x=0,y=0): return translate(s,xoff=x,yoff=y)
def scaled(s,x=1,y=1): return scale(s,xfact=x,yfact=y,origin=(0,0))
def line(points,t=T):
    return LineString(points).buffer(t/2,cap_style=2,join_style=2,mitre_limit=3)
def octagon(w,h,c=95,x=0,y=0):
    c=min(c,w/3,h/3)
    return shift(poly([(0,c),(0,h-c),(c,h),(w-c,h),(w,h-c),(w,c),(w-c,0),(c,0)]),x,y)
def ring(w=820,h=CAP,t=T,th=TH,c=95):
    return octagon(w,h,c).difference(octagon(w-2*t,h-2*th,max(25,c-t*.55),t,th))
def cform(w=820,h=CAP,t=T):
    return poly([(w,h),(95,h),(0,h-95),(0,95),(95,0),(w,0),(w,TH),(140,TH),(t,130),(t,h-130),(140,h-TH),(w,h-TH)])
def uform(w=820,h=CAP,t=T):
    outer=poly([(0,h),(w,h),(w,95),(w-95,0),(95,0),(0,95)])
    inner=poly([(t,h+10),(w-t,h+10),(w-t,130),(w-140,TH),(140,TH),(t,130)])
    return outer.difference(inner)
def dform(w=820,h=CAP):
    outer=poly([(0,0),(w-110,0),(w,110),(w,h-110),(w-110,h),(0,h)])
    inner=poly([(T,TH),(w-155,TH),(w-T,145),(w-T,h-145),(w-155,h-TH),(T,h-TH)])
    return outer.difference(inner)
def arch(w=680,h=XH):
    return shift(scaled(uform(w,h),1,-1),0,h)
def dot(x=0,y=0,s=105): return octagon(s,s,14,x,y)
def add(ch,s,w=None):
    s=s.buffer(0)
    if w is None: w=s.bounds[2] if not s.is_empty else 300
    G[ch],WIDTH[ch]=s,int(round(w))
def diag(p1,p2,t=105): return line([p1,p2],t)

# Uppercase: wide proportions, cut corners, flat terminals.
w=840
add('A',union(poly([(0,0),(355,700),(485,700),(840,0),(722,0),(420,595),(118,0)]),rect(197,225,643,315)),840)
add('B',union(dform(790,375),shift(dform(760,365),0,335)),790)
add('C',cform(),820)
add('D',dform(),820)
add('E',union(cform(780),rect(65,310,705,400)),780)
add('F',union(rect(0,0,T,700),rect(0,610,780,700),rect(0,310,700,400)),780)
add('G',union(cform(),rect(440,285,820,375),rect(720,90,820,330)),820)
add('H',union(rect(0,0,T,700),rect(720,0,820,700),rect(0,305,820,395)),820)
add('I',union(rect(0,610,360,700),rect(130,0,230,700),rect(0,0,360,90)),360)
add('J',union(uform(680).difference(rect(-10,270,130,710)),rect(305,610,680,700)),680)
add('K',union(rect(0,0,T,700),poly([(90,335),(670,700),(820,700),(220,325)]),poly([(150,395),(835,0),(655,0),(70,330)])),835)
add('L',union(rect(0,0,T,700),rect(0,0,740,90)),740)
add('M',poly([(0,0),(0,700),(110,700),(500,215),(890,700),(1000,700),(1000,0),(900,0),(900,540),(542,95),(458,95),(100,540),(100,0)]),1000)
add('N',poly([(0,0),(0,700),(110,700),(720,160),(720,700),(820,700),(820,0),(710,0),(100,540),(100,0)]),820)
add('O',ring(),820)
add('P',union(shift(dform(790,400),0,300),rect(0,0,T,400)),790)
add('Q',union(ring(),poly([(510,255),(635,255),(850,-35),(725,-35)])),850)
add('R',union(G['P'],poly([(395,335),(515,335),(835,0),(685,0)])),835)
def sform(w=800,h=700,t=100):
    mid=h/2
    pts=[(w-8,h-t/2),(125,h-t/2),(t/2,h-125),(t/2,mid+85),(130,mid),(w-130,mid),(w-t/2,mid-85),(w-t/2,125),(w-125,t/2),(8,t/2)]
    return line(pts,t)
add('S',sform(),800)
add('T',union(rect(0,610,840,700),rect(370,0,470,700)),840)
add('U',uform(),820)
add('V',poly([(0,700),(118,700),(420,100),(722,700),(840,700),(485,0),(355,0)]),840)
add('W',poly([(0,700),(112,700),(300,140),(494,700),(606,700),(800,140),(988,700),(1100,700),(866,0),(741,0),(550,554),(359,0),(234,0)]),1100)
add('X',union(poly([(0,700),(138,700),(840,0),(702,0)]),poly([(0,0),(138,0),(840,700),(702,700)])),840)
add('Y',union(poly([(0,700),(130,700),(420,370),(710,700),(840,700),(470,280),(370,280)]),rect(370,0,470,330)),840)
add('Z',union(rect(0,610,820,700),rect(0,0,820,90),poly([(0,90),(0,130),(687,700),(820,610),(133,0)])),820)

# Independent lowercase, single-storey a and g with a large x-height.
add('a',union(ring(680,XH),rect(580,0,680,XH)),680)
add('b',union(ring(680,XH),rect(0,0,100,700)),680)
add('c',cform(670,XH),670)
add('d',union(ring(680,XH),rect(580,0,680,700)),680)
add('e',union(cform(680,XH),rect(50,230,680,315),rect(580,270,680,440)),680)
add('f',union(rect(175,0,275,620),line([(225,590),(225,630),(290,680),(525,680)],100),rect(0,440,480,530)),540)
add('g',union(ring(680,XH),rect(580,-65,680,XH),line([(630,-50),(630,-90),(560,-155),(120,-155)],100)),680)
add('h',union(arch(),rect(0,0,100,700)),680)
add('i',union(rect(0,0,100,530),dot(-2,610,104)),102)
add('j',union(rect(160,-80,260,530),line([(210,-45),(210,-100),(150,-155),(0,-155)],100),dot(158,610,104)),262)
add('k',union(rect(0,0,100,700),poly([(80,235),(510,530),(660,530),(180,210)]),poly([(165,305),(685,0),(510,0),(65,255)])),685)
add('l',union(rect(0,100,100,700),line([(50,150),(50,100),(100,50),(230,50)],100)),230)
add('m',union(arch(550),shift(arch(550),450,0)),1000)
add('n',arch(),680)
add('o',ring(680,XH),680)
add('p',union(ring(680,XH),rect(0,-205,100,XH)),680)
add('q',union(ring(680,XH),rect(580,-205,680,XH)),680)
add('r',union(rect(0,0,100,530),line([(50,420),(120,480),(475,480)],100)),500)
add('s',sform(640,XH,90),640)
add('t',union(rect(145,130,245,670),rect(0,440,505,530),line([(195,150),(195,105),(255,50),(515,50)],100)),520)
add('u',uform(680,XH),680)
add('v',poly([(0,530),(112,530),(340,100),(568,530),(680,530),(397,0),(283,0)]),680)
add('w',poly([(0,530),(110,530),(250,125),(413,530),(517,530),(680,125),(820,530),(930,530),(746,0),(626,0),(465,401),(304,0),(184,0)]),930)
add('x',union(poly([(0,530),(130,530),(690,0),(560,0)]),poly([(0,0),(130,0),(690,530),(560,530)])),690)
add('y',union(poly([(0,530),(112,530),(342,92),(578,530),(690,530),(315,-175),(220,-215),(50,-215),(50,-115),(215,-115),(285,5)])),690)
add('z',union(rect(0,440,670,530),rect(0,0,670,90),poly([(0,90),(0,115),(540,530),(670,440),(130,0)])),670)

# Lining tabular numerals, 0 clearly distinguished from O with a diagonal.
nw=760
add('0',union(ring(nw),diag((170,120),(590,580),65)),nw)
add('1',union(rect(350,0,450,700),rect(125,0,655,90),poly([(350,700),(450,700),(450,590),(150,455),(108,543)])),nw)
add('2',line([(50,535),(50,580),(125,650),(630,650),(710,575),(710,445),(645,380),(50,90),(50,50),(760,50)],100),nw)
add('3',union(line([(0,650),(625,650),(710,565),(710,430),(630,350),(335,350)],100),line([(390,350),(630,350),(710,270),(710,130),(630,50),(0,50)],100)),nw)
add('4',union(poly([(505,700),(625,700),(150,235),(760,235),(760,145),(0,145),(0,240)]),rect(505,0,605,700)),nw)
add('5',line([(760,650),(50,650),(50,370),(625,370),(710,285),(710,130),(630,50),(0,50)],100),nw)
add('6',union(ring(nw,385),line([(50,315),(50,565),(135,650),(680,650)],100)),nw)
add('7',union(rect(0,610,760,700),poly([(640,660),(760,650),(315,0),(195,0)])),nw)
add('8',union(ring(nw,380),shift(ring(nw,365),0,335)),nw)
add('9',union(shift(ring(nw,385),0,315),line([(710,385),(710,135),(625,50),(80,50)],100)),nw)

# ASCII punctuation.
add(' ',GeometryCollection(),330)
add('!',union(rect(0,200,100,700),dot(0,0)),105)
add('"',union(rect(0,490,85,700),rect(185,490,270,700)),270)
add('#',union(line([(155,0),(275,700)],85),line([(460,0),(580,700)],85),rect(0,190,720,280),rect(40,420,760,510)),760)
add('$',union(scaled(G['S'],.84,1),rect(285,-90,365,790)),680)
add('%',union(shift(ring(300,300,70,65,55),0,400),shift(ring(300,300,70,65,55),490,0),diag((110,0),(680,700),85)),790)
amp=line([(735,520),(230,50),(95,50),(45,100),(45,260),(460,590),(460,645),(405,700),(220,700),(155,645),(155,570),(750,0)],90)
add('&',amp,790)
add("'",rect(0,490,85,700),85)
add('(',line([(250,790),(65,590),(65,110),(250,-90)],85),290)
add(')',line([(40,790),(225,590),(225,110),(40,-90)],85),290)
add('*',union(line([(250,650),(250,200)],70),line([(30,540),(470,310)],70),line([(30,310),(470,540)],70)),500)
add('+',union(rect(0,290,650,380),rect(280,55,370,615)),650)
add(',',union(dot(35,0),poly([(35,35),(140,35),(80,-125),(0,-125)])),145)
add('-',rect(0,290,440,380),440)
add('.',dot(),105)
add('/',diag((45,-80),(485,780),85),530)
add(':',union(dot(0,0),dot(0,400)),105)
add(';',union(G[','],dot(35,400)),145)
add('<',line([(580,620),(50,350),(580,80)],90),630)
add('=',union(rect(0,170,650,260),rect(0,430,650,520)),650)
add('>',line([(50,620),(580,350),(50,80)],90),630)
add('?',union(line([(50,540),(50,590),(115,650),(550,650),(615,585),(615,475),(345,320),(345,210)],100),dot(293,0)),665)
at=ring(940,700,80,80,105)
at=at.difference(rect(500,-1,941,100))
at=union(at,shift(ring(415,355,75,70,60),265,175),rect(605,175,680,530),line([(642,225),(642,120),(805,120),(900,215)],75))
add('@',at,940)
add('[',union(rect(0,-90,90,790),rect(0,700,290,790),rect(0,-90,290,0)),290)
add('\\',diag((45,780),(485,-80),85),530)
add(']',union(rect(200,-90,290,790),rect(0,700,290,790),rect(0,-90,290,0)),290)
add('^',line([(30,450),(300,710),(570,450)],80),600)
add('_',rect(0,-170,780,-90),780)
add('`',poly([(0,760),(95,760),(210,595),(130,595)]),210)
add('{',line([(300,750),(180,750),(125,695),(125,435),(40,350),(125,265),(125,5),(180,-50),(300,-50)],80),330)
add('|',rect(0,-90,80,790),80)
add('}',scaled(G['{'],-1,1),330)
G['}']=shift(G['}'],330,0)
add('~',line([(20,300),(130,405),(245,405),(430,285),(540,285),(650,390)],75),680)

# Non-ASCII Latin letters and symbols, all Latin-1 printable code points.
add('Æ',union(scaled(G['A'],.75,1),shift(G['E'],540,0)),1320)
add('æ',union(scaled(G['a'],.82,1),shift(G['e'],480,0)),1160)
add('Ø',union(G['O'],diag((70,-45),(750,745),85)),820)
add('ø',union(G['o'],diag((50,-40),(630,570),75)),680)
add('Ð',union(G['D'],rect(-70,305,425,395)),820)
add('ð',union(G['o'],line([(630,430),(600,610),(300,730)],90),line([(290,570),(615,730)],70)),680)
add('Þ',union(shift(dform(780,400),0,155),rect(0,0,100,700)),780)
add('þ',union(G['p'],rect(0,0,100,700)),680)
add('ß',union(rect(0,0,100,595),line([(50,560),(50,620),(110,680),(445,680),(510,615),(510,525),(350,380),(585,260),(630,210),(630,120),(560,50),(265,50)],95)),680)
add('ı',rect(0,0,100,530),100)
add('Œ',union(scaled(G['O'],.9,1),shift(G['E'],638,0)),1418)
add('œ',union(scaled(G['o'],.9,1),shift(G['e'],512,0)),1192)
add('Ł',union(G['L'],line([(-65,190),(510,510)],85)),740)
add('ł',union(G['l'],line([(-60,300),(270,515)],70)),270)
add('Đ',G['Ð'],820)
add('đ',union(G['d'],rect(345,585,785,665)),785)
add('Ħ',union(G['H'],rect(-60,475,880,555)),880)
add('ħ',union(G['h'],rect(-50,585,300,660)),680)
add('Ŋ',union(G['N'],line([(770,55),(770,-80),(695,-155),(455,-155)],100)),820)
add('ŋ',union(G['n'],line([(630,60),(630,-80),(555,-155),(335,-155)],100)),680)
add('Ŧ',union(G['T'],rect(160,340,680,430)),840)
add('ŧ',union(G['t'],rect(40,270,410,355)),520)
add('ſ',G['f'].difference(rect(275,-5,550,540)),540)
add('ĸ',scaled(G['K'],.83,.757),694)
add('Ĳ',union(G['I'],shift(G['J'],440,0)),1120)
add('ĳ',union(G['i'],shift(G['j'],210,0)),472)
add('Ŀ',union(G['L'],dot(350,305)),740)
add('ŀ',union(G['l'],dot(250,300)),355)
add('ŉ',union(shift(G['n'],145,0),rect(0,570,80,740)),825)

def accent(mark,cx,y):
    if mark=='\u0300': return shift(poly([(-165,150),(-60,150),(80,0),(-15,0)]),cx,y)
    if mark=='\u0301': return shift(poly([(-80,0),(15,0),(165,150),(60,150)]),cx,y)
    if mark=='\u0302': return shift(poly([(-210,0),(-95,0),(0,80),(95,0),(210,0),(40,155),(-40,155)]),cx,y)
    if mark=='\u0303': return shift(line([(-190,35),(-110,105),(-45,105),(50,35),(115,35),(185,105)],55),cx,y)
    if mark=='\u0308': return union(dot(cx-160,y,85),dot(cx+75,y,85))
    if mark=='\u030a': return shift(ring(195,160,50,45,40),cx-97,y)
    if mark=='\u0304': return rect(cx-180,y+30,cx+180,y+95)
    if mark=='\u0306': return shift(line([(-165,130),(-90,40),(90,40),(165,130)],60),cx,y)
    if mark=='\u0307': return dot(cx-45,y+25,90)
    if mark=='\u030b': return union(accent('\u0301',cx-105,y),accent('\u0301',cx+105,y))
    if mark=='\u030c': return shift(poly([(-210,155),(-95,155),(0,75),(95,155),(210,155),(40,0),(-40,0)]),cx,y)
    if mark=='\u0327': return shift(line([(10,5),(10,-35),(70,-85),(70,-135),(20,-175),(-85,-175)],65),cx,0)
    if mark=='\u0328': return shift(line([(85,15),(0,-75),(0,-130),(55,-175),(155,-175)],65),cx,0)
    raise ValueError(mark)

for cp in list(range(0xC0,0x100))+list(range(0x100,0x180)):
    ch=chr(cp)
    if ch in G: continue
    decomp=unicodedata.normalize('NFD',ch)
    if len(decomp)>=2 and decomp[0] in G:
        base=decomp[0]; w=WIDTH[base]
        shape=G['ı'] if base=='i' else G[base]
        if base=='j': shape=shape.difference(rect(-20,590,WIDTH[base]+20,800))
        y=max(shape.bounds[3]+55,585)
        try:
            for m in decomp[1:]:
                a=accent(m,w*.5,y)
                if w<300:
                    a=scale(a,xfact=.60,yfact=1,origin=(w*.5,0))
                shape=union(shape,a)
            add(ch,shape,w)
        except ValueError: pass

add('\u00a0',G[' '],330)
add('¡',shift(scaled(G['!'],1,-1),0,530),105)
add('¢',union(G['c'],rect(295,-90,375,620)),680)
add('£',union(line([(705,620),(635,680),(260,680),(195,615),(195,75)],100),rect(0,0,730,90),rect(60,300,515,390)),760)
add('¤',union(shift(ring(470,470,80,75,60),100,110),diag((50,60),(160,170),75),diag((510,520),(620,630),75),diag((50,630),(160,520),75),diag((510,170),(620,60),75)),680)
add('¥',union(G['Y'],rect(145,205,695,285),rect(145,70,695,150)),840)
add('¦',union(rect(0,440,80,790),rect(0,-90,80,260)),80)
add('§',union(shift(scaled(G['S'],.65,.67),0,260),shift(scaled(G['S'],.65,.67),0,-90)),530)
add('¨',accent('\u0308',180,600),360)
def enclosed(letter,registered=False):
    inside=scaled(G[letter],.47,.47)
    return union(ring(840,840,65,65,150),shift(inside,(840-WIDTH[letter]*.47)/2,255))
add('©',enclosed('C'),840)
add('®',enclosed('R',True),840)
add('ª',union(shift(scaled(G['a'],.55,.55),0,410),rect(0,310,374,370)),374)
add('º',union(shift(scaled(G['o'],.55,.55),0,410),rect(0,310,374,370)),374)
add('«',union(scaled(G['<'],.55,.72),shift(scaled(G['<'],.55,.72),265,0)),630)
add('»',union(scaled(G['>'],.55,.72),shift(scaled(G['>'],.55,.72),265,0)),630)
add('¬',union(rect(0,380,650,470),rect(560,170,650,470)),650)
add('\u00ad',G['-'],440)
add('¯',rect(0,630,430,700),430)
add('°',shift(ring(320,320,70,65,60),0,380),320)
add('±',union(shift(scaled(G['+'],1,.8),0,145),rect(0,0,650,80)),650)
for c,n in [('¹','1'),('²','2'),('³','3')]: add(c,shift(scaled(G[n],.53,.53),0,330),403)
add('´',accent('\u0301',140,590),300)
add('µ',union(G['u'],rect(0,-205,100,530)),680)
add('¶',union(shift(dform(630,420),0,280),rect(530,-90,630,700),rect(730,-90,830,700),rect(550,610,830,700)),830)
add('·',dot(0,290),105)
add('¸',shift(accent('\u0327',100,0),0,0),220)
def fraction(a,b):
    return union(shift(scaled(G[a],.47,.47),0,371),shift(scaled(G[b],.47,.47),485,0),diag((300,0),(595,700),65))
for c,a,b in [('¼','1','4'),('½','1','2'),('¾','3','4')]: add(c,fraction(a,b),850)
add('¿',shift(scaled(G['?'],-1,-1),665,530),665)
add('×',union(diag((55,100),(595,600),85),diag((55,600),(595,100),85)),650)
add('÷',union(rect(0,305,650,395),dot(272,75),dot(272,520)),650)
add('€',union(cform(760),rect(-65,395,575,470),rect(-65,240,535,315)),760)
add('ƒ',union(G['f'],line([(225,100),(225,-95),(165,-155),(0,-155)],100)),540)
add('™',union(shift(scaled(G['T'],.43,.43),0,400),shift(scaled(G['M'],.43,.43),425,400)),855)

# Typography and useful display symbols.
add('‐',G['-'],440); add('‑',G['-'],440)
add('–',rect(0,290,720,380),720); add('—',rect(0,290,1080,380),1080)
add('‘',union(rect(0,480,90,610),poly([(0,580),(90,580),(145,720),(60,720)])),145)
add('’',union(rect(55,590,145,720),poly([(55,630),(145,630),(85,480),(0,480)])),145)
add('‚',shift(G['’'],0,-590),145)
add('“',union(G['‘'],shift(G['‘'],195,0)),340)
add('”',union(G['’'],shift(G['’'],195,0)),340)
add('„',shift(G['”'],0,-590),340)
add('…',union(dot(),dot(230),dot(460)),565)
add('•',dot(0,240,185),185)
add('‹',scaled(G['<'],.55,.72),347); add('›',scaled(G['>'],.55,.72),347)
add('†',union(rect(240,-90,320,730),rect(0,410,560,490)),560)
add('‡',union(G['†'],rect(0,150,560,230)),560)
add('‰',union(scaled(G['%'],.85,1),shift(ring(270,300,65,65,50),730,0)),1000)
add('′',poly([(0,470),(85,470),(160,720),(65,720)]),160)
add('″',union(G['′'],shift(G['′'],180,0)),340)
add('−',G['-'],440)
add('≠',union(G['='],diag((190,50),(460,650),75)),650)
add('≤',union(shift(scaled(G['<'],1,.8),0,100),rect(0,0,630,75)),630)
add('≥',union(shift(scaled(G['>'],1,.8),0,100),rect(0,0,630,75)),630)
add('√',line([(0,240),(120,350),(280,30),(530,700),(800,700)],85),810)
add('∞',line([(440,350),(245,535),(100,535),(40,475),(40,235),(100,175),(245,175),(635,535),(780,535),(840,475),(840,235),(780,175),(635,175),(440,350)],85),890)
add('←',union(rect(60,310,820,390),line([(330,630),(50,350),(330,70)],85)),820)
add('→',shift(scaled(G['←'],-1,1),820,0),820)
add('↑',union(rect(310,30,390,690),line([(70,410),(350,690),(630,410)],85)),700)
add('↓',shift(scaled(G['↑'],1,-1),0,720),700)
add('↔',union(G['←'],G['→']),820)
for ch,w in [('\u2002',500),('\u2003',1000),('\u2009',200),('\u202f',200)]: add(ch,GeometryCollection(),w)

# X brand symbol on a private-use code point, available separately from letter X.
logo=union(poly([(0,700),(173,700),(534,352),(174,0),(0,0),(343,315),(417,315),(443,352),(415,382),(317,382)]),poly([(504,457),(733,700),(896,700),(574,385)]),poly([(574,310),(896,0),(723,0),(508,234)]))
# The symbol is deliberately not substituted automatically for typed X.
add('\ue000',logo,896)

# Prepare clean, rounded, consistently oriented polygon contours.
def contours(shape):
    if shape.is_empty: return []
    if shape.geom_type=='Polygon': geoms=[shape]
    else: geoms=[p for p in shape.geoms if p.geom_type=='Polygon']
    result=[]
    for p in geoms:
        p=orient(p,sign=-1)
        for r in [p.exterior,*p.interiors]:
            coords=[]
            for x,y in list(r.coords)[:-1]:
                v=(round(x),round(y))
                if not coords or v!=coords[-1]: coords.append(v)
            if len(coords)>=3: result.append(coords)
    return result

def glyphname(cp): return UV2AGL.get(cp, f'uni{cp:04X}')
CMAP={ord(ch):glyphname(ord(ch)) for ch in G}
ORDER=['.notdef','.null','nonmarkingreturn']+list(dict.fromkeys(CMAP.values()))
SHAPES={'.notdef':shift(ring(640,700,75,75,50),SB,0),'.null':GeometryCollection(),'nonmarkingreturn':GeometryCollection()}
METRICS={'.notdef':(756,58),'.null':(0,0),'nonmarkingreturn':(330,0)}
for ch,s in G.items():
    # Preserve designed proportions and sidebearings even on overhanging accents.
    s=shift(s,SB,0)
    name=CMAP[ord(ch)]
    SHAPES[name]=s
    METRICS[name]=(WIDTH[ch]+SB*2,round(s.bounds[0]) if not s.is_empty else 0)

PAIRS={}
def kern(left,right,value):
    for l in left:
        for r in right:
            if ord(l) in CMAP and ord(r) in CMAP: PAIRS[(CMAP[ord(l)],CMAP[ord(r)])]=value
kern('A','TVWY',-70); kern('A','COQGU',-20)
kern('TVWY','A',-75); kern('VYW','aeou',-55); kern('T','aeou',-65)
kern('T','r',-35); kern('F','A',-45); kern('F','aeo',-25)
kern('L','TVWY',-65); kern('P','A',-55); kern('R','TVWY',-25)
kern('KX','COQG',-30); kern('KX','aeou',-25)
kern('Y','COQG',-25); kern('OQ','A',-20)
kern('VWTY','.,',-70); kern('PFR','.,',-35)
kern('vwy','.,',-35); kern('r','.,',-25)
kern('f','aeo',-15); kern('r','aeo',-15)
kern('vwy','aeo',-20); kern('aeo','vwy',-20)
kern('‘“','A',-55); kern('A','’”',-55)
kern('X','U',-10); kern('U','Q',0); kern('Q','U',5); kern('U','T',-10); kern('T','E',0); kern('E','C',0); kern('C','H',0)

# Copy kerning to precomposed accented forms.
base_to_forms={}
for ch in G:
    nfd=unicodedata.normalize('NFD',ch)
    if len(nfd)>1 and nfd[0] in G:
        base_to_forms.setdefault(CMAP[ord(nfd[0])],[]).append(CMAP[ord(ch)])
for (l,r),v in list(PAIRS.items()):
    for ll in [l]+base_to_forms.get(l,[]):
        for rr in [r]+base_to_forms.get(r,[]): PAIRS[(ll,rr)]=v

def draw(pen,shape):
    for c in contours(shape):
        pen.moveTo(c[0])
        for pt in c[1:]: pen.lineTo(pt)
        pen.closePath()

def build(is_ttf):
    fb=FontBuilder(UPM,isTTF=is_ttf)
    fb.setupGlyphOrder(ORDER)
    fb.setupCharacterMap(CMAP)
    if is_ttf:
        glyphs={}
        for n in ORDER:
            pen=TTGlyphPen(None); draw(pen,SHAPES[n]); glyphs[n]=pen.glyph()
        fb.setupGlyf(glyphs)
    else:
        chars={}
        for n in ORDER:
            pen=T2CharStringPen(METRICS[n][0],None); draw(pen,SHAPES[n]); chars[n]=pen.getCharString()
        fb.setupCFF('XUQU-Regular',{'FullName':'XUQU Regular','FamilyName':'XUQU','Weight':'Regular','version':'1.000','Notice':'Created for XUQUTECH from the supplied logo.'},chars,{})
    fb.setupHorizontalMetrics(METRICS)
    fb.setupHorizontalHeader(ascent=960,descent=-250,lineGap=0)
    fb.setupNameTable({'familyName':'XUQU体','styleName':'Regular','uniqueFontIdentifier':'XUQUTECH:XUQU-Regular:1.000','fullName':'XUQU体 Regular','psName':'XUQU-Regular','version':'Version 1.000','copyright':'XUQU typeface. Created for XUQUTECH, 2026. Original vector outlines.','designer':'XUQUTECH / AI-assisted custom type design','description':'Wide geometric Latin display typeface based on the supplied XUQUTECH wordmark.','licenseDescription':'Custom font asset delivered to XUQUTECH. No third-party font outlines incorporated.'},mac=False)
    names=fb.font['name']
    for nid,zh,en in [(1,'XUQU体','XUQU体'),(2,'常规','Regular'),(4,'XUQU体 常规','XUQU体 Regular'),(16,'XUQU体','XUQU体'),(17,'常规','Regular')]:
        names.setName(zh,nid,3,1,0x804)
        names.setName(en,nid,3,1,0x409)
    # ASCII aliases for software relying on the legacy Macintosh name records.
    for nid,val in [(1,'XUQU'),(2,'Regular'),(4,'XUQU Regular'),(6,'XUQU-Regular')]: names.setName(val,nid,1,0,0)
    fb.setupOS2(version=4,sTypoAscender=960,sTypoDescender=-250,sTypoLineGap=0,usWinAscent=980,usWinDescent=260,sxHeight=XH,sCapHeight=CAP,usWeightClass=400,usWidthClass=7,fsType=0,fsSelection=0xC0,achVendID='XUQU')
    fb.setupPost(underlinePosition=-150,underlineThickness=70)
    fb.setupMaxp()
    if is_ttf:
        gasp=newTable('gasp'); gasp.gaspRange={65535:15}; fb.font['gasp']=gasp
    feature='languagesystem DFLT dflt;\nlanguagesystem latn dflt;\nfeature kern {\n'
    feature+='\n'.join(f'pos {l} {r} {v};' for (l,r),v in sorted(PAIRS.items()) if v)
    feature+='\n} kern;\n'
    addOpenTypeFeaturesFromString(fb.font,feature)
    if is_ttf:
        kt=newTable('kern'); kt.version=0
        st=KernTable_format_0(); st.version=0; st.coverage=1; st.kernTable={k:v for k,v in PAIRS.items() if v}
        kt.kernTables=[st]; fb.font['kern']=kt
    path=OUT/('XUQU-Regular.ttf' if is_ttf else 'XUQU-Regular.otf')
    fb.font.save(path)
    return path

if __name__=='__main__':
    ttf=build(True); otf=build(False)
    web=TTFont(ttf); web.flavor='woff2'; web.save(OUT/'XUQU-Regular.woff2')
    basic=set(range(32,127)); latin1=set(range(160,256)); extended=set(range(256,384))
    report={'family':'XUQU体','postscript_name':'XUQU-Regular','version':'1.000','style':'Regular','upm':UPM,'cap_height':CAP,'x_height':XH,'encoded_characters':len(CMAP),'glyphs':len(ORDER),'kerning_pairs':sum(bool(v) for v in PAIRS.values()),'ascii_complete':basic.issubset(CMAP),'latin1_complete':latin1.issubset(CMAP),'latin_extended_a_missing':[f'U+{cp:04X}' for cp in sorted(extended-set(CMAP))],'characters':''.join(chr(cp) for cp in sorted(CMAP)),'files':[p.name for p in sorted(OUT.iterdir())]}
    (ROOT/'source'/'character-set.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print(json.dumps({k:v for k,v in report.items() if k!='characters'},ensure_ascii=False,indent=2))
