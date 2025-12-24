---
source_image: page_239.png
page_number: 239
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.10
tokens: 8359
characters: 2088
timestamp: 2025-12-24T00:38:05.255946
finish_reason: stop
---

if self.hitID:
    self.hitID = '%s.%d' % (self.hitID, port)
    for widget in [self.bnc_frame]:
        widget.bind('<KeyPress-space>', self.panelMenu)
        widget.bind('<Button-1>', self.panelMenu)
    for widget in [self.canvas]:
        widget.bind('<1>', self.panelMenu)

We define the focus_in and focus_out methods.

def focus_in(self, event):
    self.last_bg= self.canvas.itemcget(self.bnc, 'fill')
    self.canvas.itemconfig(self.bnc, fill=Color.HIGHLIGHT)
    self.update()

def focus_out(self, event):
    self.canvas.itemconfig(self.bnc, fill=self.last_bg)
    self.update()

![Figure 9.6 Widget focus](./images/widget_focus.png)

The purpose of these methods is to change the highlight color of the widgets as we either click on them with the mouse or navigate to them using the tab key. As we navigate from widget to widget, we display a highlight to show the user where the focus is. Figure 9.6 shows the effect of tabbing through the field. Although it’s less obvious without color, the selected connector is blue; in contrast, the other connectors are gray.

This method of navigation is somewhat alien to users who have been conditioned to using the mouse to navigate GUIs. However, the ability to select tiny graphic objects is valuable and it can change a user’s opinion of a product markedly. Without naming names, I have seen network management systems which required the user to click on graphic elements no more than 2mm square!

Components_3.py contains some additional code to animate the display to show the effect of status changes. Basically, each class that defines objects which can display status appends the instance to a widget list:

st_wid.append(self)    # register for animation

We then bind the animate function to the logo:

self.img = PhotoImage(file='logo.gif')
self.logo=Label(self.outer, image=self.img, bd=0)
self.logo.place(relx=0.055, rely=0.992, anchor=SW)
self.logo.bind('<Button-1>', self.animate)

The animate function is quite simple:

def animate(self, event):
    import random
    choice = random.choice(range(0, len(st_wid)-1))