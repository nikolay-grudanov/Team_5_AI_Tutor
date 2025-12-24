---
source_image: page_235.png
page_number: 235
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.91
tokens: 8332
characters: 2029
timestamp: 2025-12-24T00:37:53.939815
finish_reason: stop
---

self.canvas.itemconfig(self.bnc, fill=Color.HIGHLIGHT)
self.update()

def focus_out(self, event):
    self.canvas.itemconfig(self.bnc, fill=self.last_bg)
    self.update()

def update(self):
    # First do the blink, if set to blink
    if self.blink:
        if self.on:
            if not self.onState:
                self.onState = self.status
                self.status = STATUS_OFF
                self.on = 0
        else:
            if self.onState:
                self.status = self.onState      # Current ON color
                self.on = 1
    # now update the status
    self.canvas.itemconfig(self.bnc, fill=self.Colors[self.status])
    self.canvas.itemconfig(self.pins, fill=self.Colors[self.status])
    self.bnc_frame.update_idletasks()
    if self.blink:
        self.bnc_frame.after(self.blinkrate * 1000, self.update)

Code comments

1 This example uses the GUICommon mixin class to define basic methods for widget state manipulation.
    class BNC(GUICommon):

2 Here we bind callbacks to FocusIn and FocusOut events.
    self.bnc_frame.bind('<FocusIn>', self.focus_in)
    self.bnc_frame.bind('<FocusOut>', self.focus_out)
    This binds the focus_in and focus_out functions to the widget so that if we tab into the widget or click the widget, we highlight it and enable the functions to be accessed.

3 All of the graphical objects (LEDs, BNC, J and FDDI connectors) define a specific update method to change the appearance of the widget based upon current status. We need specialized methods to allow us to update the color of particular areas within the composite. This method is also responsible for blinking the widget at one-second intervals.

def update(self):
    # First do the blink, if set to blink
    if self.blink:
        if self.on:
            if not self.onState:
                self.onState = self.status
                self.status = STATUS_OFF
                self.on = 0
        else:
            if self.onState:
                self.status = self.onState      # Current ON color