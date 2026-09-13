#!/usr/bin/env python3
"""One-command rebuild from committed UFO sources with fontmake.

Build does not publish, sign an agreement, or activate a license.
"""
from pathlib import Path
import argparse,json,subprocess,sys,os,hashlib,shutil
from fontTools.ttLib import TTFont,newTable
from fontTools.otlLib.builder import buildStatTable
from fontTools.ttLib.tables.O_S_2f_2 import calcCodePageRanges
import ufoLib2

ROOT=Path(__file__).resolve().parents[1]
STYLES=[('Thin',100),('Light',300),('Regular',400),('Bold',700),('ExtraBold',800)]

def main():
    cfg=json.loads((ROOT/'project.json').read_text())
    env=dict(os.environ);env['SOURCE_DATE_EPOCH']='1789257600'
    family=cfg['family_name'];stem=family.replace(' ','')
    out=ROOT/'fonts/ttf';out.mkdir(parents=True,exist_ok=True)
    web=ROOT/'fonts/webfonts';web.mkdir(parents=True,exist_ok=True)
    # When the owner changes the working family name, archive only known build
    # outputs from the previous manifest so stale names do not coexist in fonts/.
    old_manifest=ROOT/'documentation/qa/build.json'
    if old_manifest.exists():
        for row in json.loads(old_manifest.read_text()):
            old=ROOT/row['path']
            if old.parent==out and not old.name.startswith(stem+'-') and old.exists():
                dest=ROOT/'build/previous-name';dest.mkdir(parents=True,exist_ok=True)
                shutil.move(str(old),str(dest/old.name))
                oldweb=web/(old.stem+'.woff2')
                if oldweb.exists():shutil.move(str(oldweb),str(dest/oldweb.name))
    report=[]
    for style,weight in STYLES:
        source=ROOT/'sources'/f'Xuqu-{style}.ufo'
        target=out/f'{stem}-{style}.ttf'
        subprocess.run([sys.executable,'-m','fontmake','-u',str(source),'-o','ttf','--output-path',str(target),'--no-production-names','--keep-overlaps','--verbose','WARNING'],check=True,env=env)
        f=TTFont(target,recalcTimestamp=False)
        f['head'].created=f['head'].modified=3872102400
        f['OS/2'].fsSelection=(1<<7)|(1<<8)|(1<<5 if style=='Bold' else 1<<6)
        f['head'].macStyle=1 if style=='Bold' else 0
        f['OS/2'].version=4
        f['OS/2'].recalcUnicodeRanges(f)
        bits=calcCodePageRanges(set(f.getBestCmap()))
        f['OS/2'].ulCodePageRange1=sum(1<<n for n in bits if n<32)
        f['OS/2'].ulCodePageRange2=sum(1<<(n-32) for n in bits if n>=32)
        f['OS/2'].usWidthClass=5 # single-width family: no wdth variation
        gasp=newTable('gasp');gasp.gaspRange={65535:10};f['gasp']=gasp
        # Deliberately unhinted display release; fontmake's outlines are retained.
        for table in ('fpgm','prep','cvt ','kern','DSIG'):
            if table in f:del f[table]
        for g in f['glyf'].glyphs.values():
            if hasattr(g,'program'):g.program.fromBytecode([])
        # Static style names use standard RIBBI grouping.
        n=f['name'];n.names=[x for x in n.names if x.platformID==3 and x.langID==0x409]
        for id in (1,2,4,6,16,17):n.removeNames(nameID=id)
        legacy=family if style in ('Regular','Bold') else family+' '+style
        for id,val in [(1,legacy),(2,'Bold' if style=='Bold' else 'Regular'),(4,family+' '+style),(6,stem+'-'+style)]:n.setName(val,id,3,1,0x409)
        if style not in ('Regular','Bold'):
            n.setName(family,16,3,1,0x409);n.setName(style,17,3,1,0x409)
        n.setName(f"{cfg['version']};XUQU;{stem}-{style}",3,3,1,0x409)
        n.setName('Version '+cfg['version'],5,3,1,0x409)
        f['head'].fontRevision=float(cfg['version'])
        vals=[{'value':weight,'name':style,'flags':2 if style=='Regular' else 0}]
        if style=='Regular':vals[0]['linkedValue']=700
        buildStatTable(f,[{'tag':'wght','name':'Weight','ordering':0,'values':vals},{'tag':'ital','name':'Italic','ordering':1,'values':[{'value':0,'name':'Roman','flags':2,'linkedValue':1}]}],elidedFallbackName='Regular')
        meta=newTable('meta');meta.data={'dlng':'Latn','slng':'Latn'};f['meta']=meta
        f.save(target)
        wf=TTFont(target,recalcTimestamp=False);wf.flavor='woff2';wf.save(web/(target.stem+'.woff2'))
        report.append({'style':style,'weight':weight,'path':target.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'characters':len(f.getBestCmap()),'glyphs':len(f.getGlyphOrder()),'hinting':'unhinted; gasp 0x000A'})
        print(f'Built {target.name}: {len(f.getBestCmap())} characters',flush=True)
    (ROOT/'documentation/qa/build.json').write_text(json.dumps(report,indent=2)+'\n')
    css='/* Generated from project.json. Check license status before distribution. */\n'
    for style,weight in STYLES:
        css+=f"@font-face {{ font-family: {json.dumps(family)}; font-style: normal; font-weight: {weight}; font-display: swap; src: url('./fonts/webfonts/{stem}-{style}.woff2') format('woff2'); }}\n"
    css+=f".xuqu {{ font-family: {json.dumps(family)}, sans-serif; font-synthesis: none; }}\n.xuqu-tabular {{ font-variant-numeric: tabular-nums; }}\n"
    (ROOT/'webfont.css').write_text(css)

if __name__=='__main__':main()
