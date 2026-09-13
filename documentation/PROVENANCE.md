# Design and engineering provenance

## Known development history

- The user provided the XUQU Tech wordmark and requested a complete Latin font
  family called XUQU体, followed by Thin, Light, Bold and ExtraBold weights.
- The outlines were developed as a custom geometric system with AI-assisted
  Python/FontTools/Shapely engineering. They were not taken from an installed or
  third-party font. The original generation code is retained under `sources/legacy/`.
- The v1.2 work corrected weight progression across the family, including A and
  derived characters. v1.3 integrated the B join explicitly approved by the user.
- The v1.400 preparation converts those exact approved TTF outlines to editable
  UFO sources, adds missing GF Latin Core glyphs and OpenType behavior, and
  compiles through fontmake. `reference/v1.3/` contains the exact five originals
  used for regression, with checksums included in the final package manifest.

## What this does and does not establish

On 2026-09-13 the user confirmed personal copyright ownership by **Xu Zou
(邹旭)**, the family name **Xuqu**, the English public name **Xu Zou**, and a
family-wide OFL 1.1 grant covering existing and future styles. This is the
owner's recorded rights declaration. It does not replace independent legal
verification or imply that AI-assisted production was solely unaided human
work. `AUTHORS.txt` identifies the personal rights holder; the project license
is now active. The public contact email zouxu@xuqutech.com was taken from the owner’s company
website source (uxbillzou/xuqu, index.html). The connected GitHub account is
uxbillzou; the dedicated public repository is https://github.com/uxbillzou/xuqu-font.

Versions 1.401 and 1.402 update authorization, author, repository and version
metadata only. The approved 1.400 outlines, advances, kerning and OpenType
features are preserved;
see `documentation/qa/metadata-update.json` for the binary comparison.

GlyphsLib/GF glyphset data was used for glyph names, Unicode mappings and
coverage requirements only, not for glyph outlines. fontmake, FontTools,
ufoLib2, Shapely and other tools are external dependencies installed under their
own licenses. Fontspector is not redistributed in the package.

## Review changes that affect existing glyphs

- A and B: exact approved outlines and advances across all five styles.
- Figure 1: narrower default proportional advance; original design and tabular
  spacing retained in the `tnum` alternate.
- Ģģ Ķķ Ļļ Ņņ Ŗŗ: comma accent construction for Latvian/historical comma forms;
  lowercase g uses the turned comma above.
- ď Ľ ľ ť: side carons suitable for tall Czech/Slovak letterforms.
- Font naming, vertical metrics, code-page bits and other metadata are
  normalized for the new preparation; the whole family is now covered by the owner-confirmed OFL grant.

Precise per-style changes and advances are recorded in
`documentation/qa/regression.json`. Every existing encoded character is retained.
