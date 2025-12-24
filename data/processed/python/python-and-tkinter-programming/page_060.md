---
source_image: page_060.png
page_number: 60
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.59
tokens: 8248
characters: 1365
timestamp: 2025-12-24T00:32:54.639035
finish_reason: stop
---

4.1.3 Label

Label widgets are used to display text or images. Labels can contain text spanning multiple lines, but you can only use a single font. You can allow the widget to break a string of text fitting the available space or you can embed linefeed characters in the string to control breaks. Several labels are shown in figure 4.5.

![Screenshot of a window with multiple labels and images, including text and bitmaps](./images/label_widget.png)

Figure 4.5 Label widget

Although labels are not intended to be used for interacting with users, you can bind mouse and keyboard events to callbacks. This may be used as a “cheap” button for certain applications.

Label(root, text="I mean, it's a little confusing for me when you say "
    "'dog kennel' if you want a mattress. Why not just say 'mattress'?",
    wraplength=300, justify=LEFT).pack(pady=10)

f1=Frame(root)
Label(f1, text="It's not working, we need more!", relief=RAISED).pack(side=LEFT, padx=5)
Label(f1, text="I'm not coming out!", relief=SUNKEN).pack(side=LEFT, padx=5)
f1.pack()

f2=Frame(root)
for bitmap,rlf in [ ('woman',RAISED),('mensetmanus',SOLID),
    ('terminal',SUNKEN), ('escherknot',FLAT),
    ('calculator',GROOVE),('letters',RIDGE)]:
    Label(f2, bitmap='@bitmaps/%s' % bitmap, relief=rlf).pack(side=LEFT, padx=5)
f2.pack()

Documentation for the Label widget starts on page 495.