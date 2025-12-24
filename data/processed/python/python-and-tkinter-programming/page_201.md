---
source_image: page_201.png
page_number: 201
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.11
tokens: 8195
characters: 1380
timestamp: 2025-12-24T00:36:51.867932
finish_reason: stop
---

self.action = action
self.x = self.y = 0   #drawing location
self.child = []
self.state = 'collapsed'
self.selected = 0

def addChild(self, tree, icon=None, openicon=None, name=None, action=None):
    child = Node(self, tree, icon, openicon, name, action)
    self.child.append(child)
    self.tree.display()
    return child

def deleteChild(self, child):
    self.child.remove(child)
    self.tree.display()

def textForget(self):
    self.text.place_forget()
    for child in self.child:
        child.textForget()

def deselect(self):
    self.selected = 0
    for child in self.child:
        child.deselect()

def boxpress(self, event=None):
    if self.state == 'expanded':
        self.state = 'collapsed'
    elif self.state == 'collapsed':
        self.state = 'expanded'
    self.tree.display()

def invoke(self, event=None):
    if not self.selected:
        self.tree.deselectall()
        self.selected = 1
        self.tree.display()
        if self.action:
            self.action(self.name)
        self.name = self.text.get()
        self.text.config(width=len(self.name)+2)

Code comments
① We begin by importing PIL modules:
import Image, ImageTk
② The Node class defines the subordinate tree and the open and closed icons associated with the node.
class Node:
    def __init__(self, master, tree, icon=None, openicon=None, name=None, action=None):
        ...