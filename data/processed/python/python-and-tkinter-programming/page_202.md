---
source_image: page_202.png
page_number: 202
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.52
tokens: 8334
characters: 2074
timestamp: 2025-12-24T00:37:00.370738
finish_reason: stop
---

3 Each node has a Tkinter variable assigned to it since we are going to allow the nodes to be renamed (although code to use the new name is not provided in the example):
    self.name = name
    self.var = StringVar()
    self.var.set(name)
    self.text = Entry(tree, textvariable=self.var, bg=tree.bg,
4 The Entry widget does not display a highlight by default. To indicate that we are editing the filename, we add a highlight.
5 When we construct the hierarchy of nodes later, we will use the addChild method in the Node class:
    def addChild(self, tree, icon=None, openicon=None, name=None, action=None):
        child = Node(self, tree, icon, openicon, name, action)
        self.child.append(child)
        self.tree.display()
        return child
    This creates an instance of Node and appends it to the child list.
6 The boxpress method toggles the state of nodes displayed in the browser; clicking on + expands the node, while clicking on – collapses the node.
    def boxpress(self, event=None):
        if self.state == 'expanded':
            self.state = 'collapsed'
        elif self.state == 'collapsed':
            self.state = 'expanded'
        self.tree.display()
7 If the node is not currently selected, invoke supports an action assigned to either clicking or double-clicking on a node in the tree. For example, it might open the file using an appropriate target.
    def invoke(self, event=None):
        if not self.selected:
            self.tree.deselectall()
            self.selected = 1
            self.tree.display()
            if self.action:
                self.action(self.name)
        self.name = self.text.get()
        self.text.config(width=len(self.name)+2)

Example_8_10.py (continued)

def displayIconText(self):
    tree, text = self.tree, self.text
    if self.selected and self.openicon:
        self.pic = tree.create_image(self.x, self.y,
            image=self.openicon)
    else:
        self.pic = tree.create_image(self.x, self.y,
            image=self.icon)
    text.place(x=self.x+self.width/2, y=self.y, anchor=W)