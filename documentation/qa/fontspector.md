## FontSpector report

fontspector version: 1.7.4






## Check results




<details><summary>[9] /workspace/scratch/cbc03b9be171/xuqu-googlefonts-prep/build/googlefonts/ofl/xuqu/Xuqu-Bold.ttf</summary>
<div>


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
width=746: lessequal, less, greaterequal, greater
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
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. (googlefonts/glyphsets/shape_languages)</summary>
    <div>


> This check uses a heuristic to determine which GF glyphsets a font supports. Then it checks the font for correct shaping behaviour for all languages in those glyphsets.




Original proposal: [https://github.com/googlefonts/fontbakery/issues/4147]





- ⚠️ **WARN** Warning language shaping:

| Message                                                           | Languages                    |
|-------------------------------------------------------------------|------------------------------|
| Auxiliary orthography codepoints:                                 | * da_Latn (Danish)           |
|   The following auxiliary characters are missing from the font: Ǿ |                              |
|   The following auxiliary characters are missing from the font: ǿ |                              |
| Auxiliary orthography codepoints:                                 | * en_Latn (English)          |
|   The following auxiliary characters are missing from the font: ʻ |                              |
| Auxiliary orthography codepoints:                                 | * nb_Latn (Norwegian Bokmål) |
|   The following auxiliary characters are missing from the font: Ǎ |                              |
|   The following auxiliary characters are missing from the font: ǎ |                              |
| Auxiliary orthography codepoints:                                 | * fr_Latn (French)           |
|   The following auxiliary characters are missing from the font: Ǔ |                              |
|   The following auxiliary characters are missing from the font: ǔ |                              |
| Auxiliary orthography codepoints:                                 | * lt_Latn (Lithuanian)       |
|   The following auxiliary characters are missing from the font: Ẽ |                              |
|   The following auxiliary characters are missing from the font: ẽ |                              |
| Auxiliary orthography codepoints:                                 | * fi_Latn (Finnish)          |
|   The following auxiliary characters are missing from the font: Ǧ |                              |
|   The following auxiliary characters are missing from the font: Ǥ |                              |
|   The following auxiliary characters are missing from the font: Ȟ |                              |
|   The following auxiliary characters are missing from the font: Ǩ |                              |
|   The following auxiliary characters are missing from the font: Ʒ |                              |
|   The following auxiliary characters are missing from the font: Ǯ |                              |
|   The following auxiliary characters are missing from the font: ǧ |                              |
|   The following auxiliary characters are missing from the font: ǥ |                              |
|   The following auxiliary characters are missing from the font: ȟ |                              |
|   The following auxiliary characters are missing from the font: ǩ |                              |
|   The following auxiliary characters are missing from the font: ʒ |                              |
|   The following auxiliary characters are missing from the font: ǯ |                              | [code: warning-language-shaping]
  
  

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
* - ordfeminine (U+00AA): X=432,Y=702 (should be at cap-height 700?)
* - ordmasculine (U+00BA): X=114,Y=702 (should be at cap-height 700?)
* - ordmasculine (U+00BA): X=376,Y=702 (should be at cap-height 700?)
* - uni00B9 (U+00B9): X=243,Y=701 (should be at cap-height 700?)
* - uni00B9 (U+00B9): X=307,Y=701 (should be at cap-height 700?)
* - uni00B2 (U+00B2): X=118,Y=701 (should be at cap-height 700?)
* - uni00B2 (U+00B2): X=398,Y=701 (should be at cap-height 700?)
* - uni00B3 (U+00B3): X=58,Y=701 (should be at cap-height 700?)
* - uni00B3 (U+00B3): X=396,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=544,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=852,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=913,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=483,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=58,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=419,Y=701 (should be at cap-height 700?)
* - quotesinglbase (U+201A): X=214,Y=-1 (should be at baseline 0?)
* - quotesinglbase (U+201A): X=195,Y=-1 (should be at baseline 0?)
* - quotedblbase (U+201E): X=423,Y=-1 (should be at baseline 0?)
* - quotedblbase (U+201E): X=405,Y=-1 (should be at baseline 0?)
* - quotedblbase (U+201E): X=199,Y=-1 (should be at baseline 0?)
* - quotedblbase (U+201E): X=181,Y=-1 (should be at baseline 0?)
* - dotaccent (U+02D9): X=115,Y=701 (should be at cap-height 700?)
* - dotaccent (U+02D9): X=185,Y=701 (should be at cap-height 700?) [code: found-misalignments]
  
  

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
* AE (U+00C6): from (58.0, 0.0) to (129.0, 203.0) is colinear with segment from (129.0, 203.0) to (175.0, 337.0)
* AE (U+00C6): from (129.0, 203.0) to (175.0, 337.0) is colinear with segment from (175.0, 337.0) to (301.0, 700.0)
* AE (U+00C6): from (445.0, 700.0) to (571.0, 337.0) is colinear with segment from (571.0, 337.0) to (598.0, 259.0)
* Agrave (U+00C0): from (58.0, 0.0) to (152.0, 203.0) is colinear with segment from (152.0, 203.0) to (214.0, 337.0)
* Agrave (U+00C0): from (152.0, 203.0) to (214.0, 337.0) is colinear with segment from (214.0, 337.0) to (382.0, 700.0)
* Agrave (U+00C0): from (574.0, 700.0) to (742.0, 337.0) is colinear with segment from (742.0, 337.0) to (804.0, 203.0)
* Agrave (U+00C0): from (742.0, 337.0) to (804.0, 203.0) is colinear with segment from (804.0, 203.0) to (898.0, 0.0)
* Aacute (U+00C1): from (58.0, 0.0) to (152.0, 203.0) is colinear with segment from (152.0, 203.0) to (214.0, 337.0)
* Aacute (U+00C1): from (152.0, 203.0) to (214.0, 337.0) is colinear with segment from (214.0, 337.0) to (382.0, 700.0)
* Aacute (U+00C1): from (574.0, 700.0) to (742.0, 337.0) is colinear with segment from (742.0, 337.0) to (804.0, 203.0)
* Aacute (U+00C1): from (742.0, 337.0) to (804.0, 203.0) is colinear with segment from (804.0, 203.0) to (898.0, 0.0)
* Acircumflex (U+00C2): from (58.0, 0.0) to (152.0, 203.0) is colinear with segment from (152.0, 203.0) to (214.0, 337.0)
* Acircumflex (U+00C2): from (152.0, 203.0) to (214.0, 337.0) is colinear with segment from (214.0, 337.0) to (382.0, 700.0)
* Acircumflex (U+00C2): from (574.0, 700.0) to (742.0, 337.0) is colinear with segment from (742.0, 337.0) to (804.0, 203.0)
* Acircumflex (U+00C2): from (742.0, 337.0) to (804.0, 203.0) is colinear with segment from (804.0, 203.0) to (898.0, 0.0)
* Atilde (U+00C3): from (58.0, 0.0) to (152.0, 203.0) is colinear with segment from (152.0, 203.0) to (214.0, 337.0)
* Atilde (U+00C3): from (152.0, 203.0) to (214.0, 337.0) is colinear with segment from (214.0, 337.0) to (382.0, 700.0)
* Atilde (U+00C3): from (574.0, 700.0) to (742.0, 337.0) is colinear with segment from (742.0, 337.0) to (804.0, 203.0)
* Atilde (U+00C3): from (742.0, 337.0) to (804.0, 203.0) is colinear with segment from (804.0, 203.0) to (898.0, 0.0)
* Adieresis (U+00C4): from (58.0, 0.0) to (152.0, 203.0) is colinear with segment from (152.0, 203.0) to (214.0, 337.0)
* Adieresis (U+00C4): from (152.0, 203.0) to (214.0, 337.0) is colinear with segment from (214.0, 337.0) to (382.0, 700.0)
* Adieresis (U+00C4): from (574.0, 700.0) to (742.0, 337.0) is colinear with segment from (742.0, 337.0) to (804.0, 203.0)
* Adieresis (U+00C4): from (742.0, 337.0) to (804.0, 203.0) is colinear with segment from (804.0, 203.0) to (898.0, 0.0)
* Aring (U+00C5): from (58.0, 0.0) to (152.0, 203.0) is colinear with segment from (152.0, 203.0) to (214.0, 337.0)
* Aring (U+00C5): from (152.0, 203.0) to (214.0, 337.0) is colinear with segment from (214.0, 337.0) to (382.0, 700.0)
* Aring (U+00C5): from (574.0, 700.0) to (742.0, 337.0) is colinear with segment from (742.0, 337.0) to (804.0, 203.0)
* Aring (U+00C5): from (742.0, 337.0) to (804.0, 203.0) is colinear with segment from (804.0, 203.0) to (898.0, 0.0)
* Amacron (U+0100): from (58.0, 0.0) to (152.0, 203.0) is colinear with segment from (152.0, 203.0) to (214.0, 337.0)
* Amacron (U+0100): from (152.0, 203.0) to (214.0, 337.0) is colinear with segment from (214.0, 337.0) to (382.0, 700.0)
* Amacron (U+0100): from (574.0, 700.0) to (742.0, 337.0) is colinear with segment from (742.0, 337.0) to (804.0, 203.0)
* Amacron (U+0100): from (742.0, 337.0) to (804.0, 203.0) is colinear with segment from (804.0, 203.0) to (898.0, 0.0)
* Abreve (U+0102): from (58.0, 0.0) to (152.0, 203.0) is colinear with segment from (152.0, 203.0) to (214.0, 337.0)
* Abreve (U+0102): from (152.0, 203.0) to (214.0, 337.0) is colinear with segment from (214.0, 337.0) to (382.0, 700.0)
* Abreve (U+0102): from (574.0, 700.0) to (742.0, 337.0) is colinear with segment from (742.0, 337.0) to (804.0, 203.0)
* Abreve (U+0102): from (742.0, 337.0) to (804.0, 203.0) is colinear with segment from (804.0, 203.0) to (898.0, 0.0)
* Aogonek (U+0104): from (58.0, 0.0) to (152.0, 203.0) is colinear with segment from (152.0, 203.0) to (214.0, 337.0)
* Aogonek (U+0104): from (152.0, 203.0) to (214.0, 337.0) is colinear with segment from (214.0, 337.0) to (382.0, 700.0)
* Aogonek (U+0104): from (574.0, 700.0) to (742.0, 337.0) is colinear with segment from (742.0, 337.0) to (804.0, 203.0)
* Aogonek (U+0104): from (742.0, 337.0) to (804.0, 203.0) is colinear with segment from (804.0, 203.0) to (898.0, 0.0) [code: found-colinear-vectors]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table
set to optimize rendering? (googlefonts/gasp)</summary>
    <div>


> Traditionally version 0 'gasp' tables were set so that font sizes below 8 ppem had no grid fitting but did have antialiasing. From 9-16 ppem, just grid fitting. And fonts above 17ppem had both antialiasing and grid fitting toggled on. The use of accelerated graphics cards and higher resolution screens make this approach obsolete. Microsoft's DirectWrite pushed this even further with much improved rendering built into the OS and apps.
> 
> In this scenario it makes sense to simply toggle all 4 flags ON for all font sizes.




Original proposal: [https://github.com/fonttools/fontbakery/issues/4829]




  


- ⚠️ **WARN** The gasp range 0xFFFF value 0x0A should be set to 0x0F [code: unset-flags]
  
  

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


<details><summary>[10] /workspace/scratch/cbc03b9be171/xuqu-googlefonts-prep/build/googlefonts/ofl/xuqu/Xuqu-Light.ttf</summary>
<div>


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
width=746: lessequal, greaterequal, greater, less
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
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. (googlefonts/glyphsets/shape_languages)</summary>
    <div>


> This check uses a heuristic to determine which GF glyphsets a font supports. Then it checks the font for correct shaping behaviour for all languages in those glyphsets.




Original proposal: [https://github.com/googlefonts/fontbakery/issues/4147]





- ⚠️ **WARN** Warning language shaping:

| Message                                                           | Languages                    |
|-------------------------------------------------------------------|------------------------------|
| Auxiliary orthography codepoints:                                 | * fr_Latn (French)           |
|   The following auxiliary characters are missing from the font: Ǔ |                              |
|   The following auxiliary characters are missing from the font: ǔ |                              |
| Auxiliary orthography codepoints:                                 | * en_Latn (English)          |
|   The following auxiliary characters are missing from the font: ʻ |                              |
| Auxiliary orthography codepoints:                                 | * fi_Latn (Finnish)          |
|   The following auxiliary characters are missing from the font: Ǧ |                              |
|   The following auxiliary characters are missing from the font: Ǥ |                              |
|   The following auxiliary characters are missing from the font: Ȟ |                              |
|   The following auxiliary characters are missing from the font: Ǩ |                              |
|   The following auxiliary characters are missing from the font: Ʒ |                              |
|   The following auxiliary characters are missing from the font: Ǯ |                              |
|   The following auxiliary characters are missing from the font: ǧ |                              |
|   The following auxiliary characters are missing from the font: ǥ |                              |
|   The following auxiliary characters are missing from the font: ȟ |                              |
|   The following auxiliary characters are missing from the font: ǩ |                              |
|   The following auxiliary characters are missing from the font: ʒ |                              |
|   The following auxiliary characters are missing from the font: ǯ |                              |
| Auxiliary orthography codepoints:                                 | * nb_Latn (Norwegian Bokmål) |
|   The following auxiliary characters are missing from the font: Ǎ |                              |
|   The following auxiliary characters are missing from the font: ǎ |                              |
| Auxiliary orthography codepoints:                                 | * lt_Latn (Lithuanian)       |
|   The following auxiliary characters are missing from the font: Ẽ |                              |
|   The following auxiliary characters are missing from the font: ẽ |                              |
| Auxiliary orthography codepoints:                                 | * da_Latn (Danish)           |
|   The following auxiliary characters are missing from the font: Ǿ |                              |
|   The following auxiliary characters are missing from the font: ǿ |                              | [code: warning-language-shaping]
  
  

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

* - K (U+004B): X=869,Y=698 (should be at cap-height 700?)
* - K (U+004B): X=870,Y=2 (should be at baseline 0?)
* - k (U+006B): X=722,Y=2 (should be at baseline 0?)
* - z (U+007A): X=58,Y=2 (should be at baseline 0?)
* - numbersign (U+0023): X=494,Y=1 (should be at baseline 0?)
* - numbersign (U+0023): X=189,Y=1 (should be at baseline 0?)
* - numbersign (U+0023): X=357,Y=699 (should be at cap-height 700?)
* - numbersign (U+0023): X=662,Y=699 (should be at cap-height 700?)
* - percent (U+0025): X=151,Y=1 (should be at baseline 0?)
* - percent (U+0025): X=755,Y=699 (should be at cap-height 700?)
* - asciicircum (U+005E): X=358,Y=701 (should be at cap-height 700?)
* - Oslash (U+00D8): X=793,Y=702 (should be at cap-height 700?)
* - Oslash (U+00D8): X=143,Y=-2 (should be at baseline 0?)
* - kgreenlandic (U+0138): X=732,Y=1 (should be at baseline 0?)
* - Aogonek (U+0104): X=890,Y=-2 (should be at baseline 0?)
* - aogonek (U+0105): X=732,Y=-2 (should be at baseline 0?)
* - Eogonek (U+0118): X=832,Y=-2 (should be at baseline 0?)
* - eogonek (U+0119): X=642,Y=-2 (should be at baseline 0?)
* - Iogonek (U+012E): X=412,Y=-2 (should be at baseline 0?)
* - iogonek (U+012F): X=79,Y=2 (should be at baseline 0?)
* - iogonek (U+012F): X=131,Y=-2 (should be at baseline 0?)
* - uni0136 (U+0136): X=869,Y=698 (should be at cap-height 700?)
* - uni0136 (U+0136): X=870,Y=2 (should be at baseline 0?)
* - uni0137 (U+0137): X=722,Y=2 (should be at baseline 0?)
* - Uogonek (U+0172): X=791,Y=-2 (should be at baseline 0?)
* - uogonek (U+0173): X=649,Y=-2 (should be at baseline 0?)
* - zacute (U+017A): X=58,Y=2 (should be at baseline 0?)
* - zdotaccent (U+017C): X=58,Y=2 (should be at baseline 0?)
* - zcaron (U+017E): X=58,Y=2 (should be at baseline 0?)
* - section (U+00A7): X=572,Y=702 (should be at cap-height 700?)
* - section (U+00A7): X=129,Y=702 (should be at cap-height 700?)
* - ordfeminine (U+00AA): X=110,Y=702 (should be at cap-height 700?)
* - ordfeminine (U+00AA): X=432,Y=702 (should be at cap-height 700?)
* - ordmasculine (U+00BA): X=106,Y=702 (should be at cap-height 700?)
* - ordmasculine (U+00BA): X=384,Y=702 (should be at cap-height 700?)
* - uni00B9 (U+00B9): X=244,Y=701 (should be at cap-height 700?)
* - uni00B9 (U+00B9): X=286,Y=701 (should be at cap-height 700?)
* - uni00B2 (U+00B2): X=110,Y=701 (should be at cap-height 700?)
* - uni00B2 (U+00B2): X=406,Y=701 (should be at cap-height 700?)
* - uni00B3 (U+00B3): X=58,Y=701 (should be at cap-height 700?)
* - uni00B3 (U+00B3): X=404,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=518,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=878,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=913,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=483,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=58,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=419,Y=701 (should be at cap-height 700?)
* - quotesinglbase (U+201A): X=187,Y=2 (should be at baseline 0?)
* - quotesinglbase (U+201A): X=175,Y=2 (should be at baseline 0?)
* - quotedblbase (U+201E): X=361,Y=2 (should be at baseline 0?)
* - quotedblbase (U+201E): X=348,Y=2 (should be at baseline 0?)
* - quotedblbase (U+201E): X=208,Y=2 (should be at baseline 0?)
* - quotedblbase (U+201E): X=196,Y=2 (should be at baseline 0?)
* - perthousand (U+2030): X=651,Y=699 (should be at cap-height 700?)
* - perthousand (U+2030): X=137,Y=1 (should be at baseline 0?)
* - tilde (U+02DC): X=127,Y=698 (should be at cap-height 700?)
* - tilde (U+02DC): X=192,Y=698 (should be at cap-height 700?)
* - wgrave (U+1E81): X=476,Y=702 (should be at cap-height 700?)
* - wgrave (U+1E81): X=394,Y=702 (should be at cap-height 700?)
* - wacute (U+1E83): X=570,Y=702 (should be at cap-height 700?)
* - wacute (U+1E83): X=652,Y=702 (should be at cap-height 700?)
* - ygrave (U+1EF3): X=356,Y=702 (should be at cap-height 700?)
* - ygrave (U+1EF3): X=274,Y=702 (should be at cap-height 700?)
* - i.ogonek.dotless: X=79,Y=2 (should be at baseline 0?)
* - i.ogonek.dotless: X=131,Y=-2 (should be at baseline 0?) [code: found-misalignments]
  
  

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
* AE (U+00C6): from (401.0, 700.0) to (567.0, 296.0) is colinear with segment from (567.0, 296.0) to (588.0, 244.0)
* AE (U+00C6): from (567.0, 296.0) to (588.0, 244.0) is colinear with segment from (588.0, 244.0) to (598.0, 220.0)
* Agrave (U+00C0): from (516.0, 700.0) to (736.0, 296.0) is colinear with segment from (736.0, 296.0) to (765.0, 244.0)
* Agrave (U+00C0): from (736.0, 296.0) to (765.0, 244.0) is colinear with segment from (765.0, 244.0) to (898.0, 0.0)
* Aacute (U+00C1): from (516.0, 700.0) to (736.0, 296.0) is colinear with segment from (736.0, 296.0) to (765.0, 244.0)
* Aacute (U+00C1): from (736.0, 296.0) to (765.0, 244.0) is colinear with segment from (765.0, 244.0) to (898.0, 0.0)
* Acircumflex (U+00C2): from (516.0, 700.0) to (736.0, 296.0) is colinear with segment from (736.0, 296.0) to (765.0, 244.0)
* Acircumflex (U+00C2): from (736.0, 296.0) to (765.0, 244.0) is colinear with segment from (765.0, 244.0) to (898.0, 0.0)
* Atilde (U+00C3): from (516.0, 700.0) to (736.0, 296.0) is colinear with segment from (736.0, 296.0) to (765.0, 244.0)
* Atilde (U+00C3): from (736.0, 296.0) to (765.0, 244.0) is colinear with segment from (765.0, 244.0) to (898.0, 0.0)
* Adieresis (U+00C4): from (516.0, 700.0) to (736.0, 296.0) is colinear with segment from (736.0, 296.0) to (765.0, 244.0)
* Adieresis (U+00C4): from (736.0, 296.0) to (765.0, 244.0) is colinear with segment from (765.0, 244.0) to (898.0, 0.0)
* Aring (U+00C5): from (516.0, 700.0) to (736.0, 296.0) is colinear with segment from (736.0, 296.0) to (765.0, 244.0)
* Aring (U+00C5): from (736.0, 296.0) to (765.0, 244.0) is colinear with segment from (765.0, 244.0) to (898.0, 0.0)
* Amacron (U+0100): from (516.0, 700.0) to (736.0, 296.0) is colinear with segment from (736.0, 296.0) to (765.0, 244.0)
* Amacron (U+0100): from (736.0, 296.0) to (765.0, 244.0) is colinear with segment from (765.0, 244.0) to (898.0, 0.0)
* Abreve (U+0102): from (516.0, 700.0) to (736.0, 296.0) is colinear with segment from (736.0, 296.0) to (765.0, 244.0)
* Abreve (U+0102): from (736.0, 296.0) to (765.0, 244.0) is colinear with segment from (765.0, 244.0) to (898.0, 0.0)
* Aogonek (U+0104): from (516.0, 700.0) to (736.0, 296.0) is colinear with segment from (736.0, 296.0) to (765.0, 244.0)
* Aogonek (U+0104): from (736.0, 296.0) to (765.0, 244.0) is colinear with segment from (765.0, 244.0) to (898.0, 0.0) [code: found-colinear-vectors]
  
  

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
* z (U+007A) contains a short segment Line(Line { p0: (59.0, 0.0), p1: (58.0, 2.0) }) (length: 2.24, total outline: 3733.76)
* z (U+007A) contains a short segment Line(Line { p0: (727.0, 530.0), p1: (728.0, 528.0) }) (length: 2.24, total outline: 3733.76)
* two (U+0032) contains a short segment Line(Line { p0: (161.0, 75.0), p1: (164.0, 60.0) }) (length: 15.30, total outline: 5043.61)
* two (U+0032) contains a short segment Line(Line { p0: (117.0, 582.0), p1: (117.0, 571.0) }) (length: 11.00, total outline: 5043.61)
* seven (U+0037) contains a short segment Line(Line { p0: (818.0, 651.0), p1: (800.0, 651.0) }) (length: 18.00, total outline: 3181.95)
* at (U+0040) contains a short segment Line(Line { p0: (536.0, 38.0), p1: (536.0, 0.0) }) (length: 38.00, total outline: 6922.68)
* at (U+0040) contains a short segment Line(Line { p0: (905.0, 107.0), p1: (886.0, 88.0) }) (length: 26.87, total outline: 6922.68)
* AE (U+00C6) contains a short segment Line(Line { p0: (606.0, 80.0), p1: (598.0, 88.0) }) (length: 11.31, total outline: 7550.30)
* AE (U+00C6) contains a short segment Line(Line { p0: (598.0, 88.0), p1: (598.0, 99.0) }) (length: 11.00, total outline: 7550.30)
* AE (U+00C6) contains a short segment Line(Line { p0: (588.0, 244.0), p1: (598.0, 220.0) }) (length: 26.00, total outline: 7550.30)
* eth (U+00F0) contains a short segment Line(Line { p0: (733.0, 437.0), p1: (738.0, 432.0) }) (length: 7.07, total outline: 3624.18)
* germandbls (U+00DF) contains a short segment Line(Line { p0: (115.0, 586.0), p1: (118.0, 586.0) }) (length: 3.00, total outline: 4836.37)
* germandbls (U+00DF) contains a short segment Line(Line { p0: (58.0, 586.0), p1: (61.0, 586.0) }) (length: 3.00, total outline: 4836.37)
* Eng (U+014A) contains a short segment Line(Line { p0: (819.0, 10.0), p1: (794.0, 10.0) }) (length: 25.00, total outline: 5559.39)
* Ccedilla (U+00C7) contains a short segment Line(Line { p0: (488.0, 0.0), p1: (488.0, -26.0) }) (length: 26.00, total outline: 5057.57)
* Aogonek (U+0104) contains a short segment Line(Line { p0: (836.0, 0.0), p1: (832.0, 0.0) }) (length: 4.00, total outline: 3425.65)
* Aogonek (U+0104) contains a short segment Line(Line { p0: (898.0, 0.0), p1: (888.0, 0.0) }) (length: 10.00, total outline: 3425.65)
* Aogonek (U+0104) contains a short segment Line(Line { p0: (888.0, 0.0), p1: (890.0, -2.0) }) (length: 2.83, total outline: 3425.65)
* aogonek (U+0105) contains a short segment Line(Line { p0: (738.0, 0.0), p1: (730.0, 0.0) }) (length: 8.00, total outline: 2932.26)
* aogonek (U+0105) contains a short segment Line(Line { p0: (730.0, 0.0), p1: (732.0, -2.0) }) (length: 2.83, total outline: 2932.26)
* Eogonek (U+0118) contains a short segment Line(Line { p0: (838.0, 0.0), p1: (830.0, 0.0) }) (length: 8.00, total outline: 6140.87)
* Eogonek (U+0118) contains a short segment Line(Line { p0: (830.0, 0.0), p1: (832.0, -2.0) }) (length: 2.83, total outline: 6140.87)
* eogonek (U+0119) contains a short segment Line(Line { p0: (643.0, 0.0), p1: (640.0, 0.0) }) (length: 3.00, total outline: 3954.23)
* eogonek (U+0119) contains a short segment Line(Line { p0: (640.0, 0.0), p1: (642.0, -2.0) }) (length: 2.83, total outline: 3954.23)
* gcircumflex (U+011D) contains a short segment Line(Line { p0: (738.0, 0.0), p1: (733.0, 0.0) }) (length: 5.00, total outline: 3620.60)
* gbreve (U+011F) contains a short segment Line(Line { p0: (738.0, 0.0), p1: (733.0, 0.0) }) (length: 5.00, total outline: 3620.60)
* gdotaccent (U+0121) contains a short segment Line(Line { p0: (738.0, 0.0), p1: (733.0, 0.0) }) (length: 5.00, total outline: 3620.60)
* uni0123 (U+0123) contains a short segment Line(Line { p0: (738.0, 0.0), p1: (733.0, 0.0) }) (length: 5.00, total outline: 3620.60)
* Iogonek (U+012E) contains a short segment Line(Line { p0: (418.0, 0.0), p1: (410.0, 0.0) }) (length: 8.00, total outline: 3335.56)
* Iogonek (U+012E) contains a short segment Line(Line { p0: (410.0, 0.0), p1: (412.0, -2.0) }) (length: 2.83, total outline: 3335.56)
* iogonek (U+012F) contains a short segment Line(Line { p0: (137.0, 0.0), p1: (129.0, 0.0) }) (length: 8.00, total outline: 1802.39)
* iogonek (U+012F) contains a short segment Line(Line { p0: (129.0, 0.0), p1: (131.0, -2.0) }) (length: 2.83, total outline: 1802.39)
* Scedilla (U+015E) contains a short segment Line(Line { p0: (498.0, -125.0), p1: (498.0, -94.0) }) (length: 31.00, total outline: 6204.14)
* Scedilla (U+015E) contains a short segment Line(Line { p0: (478.0, 0.0), p1: (478.0, -26.0) }) (length: 26.00, total outline: 6204.14)
* scedilla (U+015F) contains a short segment Line(Line { p0: (398.0, 0.0), p1: (398.0, -26.0) }) (length: 26.00, total outline: 4859.36)
* uni0162 (U+0162) contains a short segment Line(Line { p0: (458.0, 0.0), p1: (448.0, 0.0) }) (length: 10.00, total outline: 3744.27)
* uni0162 (U+0162) contains a short segment Line(Line { p0: (508.0, 0.0), p1: (498.0, 0.0) }) (length: 10.00, total outline: 3744.27)
* Uogonek (U+0172) contains a short segment Line(Line { p0: (791.0, 0.0), p1: (789.0, 0.0) }) (length: 2.00, total outline: 4798.26)
* Uogonek (U+0172) contains a short segment Line(Line { p0: (789.0, 0.0), p1: (791.0, -2.0) }) (length: 2.83, total outline: 4798.26)
* uogonek (U+0173) contains a short segment Line(Line { p0: (650.0, 0.0), p1: (647.0, 0.0) }) (length: 3.00, total outline: 3834.25)
* uogonek (U+0173) contains a short segment Line(Line { p0: (647.0, 0.0), p1: (649.0, -2.0) }) (length: 2.83, total outline: 3834.25)
* Wcircumflex (U+0174) contains a short segment Line(Line { p0: (342.0, 55.0), p1: (344.0, 55.0) }) (length: 2.00, total outline: 5974.72)
* Wcircumflex (U+0174) contains a short segment Line(Line { p0: (872.0, 55.0), p1: (874.0, 55.0) }) (length: 2.00, total outline: 5974.72)
* Wcircumflex (U+0174) contains a short segment Line(Line { p0: (609.0, 638.0), p1: (607.0, 638.0) }) (length: 2.00, total outline: 5974.72)
* zacute (U+017A) contains a short segment Line(Line { p0: (59.0, 0.0), p1: (58.0, 2.0) }) (length: 2.24, total outline: 3733.76)
* zacute (U+017A) contains a short segment Line(Line { p0: (727.0, 530.0), p1: (728.0, 528.0) }) (length: 2.24, total outline: 3733.76)
* zdotaccent (U+017C) contains a short segment Line(Line { p0: (59.0, 0.0), p1: (58.0, 2.0) }) (length: 2.24, total outline: 3733.76)
* zdotaccent (U+017C) contains a short segment Line(Line { p0: (727.0, 530.0), p1: (728.0, 528.0) }) (length: 2.24, total outline: 3733.76)
* zcaron (U+017E) contains a short segment Line(Line { p0: (59.0, 0.0), p1: (58.0, 2.0) }) (length: 2.24, total outline: 3733.76)
* zcaron (U+017E) contains a short segment Line(Line { p0: (727.0, 530.0), p1: (728.0, 528.0) }) (length: 2.24, total outline: 3733.76)
* yen (U+00A5) contains a short segment Line(Line { p0: (446.0, 264.0), p1: (446.0, 284.0) }) (length: 20.00, total outline: 4870.54)
* yen (U+00A5) contains a short segment Line(Line { p0: (510.0, 284.0), p1: (510.0, 264.0) }) (length: 20.00, total outline: 4870.54)
* section (U+00A7) contains a short segment Line(Line { p0: (64.0, 305.0), p1: (64.0, 306.0) }) (length: 1.00, total outline: 6138.91)
* section (U+00A7) contains a short segment Line(Line { p0: (572.0, 729.0), p1: (572.0, 702.0) }) (length: 27.00, total outline: 6138.91)
* section (U+00A7) contains a short segment Line(Line { p0: (578.0, 339.0), p1: (572.0, 334.0) }) (length: 7.81, total outline: 6138.91)
* section (U+00A7) contains a short segment Line(Line { p0: (572.0, 334.0), p1: (572.0, 333.0) }) (length: 1.00, total outline: 6138.91)
* section (U+00A7) contains a short segment Line(Line { p0: (64.0, -90.0), p1: (64.0, -63.0) }) (length: 27.00, total outline: 6138.91)
* section (U+00A7) contains a short segment Line(Line { p0: (58.0, 300.0), p1: (64.0, 305.0) }) (length: 7.81, total outline: 6138.91)
* uni00B2 (U+00B2) contains a short segment Line(Line { p0: (112.0, 370.0), p1: (114.0, 362.0) }) (length: 8.25, total outline: 2673.10)
* uni00B2 (U+00B2) contains a short segment Line(Line { p0: (90.0, 639.0), p1: (90.0, 633.0) }) (length: 6.00, total outline: 2673.10)
* onehalf (U+00BD) contains a short segment Line(Line { p0: (591.0, 35.0), p1: (593.0, 28.0) }) (length: 7.28, total outline: 2370.81)
* onehalf (U+00BD) contains a short segment Line(Line { p0: (571.0, 274.0), p1: (571.0, 268.0) }) (length: 6.00, total outline: 2370.81)
* Euro (U+20AC) contains a short segment Line(Line { p0: (-7.0, 256.0), p1: (-7.0, 289.0) }) (length: 33.00, total outline: 6335.90)
* Euro (U+20AC) contains a short segment Line(Line { p0: (-7.0, 421.0), p1: (-7.0, 455.0) }) (length: 34.00, total outline: 6335.90)
* Euro (U+20AC) contains a short segment Line(Line { p0: (623.0, 455.0), p1: (623.0, 421.0) }) (length: 34.00, total outline: 6335.90)
* Euro (U+20AC) contains a short segment Line(Line { p0: (580.0, 289.0), p1: (580.0, 256.0) }) (length: 33.00, total outline: 6335.90)
* Wgrave (U+1E80) contains a short segment Line(Line { p0: (342.0, 55.0), p1: (344.0, 55.0) }) (length: 2.00, total outline: 5974.72)
* Wgrave (U+1E80) contains a short segment Line(Line { p0: (872.0, 55.0), p1: (874.0, 55.0) }) (length: 2.00, total outline: 5974.72)
* Wgrave (U+1E80) contains a short segment Line(Line { p0: (609.0, 638.0), p1: (607.0, 638.0) }) (length: 2.00, total outline: 5974.72)
* Wacute (U+1E82) contains a short segment Line(Line { p0: (342.0, 55.0), p1: (344.0, 55.0) }) (length: 2.00, total outline: 5974.72)
* Wacute (U+1E82) contains a short segment Line(Line { p0: (872.0, 55.0), p1: (874.0, 55.0) }) (length: 2.00, total outline: 5974.72)
* Wacute (U+1E82) contains a short segment Line(Line { p0: (609.0, 638.0), p1: (607.0, 638.0) }) (length: 2.00, total outline: 5974.72)
* Wdieresis (U+1E84) contains a short segment Line(Line { p0: (342.0, 55.0), p1: (344.0, 55.0) }) (length: 2.00, total outline: 5974.72)
* Wdieresis (U+1E84) contains a short segment Line(Line { p0: (872.0, 55.0), p1: (874.0, 55.0) }) (length: 2.00, total outline: 5974.72)
* Wdieresis (U+1E84) contains a short segment Line(Line { p0: (609.0, 638.0), p1: (607.0, 638.0) }) (length: 2.00, total outline: 5974.72)
* uni1E9E (U+1E9E) contains a short segment Line(Line { p0: (58.0, 582.0), p1: (61.0, 582.0) }) (length: 3.00, total outline: 4824.52)
* uni1E9E (U+1E9E) contains a short segment Line(Line { p0: (115.0, 592.0), p1: (115.0, 582.0) }) (length: 10.00, total outline: 4824.52)
* uni1E9E (U+1E9E) contains a short segment Line(Line { p0: (115.0, 582.0), p1: (118.0, 582.0) }) (length: 3.00, total outline: 4824.52)
* i.ogonek.dotless contains a short segment Line(Line { p0: (137.0, 0.0), p1: (129.0, 0.0) }) (length: 8.00, total outline: 1802.39)
* i.ogonek.dotless contains a short segment Line(Line { p0: (129.0, 0.0), p1: (131.0, -2.0) }) (length: 2.83, total outline: 1802.39)
* two.tf contains a short segment Line(Line { p0: (161.0, 75.0), p1: (164.0, 60.0) }) (length: 15.30, total outline: 5043.61)
* two.tf contains a short segment Line(Line { p0: (117.0, 582.0), p1: (117.0, 571.0) }) (length: 11.00, total outline: 5043.61)
* seven.tf contains a short segment Line(Line { p0: (818.0, 651.0), p1: (800.0, 651.0) }) (length: 18.00, total outline: 3181.95) [code: found-short-segments]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table
set to optimize rendering? (googlefonts/gasp)</summary>
    <div>


> Traditionally version 0 'gasp' tables were set so that font sizes below 8 ppem had no grid fitting but did have antialiasing. From 9-16 ppem, just grid fitting. And fonts above 17ppem had both antialiasing and grid fitting toggled on. The use of accelerated graphics cards and higher resolution screens make this approach obsolete. Microsoft's DirectWrite pushed this even further with much improved rendering built into the OS and apps.
> 
> In this scenario it makes sense to simply toggle all 4 flags ON for all font sizes.




Original proposal: [https://github.com/fonttools/fontbakery/issues/4829]




  


- ⚠️ **WARN** The gasp range 0xFFFF value 0x0A should be set to 0x0F [code: unset-flags]
  
  

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


<details><summary>[9] /workspace/scratch/cbc03b9be171/xuqu-googlefonts-prep/build/googlefonts/ofl/xuqu/Xuqu-Regular.ttf</summary>
<div>


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
width=746: greaterequal, lessequal, greater, less [code: width-outliers]
  
  

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
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. (googlefonts/glyphsets/shape_languages)</summary>
    <div>


> This check uses a heuristic to determine which GF glyphsets a font supports. Then it checks the font for correct shaping behaviour for all languages in those glyphsets.




Original proposal: [https://github.com/googlefonts/fontbakery/issues/4147]





- ⚠️ **WARN** Warning language shaping:

| Message                                                           | Languages                    |
|-------------------------------------------------------------------|------------------------------|
| Auxiliary orthography codepoints:                                 | * da_Latn (Danish)           |
|   The following auxiliary characters are missing from the font: Ǿ |                              |
|   The following auxiliary characters are missing from the font: ǿ |                              |
| Auxiliary orthography codepoints:                                 | * nb_Latn (Norwegian Bokmål) |
|   The following auxiliary characters are missing from the font: Ǎ |                              |
|   The following auxiliary characters are missing from the font: ǎ |                              |
| Auxiliary orthography codepoints:                                 | * lt_Latn (Lithuanian)       |
|   The following auxiliary characters are missing from the font: Ẽ |                              |
|   The following auxiliary characters are missing from the font: ẽ |                              |
| Auxiliary orthography codepoints:                                 | * en_Latn (English)          |
|   The following auxiliary characters are missing from the font: ʻ |                              |
| Auxiliary orthography codepoints:                                 | * fr_Latn (French)           |
|   The following auxiliary characters are missing from the font: Ǔ |                              |
|   The following auxiliary characters are missing from the font: ǔ |                              |
| Auxiliary orthography codepoints:                                 | * fi_Latn (Finnish)          |
|   The following auxiliary characters are missing from the font: Ǧ |                              |
|   The following auxiliary characters are missing from the font: Ǥ |                              |
|   The following auxiliary characters are missing from the font: Ȟ |                              |
|   The following auxiliary characters are missing from the font: Ǩ |                              |
|   The following auxiliary characters are missing from the font: Ʒ |                              |
|   The following auxiliary characters are missing from the font: Ǯ |                              |
|   The following auxiliary characters are missing from the font: ǧ |                              |
|   The following auxiliary characters are missing from the font: ǥ |                              |
|   The following auxiliary characters are missing from the font: ȟ |                              |
|   The following auxiliary characters are missing from the font: ǩ |                              |
|   The following auxiliary characters are missing from the font: ʒ |                              |
|   The following auxiliary characters are missing from the font: ǯ |                              | [code: warning-language-shaping]
  
  

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
* - ordfeminine (U+00AA): X=432,Y=702 (should be at cap-height 700?)
* - ordfeminine (U+00AA): X=110,Y=702 (should be at cap-height 700?)
* - ordmasculine (U+00BA): X=110,Y=702 (should be at cap-height 700?)
* - ordmasculine (U+00BA): X=380,Y=702 (should be at cap-height 700?)
* - uni00B9 (U+00B9): X=244,Y=701 (should be at cap-height 700?)
* - uni00B9 (U+00B9): X=296,Y=701 (should be at cap-height 700?)
* - uni00B2 (U+00B2): X=114,Y=701 (should be at cap-height 700?)
* - uni00B2 (U+00B2): X=402,Y=701 (should be at cap-height 700?)
* - uni00B3 (U+00B3): X=58,Y=701 (should be at cap-height 700?)
* - uni00B3 (U+00B3): X=400,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=530,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=866,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=913,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=483,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=58,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=419,Y=701 (should be at cap-height 700?)
* - breve (U+02D8): X=434,Y=701 (should be at cap-height 700?)
* - breve (U+02D8): X=58,Y=701 (should be at cap-height 700?) [code: found-misalignments]
  
  

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

* K (U+004B) contains a short segment Line(Line { p0: (208.0, 395.0), p1: (226.0, 384.0) }) (length: 21.10, total outline: 4564.46)
* k (U+006B) contains a short segment Line(Line { p0: (173.0, 226.0), p1: (158.0, 230.0) }) (length: 15.52, total outline: 3843.54)
* k (U+006B) contains a short segment Line(Line { p0: (223.0, 305.0), p1: (232.0, 300.0) }) (length: 10.30, total outline: 3843.54)
* r (U+0072) contains a short segment Line(Line { p0: (158.0, 530.0), p1: (158.0, 529.0) }) (length: 1.00, total outline: 1990.56)
* r (U+0072) contains a short segment Line(Line { p0: (158.0, 529.0), p1: (160.0, 530.0) }) (length: 2.24, total outline: 1990.56)
* s (U+0073) contains a short segment Line(Line { p0: (148.0, 386.0), p1: (148.0, 369.0) }) (length: 17.00, total outline: 4121.38)
* s (U+0073) contains a short segment Line(Line { p0: (608.0, 144.0), p1: (608.0, 161.0) }) (length: 17.00, total outline: 4121.38)
* two (U+0032) contains a short segment Line(Line { p0: (158.0, 558.0), p1: (158.0, 535.0) }) (length: 23.00, total outline: 4853.80)
* at (U+0040) contains a short segment Line(Line { p0: (998.0, 105.0), p1: (993.0, 100.0) }) (length: 7.07, total outline: 6713.52)
* at (U+0040) contains a short segment Line(Line { p0: (896.0, 100.0), p1: (879.0, 82.0) }) (length: 24.76, total outline: 6713.52)
* AE (U+00C6) contains a short segment Line(Line { p0: (693.0, 0.0), p1: (685.0, 8.0) }) (length: 11.31, total outline: 7397.26)
* AE (U+00C6) contains a short segment Line(Line { p0: (685.0, 8.0), p1: (688.0, 0.0) }) (length: 8.54, total outline: 7397.26)
* eth (U+00F0) contains a short segment Line(Line { p0: (732.0, 441.0), p1: (738.0, 435.0) }) (length: 8.49, total outline: 3475.29)
* germandbls (U+00DF) contains a short segment Line(Line { p0: (58.0, 595.0), p1: (60.0, 595.0) }) (length: 2.00, total outline: 4705.68)
* germandbls (U+00DF) contains a short segment Line(Line { p0: (156.0, 600.0), p1: (156.0, 595.0) }) (length: 5.00, total outline: 4705.68)
* germandbls (U+00DF) contains a short segment Line(Line { p0: (156.0, 595.0), p1: (158.0, 595.0) }) (length: 2.00, total outline: 4705.68)
* Eng (U+014A) contains a short segment Line(Line { p0: (778.0, 0.0), p1: (768.0, 0.0) }) (length: 10.00, total outline: 5381.49)
* kgreenlandic (U+0138) contains a short segment Line(Line { p0: (182.0, 299.0), p1: (198.0, 291.0) }) (length: 17.89, total outline: 3640.15)
* Ccedilla (U+00C7) contains a short segment Line(Line { p0: (496.0, -119.0), p1: (496.0, -100.0) }) (length: 19.00, total outline: 4988.11)
* Ccedilla (U+00C7) contains a short segment Line(Line { p0: (500.0, 0.0), p1: (500.0, -20.0) }) (length: 20.00, total outline: 4988.11)
* ccedilla (U+00E7) contains a short segment Line(Line { p0: (420.0, -119.0), p1: (420.0, -100.0) }) (length: 19.00, total outline: 4046.11)
* ccedilla (U+00E7) contains a short segment Line(Line { p0: (426.0, 0.0), p1: (426.0, -20.0) }) (length: 20.00, total outline: 4046.11)
* Aogonek (U+0104) contains a short segment Line(Line { p0: (875.0, 0.0), p1: (886.0, -11.0) }) (length: 15.56, total outline: 3450.84)
* aogonek (U+0105) contains a short segment Line(Line { p0: (718.0, 0.0), p1: (729.0, -11.0) }) (length: 15.56, total outline: 2943.66)
* Eogonek (U+0118) contains a short segment Line(Line { p0: (838.0, 0.0), p1: (818.0, 0.0) }) (length: 20.00, total outline: 6006.80)
* Eogonek (U+0118) contains a short segment Line(Line { p0: (818.0, 0.0), p1: (829.0, -11.0) }) (length: 15.56, total outline: 6006.80)
* Eogonek (U+0118) contains a short segment Line(Line { p0: (768.0, -73.0), p1: (768.0, -107.0) }) (length: 34.00, total outline: 6006.80)
* eogonek (U+0119) contains a short segment Line(Line { p0: (738.0, 0.0), p1: (718.0, 0.0) }) (length: 20.00, total outline: 4080.23)
* eogonek (U+0119) contains a short segment Line(Line { p0: (718.0, 0.0), p1: (729.0, -11.0) }) (length: 15.56, total outline: 4080.23)
* Iogonek (U+012E) contains a short segment Line(Line { p0: (398.0, 0.0), p1: (409.0, -11.0) }) (length: 15.56, total outline: 3274.96)
* iogonek (U+012F) contains a short segment Line(Line { p0: (69.0, 0.0), p1: (58.0, 0.0) }) (length: 11.00, total outline: 1894.96)
* uni0136 (U+0136) contains a short segment Line(Line { p0: (208.0, 395.0), p1: (226.0, 384.0) }) (length: 21.10, total outline: 4564.46)
* uni0137 (U+0137) contains a short segment Line(Line { p0: (173.0, 226.0), p1: (158.0, 230.0) }) (length: 15.52, total outline: 3843.54)
* uni0137 (U+0137) contains a short segment Line(Line { p0: (223.0, 305.0), p1: (232.0, 300.0) }) (length: 10.30, total outline: 3843.54)
* racute (U+0155) contains a short segment Line(Line { p0: (158.0, 530.0), p1: (158.0, 529.0) }) (length: 1.00, total outline: 1990.56)
* racute (U+0155) contains a short segment Line(Line { p0: (158.0, 529.0), p1: (160.0, 530.0) }) (length: 2.24, total outline: 1990.56)
* uni0157 (U+0157) contains a short segment Line(Line { p0: (158.0, 530.0), p1: (158.0, 529.0) }) (length: 1.00, total outline: 1990.56)
* uni0157 (U+0157) contains a short segment Line(Line { p0: (158.0, 529.0), p1: (160.0, 530.0) }) (length: 2.24, total outline: 1990.56)
* rcaron (U+0159) contains a short segment Line(Line { p0: (158.0, 530.0), p1: (158.0, 529.0) }) (length: 1.00, total outline: 1990.56)
* rcaron (U+0159) contains a short segment Line(Line { p0: (158.0, 529.0), p1: (160.0, 530.0) }) (length: 2.24, total outline: 1990.56)
* sacute (U+015B) contains a short segment Line(Line { p0: (608.0, 144.0), p1: (608.0, 161.0) }) (length: 17.00, total outline: 4121.38)
* sacute (U+015B) contains a short segment Line(Line { p0: (148.0, 386.0), p1: (148.0, 369.0) }) (length: 17.00, total outline: 4121.38)
* scircumflex (U+015D) contains a short segment Line(Line { p0: (608.0, 144.0), p1: (608.0, 161.0) }) (length: 17.00, total outline: 4121.38)
* scircumflex (U+015D) contains a short segment Line(Line { p0: (148.0, 386.0), p1: (148.0, 369.0) }) (length: 17.00, total outline: 4121.38)
* Scedilla (U+015E) contains a short segment Line(Line { p0: (486.0, -119.0), p1: (486.0, -100.0) }) (length: 19.00, total outline: 6065.44)
* Scedilla (U+015E) contains a short segment Line(Line { p0: (490.0, 0.0), p1: (490.0, -20.0) }) (length: 20.00, total outline: 6065.44)
* scedilla (U+015F) contains a short segment Line(Line { p0: (406.0, -119.0), p1: (406.0, -100.0) }) (length: 19.00, total outline: 4787.65)
* scedilla (U+015F) contains a short segment Line(Line { p0: (608.0, 144.0), p1: (608.0, 161.0) }) (length: 17.00, total outline: 4787.65)
* scedilla (U+015F) contains a short segment Line(Line { p0: (148.0, 386.0), p1: (148.0, 369.0) }) (length: 17.00, total outline: 4787.65)
* scedilla (U+015F) contains a short segment Line(Line { p0: (410.0, 0.0), p1: (410.0, -20.0) }) (length: 20.00, total outline: 4787.65)
* scaron (U+0161) contains a short segment Line(Line { p0: (608.0, 144.0), p1: (608.0, 161.0) }) (length: 17.00, total outline: 4121.38)
* scaron (U+0161) contains a short segment Line(Line { p0: (148.0, 386.0), p1: (148.0, 369.0) }) (length: 17.00, total outline: 4121.38)
* uni0162 (U+0162) contains a short segment Line(Line { p0: (506.0, -119.0), p1: (506.0, -100.0) }) (length: 19.00, total outline: 3746.27)
* uni0162 (U+0162) contains a short segment Line(Line { p0: (446.0, 0.0), p1: (428.0, 0.0) }) (length: 18.00, total outline: 3746.27)
* uni0162 (U+0162) contains a short segment Line(Line { p0: (528.0, 0.0), p1: (510.0, 0.0) }) (length: 18.00, total outline: 3746.27)
* uni0162 (U+0162) contains a short segment Line(Line { p0: (510.0, 0.0), p1: (510.0, -20.0) }) (length: 20.00, total outline: 3746.27)
* uni0163 (U+0163) contains a short segment Line(Line { p0: (343.0, -119.0), p1: (343.0, -100.0) }) (length: 19.00, total outline: 3495.19)
* uni0163 (U+0163) contains a short segment Line(Line { p0: (348.0, 0.0), p1: (348.0, -20.0) }) (length: 20.00, total outline: 3495.19)
* Uogonek (U+0172) contains a short segment Line(Line { p0: (783.0, 0.0), p1: (768.0, 0.0) }) (length: 15.00, total outline: 4736.80)
* Uogonek (U+0172) contains a short segment Line(Line { p0: (768.0, 0.0), p1: (779.0, -11.0) }) (length: 15.56, total outline: 4736.80)
* uogonek (U+0173) contains a short segment Line(Line { p0: (643.0, 0.0), p1: (628.0, 0.0) }) (length: 15.00, total outline: 3776.80)
* uogonek (U+0173) contains a short segment Line(Line { p0: (628.0, 0.0), p1: (639.0, -11.0) }) (length: 15.56, total outline: 3776.80)
* currency (U+00A4) contains a short segment Line(Line { p0: (161.0, 167.0), p1: (158.0, 170.0) }) (length: 4.24, total outline: 2644.51)
* currency (U+00A4) contains a short segment Line(Line { p0: (158.0, 520.0), p1: (161.0, 523.0) }) (length: 4.24, total outline: 2644.51)
* currency (U+00A4) contains a short segment Line(Line { p0: (215.0, 577.0), p1: (218.0, 580.0) }) (length: 4.24, total outline: 2644.51)
* currency (U+00A4) contains a short segment Line(Line { p0: (568.0, 580.0), p1: (571.0, 577.0) }) (length: 4.24, total outline: 2644.51)
* currency (U+00A4) contains a short segment Line(Line { p0: (625.0, 523.0), p1: (628.0, 520.0) }) (length: 4.24, total outline: 2644.51)
* currency (U+00A4) contains a short segment Line(Line { p0: (628.0, 170.0), p1: (625.0, 167.0) }) (length: 4.24, total outline: 2644.51)
* currency (U+00A4) contains a short segment Line(Line { p0: (571.0, 113.0), p1: (568.0, 110.0) }) (length: 4.24, total outline: 2644.51)
* currency (U+00A4) contains a short segment Line(Line { p0: (218.0, 110.0), p1: (215.0, 113.0) }) (length: 4.24, total outline: 2644.51)
* section (U+00A7) contains a short segment Line(Line { p0: (58.0, 309.0), p1: (63.0, 314.0) }) (length: 7.07, total outline: 5860.52)
* section (U+00A7) contains a short segment Line(Line { p0: (63.0, 314.0), p1: (63.0, 327.0) }) (length: 13.00, total outline: 5860.52)
* section (U+00A7) contains a short segment Line(Line { p0: (63.0, 327.0), p1: (75.0, 327.0) }) (length: 12.00, total outline: 5860.52)
* section (U+00A7) contains a short segment Line(Line { p0: (578.0, 330.0), p1: (573.0, 325.0) }) (length: 7.07, total outline: 5860.52)
* section (U+00A7) contains a short segment Line(Line { p0: (573.0, 325.0), p1: (573.0, 312.0) }) (length: 13.00, total outline: 5860.52)
* section (U+00A7) contains a short segment Line(Line { p0: (573.0, 312.0), p1: (561.0, 312.0) }) (length: 12.00, total outline: 5860.52)
* uni00B2 (U+00B2) contains a short segment Line(Line { p0: (111.0, 626.0), p1: (111.0, 614.0) }) (length: 12.00, total outline: 2571.90)
* paragraph (U+00B6) contains a short segment Line(Line { p0: (578.0, 700.0), p1: (588.0, 690.0) }) (length: 14.14, total outline: 4668.28)
* paragraph (U+00B6) contains a short segment Line(Line { p0: (588.0, 690.0), p1: (588.0, 700.0) }) (length: 10.00, total outline: 4668.28)
* paragraph (U+00B6) contains a short segment Line(Line { p0: (588.0, 290.0), p1: (578.0, 280.0) }) (length: 14.14, total outline: 4668.28)
* onehalf (U+00BD) contains a short segment Line(Line { p0: (590.0, 262.0), p1: (590.0, 251.0) }) (length: 11.00, total outline: 2281.13)
* uni0219 (U+0219) contains a short segment Line(Line { p0: (608.0, 144.0), p1: (608.0, 161.0) }) (length: 17.00, total outline: 4121.38)
* uni0219 (U+0219) contains a short segment Line(Line { p0: (148.0, 386.0), p1: (148.0, 369.0) }) (length: 17.00, total outline: 4121.38)
* uni1E9E (U+1E9E) contains a short segment Line(Line { p0: (58.0, 584.0), p1: (63.0, 584.0) }) (length: 5.00, total outline: 4724.13)
* uni1E9E (U+1E9E) contains a short segment Line(Line { p0: (153.0, 586.0), p1: (153.0, 584.0) }) (length: 2.00, total outline: 4724.13)
* uni1E9E (U+1E9E) contains a short segment Line(Line { p0: (153.0, 584.0), p1: (158.0, 584.0) }) (length: 5.00, total outline: 4724.13)
* i.ogonek.dotless contains a short segment Line(Line { p0: (69.0, 0.0), p1: (58.0, 0.0) }) (length: 11.00, total outline: 1894.96)
* two.tf contains a short segment Line(Line { p0: (158.0, 558.0), p1: (158.0, 535.0) }) (length: 23.00, total outline: 4853.80) [code: found-short-segments]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table
set to optimize rendering? (googlefonts/gasp)</summary>
    <div>


> Traditionally version 0 'gasp' tables were set so that font sizes below 8 ppem had no grid fitting but did have antialiasing. From 9-16 ppem, just grid fitting. And fonts above 17ppem had both antialiasing and grid fitting toggled on. The use of accelerated graphics cards and higher resolution screens make this approach obsolete. Microsoft's DirectWrite pushed this even further with much improved rendering built into the OS and apps.
> 
> In this scenario it makes sense to simply toggle all 4 flags ON for all font sizes.




Original proposal: [https://github.com/fonttools/fontbakery/issues/4829]




  


- ⚠️ **WARN** The gasp range 0xFFFF value 0x0A should be set to 0x0F [code: unset-flags]
  
  

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


<details><summary>[1] /workspace/scratch/cbc03b9be171/xuqu-googlefonts-prep/build/googlefonts/ofl/xuqu</summary>
<div>


<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. (googlefonts/metadata/unreachable_subsetting)</summary>
    <div>


> This check ensures that all encoded glyphs in the font are covered by a subset declared in the METADATA.pb. Google Fonts splits the font into a set of subset fonts based on the contents of the `subsets` field and the subset definitions in the `glyphsets` repository.
> 
> Any encoded glyphs which are not by any of these subset definitions will not be served in the subsetted fonts, and so will be unreachable to the end user.




Original proposal: [https://github.com/fonttools/fontbakery/issues/4097 and https://github.com/fonttools/fontbakery/pull/4273]





- ⚠️ **WARN** /workspace/scratch/cbc03b9be171/xuqu-googlefonts-prep/build/googlefonts/ofl/xuqu/Xuqu-Bold.ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+02D8 BREVE: try adding one of: yi, canadian-aboriginal
* U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi
* U+02DB OGONEK: try adding one of: yi, canadian-aboriginal
* U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, tifinagh, math, cherokee
* U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic
* U+0307 COMBINING DOT ABOVE: try adding one of: canadian-aboriginal, math, tifinagh, duployan, malayalam, coptic, old-permic, syriac, hebrew, todhri, tai-le
* U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan
* U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee
* U+030C COMBINING CARON: try adding one of: tai-le, cherokee
* U+0326 COMBINING COMMA BELOW: try adding math
* U+0327 COMBINING CEDILLA: try adding math
* U+2003 EM SPACE: try adding nushu
* U+200C ZERO WIDTH NON-JOINER: try adding one of: lepcha, kharoshthi, hatran, masaram-gondi, buhid, new-tai-lue, sinhala, malayalam, gunjala-gondi, limbu, tai-viet, mongolian, bhaiksuki, khmer, cham, tai-le, tibetan, sogdian, brahmi, modi, tagalog, thaana, newa, arabic, pahawh-hmong, balinese, manichaean, kayah-li, dogra, myanmar, avestan, batak, hanifi-rohingya, kaithi, duployan, kannada, mahajani, bengali, mandaic, phags-pa, sharada, tagbanwa, rejang, syriac, grantha, gurmukhi, khudawadi, khojki, warang-citi, yi, hanunoo, telugu, zanabazar-square, saurashtra, tai-tham, thai, sundanese, chakma, gujarati, meetei-mayek, tamil, syloti-nagri, buginese, takri, hebrew, oriya, siddham, tifinagh, devanagari, javanese, psalter-pahlavi, tirhuta, nko, lao
* U+200D ZERO WIDTH JOINER: try adding one of: lepcha, rejang, new-tai-lue, khmer, bengali, batak, hanunoo, mahajani, saurashtra, oriya, tagalog, tai-tham, takri, kaithi, thai, hebrew, grantha, telugu, cham, warang-citi, khojki, sogdian, tifinagh, duployan, kharoshthi, zanabazar-square, tamil, yi, devanagari, balinese, manichaean, meetei-mayek, tagbanwa, gunjala-gondi, myanmar, phags-pa, tai-viet, arabic, limbu, mongolian, dogra, kannada, brahmi, bhaiksuki, hanifi-rohingya, masaram-gondi, pahawh-hmong, thaana, tai-le, mandaic, modi, javanese, syloti-nagri, sundanese, khudawadi, chakma, kayah-li, malayalam, psalter-pahlavi, sharada, siddham, avestan, newa, buginese, gurmukhi, syriac, tibetan, nko, buhid, old-hungarian, sinhala, tirhuta, gujarati, lao
* U+2010 HYPHEN: try adding one of: coptic, lisu, armenian, cham, kharoshthi, sundanese, syloti-nagri, sora-sompeng, arabic, yi, hebrew, kayah-li, kaithi
* U+2011 NON-BREAKING HYPHEN: try adding one of: syloti-nagri, yi, arabic
* U+2021 DOUBLE DAGGER: try adding adlam
* U+202F NARROW NO-BREAK SPACE: try adding one of: phags-pa, yi, mongolian
* U+2030 PER MILLE SIGN: try adding adlam
* U+2190 LEFTWARDS ARROW: try adding one of: math, symbols
* U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols
* U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols
* U+221A SQUARE ROOT: try adding math
* U+221E INFINITY: try adding math
* U+2260 NOT EQUAL TO: try adding math
* U+2264 LESS-THAN OR EQUAL TO: try adding math
* U+2265 GREATER-THAN OR EQUAL TO: try adding math
* U+25CC DOTTED CIRCLE: try adding one of: phags-pa, miao, old-permic, canadian-aboriginal, new-tai-lue, khojki, wancho, cham, gujarati, lepcha, mende-kikakui, coptic, chakma, symbols, takri, telugu, kannada, buhid, balinese, mahajani, kaithi, zanabazar-square, osage, modi, ahom, hebrew, sinhala, sharada, armenian, math, bassa-vah, siddham, tirhuta, psalter-pahlavi, buginese, music, tagalog, adlam, hanifi-rohingya, tai-viet, marchen, bhaiksuki, javanese, oriya, khmer, masaram-gondi, tamil, thai, warang-citi, kayah-li, saurashtra, sogdian, khudawadi, hanunoo, nko, malayalam, rejang, kharoshthi, mandaic, meetei-mayek, myanmar, tibetan, gurmukhi, brahmi, tai-le, yi, mongolian, pahawh-hmong, soyombo, grantha, manichaean, tifinagh, dogra, gunjala-gondi, elbasan, syloti-nagri, limbu, lao, tagbanwa, thaana, newa, tai-tham, duployan, sundanese, batak, devanagari, syriac, bengali, caucasian-albanian

Or you can add the above codepoints to one of the subsets supported by the font: latin-ext, latin [code: unreachable-subsetting]
  
  


- ⚠️ **WARN** /workspace/scratch/cbc03b9be171/xuqu-googlefonts-prep/build/googlefonts/ofl/xuqu/Xuqu-ExtraBold.ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+02D8 BREVE: try adding one of: yi, canadian-aboriginal
* U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi
* U+02DB OGONEK: try adding one of: yi, canadian-aboriginal
* U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, tifinagh, math, cherokee
* U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic
* U+0307 COMBINING DOT ABOVE: try adding one of: canadian-aboriginal, math, tifinagh, duployan, malayalam, coptic, old-permic, syriac, hebrew, todhri, tai-le
* U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan
* U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee
* U+030C COMBINING CARON: try adding one of: tai-le, cherokee
* U+0326 COMBINING COMMA BELOW: try adding math
* U+0327 COMBINING CEDILLA: try adding math
* U+2003 EM SPACE: try adding nushu
* U+200C ZERO WIDTH NON-JOINER: try adding one of: lepcha, kharoshthi, hatran, masaram-gondi, buhid, new-tai-lue, sinhala, malayalam, gunjala-gondi, limbu, tai-viet, mongolian, bhaiksuki, khmer, cham, tai-le, tibetan, sogdian, brahmi, modi, tagalog, thaana, newa, arabic, pahawh-hmong, balinese, manichaean, kayah-li, dogra, myanmar, avestan, batak, hanifi-rohingya, kaithi, duployan, kannada, mahajani, bengali, mandaic, phags-pa, sharada, tagbanwa, rejang, syriac, grantha, gurmukhi, khudawadi, khojki, warang-citi, yi, hanunoo, telugu, zanabazar-square, saurashtra, tai-tham, thai, sundanese, chakma, gujarati, meetei-mayek, tamil, syloti-nagri, buginese, takri, hebrew, oriya, siddham, tifinagh, devanagari, javanese, psalter-pahlavi, tirhuta, nko, lao
* U+200D ZERO WIDTH JOINER: try adding one of: lepcha, rejang, new-tai-lue, khmer, bengali, batak, hanunoo, mahajani, saurashtra, oriya, tagalog, tai-tham, takri, kaithi, thai, hebrew, grantha, telugu, cham, warang-citi, khojki, sogdian, tifinagh, duployan, kharoshthi, zanabazar-square, tamil, yi, devanagari, balinese, manichaean, meetei-mayek, tagbanwa, gunjala-gondi, myanmar, phags-pa, tai-viet, arabic, limbu, mongolian, dogra, kannada, brahmi, bhaiksuki, hanifi-rohingya, masaram-gondi, pahawh-hmong, thaana, tai-le, mandaic, modi, javanese, syloti-nagri, sundanese, khudawadi, chakma, kayah-li, malayalam, psalter-pahlavi, sharada, siddham, avestan, newa, buginese, gurmukhi, syriac, tibetan, nko, buhid, old-hungarian, sinhala, tirhuta, gujarati, lao
* U+2010 HYPHEN: try adding one of: coptic, lisu, armenian, cham, kharoshthi, sundanese, syloti-nagri, sora-sompeng, arabic, yi, hebrew, kayah-li, kaithi
* U+2011 NON-BREAKING HYPHEN: try adding one of: syloti-nagri, yi, arabic
* U+2021 DOUBLE DAGGER: try adding adlam
* U+202F NARROW NO-BREAK SPACE: try adding one of: phags-pa, yi, mongolian
* U+2030 PER MILLE SIGN: try adding adlam
* U+2190 LEFTWARDS ARROW: try adding one of: math, symbols
* U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols
* U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols
* U+221A SQUARE ROOT: try adding math
* U+221E INFINITY: try adding math
* U+2260 NOT EQUAL TO: try adding math
* U+2264 LESS-THAN OR EQUAL TO: try adding math
* U+2265 GREATER-THAN OR EQUAL TO: try adding math
* U+25CC DOTTED CIRCLE: try adding one of: phags-pa, miao, old-permic, canadian-aboriginal, new-tai-lue, khojki, wancho, cham, gujarati, lepcha, mende-kikakui, coptic, chakma, symbols, takri, telugu, kannada, buhid, balinese, mahajani, kaithi, zanabazar-square, osage, modi, ahom, hebrew, sinhala, sharada, armenian, math, bassa-vah, siddham, tirhuta, psalter-pahlavi, buginese, music, tagalog, adlam, hanifi-rohingya, tai-viet, marchen, bhaiksuki, javanese, oriya, khmer, masaram-gondi, tamil, thai, warang-citi, kayah-li, saurashtra, sogdian, khudawadi, hanunoo, nko, malayalam, rejang, kharoshthi, mandaic, meetei-mayek, myanmar, tibetan, gurmukhi, brahmi, tai-le, yi, mongolian, pahawh-hmong, soyombo, grantha, manichaean, tifinagh, dogra, gunjala-gondi, elbasan, syloti-nagri, limbu, lao, tagbanwa, thaana, newa, tai-tham, duployan, sundanese, batak, devanagari, syriac, bengali, caucasian-albanian

Or you can add the above codepoints to one of the subsets supported by the font: latin-ext, latin [code: unreachable-subsetting]
  
  


- ⚠️ **WARN** /workspace/scratch/cbc03b9be171/xuqu-googlefonts-prep/build/googlefonts/ofl/xuqu/Xuqu-Light.ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+02D8 BREVE: try adding one of: yi, canadian-aboriginal
* U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi
* U+02DB OGONEK: try adding one of: yi, canadian-aboriginal
* U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, tifinagh, math, cherokee
* U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic
* U+0307 COMBINING DOT ABOVE: try adding one of: canadian-aboriginal, math, tifinagh, duployan, malayalam, coptic, old-permic, syriac, hebrew, todhri, tai-le
* U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan
* U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee
* U+030C COMBINING CARON: try adding one of: tai-le, cherokee
* U+0326 COMBINING COMMA BELOW: try adding math
* U+0327 COMBINING CEDILLA: try adding math
* U+2003 EM SPACE: try adding nushu
* U+200C ZERO WIDTH NON-JOINER: try adding one of: lepcha, kharoshthi, hatran, masaram-gondi, buhid, new-tai-lue, sinhala, malayalam, gunjala-gondi, limbu, tai-viet, mongolian, bhaiksuki, khmer, cham, tai-le, tibetan, sogdian, brahmi, modi, tagalog, thaana, newa, arabic, pahawh-hmong, balinese, manichaean, kayah-li, dogra, myanmar, avestan, batak, hanifi-rohingya, kaithi, duployan, kannada, mahajani, bengali, mandaic, phags-pa, sharada, tagbanwa, rejang, syriac, grantha, gurmukhi, khudawadi, khojki, warang-citi, yi, hanunoo, telugu, zanabazar-square, saurashtra, tai-tham, thai, sundanese, chakma, gujarati, meetei-mayek, tamil, syloti-nagri, buginese, takri, hebrew, oriya, siddham, tifinagh, devanagari, javanese, psalter-pahlavi, tirhuta, nko, lao
* U+200D ZERO WIDTH JOINER: try adding one of: lepcha, rejang, new-tai-lue, khmer, bengali, batak, hanunoo, mahajani, saurashtra, oriya, tagalog, tai-tham, takri, kaithi, thai, hebrew, grantha, telugu, cham, warang-citi, khojki, sogdian, tifinagh, duployan, kharoshthi, zanabazar-square, tamil, yi, devanagari, balinese, manichaean, meetei-mayek, tagbanwa, gunjala-gondi, myanmar, phags-pa, tai-viet, arabic, limbu, mongolian, dogra, kannada, brahmi, bhaiksuki, hanifi-rohingya, masaram-gondi, pahawh-hmong, thaana, tai-le, mandaic, modi, javanese, syloti-nagri, sundanese, khudawadi, chakma, kayah-li, malayalam, psalter-pahlavi, sharada, siddham, avestan, newa, buginese, gurmukhi, syriac, tibetan, nko, buhid, old-hungarian, sinhala, tirhuta, gujarati, lao
* U+2010 HYPHEN: try adding one of: coptic, lisu, armenian, cham, kharoshthi, sundanese, syloti-nagri, sora-sompeng, arabic, yi, hebrew, kayah-li, kaithi
* U+2011 NON-BREAKING HYPHEN: try adding one of: syloti-nagri, yi, arabic
* U+2021 DOUBLE DAGGER: try adding adlam
* U+202F NARROW NO-BREAK SPACE: try adding one of: phags-pa, yi, mongolian
* U+2030 PER MILLE SIGN: try adding adlam
* U+2190 LEFTWARDS ARROW: try adding one of: math, symbols
* U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols
* U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols
* U+221A SQUARE ROOT: try adding math
* U+221E INFINITY: try adding math
* U+2260 NOT EQUAL TO: try adding math
* U+2264 LESS-THAN OR EQUAL TO: try adding math
* U+2265 GREATER-THAN OR EQUAL TO: try adding math
* U+25CC DOTTED CIRCLE: try adding one of: phags-pa, miao, old-permic, canadian-aboriginal, new-tai-lue, khojki, wancho, cham, gujarati, lepcha, mende-kikakui, coptic, chakma, symbols, takri, telugu, kannada, buhid, balinese, mahajani, kaithi, zanabazar-square, osage, modi, ahom, hebrew, sinhala, sharada, armenian, math, bassa-vah, siddham, tirhuta, psalter-pahlavi, buginese, music, tagalog, adlam, hanifi-rohingya, tai-viet, marchen, bhaiksuki, javanese, oriya, khmer, masaram-gondi, tamil, thai, warang-citi, kayah-li, saurashtra, sogdian, khudawadi, hanunoo, nko, malayalam, rejang, kharoshthi, mandaic, meetei-mayek, myanmar, tibetan, gurmukhi, brahmi, tai-le, yi, mongolian, pahawh-hmong, soyombo, grantha, manichaean, tifinagh, dogra, gunjala-gondi, elbasan, syloti-nagri, limbu, lao, tagbanwa, thaana, newa, tai-tham, duployan, sundanese, batak, devanagari, syriac, bengali, caucasian-albanian

Or you can add the above codepoints to one of the subsets supported by the font: latin-ext, latin [code: unreachable-subsetting]
  
  


- ⚠️ **WARN** /workspace/scratch/cbc03b9be171/xuqu-googlefonts-prep/build/googlefonts/ofl/xuqu/Xuqu-Regular.ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+02D8 BREVE: try adding one of: yi, canadian-aboriginal
* U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi
* U+02DB OGONEK: try adding one of: yi, canadian-aboriginal
* U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, tifinagh, math, cherokee
* U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic
* U+0307 COMBINING DOT ABOVE: try adding one of: canadian-aboriginal, math, tifinagh, duployan, malayalam, coptic, old-permic, syriac, hebrew, todhri, tai-le
* U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan
* U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee
* U+030C COMBINING CARON: try adding one of: tai-le, cherokee
* U+0326 COMBINING COMMA BELOW: try adding math
* U+0327 COMBINING CEDILLA: try adding math
* U+2003 EM SPACE: try adding nushu
* U+200C ZERO WIDTH NON-JOINER: try adding one of: lepcha, kharoshthi, hatran, masaram-gondi, buhid, new-tai-lue, sinhala, malayalam, gunjala-gondi, limbu, tai-viet, mongolian, bhaiksuki, khmer, cham, tai-le, tibetan, sogdian, brahmi, modi, tagalog, thaana, newa, arabic, pahawh-hmong, balinese, manichaean, kayah-li, dogra, myanmar, avestan, batak, hanifi-rohingya, kaithi, duployan, kannada, mahajani, bengali, mandaic, phags-pa, sharada, tagbanwa, rejang, syriac, grantha, gurmukhi, khudawadi, khojki, warang-citi, yi, hanunoo, telugu, zanabazar-square, saurashtra, tai-tham, thai, sundanese, chakma, gujarati, meetei-mayek, tamil, syloti-nagri, buginese, takri, hebrew, oriya, siddham, tifinagh, devanagari, javanese, psalter-pahlavi, tirhuta, nko, lao
* U+200D ZERO WIDTH JOINER: try adding one of: lepcha, rejang, new-tai-lue, khmer, bengali, batak, hanunoo, mahajani, saurashtra, oriya, tagalog, tai-tham, takri, kaithi, thai, hebrew, grantha, telugu, cham, warang-citi, khojki, sogdian, tifinagh, duployan, kharoshthi, zanabazar-square, tamil, yi, devanagari, balinese, manichaean, meetei-mayek, tagbanwa, gunjala-gondi, myanmar, phags-pa, tai-viet, arabic, limbu, mongolian, dogra, kannada, brahmi, bhaiksuki, hanifi-rohingya, masaram-gondi, pahawh-hmong, thaana, tai-le, mandaic, modi, javanese, syloti-nagri, sundanese, khudawadi, chakma, kayah-li, malayalam, psalter-pahlavi, sharada, siddham, avestan, newa, buginese, gurmukhi, syriac, tibetan, nko, buhid, old-hungarian, sinhala, tirhuta, gujarati, lao
* U+2010 HYPHEN: try adding one of: coptic, lisu, armenian, cham, kharoshthi, sundanese, syloti-nagri, sora-sompeng, arabic, yi, hebrew, kayah-li, kaithi
* U+2011 NON-BREAKING HYPHEN: try adding one of: syloti-nagri, yi, arabic
* U+2021 DOUBLE DAGGER: try adding adlam
* U+202F NARROW NO-BREAK SPACE: try adding one of: phags-pa, yi, mongolian
* U+2030 PER MILLE SIGN: try adding adlam
* U+2190 LEFTWARDS ARROW: try adding one of: math, symbols
* U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols
* U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols
* U+221A SQUARE ROOT: try adding math
* U+221E INFINITY: try adding math
* U+2260 NOT EQUAL TO: try adding math
* U+2264 LESS-THAN OR EQUAL TO: try adding math
* U+2265 GREATER-THAN OR EQUAL TO: try adding math
* U+25CC DOTTED CIRCLE: try adding one of: phags-pa, miao, old-permic, canadian-aboriginal, new-tai-lue, khojki, wancho, cham, gujarati, lepcha, mende-kikakui, coptic, chakma, symbols, takri, telugu, kannada, buhid, balinese, mahajani, kaithi, zanabazar-square, osage, modi, ahom, hebrew, sinhala, sharada, armenian, math, bassa-vah, siddham, tirhuta, psalter-pahlavi, buginese, music, tagalog, adlam, hanifi-rohingya, tai-viet, marchen, bhaiksuki, javanese, oriya, khmer, masaram-gondi, tamil, thai, warang-citi, kayah-li, saurashtra, sogdian, khudawadi, hanunoo, nko, malayalam, rejang, kharoshthi, mandaic, meetei-mayek, myanmar, tibetan, gurmukhi, brahmi, tai-le, yi, mongolian, pahawh-hmong, soyombo, grantha, manichaean, tifinagh, dogra, gunjala-gondi, elbasan, syloti-nagri, limbu, lao, tagbanwa, thaana, newa, tai-tham, duployan, sundanese, batak, devanagari, syriac, bengali, caucasian-albanian

Or you can add the above codepoints to one of the subsets supported by the font: latin-ext, latin [code: unreachable-subsetting]
  
  


- ⚠️ **WARN** /workspace/scratch/cbc03b9be171/xuqu-googlefonts-prep/build/googlefonts/ofl/xuqu/Xuqu-Thin.ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+02D8 BREVE: try adding one of: yi, canadian-aboriginal
* U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi
* U+02DB OGONEK: try adding one of: yi, canadian-aboriginal
* U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, tifinagh, math, cherokee
* U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic
* U+0307 COMBINING DOT ABOVE: try adding one of: canadian-aboriginal, math, tifinagh, duployan, malayalam, coptic, old-permic, syriac, hebrew, todhri, tai-le
* U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan
* U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee
* U+030C COMBINING CARON: try adding one of: tai-le, cherokee
* U+0326 COMBINING COMMA BELOW: try adding math
* U+0327 COMBINING CEDILLA: try adding math
* U+2003 EM SPACE: try adding nushu
* U+200C ZERO WIDTH NON-JOINER: try adding one of: lepcha, kharoshthi, hatran, masaram-gondi, buhid, new-tai-lue, sinhala, malayalam, gunjala-gondi, limbu, tai-viet, mongolian, bhaiksuki, khmer, cham, tai-le, tibetan, sogdian, brahmi, modi, tagalog, thaana, newa, arabic, pahawh-hmong, balinese, manichaean, kayah-li, dogra, myanmar, avestan, batak, hanifi-rohingya, kaithi, duployan, kannada, mahajani, bengali, mandaic, phags-pa, sharada, tagbanwa, rejang, syriac, grantha, gurmukhi, khudawadi, khojki, warang-citi, yi, hanunoo, telugu, zanabazar-square, saurashtra, tai-tham, thai, sundanese, chakma, gujarati, meetei-mayek, tamil, syloti-nagri, buginese, takri, hebrew, oriya, siddham, tifinagh, devanagari, javanese, psalter-pahlavi, tirhuta, nko, lao
* U+200D ZERO WIDTH JOINER: try adding one of: lepcha, rejang, new-tai-lue, khmer, bengali, batak, hanunoo, mahajani, saurashtra, oriya, tagalog, tai-tham, takri, kaithi, thai, hebrew, grantha, telugu, cham, warang-citi, khojki, sogdian, tifinagh, duployan, kharoshthi, zanabazar-square, tamil, yi, devanagari, balinese, manichaean, meetei-mayek, tagbanwa, gunjala-gondi, myanmar, phags-pa, tai-viet, arabic, limbu, mongolian, dogra, kannada, brahmi, bhaiksuki, hanifi-rohingya, masaram-gondi, pahawh-hmong, thaana, tai-le, mandaic, modi, javanese, syloti-nagri, sundanese, khudawadi, chakma, kayah-li, malayalam, psalter-pahlavi, sharada, siddham, avestan, newa, buginese, gurmukhi, syriac, tibetan, nko, buhid, old-hungarian, sinhala, tirhuta, gujarati, lao
* U+2010 HYPHEN: try adding one of: coptic, lisu, armenian, cham, kharoshthi, sundanese, syloti-nagri, sora-sompeng, arabic, yi, hebrew, kayah-li, kaithi
* U+2011 NON-BREAKING HYPHEN: try adding one of: syloti-nagri, yi, arabic
* U+2021 DOUBLE DAGGER: try adding adlam
* U+202F NARROW NO-BREAK SPACE: try adding one of: phags-pa, yi, mongolian
* U+2030 PER MILLE SIGN: try adding adlam
* U+2190 LEFTWARDS ARROW: try adding one of: math, symbols
* U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols
* U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols
* U+221A SQUARE ROOT: try adding math
* U+221E INFINITY: try adding math
* U+2260 NOT EQUAL TO: try adding math
* U+2264 LESS-THAN OR EQUAL TO: try adding math
* U+2265 GREATER-THAN OR EQUAL TO: try adding math
* U+25CC DOTTED CIRCLE: try adding one of: phags-pa, miao, old-permic, canadian-aboriginal, new-tai-lue, khojki, wancho, cham, gujarati, lepcha, mende-kikakui, coptic, chakma, symbols, takri, telugu, kannada, buhid, balinese, mahajani, kaithi, zanabazar-square, osage, modi, ahom, hebrew, sinhala, sharada, armenian, math, bassa-vah, siddham, tirhuta, psalter-pahlavi, buginese, music, tagalog, adlam, hanifi-rohingya, tai-viet, marchen, bhaiksuki, javanese, oriya, khmer, masaram-gondi, tamil, thai, warang-citi, kayah-li, saurashtra, sogdian, khudawadi, hanunoo, nko, malayalam, rejang, kharoshthi, mandaic, meetei-mayek, myanmar, tibetan, gurmukhi, brahmi, tai-le, yi, mongolian, pahawh-hmong, soyombo, grantha, manichaean, tifinagh, dogra, gunjala-gondi, elbasan, syloti-nagri, limbu, lao, tagbanwa, thaana, newa, tai-tham, duployan, sundanese, batak, devanagari, syriac, bengali, caucasian-albanian

Or you can add the above codepoints to one of the subsets supported by the font: latin-ext, latin [code: unreachable-subsetting]
  
  

</div>
</details>


</div>
</details>


<details><summary>[9] /workspace/scratch/cbc03b9be171/xuqu-googlefonts-prep/build/googlefonts/ofl/xuqu/Xuqu-Thin.ttf</summary>
<div>


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
width=746: less, lessequal, greater, greaterequal
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
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. (googlefonts/glyphsets/shape_languages)</summary>
    <div>


> This check uses a heuristic to determine which GF glyphsets a font supports. Then it checks the font for correct shaping behaviour for all languages in those glyphsets.




Original proposal: [https://github.com/googlefonts/fontbakery/issues/4147]





- ⚠️ **WARN** Warning language shaping:

| Message                                                           | Languages                    |
|-------------------------------------------------------------------|------------------------------|
| Auxiliary orthography codepoints:                                 | * en_Latn (English)          |
|   The following auxiliary characters are missing from the font: ʻ |                              |
| Auxiliary orthography codepoints:                                 | * fi_Latn (Finnish)          |
|   The following auxiliary characters are missing from the font: Ǧ |                              |
|   The following auxiliary characters are missing from the font: Ǥ |                              |
|   The following auxiliary characters are missing from the font: Ȟ |                              |
|   The following auxiliary characters are missing from the font: Ǩ |                              |
|   The following auxiliary characters are missing from the font: Ʒ |                              |
|   The following auxiliary characters are missing from the font: Ǯ |                              |
|   The following auxiliary characters are missing from the font: ǧ |                              |
|   The following auxiliary characters are missing from the font: ǥ |                              |
|   The following auxiliary characters are missing from the font: ȟ |                              |
|   The following auxiliary characters are missing from the font: ǩ |                              |
|   The following auxiliary characters are missing from the font: ʒ |                              |
|   The following auxiliary characters are missing from the font: ǯ |                              |
| Auxiliary orthography codepoints:                                 | * nb_Latn (Norwegian Bokmål) |
|   The following auxiliary characters are missing from the font: Ǎ |                              |
|   The following auxiliary characters are missing from the font: ǎ |                              |
| Auxiliary orthography codepoints:                                 | * fr_Latn (French)           |
|   The following auxiliary characters are missing from the font: Ǔ |                              |
|   The following auxiliary characters are missing from the font: ǔ |                              |
| Auxiliary orthography codepoints:                                 | * lt_Latn (Lithuanian)       |
|   The following auxiliary characters are missing from the font: Ẽ |                              |
|   The following auxiliary characters are missing from the font: ẽ |                              |
| Auxiliary orthography codepoints:                                 | * da_Latn (Danish)           |
|   The following auxiliary characters are missing from the font: Ǿ |                              |
|   The following auxiliary characters are missing from the font: ǿ |                              | [code: warning-language-shaping]
  
  

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

* - K (U+004B): X=882,Y=699 (should be at cap-height 700?)
* - K (U+004B): X=882,Y=1 (should be at baseline 0?)
* - k (U+006B): X=733,Y=1 (should be at baseline 0?)
* - z (U+007A): X=58,Y=1 (should be at baseline 0?)
* - question (U+003F): X=438,Y=1 (should be at baseline 0?)
* - question (U+003F): X=372,Y=1 (should be at baseline 0?)
* - germandbls (U+00DF): X=509,Y=698 (should be at cap-height 700?)
* - germandbls (U+00DF): X=149,Y=698 (should be at cap-height 700?)
* - kgreenlandic (U+0138): X=742,Y=1 (should be at baseline 0?)
* - uni0136 (U+0136): X=882,Y=699 (should be at cap-height 700?)
* - uni0136 (U+0136): X=882,Y=1 (should be at baseline 0?)
* - uni0137 (U+0137): X=733,Y=1 (should be at baseline 0?)
* - uni0163 (U+0163): X=304,Y=2 (should be at baseline 0?)
* - zacute (U+017A): X=58,Y=1 (should be at baseline 0?)
* - zdotaccent (U+017C): X=58,Y=1 (should be at baseline 0?)
* - zcaron (U+017E): X=58,Y=1 (should be at baseline 0?)
* - ordfeminine (U+00AA): X=110,Y=702 (should be at cap-height 700?)
* - ordfeminine (U+00AA): X=432,Y=702 (should be at cap-height 700?)
* - ordmasculine (U+00BA): X=104,Y=702 (should be at cap-height 700?)
* - ordmasculine (U+00BA): X=386,Y=702 (should be at cap-height 700?)
* - uni00B9 (U+00B9): X=244,Y=701 (should be at cap-height 700?)
* - uni00B9 (U+00B9): X=279,Y=701 (should be at cap-height 700?)
* - uni00B2 (U+00B2): X=107,Y=701 (should be at cap-height 700?)
* - uni00B2 (U+00B2): X=409,Y=701 (should be at cap-height 700?)
* - uni00B3 (U+00B3): X=58,Y=701 (should be at cap-height 700?)
* - uni00B3 (U+00B3): X=406,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=511,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=885,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=913,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=483,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=58,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=419,Y=701 (should be at cap-height 700?)
* - uni1E9E (U+1E9E): X=738,Y=1 (should be at baseline 0?)
* - uni1E9E (U+1E9E): X=390,Y=1 (should be at baseline 0?) [code: found-misalignments]
  
  

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
* AE (U+00C6): from (58.0, 0.0) to (169.0, 257.0) is colinear with segment from (169.0, 257.0) to (174.0, 270.0)
* AE (U+00C6): from (169.0, 257.0) to (174.0, 270.0) is colinear with segment from (174.0, 270.0) to (359.0, 700.0)
* AE (U+00C6): from (387.0, 700.0) to (566.0, 283.0) is colinear with segment from (566.0, 283.0) to (569.0, 276.0)
* AE (U+00C6): from (566.0, 283.0) to (569.0, 276.0) is colinear with segment from (569.0, 276.0) to (598.0, 209.0)
* Agrave (U+00C0): from (58.0, 0.0) to (206.0, 257.0) is colinear with segment from (206.0, 257.0) to (213.0, 270.0)
* Agrave (U+00C0): from (206.0, 257.0) to (213.0, 270.0) is colinear with segment from (213.0, 270.0) to (460.0, 700.0)
* Agrave (U+00C0): from (496.0, 700.0) to (736.0, 283.0) is colinear with segment from (736.0, 283.0) to (740.0, 276.0)
* Agrave (U+00C0): from (736.0, 283.0) to (740.0, 276.0) is colinear with segment from (740.0, 276.0) to (898.0, 0.0)
* Aacute (U+00C1): from (58.0, 0.0) to (206.0, 257.0) is colinear with segment from (206.0, 257.0) to (213.0, 270.0)
* Aacute (U+00C1): from (206.0, 257.0) to (213.0, 270.0) is colinear with segment from (213.0, 270.0) to (460.0, 700.0)
* Aacute (U+00C1): from (496.0, 700.0) to (736.0, 283.0) is colinear with segment from (736.0, 283.0) to (740.0, 276.0)
* Aacute (U+00C1): from (736.0, 283.0) to (740.0, 276.0) is colinear with segment from (740.0, 276.0) to (898.0, 0.0)
* Acircumflex (U+00C2): from (58.0, 0.0) to (206.0, 257.0) is colinear with segment from (206.0, 257.0) to (213.0, 270.0)
* Acircumflex (U+00C2): from (206.0, 257.0) to (213.0, 270.0) is colinear with segment from (213.0, 270.0) to (460.0, 700.0)
* Acircumflex (U+00C2): from (496.0, 700.0) to (736.0, 283.0) is colinear with segment from (736.0, 283.0) to (740.0, 276.0)
* Acircumflex (U+00C2): from (736.0, 283.0) to (740.0, 276.0) is colinear with segment from (740.0, 276.0) to (898.0, 0.0)
* Atilde (U+00C3): from (58.0, 0.0) to (206.0, 257.0) is colinear with segment from (206.0, 257.0) to (213.0, 270.0)
* Atilde (U+00C3): from (206.0, 257.0) to (213.0, 270.0) is colinear with segment from (213.0, 270.0) to (460.0, 700.0)
* Atilde (U+00C3): from (496.0, 700.0) to (736.0, 283.0) is colinear with segment from (736.0, 283.0) to (740.0, 276.0)
* Atilde (U+00C3): from (736.0, 283.0) to (740.0, 276.0) is colinear with segment from (740.0, 276.0) to (898.0, 0.0)
* Adieresis (U+00C4): from (58.0, 0.0) to (206.0, 257.0) is colinear with segment from (206.0, 257.0) to (213.0, 270.0)
* Adieresis (U+00C4): from (206.0, 257.0) to (213.0, 270.0) is colinear with segment from (213.0, 270.0) to (460.0, 700.0)
* Adieresis (U+00C4): from (496.0, 700.0) to (736.0, 283.0) is colinear with segment from (736.0, 283.0) to (740.0, 276.0)
* Adieresis (U+00C4): from (736.0, 283.0) to (740.0, 276.0) is colinear with segment from (740.0, 276.0) to (898.0, 0.0)
* Aring (U+00C5): from (58.0, 0.0) to (206.0, 257.0) is colinear with segment from (206.0, 257.0) to (213.0, 270.0)
* Aring (U+00C5): from (206.0, 257.0) to (213.0, 270.0) is colinear with segment from (213.0, 270.0) to (460.0, 700.0)
* Aring (U+00C5): from (496.0, 700.0) to (736.0, 283.0) is colinear with segment from (736.0, 283.0) to (740.0, 276.0)
* Aring (U+00C5): from (736.0, 283.0) to (740.0, 276.0) is colinear with segment from (740.0, 276.0) to (898.0, 0.0)
* Amacron (U+0100): from (58.0, 0.0) to (206.0, 257.0) is colinear with segment from (206.0, 257.0) to (213.0, 270.0)
* Amacron (U+0100): from (206.0, 257.0) to (213.0, 270.0) is colinear with segment from (213.0, 270.0) to (460.0, 700.0)
* Amacron (U+0100): from (496.0, 700.0) to (736.0, 283.0) is colinear with segment from (736.0, 283.0) to (740.0, 276.0)
* Amacron (U+0100): from (736.0, 283.0) to (740.0, 276.0) is colinear with segment from (740.0, 276.0) to (898.0, 0.0)
* Abreve (U+0102): from (58.0, 0.0) to (206.0, 257.0) is colinear with segment from (206.0, 257.0) to (213.0, 270.0)
* Abreve (U+0102): from (206.0, 257.0) to (213.0, 270.0) is colinear with segment from (213.0, 270.0) to (460.0, 700.0)
* Abreve (U+0102): from (496.0, 700.0) to (736.0, 283.0) is colinear with segment from (736.0, 283.0) to (740.0, 276.0)
* Abreve (U+0102): from (736.0, 283.0) to (740.0, 276.0) is colinear with segment from (740.0, 276.0) to (898.0, 0.0)
* Aogonek (U+0104): from (58.0, 0.0) to (206.0, 257.0) is colinear with segment from (206.0, 257.0) to (213.0, 270.0)
* Aogonek (U+0104): from (206.0, 257.0) to (213.0, 270.0) is colinear with segment from (213.0, 270.0) to (460.0, 700.0)
* Aogonek (U+0104): from (496.0, 700.0) to (736.0, 283.0) is colinear with segment from (736.0, 283.0) to (740.0, 276.0)
* Aogonek (U+0104): from (736.0, 283.0) to (740.0, 276.0) is colinear with segment from (740.0, 276.0) to (898.0, 0.0) [code: found-colinear-vectors]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table
set to optimize rendering? (googlefonts/gasp)</summary>
    <div>


> Traditionally version 0 'gasp' tables were set so that font sizes below 8 ppem had no grid fitting but did have antialiasing. From 9-16 ppem, just grid fitting. And fonts above 17ppem had both antialiasing and grid fitting toggled on. The use of accelerated graphics cards and higher resolution screens make this approach obsolete. Microsoft's DirectWrite pushed this even further with much improved rendering built into the OS and apps.
> 
> In this scenario it makes sense to simply toggle all 4 flags ON for all font sizes.




Original proposal: [https://github.com/fonttools/fontbakery/issues/4829]




  


- ⚠️ **WARN** The gasp range 0xFFFF value 0x0A should be set to 0x0F [code: unset-flags]
  
  

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


<details><summary>[9] /workspace/scratch/cbc03b9be171/xuqu-googlefonts-prep/build/googlefonts/ofl/xuqu/Xuqu-ExtraBold.ttf</summary>
<div>


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
width=746: lessequal, greater, greaterequal, less
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
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. (googlefonts/glyphsets/shape_languages)</summary>
    <div>


> This check uses a heuristic to determine which GF glyphsets a font supports. Then it checks the font for correct shaping behaviour for all languages in those glyphsets.




Original proposal: [https://github.com/googlefonts/fontbakery/issues/4147]





- ⚠️ **WARN** Warning language shaping:

| Message                                                           | Languages                    |
|-------------------------------------------------------------------|------------------------------|
| Auxiliary orthography codepoints:                                 | * fr_Latn (French)           |
|   The following auxiliary characters are missing from the font: Ǔ |                              |
|   The following auxiliary characters are missing from the font: ǔ |                              |
| Auxiliary orthography codepoints:                                 | * nb_Latn (Norwegian Bokmål) |
|   The following auxiliary characters are missing from the font: Ǎ |                              |
|   The following auxiliary characters are missing from the font: ǎ |                              |
| Auxiliary orthography codepoints:                                 | * da_Latn (Danish)           |
|   The following auxiliary characters are missing from the font: Ǿ |                              |
|   The following auxiliary characters are missing from the font: ǿ |                              |
| Auxiliary orthography codepoints:                                 | * lt_Latn (Lithuanian)       |
|   The following auxiliary characters are missing from the font: Ẽ |                              |
|   The following auxiliary characters are missing from the font: ẽ |                              |
| Auxiliary orthography codepoints:                                 | * en_Latn (English)          |
|   The following auxiliary characters are missing from the font: ʻ |                              |
| Auxiliary orthography codepoints:                                 | * fi_Latn (Finnish)          |
|   The following auxiliary characters are missing from the font: Ǧ |                              |
|   The following auxiliary characters are missing from the font: Ǥ |                              |
|   The following auxiliary characters are missing from the font: Ȟ |                              |
|   The following auxiliary characters are missing from the font: Ǩ |                              |
|   The following auxiliary characters are missing from the font: Ʒ |                              |
|   The following auxiliary characters are missing from the font: Ǯ |                              |
|   The following auxiliary characters are missing from the font: ǧ |                              |
|   The following auxiliary characters are missing from the font: ǥ |                              |
|   The following auxiliary characters are missing from the font: ȟ |                              |
|   The following auxiliary characters are missing from the font: ǩ |                              |
|   The following auxiliary characters are missing from the font: ʒ |                              |
|   The following auxiliary characters are missing from the font: ǯ |                              | [code: warning-language-shaping]
  
  

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
* - ordmasculine (U+00BA): X=372,Y=702 (should be at cap-height 700?)
* - uni00B9 (U+00B9): X=243,Y=701 (should be at cap-height 700?)
* - uni00B9 (U+00B9): X=317,Y=701 (should be at cap-height 700?)
* - uni00B2 (U+00B2): X=122,Y=701 (should be at cap-height 700?)
* - uni00B2 (U+00B2): X=394,Y=701 (should be at cap-height 700?)
* - uni00B3 (U+00B3): X=58,Y=701 (should be at cap-height 700?)
* - uni00B3 (U+00B3): X=393,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=557,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=839,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=913,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=483,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=58,Y=701 (should be at cap-height 700?)
* - trademark (U+2122): X=419,Y=701 (should be at cap-height 700?)
* - uni0327 (U+0327): X=40,Y=-261 (should be at descender -260?)
* - uni0327 (U+0327): X=-107,Y=-261 (should be at descender -260?)
* - uni0328 (U+0328): X=195,Y=-261 (should be at descender -260?)
* - uni0328 (U+0328): X=55,Y=-261 (should be at descender -260?)
* - circumflex (U+02C6): X=322,Y=701 (should be at cap-height 700?)
* - ogonek (U+02DB): X=294,Y=-261 (should be at descender -260?)
* - ogonek (U+02DB): X=154,Y=-261 (should be at descender -260?)
* - tilde (U+02DC): X=578,Y=698 (should be at cap-height 700?) [code: found-misalignments]
  
  

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

* A (U+0041): from (58.0, 0.0) to (136.0, 184.0) is colinear with segment from (136.0, 184.0) to (186.0, 303.0)
* A (U+0041): from (136.0, 184.0) to (186.0, 303.0) is colinear with segment from (186.0, 303.0) to (209.0, 356.0)
* A (U+0041): from (186.0, 303.0) to (209.0, 356.0) is colinear with segment from (209.0, 356.0) to (354.0, 700.0)
* A (U+0041): from (602.0, 700.0) to (747.0, 356.0) is colinear with segment from (747.0, 356.0) to (749.0, 352.0)
* A (U+0041): from (747.0, 356.0) to (749.0, 352.0) is colinear with segment from (749.0, 352.0) to (820.0, 184.0)
* A (U+0041): from (749.0, 352.0) to (820.0, 184.0) is colinear with segment from (820.0, 184.0) to (898.0, 0.0)
* AE (U+00C6): from (58.0, 0.0) to (117.0, 184.0) is colinear with segment from (117.0, 184.0) to (154.0, 303.0)
* AE (U+00C6): from (117.0, 184.0) to (154.0, 303.0) is colinear with segment from (154.0, 303.0) to (171.0, 356.0)
* AE (U+00C6): from (154.0, 303.0) to (171.0, 356.0) is colinear with segment from (171.0, 356.0) to (280.0, 700.0)
* AE (U+00C6): from (466.0, 700.0) to (575.0, 356.0) is colinear with segment from (575.0, 356.0) to (576.0, 352.0)
* AE (U+00C6): from (575.0, 356.0) to (576.0, 352.0) is colinear with segment from (576.0, 352.0) to (598.0, 283.0)
* Agrave (U+00C0): from (58.0, 0.0) to (136.0, 184.0) is colinear with segment from (136.0, 184.0) to (186.0, 303.0)
* Agrave (U+00C0): from (136.0, 184.0) to (186.0, 303.0) is colinear with segment from (186.0, 303.0) to (209.0, 356.0)
* Agrave (U+00C0): from (186.0, 303.0) to (209.0, 356.0) is colinear with segment from (209.0, 356.0) to (354.0, 700.0)
* Agrave (U+00C0): from (602.0, 700.0) to (747.0, 356.0) is colinear with segment from (747.0, 356.0) to (749.0, 352.0)
* Agrave (U+00C0): from (747.0, 356.0) to (749.0, 352.0) is colinear with segment from (749.0, 352.0) to (820.0, 184.0)
* Agrave (U+00C0): from (749.0, 352.0) to (820.0, 184.0) is colinear with segment from (820.0, 184.0) to (898.0, 0.0)
* Aacute (U+00C1): from (58.0, 0.0) to (136.0, 184.0) is colinear with segment from (136.0, 184.0) to (186.0, 303.0)
* Aacute (U+00C1): from (136.0, 184.0) to (186.0, 303.0) is colinear with segment from (186.0, 303.0) to (209.0, 356.0)
* Aacute (U+00C1): from (186.0, 303.0) to (209.0, 356.0) is colinear with segment from (209.0, 356.0) to (354.0, 700.0)
* Aacute (U+00C1): from (602.0, 700.0) to (747.0, 356.0) is colinear with segment from (747.0, 356.0) to (749.0, 352.0)
* Aacute (U+00C1): from (747.0, 356.0) to (749.0, 352.0) is colinear with segment from (749.0, 352.0) to (820.0, 184.0)
* Aacute (U+00C1): from (749.0, 352.0) to (820.0, 184.0) is colinear with segment from (820.0, 184.0) to (898.0, 0.0)
* Acircumflex (U+00C2): from (58.0, 0.0) to (136.0, 184.0) is colinear with segment from (136.0, 184.0) to (186.0, 303.0)
* Acircumflex (U+00C2): from (136.0, 184.0) to (186.0, 303.0) is colinear with segment from (186.0, 303.0) to (209.0, 356.0)
* Acircumflex (U+00C2): from (186.0, 303.0) to (209.0, 356.0) is colinear with segment from (209.0, 356.0) to (354.0, 700.0)
* Acircumflex (U+00C2): from (602.0, 700.0) to (747.0, 356.0) is colinear with segment from (747.0, 356.0) to (749.0, 352.0)
* Acircumflex (U+00C2): from (747.0, 356.0) to (749.0, 352.0) is colinear with segment from (749.0, 352.0) to (820.0, 184.0)
* Acircumflex (U+00C2): from (749.0, 352.0) to (820.0, 184.0) is colinear with segment from (820.0, 184.0) to (898.0, 0.0)
* Atilde (U+00C3): from (58.0, 0.0) to (136.0, 184.0) is colinear with segment from (136.0, 184.0) to (186.0, 303.0)
* Atilde (U+00C3): from (136.0, 184.0) to (186.0, 303.0) is colinear with segment from (186.0, 303.0) to (209.0, 356.0)
* Atilde (U+00C3): from (186.0, 303.0) to (209.0, 356.0) is colinear with segment from (209.0, 356.0) to (354.0, 700.0)
* Atilde (U+00C3): from (602.0, 700.0) to (747.0, 356.0) is colinear with segment from (747.0, 356.0) to (749.0, 352.0)
* Atilde (U+00C3): from (747.0, 356.0) to (749.0, 352.0) is colinear with segment from (749.0, 352.0) to (820.0, 184.0)
* Atilde (U+00C3): from (749.0, 352.0) to (820.0, 184.0) is colinear with segment from (820.0, 184.0) to (898.0, 0.0)
* Adieresis (U+00C4): from (58.0, 0.0) to (136.0, 184.0) is colinear with segment from (136.0, 184.0) to (186.0, 303.0)
* Adieresis (U+00C4): from (136.0, 184.0) to (186.0, 303.0) is colinear with segment from (186.0, 303.0) to (209.0, 356.0)
* Adieresis (U+00C4): from (186.0, 303.0) to (209.0, 356.0) is colinear with segment from (209.0, 356.0) to (354.0, 700.0)
* Adieresis (U+00C4): from (602.0, 700.0) to (747.0, 356.0) is colinear with segment from (747.0, 356.0) to (749.0, 352.0)
* Adieresis (U+00C4): from (747.0, 356.0) to (749.0, 352.0) is colinear with segment from (749.0, 352.0) to (820.0, 184.0)
* Adieresis (U+00C4): from (749.0, 352.0) to (820.0, 184.0) is colinear with segment from (820.0, 184.0) to (898.0, 0.0)
* Aring (U+00C5): from (58.0, 0.0) to (136.0, 184.0) is colinear with segment from (136.0, 184.0) to (186.0, 303.0)
* Aring (U+00C5): from (136.0, 184.0) to (186.0, 303.0) is colinear with segment from (186.0, 303.0) to (209.0, 356.0)
* Aring (U+00C5): from (186.0, 303.0) to (209.0, 356.0) is colinear with segment from (209.0, 356.0) to (354.0, 700.0)
* Aring (U+00C5): from (602.0, 700.0) to (747.0, 356.0) is colinear with segment from (747.0, 356.0) to (749.0, 352.0)
* Aring (U+00C5): from (747.0, 356.0) to (749.0, 352.0) is colinear with segment from (749.0, 352.0) to (820.0, 184.0)
* Aring (U+00C5): from (749.0, 352.0) to (820.0, 184.0) is colinear with segment from (820.0, 184.0) to (898.0, 0.0)
* Amacron (U+0100): from (58.0, 0.0) to (136.0, 184.0) is colinear with segment from (136.0, 184.0) to (186.0, 303.0)
* Amacron (U+0100): from (136.0, 184.0) to (186.0, 303.0) is colinear with segment from (186.0, 303.0) to (209.0, 356.0)
* Amacron (U+0100): from (186.0, 303.0) to (209.0, 356.0) is colinear with segment from (209.0, 356.0) to (354.0, 700.0)
* Amacron (U+0100): from (602.0, 700.0) to (747.0, 356.0) is colinear with segment from (747.0, 356.0) to (749.0, 352.0)
* Amacron (U+0100): from (747.0, 356.0) to (749.0, 352.0) is colinear with segment from (749.0, 352.0) to (820.0, 184.0)
* Amacron (U+0100): from (749.0, 352.0) to (820.0, 184.0) is colinear with segment from (820.0, 184.0) to (898.0, 0.0)
* Abreve (U+0102): from (58.0, 0.0) to (136.0, 184.0) is colinear with segment from (136.0, 184.0) to (186.0, 303.0)
* Abreve (U+0102): from (136.0, 184.0) to (186.0, 303.0) is colinear with segment from (186.0, 303.0) to (209.0, 356.0)
* Abreve (U+0102): from (186.0, 303.0) to (209.0, 356.0) is colinear with segment from (209.0, 356.0) to (354.0, 700.0)
* Abreve (U+0102): from (602.0, 700.0) to (747.0, 356.0) is colinear with segment from (747.0, 356.0) to (749.0, 352.0)
* Abreve (U+0102): from (747.0, 356.0) to (749.0, 352.0) is colinear with segment from (749.0, 352.0) to (820.0, 184.0)
* Abreve (U+0102): from (749.0, 352.0) to (820.0, 184.0) is colinear with segment from (820.0, 184.0) to (898.0, 0.0)
* Aogonek (U+0104): from (58.0, 0.0) to (136.0, 184.0) is colinear with segment from (136.0, 184.0) to (186.0, 303.0)
* Aogonek (U+0104): from (136.0, 184.0) to (186.0, 303.0) is colinear with segment from (186.0, 303.0) to (209.0, 356.0)
* Aogonek (U+0104): from (186.0, 303.0) to (209.0, 356.0) is colinear with segment from (209.0, 356.0) to (354.0, 700.0)
* Aogonek (U+0104): from (602.0, 700.0) to (747.0, 356.0) is colinear with segment from (747.0, 356.0) to (749.0, 352.0)
* Aogonek (U+0104): from (747.0, 356.0) to (749.0, 352.0) is colinear with segment from (749.0, 352.0) to (820.0, 184.0)
* Aogonek (U+0104): from (749.0, 352.0) to (820.0, 184.0) is colinear with segment from (820.0, 184.0) to (898.0, 0.0) [code: found-colinear-vectors]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table
set to optimize rendering? (googlefonts/gasp)</summary>
    <div>


> Traditionally version 0 'gasp' tables were set so that font sizes below 8 ppem had no grid fitting but did have antialiasing. From 9-16 ppem, just grid fitting. And fonts above 17ppem had both antialiasing and grid fitting toggled on. The use of accelerated graphics cards and higher resolution screens make this approach obsolete. Microsoft's DirectWrite pushed this even further with much improved rendering built into the OS and apps.
> 
> In this scenario it makes sense to simply toggle all 4 flags ON for all font sizes.




Original proposal: [https://github.com/fonttools/fontbakery/issues/4829]




  


- ⚠️ **WARN** The gasp range 0xFFFF value 0x0A should be set to 0x0F [code: unset-flags]
  
  

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

| ⚠️ WARN | ℹ️ INFO | ✅ PASS | ⏩ SKIP | 
| ---|---|---|---|
| 51 | 32 | 467 | 303 | 
| 6% | 4% | 55% | 36% | 



