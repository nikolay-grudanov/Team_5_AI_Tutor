---
source_image: page_203.png
page_number: 203
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.92
tokens: 8318
characters: 1780
timestamp: 2025-12-24T00:36:57.793727
finish_reason: stop
---

text.bind("<ButtonPress-1>", self.invoke)
tree.tag_bind(self.pic, "<ButtonPress-1>", self.invoke, "+")
text.bind("<Double-Button-1>", self.boxpress)
tree.tag_bind(self.pic, "<Double-Button-1>",
    self.boxpress, "+")

def displayRoot(self):
    if self.state == 'expanded':
        for child in self.child:
            child.display()
    self.displayIconText()

def displayLeaf(self):
    self.tree.hline(self.y, self.master.x+1, self.x)
    self.tree.vline(self.master.x, self.master.y, self.y)
    self.displayIconText()

def displayBranch(self):
    master, tree = self.master, self.tree
    x, y = self.x, self.y
    tree.hline(y, master.x, x)
    tree.vline(master.x, master.y, y)
    if self.state == 'expanded' and self.child != []:
        for child in self.child:
            child.display()
            box = tree.create_image(master.x, y,
                image=tree.minusnode)
    elif self.state == 'collapsed' and self.child != []:
        box = tree.create_image(master.x, y,
            image=tree.plusnode)
    tree.tag_bind(box, "<ButtonPress-1>", self.boxpress, "+")
    self.displayIconText()

def findLowestChild(self, node):
    if node.state == 'expanded' and node.child != []:
        return self.findLowestChild(node.child[-1])
    else:
        return node

def display(self):
    master, tree = self.master, self.tree
    n = master.child.index(self)
    self.x = master.x + self.width
    if n == 0:
        self.y = master.y + (n+1)*self.height
    else:
        previous = master.child[n-1]
        self.y = self.findLowestChild(previous).y + self.height

    if master == tree:
        self.displayRoot()
    elif master.state == 'expanded':
        if self.child == []:
            self.displayLeaf()
        else:
            self.displayBranch()