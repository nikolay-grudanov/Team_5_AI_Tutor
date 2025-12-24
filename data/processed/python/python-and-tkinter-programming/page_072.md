---
source_image: page_072.png
page_number: 72
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.61
tokens: 8430
characters: 2085
timestamp: 2025-12-24T00:33:31.775412
finish_reason: stop
---

```python
canvas.coords('line',
    15,20,35,20,35,y2,45,y2,25,height,5,y2,15,y2,15,20)

canvas = Canvas(root, width=50, height=50, bd=0, highlightthickness=0)
canvas.create_polygon(0,0,1,1,2,2, fill='cadetblue', tags='poly')
canvas.create_line(0,0,1,1,2,2,0,0, fill='black', tags='line')

scale = Scale(root, orient=VERTICAL, length=284, from_=0, to=250,
    tickinterval=50, command=lambda h, c=canvas:setHeight(c,h))
scale.grid(row=0, column=0, sticky='NE')
canvas.grid(row=0, column=1, sticky='NWSE')
scale.set(100)

Documentation for the Scale widget starts on page 522.

4.2 Fonts and colors

The purpose of this section is to present the reader with an overview of fonts and colors as they apply to Tkinter. This will provide sufficient context to follow the examples that will be presented throughout the text.

4.2.1 Font descriptors

Those of us that have worked with X Window applications have become accustomed to the awkward and precise format of X window font descriptors. Fortunately, with release 8.0 and above of Tk, there is a solution: Tk defines font descriptors. Font descriptors are architecture independent. They allow the programmer to select a font by creating a tuple containing the family, pointsize and a string containing optional styles. The following are examples:

    ('Arial', 12, 'italic')
    ('Helvetica', 10)
    ('Verdana', 8, 'medium')

If the font family does not contain embedded spaces, you may pass the descriptor as a single string, such as:

    'Verdana 8 bold italic'

4.2.2 X Window System font descriptors

Of course, the older font descriptors are available if you really want to use them. Most X Window fonts have a 14-field name in the form:

- foundry-family-weight-slant-setwidth-style-pixelSize-pointSize-Xresolution-Yresolution-spacing-averageWidth-registry-encoding

Normally, we only care about a few of the fields:

-*--family-weight-slant-*-*-*--pointSize-*-*-*--registry-encoding

These fields are defined as follows:
• family   A string that identifies the basic typographic style for example, helvetica, arial, etc.).
```