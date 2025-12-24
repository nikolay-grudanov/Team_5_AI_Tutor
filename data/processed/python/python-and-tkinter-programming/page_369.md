---
source_image: page_369.png
page_number: 369
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.15
tokens: 8335
characters: 1947
timestamp: 2025-12-24T00:41:46.124816
finish_reason: stop
---

or Verdana for Windows and Helvetica for UNIX and MacOS, since these fonts are usually installed on their respective systems. Figure 16.9 illustrates these fonts.

<table>
  <tr>
    <th>This is Arial</th>
    <th>This Arial Bold</th>
  </tr>
  <tr>
    <td>This is Verdana</td>
    <td>This is Verdana Bold</td>
  </tr>
  <tr>
    <td>This is Switzerland</td>
    <td>This is Switzerland Bold</td>
  </tr>
</table>

Figure 16.9  Arial, Verdana and Switzerland Fonts

Now let’s take a look at what can happen if a font is selected that is just not meant to be used for a GUI. The fonts used in this GUI look great when printed, but when displayed on the screen, they produce the effect shown in figure 16.10. Although the weight of the font is adequate, it just does not look right on the screen.

![Screenshot of a GUI form with various fields filled out](./images/gui_design_8.png)

Figure 16.10  The effect of selecting the wrong font

In summary:

1. Choose sans serif fonts wherever possible.
2. Use a minimum of font types, sizes, weights and styles within a single screen.
3. Allow for different screen sizes, if possible.
4. If the user is able to choose fonts from a theme or style, use that font, even if the result offends aesthetics.

16.2.2 Use of color in graphical user interfaces

The process of selecting color schemes for a GUI is highly subjective. In many cases it is best to allow the end user complete control over the colors that will be used within an application. The current trend in systems (Windows and UNIX CDE) is to allow the user to select a theme or scheme and then apply the selected colors, extrapolating alternate colors as appropriate. If you design your GUI to look good using just shades of gray and then calculate colors based upon the user-selected scheme, the GUI will probably work well. That way the user is allowed the privilege to select bizarre combinations of colors; after all, who are we to judge?