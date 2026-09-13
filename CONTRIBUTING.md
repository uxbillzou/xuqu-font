# Contributing

The font project is licensed under SIL OFL 1.1; see OFL.txt and AUTHORS.txt.
The rights holder is Xu Zou (邹旭). The source repository is https://github.com/uxbillzou/xuqu-font.

Edit the UFO sources in `sources/`. Build with `python scripts/build.py`, run
`python scripts/validate.py`, and run the full offline Google Fonts profile with
`python scripts/run_qa.py`. Include updated proofs for visible changes.

Do not rerun the initial source importer over a designer's edits. Preserve the
approved A/B designs unless the design owner explicitly approves a change.
Record additions or intentional regressions in the changelog and QA notes.

For an actual Google Fonts submission, follow the Google project CLA process;
editing this repository does not itself sign that agreement.
