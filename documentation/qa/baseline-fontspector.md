## FontSpector report

fontspector version: 1.7.4






## Check results




<details><summary>[18] xuqu-type-family/fonts/XUQU-Regular.ttf</summary>
<div>


<details>
    <summary>🔥 <b>FAIL</b> Check code page character ranges (opentype/code_pages)</summary>
    <div>


> At least some programs (such as Word and Sublime Text) under Windows 7 do not recognize fonts unless code page bits are properly set on the ulCodePageRange1 (and/or ulCodePageRange2) fields of the OS/2 table.
> 
> More specifically, the fonts are selectable in the font menu, but whichever Windows API these applications use considers them unsuitable for any character set, so anything set in these fonts is rendered with Arial as a fallback font.
> 
> This check currently does not identify which code pages should be set. Auto-detecting coverage is not trivial since the OpenType specification leaves the interpretation of whether a given code page is "functional" or not open to the font developer to decide.
> 
> So here we simply detect as a FAIL when a given font has no code page declared at all.




Original proposal: [https://github.com/fonttools/fontbakery/issues/2474]





- 🔥 **FAIL** No code pages defined in the OS/2 table ulCodePageRange1 and CodePageRange2 fields. [code: no-code-pages]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. (googlefonts/glyphsets/shape_languages)</summary>
    <div>


> This check uses a heuristic to determine which GF glyphsets a font supports. Then it checks the font for correct shaping behaviour for all languages in those glyphsets.




Original proposal: [https://github.com/googlefonts/fontbakery/issues/4147]





- 🔥 **FAIL** Failed language shaping:

| Message                                                                           | Languages                    |
|-----------------------------------------------------------------------------------|------------------------------|
| Mandatory orthography codepoints:                                                 | * de_Latn (German)           |
|   The following base characters are missing from the font: ẞ                      |                              |
|   The following mark characters are missing from the font: ́, ̈, ̀                   |                              |
| Mandatory orthography codepoints:                                                 | * da_Latn (Danish)           |
|   The following mark characters are missing from the font: ̊, ́                     |                              |
| Mandatory orthography codepoints:                                                 | * cs_Latn (Czech)            |
|   The following mark characters are missing from the font: ́, ̊, ̌                   |                              |
| Mandatory orthography codepoints:                                                 | * en_Latn (English)          |
|   The following mark characters are missing from the font: ̂, ̈, ́, ̧, ̃, ̀             |                              |
| Mandatory orthography codepoints:                                                 | * es_Latn (Spanish)          |
|   The following mark characters are missing from the font: ̃, ́, ̈                   |                              |
| Mandatory orthography codepoints:                                                 | * cy_Latn (Welsh)            |
|   The following base characters are missing from the font: Ẃ, Ẅ, ẃ, ẅ, ẁ, Ẁ, ỳ, Ỳ |                              |
|   The following mark characters are missing from the font: ́, ̀, ̈, ̂                 |                              |
| Mandatory orthography codepoints:                                                 | * fi_Latn (Finnish)          |
|   The following mark characters are missing from the font: ̈, ̊, ̃, ̌                 |                              |
| Mandatory orthography codepoints:                                                 | * lv_Latn (Latvian)          |
|   The following mark characters are missing from the font: ̌, ̧, ̄                   |                              |
| Mandatory orthography codepoints:                                                 | * fr_Latn (French)           |
|   The following mark characters are missing from the font: ̧, ̈, ́, ̂, ̀               |                              |
| Mandatory orthography codepoints:                                                 | * hu_Latn (Hungarian)        |
|   The following mark characters are missing from the font: ̈, ́, ̋                   |                              |
| Mandatory orthography codepoints:                                                 | * ca_Latn (Catalan)          |
|   The following mark characters are missing from the font: ̧, ́, ̈, ̀                 |                              |
| Mandatory orthography codepoints:                                                 | * hr_Latn (Croatian)         |
|   The following mark characters are missing from the font: ̌, ́                     |                              |
| Mandatory orthography codepoints:                                                 | * mt_Latn (Maltese)          |
|   The following mark characters are missing from the font: ̇, ̀, ̂                   |                              |
| Mandatory orthography codepoints:                                                 | * pl_Latn (Polish)           |
|   The following mark characters are missing from the font: ̇, ́, ̨                   |                              |
| Mandatory orthography codepoints:                                                 | * pt_Latn (Portuguese)       |
|   The following mark characters are missing from the font: ̃, ́, ̀, ̈, ̧, ̂             |                              |
| Mandatory orthography codepoints:                                                 | * ro_Latn (Romanian)         |
|   The following base characters are missing from the font: Ș, ț, Ț, ș             |                              |
|   The following mark characters are missing from the font: ̧, ̆, ̂, ̦                 |                              |
| Mandatory orthography codepoints:                                                 | * nl_Latn (Dutch)            |
|   The following base characters are missing from the font: íj́, ÍJ́                 |                              |
|   The following mark characters are missing from the font: ́, ̀, ̂, ̈                 |                              |
| Mandatory orthography codepoints:                                                 | * sq_Latn (Albanian)         |
|   The following mark characters are missing from the font: ̈, ̧                     |                              |
| Mandatory orthography codepoints:                                                 | * it_Latn (Italian)          |
|   The following mark characters are missing from the font: ̂, ̀, ́, ̈                 |                              |
| Mandatory orthography codepoints:                                                 | * sv_Latn (Swedish)          |
|   The following mark characters are missing from the font: ̈, ̊, ́, ̀                 |                              |
| Mandatory orthography codepoints:                                                 | * tr_Latn (Turkish)          |
|   The following mark characters are missing from the font: ̧, ̂, ̦, ̇, ̆, ̈             |                              |
| Mandatory orthography codepoints:                                                 | * is_Latn (Icelandic)        |
|   The following mark characters are missing from the font: ̈, ́, ̨                   |                              |
| Mandatory orthography codepoints:                                                 | * lt_Latn (Lithuanian)       |
|   The following mark characters are missing from the font: ̄, ̇, ̌, ̨                 |                              |
| Mandatory orthography codepoints:                                                 | * nb_Latn (Norwegian Bokmål) |
|   The following mark characters are missing from the font: ̊, ̀, ̂, ̈, ́               |                              |
| Mandatory orthography codepoints:                                                 | * sk_Latn (Slovak)           |
|   The following mark characters are missing from the font: ̂, ́, ̌, ̈                 |                              | [code: failed-language-shaping]
  
  


- ⚠️ **WARN** Warning language shaping:

| Message                                                           | Languages                    |
|-------------------------------------------------------------------|------------------------------|
| Auxiliary orthography codepoints:                                 | * fr_Latn (French)           |
|   The following auxiliary characters are missing from the font: ẞ |                              |
|   The following auxiliary characters are missing from the font: Ǔ |                              |
|   The following auxiliary characters are missing from the font: ǔ |                              |
| Auxiliary orthography codepoints:                                 | * it_Latn (Italian)          |
|   The following auxiliary characters are missing from the font: ẞ | * pl_Latn (Polish)           |
|                                                                   | * tr_Latn (Turkish)          |
| Auxiliary orthography codepoints:                                 | * lt_Latn (Lithuanian)       |
|   The following auxiliary characters are missing from the font: Ą́ |                              |
|   The following auxiliary characters are missing from the font: Ą̃ |                              |
|   The following auxiliary characters are missing from the font: Ẽ |                              |
|   The following auxiliary characters are missing from the font: Ę́ |                              |
|   The following auxiliary characters are missing from the font: Ę̃ |                              |
|   The following auxiliary characters are missing from the font: Ė́ |                              |
|   The following auxiliary characters are missing from the font: Ė̃ |                              |
|   The following auxiliary characters are missing from the font: İ́ |                              |
|   The following auxiliary characters are missing from the font: İ́ |                              |
|   The following auxiliary characters are missing from the font: İ̀ |                              |
|   The following auxiliary characters are missing from the font: İ̀ |                              |
|   The following auxiliary characters are missing from the font: İ̃ |                              |
|   The following auxiliary characters are missing from the font: İ̃ |                              |
|   The following auxiliary characters are missing from the font: Į́ |                              |
|   The following auxiliary characters are missing from the font: Į̇́ |                              |
|   The following auxiliary characters are missing from the font: Į̃ |                              |
|   The following auxiliary characters are missing from the font: Į̇̃ |                              |
|   The following auxiliary characters are missing from the font: J̃ |                              |
|   The following auxiliary characters are missing from the font: J̇̃ |                              |
|   The following auxiliary characters are missing from the font: L̃ |                              |
|   The following auxiliary characters are missing from the font: M̃ |                              |
|   The following auxiliary characters are missing from the font: R̃ |                              |
|   The following auxiliary characters are missing from the font: Ų́ |                              |
|   The following auxiliary characters are missing from the font: Ų̃ |                              |
|   The following auxiliary characters are missing from the font: Ū́ |                              |
|   The following auxiliary characters are missing from the font: Ū̃ |                              |
|   The following auxiliary characters are missing from the font: ą́ |                              |
|   The following auxiliary characters are missing from the font: ą̃ |                              |
|   The following auxiliary characters are missing from the font: ẽ |                              |
|   The following auxiliary characters are missing from the font: ę́ |                              |
|   The following auxiliary characters are missing from the font: ę̃ |                              |
|   The following auxiliary characters are missing from the font: ė́ |                              |
|   The following auxiliary characters are missing from the font: ė̃ |                              |
|   The following auxiliary characters are missing from the font: i̇́ |                              |
|   The following auxiliary characters are missing from the font: i̇̀ |                              |
|   The following auxiliary characters are missing from the font: i̇̃ |                              |
|   The following auxiliary characters are missing from the font: į́ |                              |
|   The following auxiliary characters are missing from the font: į̇́ |                              |
|   The following auxiliary characters are missing from the font: į̃ |                              |
|   The following auxiliary characters are missing from the font: į̇̃ |                              |
|   The following auxiliary characters are missing from the font: j̃ |                              |
|   The following auxiliary characters are missing from the font: j̇̃ |                              |
|   The following auxiliary characters are missing from the font: l̃ |                              |
|   The following auxiliary characters are missing from the font: m̃ |                              |
|   The following auxiliary characters are missing from the font: r̃ |                              |
|   The following auxiliary characters are missing from the font: ų́ |                              |
|   The following auxiliary characters are missing from the font: ų̃ |                              |
|   The following auxiliary characters are missing from the font: ū́ |                              |
|   The following auxiliary characters are missing from the font: ū̃ |                              |
| Auxiliary orthography codepoints:                                 | * nb_Latn (Norwegian Bokmål) |
|   The following auxiliary characters are missing from the font: Ǎ |                              |
|   The following auxiliary characters are missing from the font: ǎ |                              |
| Auxiliary orthography codepoints:                                 | * fi_Latn (Finnish)          |
|   The following auxiliary characters are missing from the font: Ǧ |                              |
|   The following auxiliary characters are missing from the font: Ǥ |                              |
|   The following auxiliary characters are missing from the font: Ȟ |                              |
|   The following auxiliary characters are missing from the font: Ǩ |                              |
|   The following auxiliary characters are missing from the font: Ș |                              |
|   The following auxiliary characters are missing from the font: ẞ |                              |
|   The following auxiliary characters are missing from the font: Ț |                              |
|   The following auxiliary characters are missing from the font: Ʒ |                              |
|   The following auxiliary characters are missing from the font: Ǯ |                              |
|   The following auxiliary characters are missing from the font: ǧ |                              |
|   The following auxiliary characters are missing from the font: ǥ |                              |
|   The following auxiliary characters are missing from the font: ȟ |                              |
|   The following auxiliary characters are missing from the font: ǩ |                              |
|   The following auxiliary characters are missing from the font: ș |                              |
|   The following auxiliary characters are missing from the font: ț |                              |
|   The following auxiliary characters are missing from the font: ʒ |                              |
|   The following auxiliary characters are missing from the font: ǯ |                              |
| Auxiliary orthography codepoints:                                 | * en_Latn (English)          |
|   The following auxiliary characters are missing from the font: ʻ |                              |
| Auxiliary orthography codepoints:                                 | * da_Latn (Danish)           |
|   The following auxiliary characters are missing from the font: Ǿ |                              |
|   The following auxiliary characters are missing from the font: ǿ |                              | [code: warning-language-shaping]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Check family name for GF Guide compliance. (googlefonts/family_name_compliance)</summary>
    <div>


> Checks the family name for compliance with the Google Fonts Guide. https://googlefonts.github.io/gf-guide/onboarding.html#new-fonts
> 
> If you want to have your family name added to the CamelCase exceptions list, please submit a pull request to the camelcased_familyname_exceptions.txt file.
> 
> Similarly, abbreviations can be submitted to the abbreviations_familyname_exceptions.txt file.
> 
> These are located in the Lib/fontbakery/data/googlefonts/ directory of the FontBakery source code currently hosted at https://github.com/fonttools/fontbakery/




Original proposal: [https://github.com/fonttools/fontbakery/issues/4049]





- 🔥 **FAIL** "XUQU体" contains an abbreviation. [code: abbreviation]
  
  


- 🔥 **FAIL** "XUQU体" contains the following characters which are not allowed: "体". [code: forbidden-characters]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Directory name in GFonts repo structure must
    match NameID 1 of the regular. (googlefonts/repo/dirname_matches_nameid_1)</summary>
    <div>


> For static fonts, we expect to name the directory in google/fonts according to the NameID 1 of the regular font, all lower case with no hyphens or spaces. This check verifies that the directory name matches our expectations.




Original proposal: [https://github.com/fonttools/fontbakery/issues/2302]





- 🔥 **FAIL** Family name on the name table ('XUQU体') does not match directory name in the repo structure ('fonts'). Expected 'xuqu体'. [code: mismatch]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Checking file is named canonically. (googlefonts/canonical_filename)</summary>
    <div>


> A font's filename must be composed as "<familyname>-<stylename>.ttf":
> 
> - Nunito-Regular.ttf
> 
> - Oswald-BoldItalic.ttf
> 
> Variable fonts must list the axis tags in alphabetical order in square brackets and separated by commas:
> 
> - Roboto[wdth,wght].ttf
> 
> - Familyname-Italic[wght].ttf




Original proposal: [https://github.com/fonttools/fontbakery/issues/4829]





- 🔥 **FAIL** Expected "XUQU体-Regular.ttf". Got "XUQU-Regular.ttf". [code: bad-filename]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Check font names are correct (googlefonts/font_names)</summary>
    <div>


> Google Fonts has several rules which need to be adhered to when setting a font's name table. Please read: https://googlefonts.github.io/gf-guide/statics.html#supported-styles https://googlefonts.github.io/gf-guide/statics.html#style-linking https://googlefonts.github.io/gf-guide/statics.html#unsupported-styles https://googlefonts.github.io/gf-guide/statics.html#single-weight-families




Original proposal: [https://github.com/fonttools/fontbakery/pull/3800]





- 🔥 **FAIL** Font names are incorrect:

| Name                       | Current          | Expected           |
|----------------------------|------------------|--------------------|
| Family Name                | XUQU体           | XUQU体             |
| Subfamily Name             | Regular          | Regular            |
| Full Name                  | XUQU体 Regular   | XUQU体 Regular     |
| Postscript Name            | **XUQU-Regular** | **XUQU体-Regular** |
| Typographic Family Name    | XUQU体           | XUQU体             |
| Typographic Subfamily Name | **Regular**      | **常规**           | [code: bad-names]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Ensure font can render its own name. (googlefonts/render_own_name)</summary>
    <div>


> A base expectation is that a font family's regular/default (400 roman) style can render its 'menu name' (nameID 1) in itself.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3159]





- 🔥 **FAIL** .notdef glyphs were found when attempting to render XUQU体 [code: render-own-name]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check that OS/2 fsSelection WWS bit is set correctly. (opentype/fsselection_wws)</summary>
    <div>


> According to the OpenType specification, OS/2.fsSelection bit 8 (WWS) should be set if the font has name table strings consistent with a weight/width/slope family without requiring use of name IDs 21 and 22.
> 
> Conversely, if name IDs 21 and 22 are present (indicating the font names are not WWS-conformant), the WWS bit should not be set.




Original proposal: [https://github.com/fonttools/fontspector/issues/577]





- ⚠️ **WARN** OS/2 fsSelection WWS bit is not set, and the font does not have name IDs 21/22 (WWS Family/Subfamily). If the font's naming is WWS-conformant, the WWS bit should be set. [code: no-wws-without-wws-names]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron (alt_caron)</summary>
    <div>


> Lcaron, dcaron, lcaron, tcaron should NOT be composed with quoteright or quotesingle or comma or caron(comb). It should be composed with a distinctive glyph which doesn't look like an apostrophe.
> 
> Source: https://ilovetypography.com/2009/01/24/on-diacritics/ http://diacritics.typo.cz/index.php?id=5 https://www.typotheque.com/articles/lcaron




Original proposal: [https://github.com/fonttools/fontbakery/issues/3308]





- ⚠️ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  


- ⚠️ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  


- ⚠️ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  


- ⚠️ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. (contour_count)</summary>
    <div>


> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be constructured in a handful of ways. This means a glyph's contour count will only differ slightly amongst different fonts, e.g a 'g' could either be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs to a display family.
> 
> This check currently does not cover variable fonts because there's plenty of alternative ways of constructing glyphs with multiple outlines for each feature in a VarFont. The expected contour count data for this check is currently optimized for the typical construction of glyphs in static fonts.




Original proposal: [https://github.com/fonttools/fontbakery/issues/4829]





- ⚠️ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are
     inferred from the typical amounts of contours observed in a
     large collection of reference font families. The divergences
     listed below may simply indicate a significantly different
     design on some of your glyphs. On the other hand, some of these
     may flag actual bugs in the font such as glyphs mapped to an
     incorrect codepoint. Please consider reviewing the design and
     codepoint assignment of these to make sure they are correct.


    The following glyphs do not have the recommended number of contours:
* uni013C (U+013C): found 1, expected one of: [2, 3, 6]
* section (U+00A7): found 1, expected one of: [2, 4, 6] [code: contour-count]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. (math_signs_width)</summary>
    <div>


> #,         It is a common practice to have math signs sharing the same width         (preferably the same width as tabular figures accross the entire font family).
> 
> This probably comes from the will to avoid additional tabular math signs knowing that their design can easily share the same width.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3832]





- ⚠️ **WARN** The most common width is 766 among a set of 12  math glyphs.
The following math glyphs have a different width, though:
width=556: minus
width=746: greater, greaterequal, less, lessequal [code: width-outliers]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure indic fonts have the Indian Rupee Sign glyph. (rupee)</summary>
    <div>


> Per Bureau of Indian Standards every font supporting one of the official Indian languages needs to include Unicode Character “₹” (U+20B9) Indian Rupee Sign.




Original proposal: [https://github.com/fonttools/fontbakery/issues/2967]





- ⚠️ **WARN** Font is missing the Indian Rupee Sign glyph. Please add a glyph for Indian Rupee Sign (₹) at codepoint U+20B9. [code: missing-rupee]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? (soft_hyphen)</summary>
    <div>


> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character), sometimes the same as the traditional hyphen, sometimes double encoded with the hyphen.
> 
> That being said, it is recommended to not include it in the font at all, because discretionary hyphenation should be handled at the level of the shaping engine, not the font. Also, even if present, the software would not display that character.
> 
> More discussion at: https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar




Original proposal: [https://github.com/fonttools/fontbakery/issues/4046, https://github.com/fonttools/fontbakery/issues/3486]





- ⚠️ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs (unreachable_glyphs)</summary>
    <div>


> Glyphs are either accessible directly through Unicode codepoints or through        substitution rules.
> 
> In Color Fonts, glyphs are also referenced by the COLR table. And mathematical fonts also reference glyphs via the MATH table.
> 
> Any glyphs not accessible by these means are redundant and serve only to increase the font's file size.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3160]





- ⚠️ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

* .null
* nonmarkingreturn [code: unreachable-glyphs]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Font has correct separator glyphs? (googlefonts/separator_glyphs)</summary>
    <div>


> U+2028 and U+2029 should be present; otherwise tofu is displayed. (whitespace_ink will check that they are empty)




Original proposal: [https://github.com/fonttools/fontspector/issues/93]





- ⚠️ **WARN** Missing separator glyph U+2028 [code: missing-separator-glyphs]
  
  


- ⚠️ **WARN** Missing separator glyph U+2029 [code: missing-separator-glyphs]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? (outline_alignment_miss)</summary>
    <div>


> This check heuristically looks for on-curve points which are close to, but do not sit on, significant boundary coordinates. For example, a point which has a Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the baseline, here we also check for points near the x-height (but only for lowercase Latin letters), cap-height, ascender and descender Y coordinates.
> 
> Not all such misaligned curve points are a mistake, and sometimes the design may call for points in locations near the boundaries. As this check is liable to generate significant numbers of false positives, it will pass if there are more than 100 reported misalignments.




Original proposal: [https://github.com/fonttools/fontbakery/pull/3088]





- ⚠️ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

* - comma (U+002C): X=185,Y=1 (should be at baseline 0?)
* - semicolon (U+003B): X=185,Y=1 (should be at baseline 0?)
* - eth (U+00F0): X=688,Y=699 (should be at cap-height 700?)
* - germandbls (U+00DF): X=638,Y=2 (should be at baseline 0?)
* - germandbls (U+00DF): X=323,Y=2 (should be at baseline 0?)
* - ordfeminine (U+00AA): X=377,Y=702 (should be at cap-height 700?)
* - ordfeminine (U+00AA): X=380,Y=702 (should be at cap-height 700?)
* - ordfeminine (U+00AA): X=432,Y=702 (should be at cap-height 700?)
* - ordfeminine (U+00AA): X=110,Y=702 (should be at cap-height 700?)
... and 16 others [code: found-misalignments]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (googlefonts/meta/script_lang_tags)</summary>
    <div>


> The OpenType 'meta' table originated at Apple. Microsoft added it to OT with just two DataMap records:
> 
> - dlng: comma-separated ScriptLangTags that indicate which scripts,   or languages and scripts, with possible variants, the font is designed for.
> 
> - slng: comma-separated ScriptLangTags that indicate which scripts,   or languages and scripts, with possible variants, the font supports.
> 
> The slng structure is intended to describe which languages and scripts the font overall supports. For example, a Traditional Chinese font that also contains Latin characters, can indicate Hant,Latn, showing that it supports Hant, the Traditional Chinese variant of the Hani script, and it also supports the Latn script.
> 
> The dlng structure is far more interesting. A font may contain various glyphs, but only a particular subset of the glyphs may be truly "leading" in the design, while other glyphs may have been included for technical reasons. Such a Traditional Chinese font could only list Hant there, showing that it’s designed for Traditional Chinese, but the font would omit Latn, because the developers don’t think the font is really recommended for purely Latin-script use.
> 
> The tags used in the structures can comprise just script, or also language and script. For example, if a font has Bulgarian Cyrillic alternates in the locl feature for the cyrl BGR OT languagesystem, it could also indicate in dlng explicitly that it supports bul-Cyrl. (Note that the scripts and languages in meta use the ISO language and script codes, not the OpenType ones).
> 
> This check ensures that the font has the meta table containing the slng and dlng structures.
> 
> All families in the Google Fonts collection should contain the 'meta' table. Windows 10 already uses it when deciding on which fonts to fall back to. The Google Fonts API and also other environments could use the data for smarter filtering. Most importantly, those entries should be added to the Noto fonts.
> 
> In the font making process, some environments store this data in external files already. But the meta table provides a convenient way to store this inside the font file, so some tools may add the data, and unrelated tools may read this data. This makes the solution much more portable and universal.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3349]





- ⚠️ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. (googlefonts/vendor_id)</summary>
    <div>


> Microsoft keeps a list of font vendors and their respective contact info. This list is updated regularly and is indexed by a 4-char "Vendor ID" which is stored in the achVendID field of the OS/2 table.
> 
> Registering your ID is not mandatory, but it is a good practice since some applications may display the type designer / type foundry contact info on some dialog and also because that info will be visible on Microsoft's website:
> 
> https://docs.microsoft.com/en-us/typography/vendors/
> 
> This check verifies whether or not a given font's vendor ID is registered in that list or if it has some of the default values used by the most common font editors.
> 
> Each new FontBakery release includes a cached copy of that list of vendor IDs. If you registered recently, you're safe to ignore warnings emitted by this check, since your ID will soon be included in one of our upcoming releases.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3943, https://github.com/fonttools/fontbakery/issues/4829]





- ⚠️ **WARN** OS/2 VendorID value 'XUQU' is not yet recognized.
If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
  
  

</div>
</details>


</div>
</details>


<details><summary>[18] xuqu-type-family/fonts/XUQU-Bold.ttf</summary>
<div>


<details>
    <summary>🔥 <b>FAIL</b> Check code page character ranges (opentype/code_pages)</summary>
    <div>


> At least some programs (such as Word and Sublime Text) under Windows 7 do not recognize fonts unless code page bits are properly set on the ulCodePageRange1 (and/or ulCodePageRange2) fields of the OS/2 table.
> 
> More specifically, the fonts are selectable in the font menu, but whichever Windows API these applications use considers them unsuitable for any character set, so anything set in these fonts is rendered with Arial as a fallback font.
> 
> This check currently does not identify which code pages should be set. Auto-detecting coverage is not trivial since the OpenType specification leaves the interpretation of whether a given code page is "functional" or not open to the font developer to decide.
> 
> So here we simply detect as a FAIL when a given font has no code page declared at all.




Original proposal: [https://github.com/fonttools/fontbakery/issues/2474]





- 🔥 **FAIL** No code pages defined in the OS/2 table ulCodePageRange1 and CodePageRange2 fields. [code: no-code-pages]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. (googlefonts/glyphsets/shape_languages)</summary>
    <div>


> This check uses a heuristic to determine which GF glyphsets a font supports. Then it checks the font for correct shaping behaviour for all languages in those glyphsets.




Original proposal: [https://github.com/googlefonts/fontbakery/issues/4147]





- 🔥 **FAIL** Failed language shaping:

| Message                                                                           | Languages                    |
|-----------------------------------------------------------------------------------|------------------------------|
| Mandatory orthography codepoints:                                                 | * cy_Latn (Welsh)            |
|   The following base characters are missing from the font: ẁ, ẃ, ỳ, Ẃ, ẅ, Ỳ, Ẅ, Ẁ |                              |
|   The following mark characters are missing from the font: ̈, ̂, ́, ̀                 |                              |
| Mandatory orthography codepoints:                                                 | * is_Latn (Icelandic)        |
|   The following mark characters are missing from the font: ̈, ̨, ́                   |                              |
| Mandatory orthography codepoints:                                                 | * en_Latn (English)          |
|   The following mark characters are missing from the font: ̃, ́, ̂, ̧, ̈, ̀             |                              |
| Mandatory orthography codepoints:                                                 | * es_Latn (Spanish)          |
|   The following mark characters are missing from the font: ̃, ̈, ́                   |                              |
| Mandatory orthography codepoints:                                                 | * ca_Latn (Catalan)          |
|   The following mark characters are missing from the font: ̧, ̀, ́, ̈                 |                              |
| Mandatory orthography codepoints:                                                 | * da_Latn (Danish)           |
|   The following mark characters are missing from the font: ̊, ́                     |                              |
| Mandatory orthography codepoints:                                                 | * lv_Latn (Latvian)          |
|   The following mark characters are missing from the font: ̧, ̄, ̌                   |                              |
| Mandatory orthography codepoints:                                                 | * nl_Latn (Dutch)            |
|   The following base characters are missing from the font: ÍJ́, íj́                 |                              |
|   The following mark characters are missing from the font: ̀, ́, ̈, ̂                 |                              |
| Mandatory orthography codepoints:                                                 | * it_Latn (Italian)          |
|   The following mark characters are missing from the font: ̂, ̀, ́, ̈                 |                              |
| Mandatory orthography codepoints:                                                 | * lt_Latn (Lithuanian)       |
|   The following mark characters are missing from the font: ̄, ̇, ̌, ̨                 |                              |
| Mandatory orthography codepoints:                                                 | * cs_Latn (Czech)            |
|   The following mark characters are missing from the font: ́, ̊, ̌                   |                              |
| Mandatory orthography codepoints:                                                 | * nb_Latn (Norwegian Bokmål) |
|   The following mark characters are missing from the font: ̀, ̂, ́, ̊, ̈               |                              |
| Mandatory orthography codepoints:                                                 | * ro_Latn (Romanian)         |
|   The following base characters are missing from the font: Ț, ț, ș, Ș             |                              |
|   The following mark characters are missing from the font: ̆, ̧, ̂, ̦                 |                              |
| Mandatory orthography codepoints:                                                 | * sk_Latn (Slovak)           |
|   The following mark characters are missing from the font: ̈, ̌, ́, ̂                 |                              |
| Mandatory orthography codepoints:                                                 | * tr_Latn (Turkish)          |
|   The following mark characters are missing from the font: ̇, ̂, ̆, ̈, ̧, ̦             |                              |
| Mandatory orthography codepoints:                                                 | * fi_Latn (Finnish)          |
|   The following mark characters are missing from the font: ̃, ̊, ̈, ̌                 |                              |
| Mandatory orthography codepoints:                                                 | * fr_Latn (French)           |
|   The following mark characters are missing from the font: ̈, ̀, ̂, ̧, ́               |                              |
| Mandatory orthography codepoints:                                                 | * de_Latn (German)           |
|   The following base characters are missing from the font: ẞ                      |                              |
|   The following mark characters are missing from the font: ̀, ̈, ́                   |                              |
| Mandatory orthography codepoints:                                                 | * hu_Latn (Hungarian)        |
|   The following mark characters are missing from the font: ̋, ̈, ́                   |                              |
| Mandatory orthography codepoints:                                                 | * mt_Latn (Maltese)          |
|   The following mark characters are missing from the font: ̂, ̇, ̀                   |                              |
| Mandatory orthography codepoints:                                                 | * pl_Latn (Polish)           |
|   The following mark characters are missing from the font: ̇, ́, ̨                   |                              |
| Mandatory orthography codepoints:                                                 | * pt_Latn (Portuguese)       |
|   The following mark characters are missing from the font: ̃, ̀, ̧, ̂, ̈, ́             |                              |
| Mandatory orthography codepoints:                                                 | * hr_Latn (Croatian)         |
|   The following mark characters are missing from the font: ́, ̌                     |                              |
| Mandatory orthography codepoints:                                                 | * sv_Latn (Swedish)          |
|   The following mark characters are missing from the font: ̀, ̈, ́, ̊                 |                              |
| Mandatory orthography codepoints:                                                 | * sq_Latn (Albanian)         |
|   The following mark characters are missing from the font: ̧, ̈                     |                              | [code: failed-language-shaping]
  
  


- ⚠️ **WARN** Warning language shaping:

| Message                                                           | Languages                    |
|-------------------------------------------------------------------|------------------------------|
| Auxiliary orthography codepoints:                                 | * da_Latn (Danish)           |
|   The following auxiliary characters are missing from the font: Ǿ |                              |
|   The following auxiliary characters are missing from the font: ǿ |                              |
| Auxiliary orthography codepoints:                                 | * fr_Latn (French)           |
|   The following auxiliary characters are missing from the font: ẞ |                              |
|   The following auxiliary characters are missing from the font: Ǔ |                              |
|   The following auxiliary characters are missing from the font: ǔ |                              |
| Auxiliary orthography codepoints:                                 | * lt_Latn (Lithuanian)       |
|   The following auxiliary characters are missing from the font: Ą́ |                              |
|   The following auxiliary characters are missing from the font: Ą̃ |                              |
|   The following auxiliary characters are missing from the font: Ẽ |                              |
|   The following auxiliary characters are missing from the font: Ę́ |                              |
|   The following auxiliary characters are missing from the font: Ę̃ |                              |
|   The following auxiliary characters are missing from the font: Ė́ |                              |
|   The following auxiliary characters are missing from the font: Ė̃ |                              |
|   The following auxiliary characters are missing from the font: İ́ |                              |
|   The following auxiliary characters are missing from the font: İ́ |                              |
|   The following auxiliary characters are missing from the font: İ̀ |                              |
|   The following auxiliary characters are missing from the font: İ̀ |                              |
|   The following auxiliary characters are missing from the font: İ̃ |                              |
|   The following auxiliary characters are missing from the font: İ̃ |                              |
|   The following auxiliary characters are missing from the font: Į́ |                              |
|   The following auxiliary characters are missing from the font: Į̇́ |                              |
|   The following auxiliary characters are missing from the font: Į̃ |                              |
|   The following auxiliary characters are missing from the font: Į̇̃ |                              |
|   The following auxiliary characters are missing from the font: J̃ |                              |
|   The following auxiliary characters are missing from the font: J̇̃ |                              |
|   The following auxiliary characters are missing from the font: L̃ |                              |
|   The following auxiliary characters are missing from the font: M̃ |                              |
|   The following auxiliary characters are missing from the font: R̃ |                              |
|   The following auxiliary characters are missing from the font: Ų́ |                              |
|   The following auxiliary characters are missing from the font: Ų̃ |                              |
|   The following auxiliary characters are missing from the font: Ū́ |                              |
|   The following auxiliary characters are missing from the font: Ū̃ |                              |
|   The following auxiliary characters are missing from the font: ą́ |                              |
|   The following auxiliary characters are missing from the font: ą̃ |                              |
|   The following auxiliary characters are missing from the font: ẽ |                              |
|   The following auxiliary characters are missing from the font: ę́ |                              |
|   The following auxiliary characters are missing from the font: ę̃ |                              |
|   The following auxiliary characters are missing from the font: ė́ |                              |
|   The following auxiliary characters are missing from the font: ė̃ |                              |
|   The following auxiliary characters are missing from the font: i̇́ |                              |
|   The following auxiliary characters are missing from the font: i̇̀ |                              |
|   The following auxiliary characters are missing from the font: i̇̃ |                              |
|   The following auxiliary characters are missing from the font: į́ |                              |
|   The following auxiliary characters are missing from the font: į̇́ |                              |
|   The following auxiliary characters are missing from the font: į̃ |                              |
|   The following auxiliary characters are missing from the font: į̇̃ |                              |
|   The following auxiliary characters are missing from the font: j̃ |                              |
|   The following auxiliary characters are missing from the font: j̇̃ |                              |
|   The following auxiliary characters are missing from the font: l̃ |                              |
|   The following auxiliary characters are missing from the font: m̃ |                              |
|   The following auxiliary characters are missing from the font: r̃ |                              |
|   The following auxiliary characters are missing from the font: ų́ |                              |
|   The following auxiliary characters are missing from the font: ų̃ |                              |
|   The following auxiliary characters are missing from the font: ū́ |                              |
|   The following auxiliary characters are missing from the font: ū̃ |                              |
| Auxiliary orthography codepoints:                                 | * nb_Latn (Norwegian Bokmål) |
|   The following auxiliary characters are missing from the font: Ǎ |                              |
|   The following auxiliary characters are missing from the font: ǎ |                              |
| Auxiliary orthography codepoints:                                 | * fi_Latn (Finnish)          |
|   The following auxiliary characters are missing from the font: Ǧ |                              |
|   The following auxiliary characters are missing from the font: Ǥ |                              |
|   The following auxiliary characters are missing from the font: Ȟ |                              |
|   The following auxiliary characters are missing from the font: Ǩ |                              |
|   The following auxiliary characters are missing from the font: Ș |                              |
|   The following auxiliary characters are missing from the font: ẞ |                              |
|   The following auxiliary characters are missing from the font: Ț |                              |
|   The following auxiliary characters are missing from the font: Ʒ |                              |
|   The following auxiliary characters are missing from the font: Ǯ |                              |
|   The following auxiliary characters are missing from the font: ǧ |                              |
|   The following auxiliary characters are missing from the font: ǥ |                              |
|   The following auxiliary characters are missing from the font: ȟ |                              |
|   The following auxiliary characters are missing from the font: ǩ |                              |
|   The following auxiliary characters are missing from the font: ș |                              |
|   The following auxiliary characters are missing from the font: ț |                              |
|   The following auxiliary characters are missing from the font: ʒ |                              |
|   The following auxiliary characters are missing from the font: ǯ |                              |
| Auxiliary orthography codepoints:                                 | * it_Latn (Italian)          |
|   The following auxiliary characters are missing from the font: ẞ | * pl_Latn (Polish)           |
|                                                                   | * tr_Latn (Turkish)          |
| Auxiliary orthography codepoints:                                 | * en_Latn (English)          |
|   The following auxiliary characters are missing from the font: ʻ |                              | [code: warning-language-shaping]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Check family name for GF Guide compliance. (googlefonts/family_name_compliance)</summary>
    <div>


> Checks the family name for compliance with the Google Fonts Guide. https://googlefonts.github.io/gf-guide/onboarding.html#new-fonts
> 
> If you want to have your family name added to the CamelCase exceptions list, please submit a pull request to the camelcased_familyname_exceptions.txt file.
> 
> Similarly, abbreviations can be submitted to the abbreviations_familyname_exceptions.txt file.
> 
> These are located in the Lib/fontbakery/data/googlefonts/ directory of the FontBakery source code currently hosted at https://github.com/fonttools/fontbakery/




Original proposal: [https://github.com/fonttools/fontbakery/issues/4049]





- 🔥 **FAIL** "XUQU体" contains an abbreviation. [code: abbreviation]
  
  


- 🔥 **FAIL** "XUQU体" contains the following characters which are not allowed: "体". [code: forbidden-characters]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Checking file is named canonically. (googlefonts/canonical_filename)</summary>
    <div>


> A font's filename must be composed as "<familyname>-<stylename>.ttf":
> 
> - Nunito-Regular.ttf
> 
> - Oswald-BoldItalic.ttf
> 
> Variable fonts must list the axis tags in alphabetical order in square brackets and separated by commas:
> 
> - Roboto[wdth,wght].ttf
> 
> - Familyname-Italic[wght].ttf




Original proposal: [https://github.com/fonttools/fontbakery/issues/4829]





- 🔥 **FAIL** Expected "XUQU体-Bold.ttf". Got "XUQU-Bold.ttf". [code: bad-filename]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Check font names are correct (googlefonts/font_names)</summary>
    <div>


> Google Fonts has several rules which need to be adhered to when setting a font's name table. Please read: https://googlefonts.github.io/gf-guide/statics.html#supported-styles https://googlefonts.github.io/gf-guide/statics.html#style-linking https://googlefonts.github.io/gf-guide/statics.html#unsupported-styles https://googlefonts.github.io/gf-guide/statics.html#single-weight-families




Original proposal: [https://github.com/fonttools/fontbakery/pull/3800]





- 🔥 **FAIL** Font names are incorrect:

| Name                       | Current       | Expected        |
|----------------------------|---------------|-----------------|
| Family Name                | XUQU体        | XUQU体          |
| Subfamily Name             | Bold          | Bold            |
| Full Name                  | XUQU体 Bold   | XUQU体 Bold     |
| Postscript Name            | **XUQU-Bold** | **XUQU体-Bold** |
| Typographic Family Name    | XUQU体        | XUQU体          |
| Typographic Subfamily Name | **Bold**      | **粗体**        | [code: bad-names]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Ensure font can render its own name. (googlefonts/render_own_name)</summary>
    <div>


> A base expectation is that a font family's regular/default (400 roman) style can render its 'menu name' (nameID 1) in itself.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3159]





- 🔥 **FAIL** .notdef glyphs were found when attempting to render XUQU体 [code: render-own-name]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check that OS/2 fsSelection WWS bit is set correctly. (opentype/fsselection_wws)</summary>
    <div>


> According to the OpenType specification, OS/2.fsSelection bit 8 (WWS) should be set if the font has name table strings consistent with a weight/width/slope family without requiring use of name IDs 21 and 22.
> 
> Conversely, if name IDs 21 and 22 are present (indicating the font names are not WWS-conformant), the WWS bit should not be set.




Original proposal: [https://github.com/fonttools/fontspector/issues/577]





- ⚠️ **WARN** OS/2 fsSelection WWS bit is not set, and the font does not have name IDs 21/22 (WWS Family/Subfamily). If the font's naming is WWS-conformant, the WWS bit should be set. [code: no-wws-without-wws-names]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron (alt_caron)</summary>
    <div>


> Lcaron, dcaron, lcaron, tcaron should NOT be composed with quoteright or quotesingle or comma or caron(comb). It should be composed with a distinctive glyph which doesn't look like an apostrophe.
> 
> Source: https://ilovetypography.com/2009/01/24/on-diacritics/ http://diacritics.typo.cz/index.php?id=5 https://www.typotheque.com/articles/lcaron




Original proposal: [https://github.com/fonttools/fontbakery/issues/3308]





- ⚠️ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  


- ⚠️ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  


- ⚠️ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  


- ⚠️ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. (contour_count)</summary>
    <div>


> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be constructured in a handful of ways. This means a glyph's contour count will only differ slightly amongst different fonts, e.g a 'g' could either be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs to a display family.
> 
> This check currently does not cover variable fonts because there's plenty of alternative ways of constructing glyphs with multiple outlines for each feature in a VarFont. The expected contour count data for this check is currently optimized for the typical construction of glyphs in static fonts.




Original proposal: [https://github.com/fonttools/fontbakery/issues/4829]





- ⚠️ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are
     inferred from the typical amounts of contours observed in a
     large collection of reference font families. The divergences
     listed below may simply indicate a significantly different
     design on some of your glyphs. On the other hand, some of these
     may flag actual bugs in the font such as glyphs mapped to an
     incorrect codepoint. Please consider reviewing the design and
     codepoint assignment of these to make sure they are correct.


    The following glyphs do not have the recommended number of contours:
* uni013C (U+013C): found 1, expected one of: [2, 3, 6]
* section (U+00A7): found 1, expected one of: [2, 4, 6] [code: contour-count]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. (math_signs_width)</summary>
    <div>


> #,         It is a common practice to have math signs sharing the same width         (preferably the same width as tabular figures accross the entire font family).
> 
> This probably comes from the will to avoid additional tabular math signs knowing that their design can easily share the same width.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3832]





- ⚠️ **WARN** The most common width is 766 among a set of 12  math glyphs.
The following math glyphs have a different width, though:
width=746: greater, less, greaterequal, lessequal
width=556: minus [code: width-outliers]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure indic fonts have the Indian Rupee Sign glyph. (rupee)</summary>
    <div>


> Per Bureau of Indian Standards every font supporting one of the official Indian languages needs to include Unicode Character “₹” (U+20B9) Indian Rupee Sign.




Original proposal: [https://github.com/fonttools/fontbakery/issues/2967]





- ⚠️ **WARN** Font is missing the Indian Rupee Sign glyph. Please add a glyph for Indian Rupee Sign (₹) at codepoint U+20B9. [code: missing-rupee]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? (soft_hyphen)</summary>
    <div>


> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character), sometimes the same as the traditional hyphen, sometimes double encoded with the hyphen.
> 
> That being said, it is recommended to not include it in the font at all, because discretionary hyphenation should be handled at the level of the shaping engine, not the font. Also, even if present, the software would not display that character.
> 
> More discussion at: https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar




Original proposal: [https://github.com/fonttools/fontbakery/issues/4046, https://github.com/fonttools/fontbakery/issues/3486]





- ⚠️ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs (unreachable_glyphs)</summary>
    <div>


> Glyphs are either accessible directly through Unicode codepoints or through        substitution rules.
> 
> In Color Fonts, glyphs are also referenced by the COLR table. And mathematical fonts also reference glyphs via the MATH table.
> 
> Any glyphs not accessible by these means are redundant and serve only to increase the font's file size.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3160]





- ⚠️ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

* .null
* nonmarkingreturn [code: unreachable-glyphs]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Font has correct separator glyphs? (googlefonts/separator_glyphs)</summary>
    <div>


> U+2028 and U+2029 should be present; otherwise tofu is displayed. (whitespace_ink will check that they are empty)




Original proposal: [https://github.com/fonttools/fontspector/issues/93]





- ⚠️ **WARN** Missing separator glyph U+2028 [code: missing-separator-glyphs]
  
  


- ⚠️ **WARN** Missing separator glyph U+2029 [code: missing-separator-glyphs]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? (outline_alignment_miss)</summary>
    <div>


> This check heuristically looks for on-curve points which are close to, but do not sit on, significant boundary coordinates. For example, a point which has a Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the baseline, here we also check for points near the x-height (but only for lowercase Latin letters), cap-height, ascender and descender Y coordinates.
> 
> Not all such misaligned curve points are a mistake, and sometimes the design may call for points in locations near the boundaries. As this check is liable to generate significant numbers of false positives, it will pass if there are more than 100 reported misalignments.




Original proposal: [https://github.com/fonttools/fontbakery/pull/3088]





- ⚠️ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

* - ampersand (U+0026): X=323,Y=-2 (should be at baseline 0?)
* - ampersand (U+0026): X=143,Y=-2 (should be at baseline 0?)
* - braceleft (U+007B): X=135,Y=-1 (should be at baseline 0?)
* - braceleft (U+007B): X=135,Y=701 (should be at cap-height 700?)
* - braceright (U+007D): X=311,Y=701 (should be at cap-height 700?)
* - braceright (U+007D): X=311,Y=-1 (should be at baseline 0?)
* - germandbls (U+00DF): X=630,Y=2 (should be at baseline 0?)
* - germandbls (U+00DF): X=303,Y=2 (should be at baseline 0?)
* - ordfeminine (U+00AA): X=110,Y=702 (should be at cap-height 700?)
... and 21 others [code: found-misalignments]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? (outline_colinear_vectors)</summary>
    <div>


> This check looks for consecutive line segments which have the same angle. This normally happens if an outline point has been added by accident.
> 
> This check is not run for variable fonts, as they may legitimately have colinear vectors.




Original proposal: [https://github.com/fonttools/fontbakery/pull/3088]





- ⚠️ **WARN** The following glyphs have colinear vectors:

* A (U+0041): from (58.0, 0.0) to (152.0, 203.0) is colinear with segment from (152.0, 203.0) to (214.0, 337.0)
* A (U+0041): from (152.0, 203.0) to (214.0, 337.0) is colinear with segment from (214.0, 337.0) to (382.0, 700.0)
* A (U+0041): from (574.0, 700.0) to (742.0, 337.0) is colinear with segment from (742.0, 337.0) to (804.0, 203.0)
* A (U+0041): from (742.0, 337.0) to (804.0, 203.0) is colinear with segment from (804.0, 203.0) to (898.0, 0.0)
* b (U+0062): from (643.0, 0.0) to (206.0, 0.0) is colinear with segment from (206.0, 0.0) to (58.0, 0.0)
* b (U+0062): from (58.0, 0.0) to (58.0, 530.0) is colinear with segment from (58.0, 530.0) to (58.0, 700.0)
* d (U+0064): from (738.0, 700.0) to (738.0, 530.0) is colinear with segment from (738.0, 530.0) to (738.0, 0.0)
* d (U+0064): from (738.0, 0.0) to (590.0, 0.0) is colinear with segment from (590.0, 0.0) to (153.0, 0.0)
* p (U+0070): from (58.0, -205.0) to (58.0, 0.0) is colinear with segment from (58.0, 0.0) to (58.0, 530.0)
... and 86 others [code: found-colinear-vectors]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (googlefonts/meta/script_lang_tags)</summary>
    <div>


> The OpenType 'meta' table originated at Apple. Microsoft added it to OT with just two DataMap records:
> 
> - dlng: comma-separated ScriptLangTags that indicate which scripts,   or languages and scripts, with possible variants, the font is designed for.
> 
> - slng: comma-separated ScriptLangTags that indicate which scripts,   or languages and scripts, with possible variants, the font supports.
> 
> The slng structure is intended to describe which languages and scripts the font overall supports. For example, a Traditional Chinese font that also contains Latin characters, can indicate Hant,Latn, showing that it supports Hant, the Traditional Chinese variant of the Hani script, and it also supports the Latn script.
> 
> The dlng structure is far more interesting. A font may contain various glyphs, but only a particular subset of the glyphs may be truly "leading" in the design, while other glyphs may have been included for technical reasons. Such a Traditional Chinese font could only list Hant there, showing that it’s designed for Traditional Chinese, but the font would omit Latn, because the developers don’t think the font is really recommended for purely Latin-script use.
> 
> The tags used in the structures can comprise just script, or also language and script. For example, if a font has Bulgarian Cyrillic alternates in the locl feature for the cyrl BGR OT languagesystem, it could also indicate in dlng explicitly that it supports bul-Cyrl. (Note that the scripts and languages in meta use the ISO language and script codes, not the OpenType ones).
> 
> This check ensures that the font has the meta table containing the slng and dlng structures.
> 
> All families in the Google Fonts collection should contain the 'meta' table. Windows 10 already uses it when deciding on which fonts to fall back to. The Google Fonts API and also other environments could use the data for smarter filtering. Most importantly, those entries should be added to the Noto fonts.
> 
> In the font making process, some environments store this data in external files already. But the meta table provides a convenient way to store this inside the font file, so some tools may add the data, and unrelated tools may read this data. This makes the solution much more portable and universal.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3349]





- ⚠️ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. (googlefonts/vendor_id)</summary>
    <div>


> Microsoft keeps a list of font vendors and their respective contact info. This list is updated regularly and is indexed by a 4-char "Vendor ID" which is stored in the achVendID field of the OS/2 table.
> 
> Registering your ID is not mandatory, but it is a good practice since some applications may display the type designer / type foundry contact info on some dialog and also because that info will be visible on Microsoft's website:
> 
> https://docs.microsoft.com/en-us/typography/vendors/
> 
> This check verifies whether or not a given font's vendor ID is registered in that list or if it has some of the default values used by the most common font editors.
> 
> Each new FontBakery release includes a cached copy of that list of vendor IDs. If you registered recently, you're safe to ignore warnings emitted by this check, since your ID will soon be included in one of our upcoming releases.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3943, https://github.com/fonttools/fontbakery/issues/4829]





- ⚠️ **WARN** OS/2 VendorID value 'XUQU' is not yet recognized.
If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
  
  

</div>
</details>


</div>
</details>


<details><summary>[19] xuqu-type-family/fonts/XUQU-Light.ttf</summary>
<div>


<details>
    <summary>🔥 <b>FAIL</b> Check code page character ranges (opentype/code_pages)</summary>
    <div>


> At least some programs (such as Word and Sublime Text) under Windows 7 do not recognize fonts unless code page bits are properly set on the ulCodePageRange1 (and/or ulCodePageRange2) fields of the OS/2 table.
> 
> More specifically, the fonts are selectable in the font menu, but whichever Windows API these applications use considers them unsuitable for any character set, so anything set in these fonts is rendered with Arial as a fallback font.
> 
> This check currently does not identify which code pages should be set. Auto-detecting coverage is not trivial since the OpenType specification leaves the interpretation of whether a given code page is "functional" or not open to the font developer to decide.
> 
> So here we simply detect as a FAIL when a given font has no code page declared at all.




Original proposal: [https://github.com/fonttools/fontbakery/issues/2474]





- 🔥 **FAIL** No code pages defined in the OS/2 table ulCodePageRange1 and CodePageRange2 fields. [code: no-code-pages]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. (googlefonts/glyphsets/shape_languages)</summary>
    <div>


> This check uses a heuristic to determine which GF glyphsets a font supports. Then it checks the font for correct shaping behaviour for all languages in those glyphsets.




Original proposal: [https://github.com/googlefonts/fontbakery/issues/4147]





- 🔥 **FAIL** Failed language shaping:

| Message                                                                           | Languages                    |
|-----------------------------------------------------------------------------------|------------------------------|
| Mandatory orthography codepoints:                                                 | * ca_Latn (Catalan)          |
|   The following mark characters are missing from the font: ̧, ̀, ́, ̈                 |                              |
| Mandatory orthography codepoints:                                                 | * cy_Latn (Welsh)            |
|   The following base characters are missing from the font: ẁ, Ẅ, ỳ, Ỳ, ẃ, Ẁ, ẅ, Ẃ |                              |
|   The following mark characters are missing from the font: ́, ̂, ̈, ̀                 |                              |
| Mandatory orthography codepoints:                                                 | * ro_Latn (Romanian)         |
|   The following base characters are missing from the font: Ș, ș, ț, Ț             |                              |
|   The following mark characters are missing from the font: ̂, ̧, ̆, ̦                 |                              |
| Mandatory orthography codepoints:                                                 | * sq_Latn (Albanian)         |
|   The following mark characters are missing from the font: ̈, ̧                     |                              |
| Mandatory orthography codepoints:                                                 | * de_Latn (German)           |
|   The following base characters are missing from the font: ẞ                      |                              |
|   The following mark characters are missing from the font: ́, ̀, ̈                   |                              |
| Mandatory orthography codepoints:                                                 | * fr_Latn (French)           |
|   The following mark characters are missing from the font: ̧, ̀, ́, ̈, ̂               |                              |
| Mandatory orthography codepoints:                                                 | * is_Latn (Icelandic)        |
|   The following mark characters are missing from the font: ̨, ́, ̈                   |                              |
| Mandatory orthography codepoints:                                                 | * it_Latn (Italian)          |
|   The following mark characters are missing from the font: ̂, ́, ̀, ̈                 |                              |
| Mandatory orthography codepoints:                                                 | * hr_Latn (Croatian)         |
|   The following mark characters are missing from the font: ̌, ́                     |                              |
| Mandatory orthography codepoints:                                                 | * nl_Latn (Dutch)            |
|   The following base characters are missing from the font: ÍJ́, íj́                 |                              |
|   The following mark characters are missing from the font: ̀, ́, ̂, ̈                 |                              |
| Mandatory orthography codepoints:                                                 | * pt_Latn (Portuguese)       |
|   The following mark characters are missing from the font: ́, ̃, ̀, ̧, ̂, ̈             |                              |
| Mandatory orthography codepoints:                                                 | * sk_Latn (Slovak)           |
|   The following mark characters are missing from the font: ̈, ̌, ́, ̂                 |                              |
| Mandatory orthography codepoints:                                                 | * en_Latn (English)          |
|   The following mark characters are missing from the font: ̂, ̧, ̀, ̃, ́, ̈             |                              |
| Mandatory orthography codepoints:                                                 | * cs_Latn (Czech)            |
|   The following mark characters are missing from the font: ̊, ́, ̌                   |                              |
| Mandatory orthography codepoints:                                                 | * lv_Latn (Latvian)          |
|   The following mark characters are missing from the font: ̌, ̧, ̄                   |                              |
| Mandatory orthography codepoints:                                                 | * nb_Latn (Norwegian Bokmål) |
|   The following mark characters are missing from the font: ̀, ̂, ̈, ̊, ́               |                              |
| Mandatory orthography codepoints:                                                 | * es_Latn (Spanish)          |
|   The following mark characters are missing from the font: ̃, ̈, ́                   |                              |
| Mandatory orthography codepoints:                                                 | * da_Latn (Danish)           |
|   The following mark characters are missing from the font: ̊, ́                     |                              |
| Mandatory orthography codepoints:                                                 | * sv_Latn (Swedish)          |
|   The following mark characters are missing from the font: ́, ̊, ̀, ̈                 |                              |
| Mandatory orthography codepoints:                                                 | * mt_Latn (Maltese)          |
|   The following mark characters are missing from the font: ̇, ̀, ̂                   |                              |
| Mandatory orthography codepoints:                                                 | * pl_Latn (Polish)           |
|   The following mark characters are missing from the font: ̇, ̨, ́                   |                              |
| Mandatory orthography codepoints:                                                 | * fi_Latn (Finnish)          |
|   The following mark characters are missing from the font: ̌, ̈, ̊, ̃                 |                              |
| Mandatory orthography codepoints:                                                 | * lt_Latn (Lithuanian)       |
|   The following mark characters are missing from the font: ̇, ̌, ̨, ̄                 |                              |
| Mandatory orthography codepoints:                                                 | * tr_Latn (Turkish)          |
|   The following mark characters are missing from the font: ̧, ̇, ̈, ̂, ̆, ̦             |                              |
| Mandatory orthography codepoints:                                                 | * hu_Latn (Hungarian)        |
|   The following mark characters are missing from the font: ́, ̈, ̋                   |                              | [code: failed-language-shaping]
  
  


- ⚠️ **WARN** Warning language shaping:

| Message                                                           | Languages                    |
|-------------------------------------------------------------------|------------------------------|
| Auxiliary orthography codepoints:                                 | * lt_Latn (Lithuanian)       |
|   The following auxiliary characters are missing from the font: Ą́ |                              |
|   The following auxiliary characters are missing from the font: Ą̃ |                              |
|   The following auxiliary characters are missing from the font: Ẽ |                              |
|   The following auxiliary characters are missing from the font: Ę́ |                              |
|   The following auxiliary characters are missing from the font: Ę̃ |                              |
|   The following auxiliary characters are missing from the font: Ė́ |                              |
|   The following auxiliary characters are missing from the font: Ė̃ |                              |
|   The following auxiliary characters are missing from the font: İ́ |                              |
|   The following auxiliary characters are missing from the font: İ́ |                              |
|   The following auxiliary characters are missing from the font: İ̀ |                              |
|   The following auxiliary characters are missing from the font: İ̀ |                              |
|   The following auxiliary characters are missing from the font: İ̃ |                              |
|   The following auxiliary characters are missing from the font: İ̃ |                              |
|   The following auxiliary characters are missing from the font: Į́ |                              |
|   The following auxiliary characters are missing from the font: Į̇́ |                              |
|   The following auxiliary characters are missing from the font: Į̃ |                              |
|   The following auxiliary characters are missing from the font: Į̇̃ |                              |
|   The following auxiliary characters are missing from the font: J̃ |                              |
|   The following auxiliary characters are missing from the font: J̇̃ |                              |
|   The following auxiliary characters are missing from the font: L̃ |                              |
|   The following auxiliary characters are missing from the font: M̃ |                              |
|   The following auxiliary characters are missing from the font: R̃ |                              |
|   The following auxiliary characters are missing from the font: Ų́ |                              |
|   The following auxiliary characters are missing from the font: Ų̃ |                              |
|   The following auxiliary characters are missing from the font: Ū́ |                              |
|   The following auxiliary characters are missing from the font: Ū̃ |                              |
|   The following auxiliary characters are missing from the font: ą́ |                              |
|   The following auxiliary characters are missing from the font: ą̃ |                              |
|   The following auxiliary characters are missing from the font: ẽ |                              |
|   The following auxiliary characters are missing from the font: ę́ |                              |
|   The following auxiliary characters are missing from the font: ę̃ |                              |
|   The following auxiliary characters are missing from the font: ė́ |                              |
|   The following auxiliary characters are missing from the font: ė̃ |                              |
|   The following auxiliary characters are missing from the font: i̇́ |                              |
|   The following auxiliary characters are missing from the font: i̇̀ |                              |
|   The following auxiliary characters are missing from the font: i̇̃ |                              |
|   The following auxiliary characters are missing from the font: į́ |                              |
|   The following auxiliary characters are missing from the font: į̇́ |                              |
|   The following auxiliary characters are missing from the font: į̃ |                              |
|   The following auxiliary characters are missing from the font: į̇̃ |                              |
|   The following auxiliary characters are missing from the font: j̃ |                              |
|   The following auxiliary characters are missing from the font: j̇̃ |                              |
|   The following auxiliary characters are missing from the font: l̃ |                              |
|   The following auxiliary characters are missing from the font: m̃ |                              |
|   The following auxiliary characters are missing from the font: r̃ |                              |
|   The following auxiliary characters are missing from the font: ų́ |                              |
|   The following auxiliary characters are missing from the font: ų̃ |                              |
|   The following auxiliary characters are missing from the font: ū́ |                              |
|   The following auxiliary characters are missing from the font: ū̃ |                              |
| Auxiliary orthography codepoints:                                 | * nb_Latn (Norwegian Bokmål) |
|   The following auxiliary characters are missing from the font: Ǎ |                              |
|   The following auxiliary characters are missing from the font: ǎ |                              |
| Auxiliary orthography codepoints:                                 | * fi_Latn (Finnish)          |
|   The following auxiliary characters are missing from the font: Ǧ |                              |
|   The following auxiliary characters are missing from the font: Ǥ |                              |
|   The following auxiliary characters are missing from the font: Ȟ |                              |
|   The following auxiliary characters are missing from the font: Ǩ |                              |
|   The following auxiliary characters are missing from the font: Ș |                              |
|   The following auxiliary characters are missing from the font: ẞ |                              |
|   The following auxiliary characters are missing from the font: Ț |                              |
|   The following auxiliary characters are missing from the font: Ʒ |                              |
|   The following auxiliary characters are missing from the font: Ǯ |                              |
|   The following auxiliary characters are missing from the font: ǧ |                              |
|   The following auxiliary characters are missing from the font: ǥ |                              |
|   The following auxiliary characters are missing from the font: ȟ |                              |
|   The following auxiliary characters are missing from the font: ǩ |                              |
|   The following auxiliary characters are missing from the font: ș |                              |
|   The following auxiliary characters are missing from the font: ț |                              |
|   The following auxiliary characters are missing from the font: ʒ |                              |
|   The following auxiliary characters are missing from the font: ǯ |                              |
| Auxiliary orthography codepoints:                                 | * fr_Latn (French)           |
|   The following auxiliary characters are missing from the font: ẞ |                              |
|   The following auxiliary characters are missing from the font: Ǔ |                              |
|   The following auxiliary characters are missing from the font: ǔ |                              |
| Auxiliary orthography codepoints:                                 | * en_Latn (English)          |
|   The following auxiliary characters are missing from the font: ʻ |                              |
| Auxiliary orthography codepoints:                                 | * da_Latn (Danish)           |
|   The following auxiliary characters are missing from the font: Ǿ |                              |
|   The following auxiliary characters are missing from the font: ǿ |                              |
| Auxiliary orthography codepoints:                                 | * it_Latn (Italian)          |
|   The following auxiliary characters are missing from the font: ẞ | * pl_Latn (Polish)           |
|                                                                   | * tr_Latn (Turkish)          | [code: warning-language-shaping]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Check family name for GF Guide compliance. (googlefonts/family_name_compliance)</summary>
    <div>


> Checks the family name for compliance with the Google Fonts Guide. https://googlefonts.github.io/gf-guide/onboarding.html#new-fonts
> 
> If you want to have your family name added to the CamelCase exceptions list, please submit a pull request to the camelcased_familyname_exceptions.txt file.
> 
> Similarly, abbreviations can be submitted to the abbreviations_familyname_exceptions.txt file.
> 
> These are located in the Lib/fontbakery/data/googlefonts/ directory of the FontBakery source code currently hosted at https://github.com/fonttools/fontbakery/




Original proposal: [https://github.com/fonttools/fontbakery/issues/4049]





- 🔥 **FAIL** "XUQU体" contains an abbreviation. [code: abbreviation]
  
  


- 🔥 **FAIL** "XUQU体" contains the following characters which are not allowed: "体". [code: forbidden-characters]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Checking file is named canonically. (googlefonts/canonical_filename)</summary>
    <div>


> A font's filename must be composed as "<familyname>-<stylename>.ttf":
> 
> - Nunito-Regular.ttf
> 
> - Oswald-BoldItalic.ttf
> 
> Variable fonts must list the axis tags in alphabetical order in square brackets and separated by commas:
> 
> - Roboto[wdth,wght].ttf
> 
> - Familyname-Italic[wght].ttf




Original proposal: [https://github.com/fonttools/fontbakery/issues/4829]





- 🔥 **FAIL** Expected "XUQU体-Light.ttf". Got "XUQU-Light.ttf". [code: bad-filename]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Check font names are correct (googlefonts/font_names)</summary>
    <div>


> Google Fonts has several rules which need to be adhered to when setting a font's name table. Please read: https://googlefonts.github.io/gf-guide/statics.html#supported-styles https://googlefonts.github.io/gf-guide/statics.html#style-linking https://googlefonts.github.io/gf-guide/statics.html#unsupported-styles https://googlefonts.github.io/gf-guide/statics.html#single-weight-families




Original proposal: [https://github.com/fonttools/fontbakery/pull/3800]





- 🔥 **FAIL** Font names are incorrect:

| Name                       | Current        | Expected         |
|----------------------------|----------------|------------------|
| Family Name                | XUQU体 Light   | XUQU体 Light     |
| Subfamily Name             | Regular        | Regular          |
| Full Name                  | XUQU体 Light   | XUQU体 Light     |
| Postscript Name            | **XUQU-Light** | **XUQU体-Light** |
| Typographic Family Name    | XUQU体         | XUQU体           |
| Typographic Subfamily Name | Light          | Light            | [code: bad-names]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Ensure font can render its own name. (googlefonts/render_own_name)</summary>
    <div>


> A base expectation is that a font family's regular/default (400 roman) style can render its 'menu name' (nameID 1) in itself.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3159]





- 🔥 **FAIL** .notdef glyphs were found when attempting to render XUQU体 Light [code: render-own-name]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check that OS/2 fsSelection WWS bit is set correctly. (opentype/fsselection_wws)</summary>
    <div>


> According to the OpenType specification, OS/2.fsSelection bit 8 (WWS) should be set if the font has name table strings consistent with a weight/width/slope family without requiring use of name IDs 21 and 22.
> 
> Conversely, if name IDs 21 and 22 are present (indicating the font names are not WWS-conformant), the WWS bit should not be set.




Original proposal: [https://github.com/fonttools/fontspector/issues/577]





- ⚠️ **WARN** OS/2 fsSelection WWS bit is not set, and the font does not have name IDs 21/22 (WWS Family/Subfamily). If the font's naming is WWS-conformant, the WWS bit should be set. [code: no-wws-without-wws-names]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron (alt_caron)</summary>
    <div>


> Lcaron, dcaron, lcaron, tcaron should NOT be composed with quoteright or quotesingle or comma or caron(comb). It should be composed with a distinctive glyph which doesn't look like an apostrophe.
> 
> Source: https://ilovetypography.com/2009/01/24/on-diacritics/ http://diacritics.typo.cz/index.php?id=5 https://www.typotheque.com/articles/lcaron




Original proposal: [https://github.com/fonttools/fontbakery/issues/3308]





- ⚠️ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  


- ⚠️ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  


- ⚠️ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  


- ⚠️ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. (contour_count)</summary>
    <div>


> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be constructured in a handful of ways. This means a glyph's contour count will only differ slightly amongst different fonts, e.g a 'g' could either be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs to a display family.
> 
> This check currently does not cover variable fonts because there's plenty of alternative ways of constructing glyphs with multiple outlines for each feature in a VarFont. The expected contour count data for this check is currently optimized for the typical construction of glyphs in static fonts.




Original proposal: [https://github.com/fonttools/fontbakery/issues/4829]





- ⚠️ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are
     inferred from the typical amounts of contours observed in a
     large collection of reference font families. The divergences
     listed below may simply indicate a significantly different
     design on some of your glyphs. On the other hand, some of these
     may flag actual bugs in the font such as glyphs mapped to an
     incorrect codepoint. Please consider reviewing the design and
     codepoint assignment of these to make sure they are correct.


    The following glyphs do not have the recommended number of contours:
* uni013C (U+013C): found 1, expected one of: [2, 3, 6]
* section (U+00A7): found 1, expected one of: [2, 4, 6] [code: contour-count]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. (math_signs_width)</summary>
    <div>


> #,         It is a common practice to have math signs sharing the same width         (preferably the same width as tabular figures accross the entire font family).
> 
> This probably comes from the will to avoid additional tabular math signs knowing that their design can easily share the same width.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3832]





- ⚠️ **WARN** The most common width is 766 among a set of 12  math glyphs.
The following math glyphs have a different width, though:
width=746: less, greater, greaterequal, lessequal
width=556: minus [code: width-outliers]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure indic fonts have the Indian Rupee Sign glyph. (rupee)</summary>
    <div>


> Per Bureau of Indian Standards every font supporting one of the official Indian languages needs to include Unicode Character “₹” (U+20B9) Indian Rupee Sign.




Original proposal: [https://github.com/fonttools/fontbakery/issues/2967]





- ⚠️ **WARN** Font is missing the Indian Rupee Sign glyph. Please add a glyph for Indian Rupee Sign (₹) at codepoint U+20B9. [code: missing-rupee]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? (soft_hyphen)</summary>
    <div>


> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character), sometimes the same as the traditional hyphen, sometimes double encoded with the hyphen.
> 
> That being said, it is recommended to not include it in the font at all, because discretionary hyphenation should be handled at the level of the shaping engine, not the font. Also, even if present, the software would not display that character.
> 
> More discussion at: https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar




Original proposal: [https://github.com/fonttools/fontbakery/issues/4046, https://github.com/fonttools/fontbakery/issues/3486]





- ⚠️ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs (unreachable_glyphs)</summary>
    <div>


> Glyphs are either accessible directly through Unicode codepoints or through        substitution rules.
> 
> In Color Fonts, glyphs are also referenced by the COLR table. And mathematical fonts also reference glyphs via the MATH table.
> 
> Any glyphs not accessible by these means are redundant and serve only to increase the font's file size.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3160]





- ⚠️ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

* .null
* nonmarkingreturn [code: unreachable-glyphs]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Font has correct separator glyphs? (googlefonts/separator_glyphs)</summary>
    <div>


> U+2028 and U+2029 should be present; otherwise tofu is displayed. (whitespace_ink will check that they are empty)




Original proposal: [https://github.com/fonttools/fontspector/issues/93]





- ⚠️ **WARN** Missing separator glyph U+2028 [code: missing-separator-glyphs]
  
  


- ⚠️ **WARN** Missing separator glyph U+2029 [code: missing-separator-glyphs]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? (outline_alignment_miss)</summary>
    <div>


> This check heuristically looks for on-curve points which are close to, but do not sit on, significant boundary coordinates. For example, a point which has a Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the baseline, here we also check for points near the x-height (but only for lowercase Latin letters), cap-height, ascender and descender Y coordinates.
> 
> Not all such misaligned curve points are a mistake, and sometimes the design may call for points in locations near the boundaries. As this check is liable to generate significant numbers of false positives, it will pass if there are more than 100 reported misalignments.




Original proposal: [https://github.com/fonttools/fontbakery/pull/3088]





- ⚠️ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

* - K (U+004B): X=870,Y=2 (should be at baseline 0?)
* - K (U+004B): X=869,Y=698 (should be at cap-height 700?)
* - k (U+006B): X=722,Y=2 (should be at baseline 0?)
* - z (U+007A): X=58,Y=2 (should be at baseline 0?)
* - numbersign (U+0023): X=494,Y=1 (should be at baseline 0?)
* - numbersign (U+0023): X=189,Y=1 (should be at baseline 0?)
* - numbersign (U+0023): X=357,Y=699 (should be at cap-height 700?)
* - numbersign (U+0023): X=662,Y=699 (should be at cap-height 700?)
* - percent (U+0025): X=755,Y=699 (should be at cap-height 700?)
... and 46 others [code: found-misalignments]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? (outline_colinear_vectors)</summary>
    <div>


> This check looks for consecutive line segments which have the same angle. This normally happens if an outline point has been added by accident.
> 
> This check is not run for variable fonts, as they may legitimately have colinear vectors.




Original proposal: [https://github.com/fonttools/fontbakery/pull/3088]





- ⚠️ **WARN** The following glyphs have colinear vectors:

* A (U+0041): from (516.0, 700.0) to (736.0, 296.0) is colinear with segment from (736.0, 296.0) to (765.0, 244.0)
* A (U+0041): from (736.0, 296.0) to (765.0, 244.0) is colinear with segment from (765.0, 244.0) to (898.0, 0.0)
* b (U+0062): from (643.0, 0.0) to (116.0, 0.0) is colinear with segment from (116.0, 0.0) to (58.0, 0.0)
* b (U+0062): from (58.0, 0.0) to (58.0, 530.0) is colinear with segment from (58.0, 530.0) to (58.0, 700.0)
* d (U+0064): from (738.0, 700.0) to (738.0, 530.0) is colinear with segment from (738.0, 530.0) to (738.0, 0.0)
* d (U+0064): from (738.0, 0.0) to (680.0, 0.0) is colinear with segment from (680.0, 0.0) to (153.0, 0.0)
* p (U+0070): from (58.0, -205.0) to (58.0, 0.0) is colinear with segment from (58.0, 0.0) to (58.0, 530.0)
* p (U+0070): from (58.0, 530.0) to (116.0, 530.0) is colinear with segment from (116.0, 530.0) to (643.0, 530.0)
* q (U+0071): from (153.0, 530.0) to (680.0, 530.0) is colinear with segment from (680.0, 530.0) to (738.0, 530.0)
... and 54 others [code: found-colinear-vectors]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Are any segments inordinately short? (outline_short_segments)</summary>
    <div>


> This check looks for outline segments which seem particularly short (less than 0.6% of the overall path length).
> 
> This check is not run for variable fonts, as they may legitimately have short segments. As this check is liable to generate significant numbers of false positives, it will pass if there are more than 100 reported short segments.




Original proposal: [https://github.com/fonttools/fontbakery/pull/3088]





- ⚠️ **WARN** The following glyphs have short segments:

* B (U+0042) contains a short segment Line(Line { p0: (743.0, 361.0), p1: (743.0, 349.0) }) (length: 12.00, total outline: 2895.69)
* Q (U+0051) contains a short segment Line(Line { p0: (757.0, 52.0), p1: (765.0, 60.0) }) (length: 11.31, total outline: 2899.79)
* W (U+0057) contains a short segment Line(Line { p0: (342.0, 55.0), p1: (344.0, 55.0) }) (length: 2.00, total outline: 5974.72)
* W (U+0057) contains a short segment Line(Line { p0: (872.0, 55.0), p1: (874.0, 55.0) }) (length: 2.00, total outline: 5974.72)
* W (U+0057) contains a short segment Line(Line { p0: (609.0, 638.0), p1: (607.0, 638.0) }) (length: 2.00, total outline: 5974.72)
* g (U+0067) contains a short segment Line(Line { p0: (738.0, 0.0), p1: (733.0, 0.0) }) (length: 5.00, total outline: 3620.60)
* z (U+007A) contains a short segment Line(Line { p0: (727.0, 530.0), p1: (728.0, 528.0) }) (length: 2.24, total outline: 3733.76)
* z (U+007A) contains a short segment Line(Line { p0: (59.0, 0.0), p1: (58.0, 2.0) }) (length: 2.24, total outline: 3733.76)
* two (U+0032) contains a short segment Line(Line { p0: (161.0, 75.0), p1: (164.0, 60.0) }) (length: 15.30, total outline: 5043.61)
... and 70 others [code: found-short-segments]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (googlefonts/meta/script_lang_tags)</summary>
    <div>


> The OpenType 'meta' table originated at Apple. Microsoft added it to OT with just two DataMap records:
> 
> - dlng: comma-separated ScriptLangTags that indicate which scripts,   or languages and scripts, with possible variants, the font is designed for.
> 
> - slng: comma-separated ScriptLangTags that indicate which scripts,   or languages and scripts, with possible variants, the font supports.
> 
> The slng structure is intended to describe which languages and scripts the font overall supports. For example, a Traditional Chinese font that also contains Latin characters, can indicate Hant,Latn, showing that it supports Hant, the Traditional Chinese variant of the Hani script, and it also supports the Latn script.
> 
> The dlng structure is far more interesting. A font may contain various glyphs, but only a particular subset of the glyphs may be truly "leading" in the design, while other glyphs may have been included for technical reasons. Such a Traditional Chinese font could only list Hant there, showing that it’s designed for Traditional Chinese, but the font would omit Latn, because the developers don’t think the font is really recommended for purely Latin-script use.
> 
> The tags used in the structures can comprise just script, or also language and script. For example, if a font has Bulgarian Cyrillic alternates in the locl feature for the cyrl BGR OT languagesystem, it could also indicate in dlng explicitly that it supports bul-Cyrl. (Note that the scripts and languages in meta use the ISO language and script codes, not the OpenType ones).
> 
> This check ensures that the font has the meta table containing the slng and dlng structures.
> 
> All families in the Google Fonts collection should contain the 'meta' table. Windows 10 already uses it when deciding on which fonts to fall back to. The Google Fonts API and also other environments could use the data for smarter filtering. Most importantly, those entries should be added to the Noto fonts.
> 
> In the font making process, some environments store this data in external files already. But the meta table provides a convenient way to store this inside the font file, so some tools may add the data, and unrelated tools may read this data. This makes the solution much more portable and universal.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3349]





- ⚠️ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. (googlefonts/vendor_id)</summary>
    <div>


> Microsoft keeps a list of font vendors and their respective contact info. This list is updated regularly and is indexed by a 4-char "Vendor ID" which is stored in the achVendID field of the OS/2 table.
> 
> Registering your ID is not mandatory, but it is a good practice since some applications may display the type designer / type foundry contact info on some dialog and also because that info will be visible on Microsoft's website:
> 
> https://docs.microsoft.com/en-us/typography/vendors/
> 
> This check verifies whether or not a given font's vendor ID is registered in that list or if it has some of the default values used by the most common font editors.
> 
> Each new FontBakery release includes a cached copy of that list of vendor IDs. If you registered recently, you're safe to ignore warnings emitted by this check, since your ID will soon be included in one of our upcoming releases.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3943, https://github.com/fonttools/fontbakery/issues/4829]





- ⚠️ **WARN** OS/2 VendorID value 'XUQU' is not yet recognized.
If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
  
  

</div>
</details>


</div>
</details>


<details><summary>[17] xuqu-type-family/fonts/XUQU-ExtraBold.ttf</summary>
<div>


<details>
    <summary>🔥 <b>FAIL</b> Check code page character ranges (opentype/code_pages)</summary>
    <div>


> At least some programs (such as Word and Sublime Text) under Windows 7 do not recognize fonts unless code page bits are properly set on the ulCodePageRange1 (and/or ulCodePageRange2) fields of the OS/2 table.
> 
> More specifically, the fonts are selectable in the font menu, but whichever Windows API these applications use considers them unsuitable for any character set, so anything set in these fonts is rendered with Arial as a fallback font.
> 
> This check currently does not identify which code pages should be set. Auto-detecting coverage is not trivial since the OpenType specification leaves the interpretation of whether a given code page is "functional" or not open to the font developer to decide.
> 
> So here we simply detect as a FAIL when a given font has no code page declared at all.




Original proposal: [https://github.com/fonttools/fontbakery/issues/2474]





- 🔥 **FAIL** No code pages defined in the OS/2 table ulCodePageRange1 and CodePageRange2 fields. [code: no-code-pages]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. (googlefonts/glyphsets/shape_languages)</summary>
    <div>


> This check uses a heuristic to determine which GF glyphsets a font supports. Then it checks the font for correct shaping behaviour for all languages in those glyphsets.




Original proposal: [https://github.com/googlefonts/fontbakery/issues/4147]





- 🔥 **FAIL** Failed language shaping:

| Message                                                                           | Languages                    |
|-----------------------------------------------------------------------------------|------------------------------|
| Mandatory orthography codepoints:                                                 | * lt_Latn (Lithuanian)       |
|   The following mark characters are missing from the font: ̄, ̌, ̨, ̇                 |                              |
| Mandatory orthography codepoints:                                                 | * lv_Latn (Latvian)          |
|   The following mark characters are missing from the font: ̌, ̧, ̄                   |                              |
| Mandatory orthography codepoints:                                                 | * cs_Latn (Czech)            |
|   The following mark characters are missing from the font: ̊, ́, ̌                   |                              |
| Mandatory orthography codepoints:                                                 | * hu_Latn (Hungarian)        |
|   The following mark characters are missing from the font: ́, ̋, ̈                   |                              |
| Mandatory orthography codepoints:                                                 | * da_Latn (Danish)           |
|   The following mark characters are missing from the font: ̊, ́                     |                              |
| Mandatory orthography codepoints:                                                 | * nb_Latn (Norwegian Bokmål) |
|   The following mark characters are missing from the font: ̊, ̂, ̈, ̀, ́               |                              |
| Mandatory orthography codepoints:                                                 | * it_Latn (Italian)          |
|   The following mark characters are missing from the font: ̂, ̀, ́, ̈                 |                              |
| Mandatory orthography codepoints:                                                 | * sk_Latn (Slovak)           |
|   The following mark characters are missing from the font: ́, ̈, ̂, ̌                 |                              |
| Mandatory orthography codepoints:                                                 | * sv_Latn (Swedish)          |
|   The following mark characters are missing from the font: ̊, ̈, ́, ̀                 |                              |
| Mandatory orthography codepoints:                                                 | * nl_Latn (Dutch)            |
|   The following base characters are missing from the font: ÍJ́, íj́                 |                              |
|   The following mark characters are missing from the font: ̀, ́, ̈, ̂                 |                              |
| Mandatory orthography codepoints:                                                 | * tr_Latn (Turkish)          |
|   The following mark characters are missing from the font: ̈, ̆, ̦, ̧, ̇, ̂             |                              |
| Mandatory orthography codepoints:                                                 | * is_Latn (Icelandic)        |
|   The following mark characters are missing from the font: ̈, ́, ̨                   |                              |
| Mandatory orthography codepoints:                                                 | * en_Latn (English)          |
|   The following mark characters are missing from the font: ̂, ̧, ̀, ́, ̃, ̈             |                              |
| Mandatory orthography codepoints:                                                 | * fi_Latn (Finnish)          |
|   The following mark characters are missing from the font: ̈, ̊, ̌, ̃                 |                              |
| Mandatory orthography codepoints:                                                 | * es_Latn (Spanish)          |
|   The following mark characters are missing from the font: ̃, ́, ̈                   |                              |
| Mandatory orthography codepoints:                                                 | * ca_Latn (Catalan)          |
|   The following mark characters are missing from the font: ̀, ̧, ́, ̈                 |                              |
| Mandatory orthography codepoints:                                                 | * fr_Latn (French)           |
|   The following mark characters are missing from the font: ̂, ̀, ̧, ́, ̈               |                              |
| Mandatory orthography codepoints:                                                 | * hr_Latn (Croatian)         |
|   The following mark characters are missing from the font: ́, ̌                     |                              |
| Mandatory orthography codepoints:                                                 | * sq_Latn (Albanian)         |
|   The following mark characters are missing from the font: ̧, ̈                     |                              |
| Mandatory orthography codepoints:                                                 | * pl_Latn (Polish)           |
|   The following mark characters are missing from the font: ̇, ́, ̨                   |                              |
| Mandatory orthography codepoints:                                                 | * ro_Latn (Romanian)         |
|   The following base characters are missing from the font: ț, Ș, ș, Ț             |                              |
|   The following mark characters are missing from the font: ̂, ̆, ̦, ̧                 |                              |
| Mandatory orthography codepoints:                                                 | * mt_Latn (Maltese)          |
|   The following mark characters are missing from the font: ̇, ̂, ̀                   |                              |
| Mandatory orthography codepoints:                                                 | * cy_Latn (Welsh)            |
|   The following base characters are missing from the font: ẁ, ẃ, Ẁ, Ẅ, ỳ, ẅ, Ỳ, Ẃ |                              |
|   The following mark characters are missing from the font: ̈, ́, ̂, ̀                 |                              |
| Mandatory orthography codepoints:                                                 | * de_Latn (German)           |
|   The following base characters are missing from the font: ẞ                      |                              |
|   The following mark characters are missing from the font: ̈, ̀, ́                   |                              |
| Mandatory orthography codepoints:                                                 | * pt_Latn (Portuguese)       |
|   The following mark characters are missing from the font: ̀, ̃, ́, ̧, ̈, ̂             |                              | [code: failed-language-shaping]
  
  


- ⚠️ **WARN** Warning language shaping:

| Message                                                           | Languages                    |
|-------------------------------------------------------------------|------------------------------|
| Auxiliary orthography codepoints:                                 | * fi_Latn (Finnish)          |
|   The following auxiliary characters are missing from the font: Ǧ |                              |
|   The following auxiliary characters are missing from the font: Ǥ |                              |
|   The following auxiliary characters are missing from the font: Ȟ |                              |
|   The following auxiliary characters are missing from the font: Ǩ |                              |
|   The following auxiliary characters are missing from the font: Ș |                              |
|   The following auxiliary characters are missing from the font: ẞ |                              |
|   The following auxiliary characters are missing from the font: Ț |                              |
|   The following auxiliary characters are missing from the font: Ʒ |                              |
|   The following auxiliary characters are missing from the font: Ǯ |                              |
|   The following auxiliary characters are missing from the font: ǧ |                              |
|   The following auxiliary characters are missing from the font: ǥ |                              |
|   The following auxiliary characters are missing from the font: ȟ |                              |
|   The following auxiliary characters are missing from the font: ǩ |                              |
|   The following auxiliary characters are missing from the font: ș |                              |
|   The following auxiliary characters are missing from the font: ț |                              |
|   The following auxiliary characters are missing from the font: ʒ |                              |
|   The following auxiliary characters are missing from the font: ǯ |                              |
| Auxiliary orthography codepoints:                                 | * en_Latn (English)          |
|   The following auxiliary characters are missing from the font: ʻ |                              |
| Auxiliary orthography codepoints:                                 | * lt_Latn (Lithuanian)       |
|   The following auxiliary characters are missing from the font: Ą́ |                              |
|   The following auxiliary characters are missing from the font: Ą̃ |                              |
|   The following auxiliary characters are missing from the font: Ẽ |                              |
|   The following auxiliary characters are missing from the font: Ę́ |                              |
|   The following auxiliary characters are missing from the font: Ę̃ |                              |
|   The following auxiliary characters are missing from the font: Ė́ |                              |
|   The following auxiliary characters are missing from the font: Ė̃ |                              |
|   The following auxiliary characters are missing from the font: İ́ |                              |
|   The following auxiliary characters are missing from the font: İ́ |                              |
|   The following auxiliary characters are missing from the font: İ̀ |                              |
|   The following auxiliary characters are missing from the font: İ̀ |                              |
|   The following auxiliary characters are missing from the font: İ̃ |                              |
|   The following auxiliary characters are missing from the font: İ̃ |                              |
|   The following auxiliary characters are missing from the font: Į́ |                              |
|   The following auxiliary characters are missing from the font: Į̇́ |                              |
|   The following auxiliary characters are missing from the font: Į̃ |                              |
|   The following auxiliary characters are missing from the font: Į̇̃ |                              |
|   The following auxiliary characters are missing from the font: J̃ |                              |
|   The following auxiliary characters are missing from the font: J̇̃ |                              |
|   The following auxiliary characters are missing from the font: L̃ |                              |
|   The following auxiliary characters are missing from the font: M̃ |                              |
|   The following auxiliary characters are missing from the font: R̃ |                              |
|   The following auxiliary characters are missing from the font: Ų́ |                              |
|   The following auxiliary characters are missing from the font: Ų̃ |                              |
|   The following auxiliary characters are missing from the font: Ū́ |                              |
|   The following auxiliary characters are missing from the font: Ū̃ |                              |
|   The following auxiliary characters are missing from the font: ą́ |                              |
|   The following auxiliary characters are missing from the font: ą̃ |                              |
|   The following auxiliary characters are missing from the font: ẽ |                              |
|   The following auxiliary characters are missing from the font: ę́ |                              |
|   The following auxiliary characters are missing from the font: ę̃ |                              |
|   The following auxiliary characters are missing from the font: ė́ |                              |
|   The following auxiliary characters are missing from the font: ė̃ |                              |
|   The following auxiliary characters are missing from the font: i̇́ |                              |
|   The following auxiliary characters are missing from the font: i̇̀ |                              |
|   The following auxiliary characters are missing from the font: i̇̃ |                              |
|   The following auxiliary characters are missing from the font: į́ |                              |
|   The following auxiliary characters are missing from the font: į̇́ |                              |
|   The following auxiliary characters are missing from the font: į̃ |                              |
|   The following auxiliary characters are missing from the font: į̇̃ |                              |
|   The following auxiliary characters are missing from the font: j̃ |                              |
|   The following auxiliary characters are missing from the font: j̇̃ |                              |
|   The following auxiliary characters are missing from the font: l̃ |                              |
|   The following auxiliary characters are missing from the font: m̃ |                              |
|   The following auxiliary characters are missing from the font: r̃ |                              |
|   The following auxiliary characters are missing from the font: ų́ |                              |
|   The following auxiliary characters are missing from the font: ų̃ |                              |
|   The following auxiliary characters are missing from the font: ū́ |                              |
|   The following auxiliary characters are missing from the font: ū̃ |                              |
| Auxiliary orthography codepoints:                                 | * nb_Latn (Norwegian Bokmål) |
|   The following auxiliary characters are missing from the font: Ǎ |                              |
|   The following auxiliary characters are missing from the font: ǎ |                              |
| Auxiliary orthography codepoints:                                 | * da_Latn (Danish)           |
|   The following auxiliary characters are missing from the font: Ǿ |                              |
|   The following auxiliary characters are missing from the font: ǿ |                              |
| Auxiliary orthography codepoints:                                 | * it_Latn (Italian)          |
|   The following auxiliary characters are missing from the font: ẞ | * pl_Latn (Polish)           |
|                                                                   | * tr_Latn (Turkish)          |
| Auxiliary orthography codepoints:                                 | * fr_Latn (French)           |
|   The following auxiliary characters are missing from the font: ẞ |                              |
|   The following auxiliary characters are missing from the font: Ǔ |                              |
|   The following auxiliary characters are missing from the font: ǔ |                              | [code: warning-language-shaping]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Check family name for GF Guide compliance. (googlefonts/family_name_compliance)</summary>
    <div>


> Checks the family name for compliance with the Google Fonts Guide. https://googlefonts.github.io/gf-guide/onboarding.html#new-fonts
> 
> If you want to have your family name added to the CamelCase exceptions list, please submit a pull request to the camelcased_familyname_exceptions.txt file.
> 
> Similarly, abbreviations can be submitted to the abbreviations_familyname_exceptions.txt file.
> 
> These are located in the Lib/fontbakery/data/googlefonts/ directory of the FontBakery source code currently hosted at https://github.com/fonttools/fontbakery/




Original proposal: [https://github.com/fonttools/fontbakery/issues/4049]





- 🔥 **FAIL** "XUQU体" contains an abbreviation. [code: abbreviation]
  
  


- 🔥 **FAIL** "XUQU体" contains the following characters which are not allowed: "体". [code: forbidden-characters]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Checking file is named canonically. (googlefonts/canonical_filename)</summary>
    <div>


> A font's filename must be composed as "<familyname>-<stylename>.ttf":
> 
> - Nunito-Regular.ttf
> 
> - Oswald-BoldItalic.ttf
> 
> Variable fonts must list the axis tags in alphabetical order in square brackets and separated by commas:
> 
> - Roboto[wdth,wght].ttf
> 
> - Familyname-Italic[wght].ttf




Original proposal: [https://github.com/fonttools/fontbakery/issues/4829]





- 🔥 **FAIL** Expected "XUQU体-ExtraBold.ttf". Got "XUQU-ExtraBold.ttf". [code: bad-filename]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Check font names are correct (googlefonts/font_names)</summary>
    <div>


> Google Fonts has several rules which need to be adhered to when setting a font's name table. Please read: https://googlefonts.github.io/gf-guide/statics.html#supported-styles https://googlefonts.github.io/gf-guide/statics.html#style-linking https://googlefonts.github.io/gf-guide/statics.html#unsupported-styles https://googlefonts.github.io/gf-guide/statics.html#single-weight-families




Original proposal: [https://github.com/fonttools/fontbakery/pull/3800]





- 🔥 **FAIL** Font names are incorrect:

| Name                       | Current            | Expected             |
|----------------------------|--------------------|----------------------|
| Family Name                | XUQU体 ExtraBold   | XUQU体 ExtraBold     |
| Subfamily Name             | Regular            | Regular              |
| Full Name                  | XUQU体 ExtraBold   | XUQU体 ExtraBold     |
| Postscript Name            | **XUQU-ExtraBold** | **XUQU体-ExtraBold** |
| Typographic Family Name    | XUQU体             | XUQU体               |
| Typographic Subfamily Name | ExtraBold          | ExtraBold            | [code: bad-names]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Ensure font can render its own name. (googlefonts/render_own_name)</summary>
    <div>


> A base expectation is that a font family's regular/default (400 roman) style can render its 'menu name' (nameID 1) in itself.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3159]





- 🔥 **FAIL** .notdef glyphs were found when attempting to render XUQU体 ExtraBold [code: render-own-name]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check that OS/2 fsSelection WWS bit is set correctly. (opentype/fsselection_wws)</summary>
    <div>


> According to the OpenType specification, OS/2.fsSelection bit 8 (WWS) should be set if the font has name table strings consistent with a weight/width/slope family without requiring use of name IDs 21 and 22.
> 
> Conversely, if name IDs 21 and 22 are present (indicating the font names are not WWS-conformant), the WWS bit should not be set.




Original proposal: [https://github.com/fonttools/fontspector/issues/577]





- ⚠️ **WARN** OS/2 fsSelection WWS bit is not set, and the font does not have name IDs 21/22 (WWS Family/Subfamily). If the font's naming is WWS-conformant, the WWS bit should be set. [code: no-wws-without-wws-names]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron (alt_caron)</summary>
    <div>


> Lcaron, dcaron, lcaron, tcaron should NOT be composed with quoteright or quotesingle or comma or caron(comb). It should be composed with a distinctive glyph which doesn't look like an apostrophe.
> 
> Source: https://ilovetypography.com/2009/01/24/on-diacritics/ http://diacritics.typo.cz/index.php?id=5 https://www.typotheque.com/articles/lcaron




Original proposal: [https://github.com/fonttools/fontbakery/issues/3308]





- ⚠️ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  


- ⚠️ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  


- ⚠️ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  


- ⚠️ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. (contour_count)</summary>
    <div>


> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be constructured in a handful of ways. This means a glyph's contour count will only differ slightly amongst different fonts, e.g a 'g' could either be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs to a display family.
> 
> This check currently does not cover variable fonts because there's plenty of alternative ways of constructing glyphs with multiple outlines for each feature in a VarFont. The expected contour count data for this check is currently optimized for the typical construction of glyphs in static fonts.




Original proposal: [https://github.com/fonttools/fontbakery/issues/4829]





- ⚠️ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are
     inferred from the typical amounts of contours observed in a
     large collection of reference font families. The divergences
     listed below may simply indicate a significantly different
     design on some of your glyphs. On the other hand, some of these
     may flag actual bugs in the font such as glyphs mapped to an
     incorrect codepoint. Please consider reviewing the design and
     codepoint assignment of these to make sure they are correct.


    The following glyphs do not have the recommended number of contours:
* uni013C (U+013C): found 1, expected one of: [2, 3, 6]
* section (U+00A7): found 1, expected one of: [2, 4, 6] [code: contour-count]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. (math_signs_width)</summary>
    <div>


> #,         It is a common practice to have math signs sharing the same width         (preferably the same width as tabular figures accross the entire font family).
> 
> This probably comes from the will to avoid additional tabular math signs knowing that their design can easily share the same width.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3832]





- ⚠️ **WARN** The most common width is 766 among a set of 12  math glyphs.
The following math glyphs have a different width, though:
width=746: greater, greaterequal, less, lessequal
width=556: minus [code: width-outliers]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure indic fonts have the Indian Rupee Sign glyph. (rupee)</summary>
    <div>


> Per Bureau of Indian Standards every font supporting one of the official Indian languages needs to include Unicode Character “₹” (U+20B9) Indian Rupee Sign.




Original proposal: [https://github.com/fonttools/fontbakery/issues/2967]





- ⚠️ **WARN** Font is missing the Indian Rupee Sign glyph. Please add a glyph for Indian Rupee Sign (₹) at codepoint U+20B9. [code: missing-rupee]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? (soft_hyphen)</summary>
    <div>


> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character), sometimes the same as the traditional hyphen, sometimes double encoded with the hyphen.
> 
> That being said, it is recommended to not include it in the font at all, because discretionary hyphenation should be handled at the level of the shaping engine, not the font. Also, even if present, the software would not display that character.
> 
> More discussion at: https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar




Original proposal: [https://github.com/fonttools/fontbakery/issues/4046, https://github.com/fonttools/fontbakery/issues/3486]





- ⚠️ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs (unreachable_glyphs)</summary>
    <div>


> Glyphs are either accessible directly through Unicode codepoints or through        substitution rules.
> 
> In Color Fonts, glyphs are also referenced by the COLR table. And mathematical fonts also reference glyphs via the MATH table.
> 
> Any glyphs not accessible by these means are redundant and serve only to increase the font's file size.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3160]





- ⚠️ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

* .null
* nonmarkingreturn [code: unreachable-glyphs]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Font has correct separator glyphs? (googlefonts/separator_glyphs)</summary>
    <div>


> U+2028 and U+2029 should be present; otherwise tofu is displayed. (whitespace_ink will check that they are empty)




Original proposal: [https://github.com/fonttools/fontspector/issues/93]





- ⚠️ **WARN** Missing separator glyph U+2028 [code: missing-separator-glyphs]
  
  


- ⚠️ **WARN** Missing separator glyph U+2029 [code: missing-separator-glyphs]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? (outline_alignment_miss)</summary>
    <div>


> This check heuristically looks for on-curve points which are close to, but do not sit on, significant boundary coordinates. For example, a point which has a Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the baseline, here we also check for points near the x-height (but only for lowercase Latin letters), cap-height, ascender and descender Y coordinates.
> 
> Not all such misaligned curve points are a mistake, and sometimes the design may call for points in locations near the boundaries. As this check is liable to generate significant numbers of false positives, it will pass if there are more than 100 reported misalignments.




Original proposal: [https://github.com/fonttools/fontbakery/pull/3088]





- ⚠️ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

* - germandbls (U+00DF): X=624,Y=2 (should be at baseline 0?)
* - germandbls (U+00DF): X=286,Y=2 (should be at baseline 0?)
* - dieresis (U+00A8): X=355,Y=699 (should be at cap-height 700?)
* - dieresis (U+00A8): X=431,Y=699 (should be at cap-height 700?)
* - dieresis (U+00A8): X=45,Y=699 (should be at cap-height 700?)
* - dieresis (U+00A8): X=121,Y=699 (should be at cap-height 700?)
* - ordfeminine (U+00AA): X=110,Y=702 (should be at cap-height 700?)
* - ordfeminine (U+00AA): X=432,Y=702 (should be at cap-height 700?)
* - ordmasculine (U+00BA): X=118,Y=702 (should be at cap-height 700?)
... and 13 others [code: found-misalignments]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (googlefonts/meta/script_lang_tags)</summary>
    <div>


> The OpenType 'meta' table originated at Apple. Microsoft added it to OT with just two DataMap records:
> 
> - dlng: comma-separated ScriptLangTags that indicate which scripts,   or languages and scripts, with possible variants, the font is designed for.
> 
> - slng: comma-separated ScriptLangTags that indicate which scripts,   or languages and scripts, with possible variants, the font supports.
> 
> The slng structure is intended to describe which languages and scripts the font overall supports. For example, a Traditional Chinese font that also contains Latin characters, can indicate Hant,Latn, showing that it supports Hant, the Traditional Chinese variant of the Hani script, and it also supports the Latn script.
> 
> The dlng structure is far more interesting. A font may contain various glyphs, but only a particular subset of the glyphs may be truly "leading" in the design, while other glyphs may have been included for technical reasons. Such a Traditional Chinese font could only list Hant there, showing that it’s designed for Traditional Chinese, but the font would omit Latn, because the developers don’t think the font is really recommended for purely Latin-script use.
> 
> The tags used in the structures can comprise just script, or also language and script. For example, if a font has Bulgarian Cyrillic alternates in the locl feature for the cyrl BGR OT languagesystem, it could also indicate in dlng explicitly that it supports bul-Cyrl. (Note that the scripts and languages in meta use the ISO language and script codes, not the OpenType ones).
> 
> This check ensures that the font has the meta table containing the slng and dlng structures.
> 
> All families in the Google Fonts collection should contain the 'meta' table. Windows 10 already uses it when deciding on which fonts to fall back to. The Google Fonts API and also other environments could use the data for smarter filtering. Most importantly, those entries should be added to the Noto fonts.
> 
> In the font making process, some environments store this data in external files already. But the meta table provides a convenient way to store this inside the font file, so some tools may add the data, and unrelated tools may read this data. This makes the solution much more portable and universal.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3349]





- ⚠️ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. (googlefonts/vendor_id)</summary>
    <div>


> Microsoft keeps a list of font vendors and their respective contact info. This list is updated regularly and is indexed by a 4-char "Vendor ID" which is stored in the achVendID field of the OS/2 table.
> 
> Registering your ID is not mandatory, but it is a good practice since some applications may display the type designer / type foundry contact info on some dialog and also because that info will be visible on Microsoft's website:
> 
> https://docs.microsoft.com/en-us/typography/vendors/
> 
> This check verifies whether or not a given font's vendor ID is registered in that list or if it has some of the default values used by the most common font editors.
> 
> Each new FontBakery release includes a cached copy of that list of vendor IDs. If you registered recently, you're safe to ignore warnings emitted by this check, since your ID will soon be included in one of our upcoming releases.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3943, https://github.com/fonttools/fontbakery/issues/4829]





- ⚠️ **WARN** OS/2 VendorID value 'XUQU' is not yet recognized.
If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
  
  

</div>
</details>


</div>
</details>


<details><summary>[5] xuqu-type-family/fonts</summary>
<div>


<details>
    <summary>🔥 <b>FAIL</b> Fonts have consistent underline thickness? (opentype/family/underline_thickness)</summary>
    <div>


> Dave C Lemon (Adobe Type Team) recommends setting the underline thickness to be consistent across the family.
> 
> If thicknesses are not family consistent, words set on the same line which have different styles look strange.




Original proposal: [https://github.com/fonttools/fontbakery/issues/4829]





- 🔥 **FAIL** Underline thickness is inconsistent. Detected underline thickness values are:

* xuqu-type-family/fonts/XUQU-Bold.ttf: 122
* xuqu-type-family/fonts/XUQU-ExtraBold.ttf: 140
* xuqu-type-family/fonts/XUQU-Light.ttf: 52
* xuqu-type-family/fonts/XUQU-Regular.ttf: 70
* xuqu-type-family/fonts/XUQU-Thin.ttf: 30
 [code: inconsistent-underline-thickness]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Copyright notices match canonical pattern in fonts (googlefonts/font_copyright)</summary>
    <div>


> This check aims at ensuring a uniform and legally accurate copyright statement on the name table entries and METADATA.pb files of font files across the Google Fonts library.
> 
> We also check that the copyright field in METADATA.pb matches the contents of the name table nameID 0 (Copyright), and that the copyright notice within the METADATA.pb file is not too long; if it is more than 500 characters, this may be an indication that either a full license or the font's description has been included in this field by mistake.
> 
> The expected pattern for the copyright string adheres to the following rules:
> 
> * It must say "Copyright" followed by a 4 digit year (optionally followed by   a hyphen and another 4 digit year)
> 
> * Additional years or year ranges are also valid.
> 
> * An optional comma can be placed here.
> 
> * Then it must say "The <familyname> Project Authors" and, within parentheses,   a URL for a git repository must be provided. But we have an exception   for the fonts from the Noto project, that simply have   "google llc. all rights reserved" here.
> 
> * The check is case insensitive and does not validate whether the familyname   is correct, even though we'd obviously expect it to be.
> 
> Here is an example of a valid copyright string:
> 
> "Copyright 2017 The Archivo Black Project Authors  (https://github.com/Omnibus-Type/ArchivoBlack)"




Original proposal: [https://github.com/fonttools/fontbakery/pull/2383, https://github.com/fonttools/fontbakery/issues/4829]





- 🔥 **FAIL** XUQU-Bold.ttf: Name Table entry: Copyright notices should match a pattern similar to:

"Copyright 2020 The Familyname Project Authors (git url)"

But instead we have got:

"xuqu typeface. created for xuqutech, 2026." [code: bad-notice-format]
  
  


- 🔥 **FAIL** XUQU-ExtraBold.ttf: Name Table entry: Copyright notices should match a pattern similar to:

"Copyright 2020 The Familyname Project Authors (git url)"

But instead we have got:

"xuqu typeface. created for xuqutech, 2026." [code: bad-notice-format]
  
  


- 🔥 **FAIL** XUQU-Light.ttf: Name Table entry: Copyright notices should match a pattern similar to:

"Copyright 2020 The Familyname Project Authors (git url)"

But instead we have got:

"xuqu typeface. created for xuqutech, 2026." [code: bad-notice-format]
  
  


- 🔥 **FAIL** XUQU-Regular.ttf: Name Table entry: Copyright notices should match a pattern similar to:

"Copyright 2020 The Familyname Project Authors (git url)"

But instead we have got:

"xuqu typeface. created for xuqutech, 2026." [code: bad-notice-format]
  
  


- 🔥 **FAIL** XUQU-Thin.ttf: Name Table entry: Copyright notices should match a pattern similar to:

"Copyright 2020 The Familyname Project Authors (git url)"

But instead we have got:

"xuqu typeface. created for xuqutech, 2026." [code: bad-notice-format]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Check Google Fonts glyph coverage. (googlefonts/glyph_coverage)</summary>
    <div>


> Google Fonts expects that fonts in its collection support at least the minimal set of characters defined in the `GF-latin-core` glyph-set.




Original proposal: [https://github.com/fonttools/fontbakery/pull/2488]





- 🔥 **FAIL** xuqu-type-family/fonts/XUQU-Bold.ttf missing required codepoints:

* 0x0218: LATIN CAPITAL LETTER S WITH COMMA BELOW
* 0x0219: LATIN SMALL LETTER S WITH COMMA BELOW
* 0x021A: LATIN CAPITAL LETTER T WITH COMMA BELOW
* 0x021B: LATIN SMALL LETTER T WITH COMMA BELOW
* 0x0237: LATIN SMALL LETTER DOTLESS J
* 0x02C6: MODIFIER LETTER CIRCUMFLEX ACCENT
* 0x02C7: CARON
* 0x02D8: BREVE
* 0x02D9: DOT ABOVE
... and 27 others [code: missing-codepoints]
  
  


- 🔥 **FAIL** xuqu-type-family/fonts/XUQU-ExtraBold.ttf missing required codepoints:

* 0x0218: LATIN CAPITAL LETTER S WITH COMMA BELOW
* 0x0219: LATIN SMALL LETTER S WITH COMMA BELOW
* 0x021A: LATIN CAPITAL LETTER T WITH COMMA BELOW
* 0x021B: LATIN SMALL LETTER T WITH COMMA BELOW
* 0x0237: LATIN SMALL LETTER DOTLESS J
* 0x02C6: MODIFIER LETTER CIRCUMFLEX ACCENT
* 0x02C7: CARON
* 0x02D8: BREVE
* 0x02D9: DOT ABOVE
... and 27 others [code: missing-codepoints]
  
  


- 🔥 **FAIL** xuqu-type-family/fonts/XUQU-Light.ttf missing required codepoints:

* 0x0218: LATIN CAPITAL LETTER S WITH COMMA BELOW
* 0x0219: LATIN SMALL LETTER S WITH COMMA BELOW
* 0x021A: LATIN CAPITAL LETTER T WITH COMMA BELOW
* 0x021B: LATIN SMALL LETTER T WITH COMMA BELOW
* 0x0237: LATIN SMALL LETTER DOTLESS J
* 0x02C6: MODIFIER LETTER CIRCUMFLEX ACCENT
* 0x02C7: CARON
* 0x02D8: BREVE
* 0x02D9: DOT ABOVE
... and 27 others [code: missing-codepoints]
  
  


- 🔥 **FAIL** xuqu-type-family/fonts/XUQU-Regular.ttf missing required codepoints:

* 0x0218: LATIN CAPITAL LETTER S WITH COMMA BELOW
* 0x0219: LATIN SMALL LETTER S WITH COMMA BELOW
* 0x021A: LATIN CAPITAL LETTER T WITH COMMA BELOW
* 0x021B: LATIN SMALL LETTER T WITH COMMA BELOW
* 0x0237: LATIN SMALL LETTER DOTLESS J
* 0x02C6: MODIFIER LETTER CIRCUMFLEX ACCENT
* 0x02C7: CARON
* 0x02D8: BREVE
* 0x02D9: DOT ABOVE
... and 27 others [code: missing-codepoints]
  
  


- 🔥 **FAIL** xuqu-type-family/fonts/XUQU-Thin.ttf missing required codepoints:

* 0x0218: LATIN CAPITAL LETTER S WITH COMMA BELOW
* 0x0219: LATIN SMALL LETTER S WITH COMMA BELOW
* 0x021A: LATIN CAPITAL LETTER T WITH COMMA BELOW
* 0x021B: LATIN SMALL LETTER T WITH COMMA BELOW
* 0x0237: LATIN SMALL LETTER DOTLESS J
* 0x02C6: MODIFIER LETTER CIRCUMFLEX ACCENT
* 0x02C7: CARON
* 0x02D8: BREVE
* 0x02D9: DOT ABOVE
... and 27 others [code: missing-codepoints]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure Fonts have 'ital' STAT axis. (opentype/STAT/ital_axis)</summary>
    <div>


> Check that related Upright and Italic have an 'ital' axis in the STAT table.
> 
> Since the STAT table can be used to create new instances, it is important to ensure that such an 'ital' axis be the last one declared in the STAT table so that the eventual naming of new instances follows the subfamily traditional scheme (RIBBI / WWS) where "Italic" is always last.
> 
> The 'ital' axis should also be strictly boolean, only accepting values of 0 (for Uprights) or 1 (for Italics). This usually works as a mechanism for selecting between two linked variable font files.
> 
> Also, the axis value name for uprights must be set as elidable.




Original proposal: [https://github.com/fonttools/fontbakery/issues/2934, https://github.com/fonttools/fontbakery/issues/3668, https://github.com/fonttools/fontbakery/issues/3669]





- ⚠️ **WARN** Static font is missing the 'STAT' table. [code: no-stat-table]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. (googlefonts/metadata/unreachable_subsetting)</summary>
    <div>


> This check ensures that all encoded glyphs in the font are covered by a subset declared in the METADATA.pb. Google Fonts splits the font into a set of subset fonts based on the contents of the `subsets` field and the subset definitions in the `glyphsets` repository.
> 
> Any encoded glyphs which are not by any of these subset definitions will not be served in the subsetted fonts, and so will be unreachable to the end user.




Original proposal: [https://github.com/fonttools/fontbakery/issues/4097 and https://github.com/fonttools/fontbakery/pull/4273]





- ⚠️ **WARN** xuqu-type-family/fonts/XUQU-Bold.ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+2003 EM SPACE: try adding nushu
* U+2010 HYPHEN: try adding one of: lisu, sora-sompeng, yi, sundanese, coptic, arabic, armenian, cham, hebrew, kaithi, syloti-nagri, kayah-li, kharoshthi
* U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, syloti-nagri, yi
* U+2021 DOUBLE DAGGER: try adding adlam
* U+202F NARROW NO-BREAK SPACE: try adding one of: yi, phags-pa, mongolian
* U+2030 PER MILLE SIGN: try adding adlam
* U+2190 LEFTWARDS ARROW: try adding one of: symbols, math
* U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math
* U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math
... and 5 others

Or you can add the above codepoints to one of the subsets supported by the font: latin-ext, latin [code: unreachable-subsetting]
  
  


- ⚠️ **WARN** xuqu-type-family/fonts/XUQU-ExtraBold.ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+2003 EM SPACE: try adding nushu
* U+2010 HYPHEN: try adding one of: lisu, sora-sompeng, yi, sundanese, coptic, arabic, armenian, cham, hebrew, kaithi, syloti-nagri, kayah-li, kharoshthi
* U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, syloti-nagri, yi
* U+2021 DOUBLE DAGGER: try adding adlam
* U+202F NARROW NO-BREAK SPACE: try adding one of: yi, phags-pa, mongolian
* U+2030 PER MILLE SIGN: try adding adlam
* U+2190 LEFTWARDS ARROW: try adding one of: symbols, math
* U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math
* U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math
... and 5 others

Or you can add the above codepoints to one of the subsets supported by the font: latin-ext, latin [code: unreachable-subsetting]
  
  


- ⚠️ **WARN** xuqu-type-family/fonts/XUQU-Light.ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+2003 EM SPACE: try adding nushu
* U+2010 HYPHEN: try adding one of: lisu, sora-sompeng, yi, sundanese, coptic, arabic, armenian, cham, hebrew, kaithi, syloti-nagri, kayah-li, kharoshthi
* U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, syloti-nagri, yi
* U+2021 DOUBLE DAGGER: try adding adlam
* U+202F NARROW NO-BREAK SPACE: try adding one of: yi, phags-pa, mongolian
* U+2030 PER MILLE SIGN: try adding adlam
* U+2190 LEFTWARDS ARROW: try adding one of: symbols, math
* U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math
* U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math
... and 5 others

Or you can add the above codepoints to one of the subsets supported by the font: latin-ext, latin [code: unreachable-subsetting]
  
  


- ⚠️ **WARN** xuqu-type-family/fonts/XUQU-Regular.ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+2003 EM SPACE: try adding nushu
* U+2010 HYPHEN: try adding one of: lisu, sora-sompeng, yi, sundanese, coptic, arabic, armenian, cham, hebrew, kaithi, syloti-nagri, kayah-li, kharoshthi
* U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, syloti-nagri, yi
* U+2021 DOUBLE DAGGER: try adding adlam
* U+202F NARROW NO-BREAK SPACE: try adding one of: yi, phags-pa, mongolian
* U+2030 PER MILLE SIGN: try adding adlam
* U+2190 LEFTWARDS ARROW: try adding one of: symbols, math
* U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math
* U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math
... and 5 others

Or you can add the above codepoints to one of the subsets supported by the font: latin-ext, latin [code: unreachable-subsetting]
  
  


- ⚠️ **WARN** xuqu-type-family/fonts/XUQU-Thin.ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+2003 EM SPACE: try adding nushu
* U+2010 HYPHEN: try adding one of: lisu, sora-sompeng, yi, sundanese, coptic, arabic, armenian, cham, hebrew, kaithi, syloti-nagri, kayah-li, kharoshthi
* U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, syloti-nagri, yi
* U+2021 DOUBLE DAGGER: try adding adlam
* U+202F NARROW NO-BREAK SPACE: try adding one of: yi, phags-pa, mongolian
* U+2030 PER MILLE SIGN: try adding adlam
* U+2190 LEFTWARDS ARROW: try adding one of: symbols, math
* U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math
* U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math
... and 5 others

Or you can add the above codepoints to one of the subsets supported by the font: latin-ext, latin [code: unreachable-subsetting]
  
  

</div>
</details>


</div>
</details>


<details><summary>[18] xuqu-type-family/fonts/XUQU-Thin.ttf</summary>
<div>


<details>
    <summary>🔥 <b>FAIL</b> Check code page character ranges (opentype/code_pages)</summary>
    <div>


> At least some programs (such as Word and Sublime Text) under Windows 7 do not recognize fonts unless code page bits are properly set on the ulCodePageRange1 (and/or ulCodePageRange2) fields of the OS/2 table.
> 
> More specifically, the fonts are selectable in the font menu, but whichever Windows API these applications use considers them unsuitable for any character set, so anything set in these fonts is rendered with Arial as a fallback font.
> 
> This check currently does not identify which code pages should be set. Auto-detecting coverage is not trivial since the OpenType specification leaves the interpretation of whether a given code page is "functional" or not open to the font developer to decide.
> 
> So here we simply detect as a FAIL when a given font has no code page declared at all.




Original proposal: [https://github.com/fonttools/fontbakery/issues/2474]





- 🔥 **FAIL** No code pages defined in the OS/2 table ulCodePageRange1 and CodePageRange2 fields. [code: no-code-pages]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. (googlefonts/glyphsets/shape_languages)</summary>
    <div>


> This check uses a heuristic to determine which GF glyphsets a font supports. Then it checks the font for correct shaping behaviour for all languages in those glyphsets.




Original proposal: [https://github.com/googlefonts/fontbakery/issues/4147]





- 🔥 **FAIL** Failed language shaping:

| Message                                                                           | Languages                    |
|-----------------------------------------------------------------------------------|------------------------------|
| Mandatory orthography codepoints:                                                 | * lt_Latn (Lithuanian)       |
|   The following mark characters are missing from the font: ̨, ̇, ̄, ̌                 |                              |
| Mandatory orthography codepoints:                                                 | * mt_Latn (Maltese)          |
|   The following mark characters are missing from the font: ̂, ̇, ̀                   |                              |
| Mandatory orthography codepoints:                                                 | * es_Latn (Spanish)          |
|   The following mark characters are missing from the font: ́, ̃, ̈                   |                              |
| Mandatory orthography codepoints:                                                 | * pt_Latn (Portuguese)       |
|   The following mark characters are missing from the font: ̂, ̈, ́, ̃, ̧, ̀             |                              |
| Mandatory orthography codepoints:                                                 | * hr_Latn (Croatian)         |
|   The following mark characters are missing from the font: ́, ̌                     |                              |
| Mandatory orthography codepoints:                                                 | * cy_Latn (Welsh)            |
|   The following base characters are missing from the font: ẃ, ỳ, Ỳ, Ẅ, Ẁ, Ẃ, ẁ, ẅ |                              |
|   The following mark characters are missing from the font: ́, ̂, ̀, ̈                 |                              |
| Mandatory orthography codepoints:                                                 | * cs_Latn (Czech)            |
|   The following mark characters are missing from the font: ̌, ́, ̊                   |                              |
| Mandatory orthography codepoints:                                                 | * fi_Latn (Finnish)          |
|   The following mark characters are missing from the font: ̊, ̌, ̈, ̃                 |                              |
| Mandatory orthography codepoints:                                                 | * nb_Latn (Norwegian Bokmål) |
|   The following mark characters are missing from the font: ̂, ̀, ̈, ̊, ́               |                              |
| Mandatory orthography codepoints:                                                 | * sk_Latn (Slovak)           |
|   The following mark characters are missing from the font: ̈, ́, ̌, ̂                 |                              |
| Mandatory orthography codepoints:                                                 | * ca_Latn (Catalan)          |
|   The following mark characters are missing from the font: ̧, ̀, ́, ̈                 |                              |
| Mandatory orthography codepoints:                                                 | * en_Latn (English)          |
|   The following mark characters are missing from the font: ̧, ̂, ́, ̀, ̃, ̈             |                              |
| Mandatory orthography codepoints:                                                 | * nl_Latn (Dutch)            |
|   The following base characters are missing from the font: íj́, ÍJ́                 |                              |
|   The following mark characters are missing from the font: ̂, ̈, ́, ̀                 |                              |
| Mandatory orthography codepoints:                                                 | * is_Latn (Icelandic)        |
|   The following mark characters are missing from the font: ́, ̨, ̈                   |                              |
| Mandatory orthography codepoints:                                                 | * ro_Latn (Romanian)         |
|   The following base characters are missing from the font: ț, Ș, ș, Ț             |                              |
|   The following mark characters are missing from the font: ̂, ̧, ̦, ̆                 |                              |
| Mandatory orthography codepoints:                                                 | * pl_Latn (Polish)           |
|   The following mark characters are missing from the font: ̨, ̇, ́                   |                              |
| Mandatory orthography codepoints:                                                 | * de_Latn (German)           |
|   The following base characters are missing from the font: ẞ                      |                              |
|   The following mark characters are missing from the font: ̈, ́, ̀                   |                              |
| Mandatory orthography codepoints:                                                 | * it_Latn (Italian)          |
|   The following mark characters are missing from the font: ̈, ̂, ́, ̀                 |                              |
| Mandatory orthography codepoints:                                                 | * sq_Latn (Albanian)         |
|   The following mark characters are missing from the font: ̈, ̧                     |                              |
| Mandatory orthography codepoints:                                                 | * da_Latn (Danish)           |
|   The following mark characters are missing from the font: ́, ̊                     |                              |
| Mandatory orthography codepoints:                                                 | * sv_Latn (Swedish)          |
|   The following mark characters are missing from the font: ̀, ̊, ̈, ́                 |                              |
| Mandatory orthography codepoints:                                                 | * lv_Latn (Latvian)          |
|   The following mark characters are missing from the font: ̧, ̄, ̌                   |                              |
| Mandatory orthography codepoints:                                                 | * fr_Latn (French)           |
|   The following mark characters are missing from the font: ́, ̀, ̂, ̧, ̈               |                              |
| Mandatory orthography codepoints:                                                 | * tr_Latn (Turkish)          |
|   The following mark characters are missing from the font: ̧, ̆, ̦, ̇, ̈, ̂             |                              |
| Mandatory orthography codepoints:                                                 | * hu_Latn (Hungarian)        |
|   The following mark characters are missing from the font: ́, ̈, ̋                   |                              | [code: failed-language-shaping]
  
  


- ⚠️ **WARN** Warning language shaping:

| Message                                                           | Languages                    |
|-------------------------------------------------------------------|------------------------------|
| Auxiliary orthography codepoints:                                 | * da_Latn (Danish)           |
|   The following auxiliary characters are missing from the font: Ǿ |                              |
|   The following auxiliary characters are missing from the font: ǿ |                              |
| Auxiliary orthography codepoints:                                 | * nb_Latn (Norwegian Bokmål) |
|   The following auxiliary characters are missing from the font: Ǎ |                              |
|   The following auxiliary characters are missing from the font: ǎ |                              |
| Auxiliary orthography codepoints:                                 | * en_Latn (English)          |
|   The following auxiliary characters are missing from the font: ʻ |                              |
| Auxiliary orthography codepoints:                                 | * fi_Latn (Finnish)          |
|   The following auxiliary characters are missing from the font: Ǧ |                              |
|   The following auxiliary characters are missing from the font: Ǥ |                              |
|   The following auxiliary characters are missing from the font: Ȟ |                              |
|   The following auxiliary characters are missing from the font: Ǩ |                              |
|   The following auxiliary characters are missing from the font: Ș |                              |
|   The following auxiliary characters are missing from the font: ẞ |                              |
|   The following auxiliary characters are missing from the font: Ț |                              |
|   The following auxiliary characters are missing from the font: Ʒ |                              |
|   The following auxiliary characters are missing from the font: Ǯ |                              |
|   The following auxiliary characters are missing from the font: ǧ |                              |
|   The following auxiliary characters are missing from the font: ǥ |                              |
|   The following auxiliary characters are missing from the font: ȟ |                              |
|   The following auxiliary characters are missing from the font: ǩ |                              |
|   The following auxiliary characters are missing from the font: ș |                              |
|   The following auxiliary characters are missing from the font: ț |                              |
|   The following auxiliary characters are missing from the font: ʒ |                              |
|   The following auxiliary characters are missing from the font: ǯ |                              |
| Auxiliary orthography codepoints:                                 | * fr_Latn (French)           |
|   The following auxiliary characters are missing from the font: ẞ |                              |
|   The following auxiliary characters are missing from the font: Ǔ |                              |
|   The following auxiliary characters are missing from the font: ǔ |                              |
| Auxiliary orthography codepoints:                                 | * it_Latn (Italian)          |
|   The following auxiliary characters are missing from the font: ẞ | * pl_Latn (Polish)           |
|                                                                   | * tr_Latn (Turkish)          |
| Auxiliary orthography codepoints:                                 | * lt_Latn (Lithuanian)       |
|   The following auxiliary characters are missing from the font: Ą́ |                              |
|   The following auxiliary characters are missing from the font: Ą̃ |                              |
|   The following auxiliary characters are missing from the font: Ẽ |                              |
|   The following auxiliary characters are missing from the font: Ę́ |                              |
|   The following auxiliary characters are missing from the font: Ę̃ |                              |
|   The following auxiliary characters are missing from the font: Ė́ |                              |
|   The following auxiliary characters are missing from the font: Ė̃ |                              |
|   The following auxiliary characters are missing from the font: İ́ |                              |
|   The following auxiliary characters are missing from the font: İ́ |                              |
|   The following auxiliary characters are missing from the font: İ̀ |                              |
|   The following auxiliary characters are missing from the font: İ̀ |                              |
|   The following auxiliary characters are missing from the font: İ̃ |                              |
|   The following auxiliary characters are missing from the font: İ̃ |                              |
|   The following auxiliary characters are missing from the font: Į́ |                              |
|   The following auxiliary characters are missing from the font: Į̇́ |                              |
|   The following auxiliary characters are missing from the font: Į̃ |                              |
|   The following auxiliary characters are missing from the font: Į̇̃ |                              |
|   The following auxiliary characters are missing from the font: J̃ |                              |
|   The following auxiliary characters are missing from the font: J̇̃ |                              |
|   The following auxiliary characters are missing from the font: L̃ |                              |
|   The following auxiliary characters are missing from the font: M̃ |                              |
|   The following auxiliary characters are missing from the font: R̃ |                              |
|   The following auxiliary characters are missing from the font: Ų́ |                              |
|   The following auxiliary characters are missing from the font: Ų̃ |                              |
|   The following auxiliary characters are missing from the font: Ū́ |                              |
|   The following auxiliary characters are missing from the font: Ū̃ |                              |
|   The following auxiliary characters are missing from the font: ą́ |                              |
|   The following auxiliary characters are missing from the font: ą̃ |                              |
|   The following auxiliary characters are missing from the font: ẽ |                              |
|   The following auxiliary characters are missing from the font: ę́ |                              |
|   The following auxiliary characters are missing from the font: ę̃ |                              |
|   The following auxiliary characters are missing from the font: ė́ |                              |
|   The following auxiliary characters are missing from the font: ė̃ |                              |
|   The following auxiliary characters are missing from the font: i̇́ |                              |
|   The following auxiliary characters are missing from the font: i̇̀ |                              |
|   The following auxiliary characters are missing from the font: i̇̃ |                              |
|   The following auxiliary characters are missing from the font: į́ |                              |
|   The following auxiliary characters are missing from the font: į̇́ |                              |
|   The following auxiliary characters are missing from the font: į̃ |                              |
|   The following auxiliary characters are missing from the font: į̇̃ |                              |
|   The following auxiliary characters are missing from the font: j̃ |                              |
|   The following auxiliary characters are missing from the font: j̇̃ |                              |
|   The following auxiliary characters are missing from the font: l̃ |                              |
|   The following auxiliary characters are missing from the font: m̃ |                              |
|   The following auxiliary characters are missing from the font: r̃ |                              |
|   The following auxiliary characters are missing from the font: ų́ |                              |
|   The following auxiliary characters are missing from the font: ų̃ |                              |
|   The following auxiliary characters are missing from the font: ū́ |                              |
|   The following auxiliary characters are missing from the font: ū̃ |                              | [code: warning-language-shaping]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Check family name for GF Guide compliance. (googlefonts/family_name_compliance)</summary>
    <div>


> Checks the family name for compliance with the Google Fonts Guide. https://googlefonts.github.io/gf-guide/onboarding.html#new-fonts
> 
> If you want to have your family name added to the CamelCase exceptions list, please submit a pull request to the camelcased_familyname_exceptions.txt file.
> 
> Similarly, abbreviations can be submitted to the abbreviations_familyname_exceptions.txt file.
> 
> These are located in the Lib/fontbakery/data/googlefonts/ directory of the FontBakery source code currently hosted at https://github.com/fonttools/fontbakery/




Original proposal: [https://github.com/fonttools/fontbakery/issues/4049]





- 🔥 **FAIL** "XUQU体" contains an abbreviation. [code: abbreviation]
  
  


- 🔥 **FAIL** "XUQU体" contains the following characters which are not allowed: "体". [code: forbidden-characters]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Checking file is named canonically. (googlefonts/canonical_filename)</summary>
    <div>


> A font's filename must be composed as "<familyname>-<stylename>.ttf":
> 
> - Nunito-Regular.ttf
> 
> - Oswald-BoldItalic.ttf
> 
> Variable fonts must list the axis tags in alphabetical order in square brackets and separated by commas:
> 
> - Roboto[wdth,wght].ttf
> 
> - Familyname-Italic[wght].ttf




Original proposal: [https://github.com/fonttools/fontbakery/issues/4829]





- 🔥 **FAIL** Expected "XUQU体-Thin.ttf". Got "XUQU-Thin.ttf". [code: bad-filename]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Check font names are correct (googlefonts/font_names)</summary>
    <div>


> Google Fonts has several rules which need to be adhered to when setting a font's name table. Please read: https://googlefonts.github.io/gf-guide/statics.html#supported-styles https://googlefonts.github.io/gf-guide/statics.html#style-linking https://googlefonts.github.io/gf-guide/statics.html#unsupported-styles https://googlefonts.github.io/gf-guide/statics.html#single-weight-families




Original proposal: [https://github.com/fonttools/fontbakery/pull/3800]





- 🔥 **FAIL** Font names are incorrect:

| Name                       | Current       | Expected        |
|----------------------------|---------------|-----------------|
| Family Name                | XUQU体 Thin   | XUQU体 Thin     |
| Subfamily Name             | Regular       | Regular         |
| Full Name                  | XUQU体 Thin   | XUQU体 Thin     |
| Postscript Name            | **XUQU-Thin** | **XUQU体-Thin** |
| Typographic Family Name    | XUQU体        | XUQU体          |
| Typographic Subfamily Name | Thin          | Thin            | [code: bad-names]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Ensure font can render its own name. (googlefonts/render_own_name)</summary>
    <div>


> A base expectation is that a font family's regular/default (400 roman) style can render its 'menu name' (nameID 1) in itself.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3159]





- 🔥 **FAIL** .notdef glyphs were found when attempting to render XUQU体 Thin [code: render-own-name]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check that OS/2 fsSelection WWS bit is set correctly. (opentype/fsselection_wws)</summary>
    <div>


> According to the OpenType specification, OS/2.fsSelection bit 8 (WWS) should be set if the font has name table strings consistent with a weight/width/slope family without requiring use of name IDs 21 and 22.
> 
> Conversely, if name IDs 21 and 22 are present (indicating the font names are not WWS-conformant), the WWS bit should not be set.




Original proposal: [https://github.com/fonttools/fontspector/issues/577]





- ⚠️ **WARN** OS/2 fsSelection WWS bit is not set, and the font does not have name IDs 21/22 (WWS Family/Subfamily). If the font's naming is WWS-conformant, the WWS bit should be set. [code: no-wws-without-wws-names]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron (alt_caron)</summary>
    <div>


> Lcaron, dcaron, lcaron, tcaron should NOT be composed with quoteright or quotesingle or comma or caron(comb). It should be composed with a distinctive glyph which doesn't look like an apostrophe.
> 
> Source: https://ilovetypography.com/2009/01/24/on-diacritics/ http://diacritics.typo.cz/index.php?id=5 https://www.typotheque.com/articles/lcaron




Original proposal: [https://github.com/fonttools/fontbakery/issues/3308]





- ⚠️ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  


- ⚠️ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  


- ⚠️ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  


- ⚠️ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. (contour_count)</summary>
    <div>


> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be constructured in a handful of ways. This means a glyph's contour count will only differ slightly amongst different fonts, e.g a 'g' could either be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs to a display family.
> 
> This check currently does not cover variable fonts because there's plenty of alternative ways of constructing glyphs with multiple outlines for each feature in a VarFont. The expected contour count data for this check is currently optimized for the typical construction of glyphs in static fonts.




Original proposal: [https://github.com/fonttools/fontbakery/issues/4829]





- ⚠️ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are
     inferred from the typical amounts of contours observed in a
     large collection of reference font families. The divergences
     listed below may simply indicate a significantly different
     design on some of your glyphs. On the other hand, some of these
     may flag actual bugs in the font such as glyphs mapped to an
     incorrect codepoint. Please consider reviewing the design and
     codepoint assignment of these to make sure they are correct.


    The following glyphs do not have the recommended number of contours:
* uni013C (U+013C): found 1, expected one of: [2, 3, 6]
* section (U+00A7): found 1, expected one of: [2, 4, 6] [code: contour-count]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. (math_signs_width)</summary>
    <div>


> #,         It is a common practice to have math signs sharing the same width         (preferably the same width as tabular figures accross the entire font family).
> 
> This probably comes from the will to avoid additional tabular math signs knowing that their design can easily share the same width.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3832]





- ⚠️ **WARN** The most common width is 766 among a set of 12  math glyphs.
The following math glyphs have a different width, though:
width=746: greater, less, lessequal, greaterequal
width=556: minus [code: width-outliers]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure indic fonts have the Indian Rupee Sign glyph. (rupee)</summary>
    <div>


> Per Bureau of Indian Standards every font supporting one of the official Indian languages needs to include Unicode Character “₹” (U+20B9) Indian Rupee Sign.




Original proposal: [https://github.com/fonttools/fontbakery/issues/2967]





- ⚠️ **WARN** Font is missing the Indian Rupee Sign glyph. Please add a glyph for Indian Rupee Sign (₹) at codepoint U+20B9. [code: missing-rupee]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? (soft_hyphen)</summary>
    <div>


> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark a hyphenation possibility within a word in the absence of or overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character), sometimes the same as the traditional hyphen, sometimes double encoded with the hyphen.
> 
> That being said, it is recommended to not include it in the font at all, because discretionary hyphenation should be handled at the level of the shaping engine, not the font. Also, even if present, the software would not display that character.
> 
> More discussion at: https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar




Original proposal: [https://github.com/fonttools/fontbakery/issues/4046, https://github.com/fonttools/fontbakery/issues/3486]





- ⚠️ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs (unreachable_glyphs)</summary>
    <div>


> Glyphs are either accessible directly through Unicode codepoints or through        substitution rules.
> 
> In Color Fonts, glyphs are also referenced by the COLR table. And mathematical fonts also reference glyphs via the MATH table.
> 
> Any glyphs not accessible by these means are redundant and serve only to increase the font's file size.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3160]





- ⚠️ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

* .null
* nonmarkingreturn [code: unreachable-glyphs]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Font has correct separator glyphs? (googlefonts/separator_glyphs)</summary>
    <div>


> U+2028 and U+2029 should be present; otherwise tofu is displayed. (whitespace_ink will check that they are empty)




Original proposal: [https://github.com/fonttools/fontspector/issues/93]





- ⚠️ **WARN** Missing separator glyph U+2028 [code: missing-separator-glyphs]
  
  


- ⚠️ **WARN** Missing separator glyph U+2029 [code: missing-separator-glyphs]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? (outline_alignment_miss)</summary>
    <div>


> This check heuristically looks for on-curve points which are close to, but do not sit on, significant boundary coordinates. For example, a point which has a Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the baseline, here we also check for points near the x-height (but only for lowercase Latin letters), cap-height, ascender and descender Y coordinates.
> 
> Not all such misaligned curve points are a mistake, and sometimes the design may call for points in locations near the boundaries. As this check is liable to generate significant numbers of false positives, it will pass if there are more than 100 reported misalignments.




Original proposal: [https://github.com/fonttools/fontbakery/pull/3088]





- ⚠️ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

* - K (U+004B): X=882,Y=1 (should be at baseline 0?)
* - K (U+004B): X=882,Y=699 (should be at cap-height 700?)
* - k (U+006B): X=733,Y=1 (should be at baseline 0?)
* - z (U+007A): X=58,Y=1 (should be at baseline 0?)
* - question (U+003F): X=438,Y=1 (should be at baseline 0?)
* - question (U+003F): X=372,Y=1 (should be at baseline 0?)
* - germandbls (U+00DF): X=509,Y=698 (should be at cap-height 700?)
* - germandbls (U+00DF): X=149,Y=698 (should be at cap-height 700?)
* - kgreenlandic (U+0138): X=742,Y=1 (should be at baseline 0?)
... and 23 others [code: found-misalignments]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? (outline_colinear_vectors)</summary>
    <div>


> This check looks for consecutive line segments which have the same angle. This normally happens if an outline point has been added by accident.
> 
> This check is not run for variable fonts, as they may legitimately have colinear vectors.




Original proposal: [https://github.com/fonttools/fontbakery/pull/3088]





- ⚠️ **WARN** The following glyphs have colinear vectors:

* A (U+0041): from (58.0, 0.0) to (206.0, 257.0) is colinear with segment from (206.0, 257.0) to (213.0, 270.0)
* A (U+0041): from (206.0, 257.0) to (213.0, 270.0) is colinear with segment from (213.0, 270.0) to (460.0, 700.0)
* A (U+0041): from (496.0, 700.0) to (736.0, 283.0) is colinear with segment from (736.0, 283.0) to (740.0, 276.0)
* A (U+0041): from (736.0, 283.0) to (740.0, 276.0) is colinear with segment from (740.0, 276.0) to (898.0, 0.0)
* b (U+0062): from (643.0, 0.0) to (86.0, 0.0) is colinear with segment from (86.0, 0.0) to (58.0, 0.0)
* b (U+0062): from (58.0, 0.0) to (58.0, 530.0) is colinear with segment from (58.0, 530.0) to (58.0, 700.0)
* d (U+0064): from (738.0, 700.0) to (738.0, 530.0) is colinear with segment from (738.0, 530.0) to (738.0, 0.0)
* d (U+0064): from (738.0, 0.0) to (710.0, 0.0) is colinear with segment from (710.0, 0.0) to (153.0, 0.0)
* p (U+0070): from (58.0, -205.0) to (58.0, 0.0) is colinear with segment from (58.0, 0.0) to (58.0, 530.0)
... and 85 others [code: found-colinear-vectors]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (googlefonts/meta/script_lang_tags)</summary>
    <div>


> The OpenType 'meta' table originated at Apple. Microsoft added it to OT with just two DataMap records:
> 
> - dlng: comma-separated ScriptLangTags that indicate which scripts,   or languages and scripts, with possible variants, the font is designed for.
> 
> - slng: comma-separated ScriptLangTags that indicate which scripts,   or languages and scripts, with possible variants, the font supports.
> 
> The slng structure is intended to describe which languages and scripts the font overall supports. For example, a Traditional Chinese font that also contains Latin characters, can indicate Hant,Latn, showing that it supports Hant, the Traditional Chinese variant of the Hani script, and it also supports the Latn script.
> 
> The dlng structure is far more interesting. A font may contain various glyphs, but only a particular subset of the glyphs may be truly "leading" in the design, while other glyphs may have been included for technical reasons. Such a Traditional Chinese font could only list Hant there, showing that it’s designed for Traditional Chinese, but the font would omit Latn, because the developers don’t think the font is really recommended for purely Latin-script use.
> 
> The tags used in the structures can comprise just script, or also language and script. For example, if a font has Bulgarian Cyrillic alternates in the locl feature for the cyrl BGR OT languagesystem, it could also indicate in dlng explicitly that it supports bul-Cyrl. (Note that the scripts and languages in meta use the ISO language and script codes, not the OpenType ones).
> 
> This check ensures that the font has the meta table containing the slng and dlng structures.
> 
> All families in the Google Fonts collection should contain the 'meta' table. Windows 10 already uses it when deciding on which fonts to fall back to. The Google Fonts API and also other environments could use the data for smarter filtering. Most importantly, those entries should be added to the Noto fonts.
> 
> In the font making process, some environments store this data in external files already. But the meta table provides a convenient way to store this inside the font file, so some tools may add the data, and unrelated tools may read this data. This makes the solution much more portable and universal.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3349]





- ⚠️ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. (googlefonts/vendor_id)</summary>
    <div>


> Microsoft keeps a list of font vendors and their respective contact info. This list is updated regularly and is indexed by a 4-char "Vendor ID" which is stored in the achVendID field of the OS/2 table.
> 
> Registering your ID is not mandatory, but it is a good practice since some applications may display the type designer / type foundry contact info on some dialog and also because that info will be visible on Microsoft's website:
> 
> https://docs.microsoft.com/en-us/typography/vendors/
> 
> This check verifies whether or not a given font's vendor ID is registered in that list or if it has some of the default values used by the most common font editors.
> 
> Each new FontBakery release includes a cached copy of that list of vendor IDs. If you registered recently, you're safe to ignore warnings emitted by this check, since your ID will soon be included in one of our upcoming releases.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3943, https://github.com/fonttools/fontbakery/issues/4829]





- ⚠️ **WARN** OS/2 VendorID value 'XUQU' is not yet recognized.
If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
  
  

</div>
</details>


</div>
</details>






### Summary

| 🔥 FAIL | ⚠️ WARN | ℹ️ INFO | ✅ PASS | ⏩ SKIP | 
| ---|---|---|---|---|
| 47 | 90 | 17 | 380 | 350 | 
| 5% | 10% | 2% | 43% | 40% | 



