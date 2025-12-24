---
source_image: page_092.png
page_number: 92
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.34
tokens: 8246
characters: 1226
timestamp: 2025-12-24T00:33:57.854041
finish_reason: stop
---

horiz.invoke('Mangoes in syrup')

multiple = Pmw.RadioSelect(root, labelpos=W, label_text='Multiple\nselection',
    frame_borderwidth=2, frame_relief=RIDGE, selectmode=MULTIPLE)
multiple.pack(fill=X, padx=10)

for text in ('Doug', 'Dinsdale', "Stig O'Tracy", 'Vince', 'Gloria Pules'):
    multiple.add(text)
multiple.invoke('Dinsdale')

Documentation for the RadioSelect widget starts on page 589.

4.3.22 ScrolledCanvas

The ScrolledCanvas widget is a convenience widget providing a Canvas widget with associated horizontal and vertical scrollbars. An example is shown in figure 4.44.

![ScrolledCanvas widget](figure_4.44.png)

Figure 4.44 Pmw ScrolledCanvas widget

sc = Pmw.ScrolledCanvas(root, borderframe=1, labelpos=N,
    label_text='ScrolledCanvas', usehullsize=1,
    hull_width=400,hull_height=300)

for i in range(20):
    x = -10 + 3*i
    y = -10
    for j in range(10):
        sc.create_rectangle('%dc'%x,'%dc'%y,'%dc'%(x+2),'%dc'%(y+2),
            fill='cadetblue', outline='black')
        sc.create_text('%dc'%(x+1),'%dc'%(y+1),text='%d,%d'%(i,j),
            anchor=CENTER, fill='white')
        y = y + 3
sc.pack()
sc.resizescrollregion()

Documentation for the ScrolledCanvas widget starts on page 592.