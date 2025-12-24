---
source_image: page_286.png
page_number: 286
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.00
tokens: 8545
characters: 2061
timestamp: 2025-12-24T00:39:27.996683
finish_reason: stop
---

```python
tags=('box2', 'box'))
self.canvas.create_rectangle(self.x1-5,
    self.y-5*self.width-5, self.x1+5,
    self.y-5*self.width+5, fill=self.boxFill,
    outline='black', tags=('box3', 'box'))
if cur:
    self.canvas.itemconfig(cur, fill=self.activeFill)
self.canvas.create_line(self.x2+50, 0, self.x2+50,
    1000, width=2)
tmp = self.x2+100
self.canvas.create_line(tmp, self.y-125, tmp, self.y-75,
    width=self.width, arrow='both',
    arrowshape=(self.a, self.b, self.c))
self.canvas.create_line(tmp-25, self.y, tmp+25, self.y,
    width=self.width, arrow='both',
    arrowshape=(self.a, self.b, self.c))
self.canvas.create_line(tmp-25, self.y+75, tmp+25, self.y+125,
    width=self.width, arrow='both',
    arrowshape=(self.a, self.b, self.c))

tmp = self.x2+10
self.canvas.create_line(tmp, self.y-5*self.width, tmp,
    self.y-deltaY, arrow='both', arrowshape=self.smallTips)
self.canvas.create_text(self.x2+15, self.y-deltaY+5*self.c,
    text=self.c, anchor=W)
tmp = self.x1-10
self.canvas.create_line(tmp, self.y-5*self.width, tmp,
    self.y+5*self.width, arrow='both',
    arrowshape=self.smallTips)
self.canvas.create_text(self.x1-15, self.y,
    text=self.width, anchor=E)
tmp = self.y+5*self.width+10*self.c+10
self.canvas.create_line(self.x2-10*self.a, tmp, self.x2, tmp,
    arrow='both', arrowshape=self.smallTips)
self.canvas.create_text(self.x2-5*self.a, tmp+5,
    text=self.a, anchor=N)
tmp = tmp+25
self.canvas.create_line(self.x2-10*self.b, tmp, self.x2, tmp,
    arrow='both', arrowshape=self.smallTips)
self.canvas.create_text(self.x2-5*self.b, tmp+5,
    text=self.b, anchor=N)

self.canvas.create_text(self.x1, 310, text="width=%d" % \
    self.width, anchor=W, font=('Verdana', 18))
self.canvas.create_text(self.x1, 330,
    text="arrowshape=(%d,%d,%d)" % \
    (self.a, self.b, self.c),
    anchor=W, font=('Verdana', 18))

if __name__ == '__main__':
    root = Tk()
    root.option_add('*Font', 'Verdana 10')
    root.title('Arrow Editor')
    arrow = ArrowEditor(root)
    root.mainloop()
```

**STRETCHING CANVAS OBJECTS**