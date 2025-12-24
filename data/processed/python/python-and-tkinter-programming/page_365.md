---
source_image: page_365.png
page_number: 365
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.96
tokens: 8293
characters: 1999
timestamp: 2025-12-24T00:41:35.900630
finish_reason: stop
---

1 This interface uses the grid manager; the previous interface used the pack manager (see “Grid” on page 86 for details of the geometry managers). This has corrected the jagged alignment of the labels and fields.

2 The font has been changed to a larger sans serif font which improves readability when compared to the previous example, but see “Choosing fonts” on page 343.

3 The background color of the entry fields has been changed to narrow the contrast between the labels and fields.

4 A small amount of padding has been applied around the fields to make scanning easier.

Figure 16.2  A better interface

The interface is better, but it can still be improved more. Arranging the fields in logical groups and setting the size of some of the fields to an appropriate width will assist the user to fill in the information. Also, grouping some of the fields on the same line will result in a less vertically-linear layout, which fits scan patterns better since we tend to scan horizontally better than we scan vertically—that is how we learned to read, after all. This may not apply to cultures where printed characters are read vertically, however.

The next example implements the points discussed above.

The GUI in figure 16.3 is beginning to show signs of improvement since the fields are grouped logically and the width of the entries matches the data widths that they support. The Position entry has been replaced by a ComboBox (a Pmw widget) which allows the user to select from a list of available options (see figure 16.4).

Figure 16.3  A GUI showing logical field grouping

We can improve the interface further by breaking appropriate fields into subfields. For example, social security numbers always have a 3-2-4 format. We can handle this situation in two ways:

1 Use three separate fields for each of the subfields.
2 Use a smart widget that automatically formats the data to insert the hyphens in the data.
Smart widgets are discussed in “Formatted (smart) widgets” on page 117.