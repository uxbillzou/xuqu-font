#!/usr/bin/env python3
"""Run the full Google Fonts profile offline, with no font/name egress.

The tool is not bundled. Install Fontspector 1.7.4 (or review a newer version)
from its official releases. Network checks are intentionally skipped; no
check IDs are excluded and failure exit codes are propagated.
"""
from pathlib import Path
import argparse,json,shutil,subprocess,sys

ROOT=Path(__file__).resolve().parents[1]

def main():
    p=argparse.ArgumentParser();p.add_argument('--fontspector',default='fontspector');a=p.parse_args()
    cfg=json.loads((ROOT/'project.json').read_text());fam=cfg['family_name'].lower().replace(' ','')
    stage=ROOT/'build/googlefonts/ofl'/fam;stage.mkdir(parents=True,exist_ok=True)
    fonts=list((ROOT/'fonts/ttf').glob('*.ttf'))
    if len(fonts)!=5:raise SystemExit('Expected exactly 5 TTFs; build first.')
    for old in stage.glob('*.ttf'):old.unlink()
    for f in fonts:shutil.copyfile(f,stage/f.name)
    # Only an explicitly activated license is copied into the QA staging area.
    if (ROOT/'OFL.txt').exists():shutil.copyfile(ROOT/'OFL.txt',stage/'OFL.txt')
    elif (stage/'OFL.txt').exists():(stage/'OFL.txt').unlink()
    # Fontspector checks its explicit file collection; nearby files alone are
    # not necessarily included. Supply the real license file as an input.
    inputs=sorted(stage.glob('*.ttf'))
    if (stage/'OFL.txt').exists():inputs.append(stage/'OFL.txt')
    qa=ROOT/'documentation/qa'
    args=[a.fontspector,'-p','googlefonts','--skip-network','--full-lists','--json',str(qa/'fontspector.json'),'--ghmarkdown',str(qa/'fontspector.md'),'--html',str(qa/'fontspector.html'),*[str(x) for x in inputs]]
    with (qa/'fontspector-console.txt').open('w') as log:
        result=subprocess.run(args,stdout=log,stderr=subprocess.STDOUT)
    (qa/'execution.json').write_text(json.dumps({'command':['fontspector',*args[1:]],'network_checks':'skipped; external metadata egress not authorized','excluded_checks':[],'returncode':result.returncode},indent=2)+'\n')
    if (qa/'fontspector.json').exists():print(json.loads((qa/'fontspector.json').read_text())['summary'])
    else:print('Fontspector did not produce a report; see console log.')
    return result.returncode
if __name__=='__main__':sys.exit(main())
