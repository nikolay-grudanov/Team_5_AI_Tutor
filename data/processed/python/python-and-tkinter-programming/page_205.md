---
source_image: page_205.png
page_number: 205
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.57
tokens: 8308
characters: 1735
timestamp: 2025-12-24T00:36:57.793842
finish_reason: stop
---

9 displayLeaf draws a horizontal and vertical line connecting the icon with the current place in the tree:

def displayLeaf(self):
    self.tree.hline(self.y, self.master.x+1, self.x)
    self.tree.vline(self.master.x, self.master.y, self.y)
    self.displayIconText()

10 Similarly, displayBranch draws the lines and an open or closed box:

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

11 findLowestChild is a recursive method that finds the lowest terminal child in a given branch:

def findLowestChild(self, node):
    if node.state == 'expanded' and node.child != []:
        return self.findLowestChild(node.child[-1])
    else:
        return node

12 We define a flag called inhibitDraw to prevent the tree from being redrawn every time we add a node. This speeds up the time it takes to construct a complex tree by saving many CPU cycles:

self.inhibitDraw = 1

13 vline and hline are simple routines to draw vertical and horizontal lines:

def vline(self, x, y, y1):
    for i in range(0, abs(y-y1), 2):
        self.create_line(x, y+i, x, y+i+1, fill=self.linecolor,
            tags='line')

Example_8_10.py (continued)

class ImageBrowser(AppShell.AppShell):
    usecommandarea=1