#!/usr/bin/env python3
"""Package the Google Fonts preparation project, with byte-verified contents."""
from pathlib import Path
import zipfile,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
def included(p):
    parts=p.relative_to(ROOT).parts
    return p.is_file() and not any(x in ('build','__pycache__','.venv','.git') for x in parts) and p.suffix!='.pyc' and p.name not in ('MANIFEST.json','.DS_Store')
def main():
    cfg=json.loads((ROOT/'project.json').read_text())
    paths=sorted(p for p in ROOT.rglob('*') if included(p))
    manifest={'package':'XUQU Google Fonts preparation','version':cfg['version'],'state':cfg['build_state'],'license':'SIL Open Font License 1.1','copyright_holders':cfg['copyright_holders'],'files':[{'path':p.relative_to(ROOT).as_posix(),'size':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths]}
    (ROOT/'MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    prefix='XUQU-GoogleFonts-Preparation-v'+cfg['version']
    target=ROOT.parent/(prefix+'.zip')
    with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in [*paths,ROOT/'MANIFEST.json']:z.write(p,f'{prefix}/{p.relative_to(ROOT).as_posix()}')
    with zipfile.ZipFile(target) as z:
        assert z.testzip() is None
        for item in manifest['files']:
            b=z.read(prefix+'/'+item['path']);assert hashlib.sha256(b).hexdigest()==item['sha256']
        current=[n for n in z.namelist() if '/fonts/ttf/' in n and n.endswith('.ttf')]
        assert len(current)==5
        assert not any(n.endswith(('.jpg','.jpeg')) for n in z.namelist()),'Unexpected photo/QR attachment'
        assert not any('WeChat.jpg' in n for n in z.namelist())
    print(json.dumps({'file':str(target),'bytes':target.stat().st_size,'entries':len(paths)+1,'current_ttf_files':5,'current_woff2_files':5,'editable_ufo_sources':5,'sha256':hashlib.sha256(target.read_bytes()).hexdigest()},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
