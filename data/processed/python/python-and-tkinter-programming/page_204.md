---
source_image: page_204.png
page_number: 204
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.83
tokens: 8453
characters: 2418
timestamp: 2025-12-24T00:37:10.038602
finish_reason: stop
---

```python
tree.lower('line')

class Tree(Canvas):
    def __init__(self, master, icon, openicon, treename, action,
                 bg='white', relief='sunken', bd=2,
                 linecolor='#808080', textcolor='black',
                 font=('MS Sans Serif', 8)):
        Canvas.__init__(self, master, bg=bg, relief=relief, bd=bd,
                        highlightthickness=0)
        self.pack(side='left', anchor=NW, fill='both', expand=1)

        self.bg, self.font = bg, font
        self.linecolor, self.textcolor = linecolor, textcolor
        self.master = master
        self.plusnode = PhotoImage(file=os.path.join(path, 'plusnode.gif'))
        self.minusnode = PhotoImage(file=os.path.join(path, 'minusnode.gif'))
        self.inhibitDraw = 1
        self.imageLabel = None
        self.imageData = None
        self.child = []
        self.x = self.y = -10

        self.child.append(Node(self, self, action=action,
                               icon=icon, openicon=openicon, name=treename))

    def display(self):
        if self.inhibitDraw: return
        self.delete(ALL)
        for child in self.child:
            child.textForget()
            child.display()

    def deselectall(self):
        for child in self.child:
            child.deselect()

    def vline(self, x, y, y1):
        for i in range(0, abs(y-y1), 2):
            self.create_line(x, y+i, x, y+i+1, fill=self.linecolor,
                             tags='line')

    def hline(self, y, x, x1):
        for i in range(0, abs(x-x1), 2):
            self.create_line(x+i, y, x+i+1, y, fill=self.linecolor,
                             tags='line')

Code comments (continued)

displayIconText displays the open or closed icon and the text associated with the node, and it binds single- and double-button-clicks to the text field:

def displayIconText(self):
    tree, text = self.tree, self.text
    if self.selected and self.openicon:
        self.pic = tree.create_image(self.x, self.y,
                                     image=self.openicon)
```

8 displayIconText displays the open or closed icon and the text associated with the node, and it binds single- and double-button-clicks to the text field:

def displayIconText(self):
    tree, text = self.tree, self.text
    if self.selected and self.openicon:
        self.pic = tree.create_image(self.x, self.y,
                                     image=self.openicon)