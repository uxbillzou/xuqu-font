#!/usr/bin/env python3
"""Apply the owner's recorded decisions to local sources and license files.

Public account details are separate from an OFL grant. No upload or CLA signing
occurs. Optional confirmation flags record new explicit owner decisions; an
already recorded decision need not be confirmed again.
"""
from pathlib import Path
import argparse, json, re
from urllib.parse import urlparse
import ufoLib2

ROOT = Path(__file__).resolve().parents[1]
LICENSE_URL = 'https://openfontlicense.org'
LICENSE_TEXT = ('This Font Software is licensed under the SIL Open Font License, '
                'Version 1.1. This license is available with a FAQ at: '
                'https://openfontlicense.org')

def copyright_string(cfg):
    value = f"Copyright {cfg.get('copyright_year', 2026)} The {cfg['family_name']} Project Authors"
    repo = cfg.get('repository_url', '').strip()
    return value + (f' ({repo})' if repo else '')

def apply_project_metadata(u, cfg):
    i = u.info
    family, style = cfg['family_name'], i.styleName
    i.versionMajor, i.versionMinor = map(int, cfg['version'].split('.'))
    i.familyName = family
    i.styleMapFamilyName = family if style in ('Regular', 'Bold') else family + ' ' + style
    i.openTypeNamePreferredFamilyName = family
    i.postscriptFontName = family.replace(' ', '') + '-' + style
    i.openTypeNameDesigner = cfg['author_display']
    i.openTypeNameDesignerURL = cfg.get('designer_url') or cfg.get('repository_url') or None
    i.openTypeNameDescription = 'Wide geometric Latin display family with five static weights.'
    if cfg.get('ofl_entire_family_approved') and cfg.get('copyright_holders_confirmed'):
        i.copyright = copyright_string(cfg)
        i.openTypeNameLicense = LICENSE_TEXT
        i.openTypeNameLicenseURL = LICENSE_URL
    else:
        i.copyright = 'Preparation build. Copyright holder pending confirmation.'
        i.openTypeNameLicense = 'Private preparation build. OFL release is pending copyright holder confirmation.'
        i.openTypeNameLicenseURL = None

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--confirm-ofl-entire-family', action='store_true')
    p.add_argument('--confirm-name', action='store_true')
    p.add_argument('--confirm-copyright-holders', action='store_true')
    p.add_argument('--require-googlefonts-metadata', action='store_true',
                   help='Require a real public repository and email for submission metadata.')
    args = p.parse_args()
    cfg = json.loads((ROOT / 'project.json').read_text())
    for flag, key in ((args.confirm_ofl_entire_family, 'ofl_entire_family_approved'),
                      (args.confirm_name, 'name_approved'),
                      (args.confirm_copyright_holders, 'copyright_holders_confirmed')):
        if flag:
            cfg[key] = True
    if not all(cfg.get(k) for k in ('ofl_entire_family_approved', 'name_approved', 'copyright_holders_confirmed')):
        raise SystemExit('Record the actual owner decisions first; see review/OWNER-CHECKLIST.md.')
    family = cfg['family_name']
    if not re.fullmatch(r'[A-Z][a-zA-Z0-9]*(?: [A-Z][a-zA-Z0-9]*)*', family) or family.upper() == family:
        raise SystemExit('Use a basic ASCII, title-case family name. Google name acceptance is a separate review.')
    if len(family + ' ExtraBold') > 32:
        raise SystemExit('Family + style must fit 32 characters.')
    repo, email = cfg.get('repository_url', '').strip(), cfg.get('author_email', '').strip()
    if repo:
        parsed = urlparse(repo)
        if (parsed.scheme != 'https' or not parsed.netloc or not parsed.path.strip('/')
                or any(x in repo.lower() for x in ['example', 'pending', 'yourname', 'placeholder', '<', '>'])):
            raise SystemExit('Use the actual public project repository URL.')
    if email and not re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+', email):
        raise SystemExit('Use a valid public contact email.')
    holders = cfg.get('copyright_holders', [])
    if not holders or not all(isinstance(x, str) and x.strip() for x in holders):
        raise SystemExit('List the actual confirmed copyright holder(s).')
    missing = [key for key, value in [('repository_url', repo), ('author_email', email)] if not value]
    if args.require_googlefonts_metadata and missing:
        raise SystemExit('Still needed for Google Fonts submission metadata: ' + ', '.join(missing))
    cfg['repository_url'], cfg['author_email'] = repo, email
    for path in sorted((ROOT / 'sources').glob('*.ufo')):
        u = ufoLib2.Font.open(path)
        apply_project_metadata(u, cfg)
        u.save(path, overwrite=True)
    template = (ROOT / 'review/OFL.txt.in').read_text()
    (ROOT / 'OFL.txt').write_text(template.replace('{{COPYRIGHT_STRING}}', copyright_string(cfg)))
    contact = f' <{email}>' if email else ''
    (ROOT / 'AUTHORS.txt').write_text('\n'.join(x + contact for x in holders) + '\n')
    (ROOT / 'CONTRIBUTORS.txt').write_text(cfg['author_display'] + contact + '\n')
    cfg['build_state'] = 'ofl_authorized_repository_pending' if missing else 'local_release_metadata_prepared'
    (ROOT / 'project.json').write_text(json.dumps(cfg, ensure_ascii=False, indent=2) + '\n')
    print('Recorded owner decisions applied; local OFL and font metadata updated. Rebuild and rerun QA.')
    if missing:
        print('Submission metadata still needs: ' + ', '.join(missing) + '. No placeholder URL/email was inserted.')
    print('This script does not upload files, send submissions or sign a CLA. Existing owner-reported status is preserved.')

if __name__ == '__main__':
    main()
