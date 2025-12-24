---
source_image: page_260.png
page_number: 260
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.59
tokens: 8367
characters: 2025
timestamp: 2025-12-24T00:38:44.032633
finish_reason: stop
---

self.b1 = self.canvas.create_oval(216,285, 270,340, fill="", outline='#226644', width=3, tags='b_1')

2 The transparent fill on the circle has a side effect: a transparent object does not receive button events, so we bind enter and leave events to the line drawn for the circle.

    self.canvas.tag_bind(self.b2, "<Any-Enter>", self.mouseEnter)
    self.canvas.tag_bind(self.b2, "<Any-Leave>", self.mouseLeave)
    Widget.bind(self.canvas, "<1>", self.mouseDown)

We also bind left-mouse-button to the whole canvas. Note that we use the bind method of the mixin Widget to bind the event.

3 self.buttonAction is a very simple dispatcher:

    self.buttonAction = {'b_1': self.b1_action,
                        'b_2': self.b2_action}

4 mouseDown dispatches to the appropriate function using the tag of the canvas item receiving the event:

    def mouseDown(self, event):
        if event.widget.find_withtag(CURRENT):
            tags = self.canvas.gettags('current')
            if '_' in tags[0]:
                self.buttonAction[tags[0]]()

5 mouseEnter fills the circle with a color so that it can receive button events:

    def mouseEnter(self, event):
        tags = self.canvas.gettags('current')
        usetag= tags[0]
        self.lastcolor = self.canvas.itemcget(usetag, 'outline')
        self.canvas.itemconfig(usetag,outline=Color.HIGHLIGHT)
        self.canvas.itemconfig(usetag,fill=self.lastcolor)

6 mouseLeave removes the fill as the cursor leaves the button:

    def mouseLeave(self, event):
        tags = self.canvas.gettags('current')
        usetag= tags[0]
        self.canvas.itemconfig(usetag, outline=self.lastcolor)
        self.canvas.itemconfig(usetag,fill="")

7 Finally, when certain conditions have been met, we call mouseLeave directly to remove the highlight, even if the cursor is over the canvas item:

    self.canvas.delete('settag')
    self.mouseLeave(None)

If you run Example_9_3.py and work out the sequence, you should see a display similar to the one shown in figure 9.16.