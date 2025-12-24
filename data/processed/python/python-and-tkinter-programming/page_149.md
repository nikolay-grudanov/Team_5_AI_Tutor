---
source_image: page_149.png
page_number: 149
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.57
tokens: 8488
characters: 2357
timestamp: 2025-12-24T00:35:45.890421
finish_reason: stop
---

```python
self.status = self.onState    # Current ON color
self.on = 1

if self.status == STATUS_ON:   ➊
    self.canvas.itemconfig(self.light, fill=self.onColor)
elif self.status == STATUS_OFF:
    self.canvas.itemconfig(self.light, fill=self.offColor)
elif self.status == STATUS_WARN:
    self.canvas.itemconfig(self.light, fill=self.warningColor)
elif self.status == STATUS_SET:
    self.canvas.itemconfig(self.light, fill=self.specialColor)
else:
    self.canvas.itemconfig(self.light, fill=self.alarmColor)
self.canvas.update_idletasks() ➋
if self.blink:
    self.frame.after(self.blinkrate * 1000, self.update)

if __name__ == '__main__':
    class TestLEDs(Frame):
        def __init__(self, parent=None):
            # List of Colors and Blink On/Off
            states = [(STATUS_OFF, 0),
                      (STATUS_ON, 0),
                      (STATUS_WARN, 0),
                      (STATUS_ALARM, 0),
                      (STATUS_SET, 0),
                      (STATUS_ON, 1),
                      (STATUS_WARN, 1),
                      (STATUS_ALARM, 1),
                      (STATUS_SET, 1)]
            # List of LED types to display,
            # with sizes and other attributes
            leds = [(ROUND, 25, 25, FLAT, 0, None, ""),
                    (ROUND, 15, 15, RAISED, 1, None, ""),
                    (SQUARE, 20, 20, SUNKEN, 1, None, ""),
                    (SQUARE, 8, 8, FLAT, 0, None, ""),
                    (SQUARE, 8, 8, RAISED, 1, None, ""),
                    (SQUARE, 16, 8, FLAT, 1, None, ""),
                    (ARROW, 14, 14, RIDGE, 1, POINT_UP, ""),
                    (ARROW, 14, 14, RIDGE, 0, POINT_RIGHT, ""),
                    (ARROW, 14, 14, FLAT, 0, POINT_DOWN, "white")]

            Frame.__init__(self)  # Do superclass init
            self.pack()
            self.master.title('LED Example - Stage 1')

            # Iterate for each type of LED
            for shape, w, h, app, bd, orient, outline in leds:
                frame = Frame(self, bg=Color.PANEL)
                frame.pack(anchor=N, expand=YES, fill=X)
                # Iterate for selected states
                for state, blink in states:
                    LED(frame, shape=shape, status=state,
                        width=w, height=h, appearance=app,
                        orient=orient, blink=blink, bd=bd,
```