---
source_image: page_368.png
page_number: 368
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.20
tokens: 8612
characters: 3159
timestamp: 2025-12-24T00:41:58.027027
finish_reason: stop
---

8 Some platforms may have GUI style guides that constrain the design. These should be adhered to, even if it means developing platform-specific versions.

9 Provide help wherever possible. Balloon help* can be useful for beginning users but may be annoying to experts. Consequently it is important to provide the user with a means of turning off such facilities.

10 The UI should be intuitive so that it is not necessary to provide documentation. Careful field labeling, clues to input format and clear validation schemes can go a long way to achieve this goal.

11 Whenever possible, test the UI with end users. Building prototypes in Python is easy, so take advantage of this and get feedback from the target audience for your work.

16.2.1 Choosing fonts

Choosing an appropriate font for a GUI is important to ensure that an interface is effective. Readability is an important factor here. A font that is highly readable when displayed at a screen resolution of 640 x 480 may be too small to read when displayed at a resolution of 1024 x 768 or greater. The size of the font should, therefore, be either calculated based on the screen resolution or selected by the end user. However, in the latter case, you should ensure that the end user is given a range of fonts that the application can display without changing screen layouts or causing overflows, overlaps or other problems.

Font selection can be crucial to achieving an effective interface. In general, serif† fonts should be avoided. Most of us are used to reading serif fonts on printed material (in fact, the body of this book is set in Adobe Garamond, a font with a light serif) since we believe that we are able to recognize word forms faster in serif as opposed to sans serif fonts. Unfortunately, many serif fonts do not display as clearly on screens as they do when printed, since the resolution of most printers is better than that of displays.

Take a look at figure 16.8. This shows a screen grab, at 1024×768 resolution, of Times New Roman and Verdana fonts in three point sizes. The sans serif font results in a crisper image, although the overall width of the text is greater. In most cases, it is easier to select Arial.

<table>
  <tr>
    <th>This is an 8pt serif font</th>
    <th>This is an 8pt sans serif font</th>
  </tr>
  <tr>
    <td>This is a 10pt serif font</td>
    <td>This is a 10pt sans serif font</td>
  </tr>
  <tr>
    <td>This is a 12pt serif font</td>
    <td>This is a 12pt sans serif font</td>
  </tr>
</table>

Figure 16.8 Comparing Serif and Sans Serif Fonts

* Balloon help is displayed when the cursor is placed over a field or control without moving it for a short time. The help may be displayed as a message in the status area of a window, if it has one, or in a popup balloon close to the field or control.

† A serif font is one in which each of the letters contain small artistic flourishes that appear to give the glyphs ledges and feet. Common serif fonts include Times, Bookman, Palatino, and Garamond. A sans serif font is one that does not contain these extra flourishes. Common sans serif fonts are Helvetica, Arial, Geneva, Gothic, and Swiss.