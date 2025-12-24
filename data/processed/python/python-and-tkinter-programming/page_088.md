---
source_image: page_088.png
page_number: 88
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.57
tokens: 8251
characters: 1161
timestamp: 2025-12-24T00:33:47.320064
finish_reason: stop
---

f1 = nb.getPage('Page 1')
f2 = nb.getPage('Page 2')
f3 = nb.getPage('Page 3')

nb.pack(pady=10, padx=10, fill=BOTH, expand=1)
Button(f1, text='This is text on page 1', fg='blue').pack(pady=40)

c = Canvas(f2, bg='gray30')
w = c.winfo_reqwidth()
h = c.winfo_reqheight()
c.create_oval(10,10,w-10,h-10,fill='DeepSkyBlue1')
c.create_text(w/2,h/2,text='This is text on a canvas', fill='white',
    font=('Verdana', 14, 'bold'))
c.pack(fill=BOTH, expand=1)

Documentation for the NotebookS widget starts on page 582.

4.3.17 NoteBook

Release 0.8.3 of Pmw replaces NoteBookR and NoteBookS with Notebook. While it is quite similar to the previous notebooks, there are some small changes. In fact, you will have to make changes to your code to use NoteBook with existing code. However, the changes are minor and the new form may be a little easier to use. Figure 4.39 illustrates the new widget.

![Pmw NoteBook widget (version 0.8.3)](figure_4_39.png)

Figure 4.39  Pmw NoteBook widget (version 0.8.3)

from Tkinter import *
import Pmw

root = Tk()
root.option_readfile('optionDB')
root.title('Notebook')
Pmw.initialise()

nb = Pmw.NoteBook(root)
p1 = nb.add('Page 1')