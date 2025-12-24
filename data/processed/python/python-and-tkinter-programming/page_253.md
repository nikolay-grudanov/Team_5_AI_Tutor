---
source_image: page_253.png
page_number: 253
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.63
tokens: 8366
characters: 1760
timestamp: 2025-12-24T00:38:30.956527
finish_reason: stop
---

self.canvas.create_text(263, 67, text=self.holdVal,
    font=("Digiface", 16),
    fill="#333377",
    anchor = E,
    tags="holdval")

range, openline = self.getRange(tag, val, units)
if range:    # Change the control to reflect the range
    if not self.curRange == range:
        self.curRange = range
        self.canvas.delete('control')
        self.canvas.create_image(146, 441, anchor=CENTER,
            image=getattr(self, 'i%s' % range).
            tags="control")
        self.holdVal = '0.0'  # reset
    if openline:
        self.startAnimation()
else:
    self.stopAnimation()

# Now we will update the units symbols on the display
ma,ua,a,mv,v,ko,mo,o,nf,uf,f,mhz,khz,hz,ac, ctrl, lbl = \
    SECONDARY_DATA[range]

for tag in ['ma','ua','a','mv','v','ko','mo','o',
    'nf','uf','f','mhz','khz','hz','ac']:
    self.canvas.itemconfig(tag,
        fill=['gray75','#333377'][eval(tag)])
    # Update the label field if there is one
    self.canvas.delete('label')
    if lbl:
        self.canvas.create_text(55, 150, text=lbl,
            font=("Arial", 12),
            fill="#333377",
            anchor = CENTER,
            tags="label")

# Finally, display the value
self.canvas.create_text(214, 100, text=val,
    font=("Digiface", 48),
    fill="#333377",
    anchor = E,
    tags="display")

if __name__ == '__main__':
    root = Tk()
    multimeter = MultiMeter(root)
    multimeter.root.mainloop()

Code comments (continued)

5 The animate method displays a rapidly increasing row of vertical bars which reset when they reach the right-hand side of the display.

6 buildScanner builds a dictionary from PRIMARY_DATA to provide the primary lookup for the messages received from the meter. The GIF images are also loaded as PhotoImages.