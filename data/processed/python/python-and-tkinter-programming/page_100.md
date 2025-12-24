---
source_image: page_100.png
page_number: 100
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.86
tokens: 8351
characters: 1729
timestamp: 2025-12-24T00:34:14.465866
finish_reason: stop
---

from_ = self['min'],
to    = self['max'],
showvalue=self['showvalue'])
self.scale.grid()

value=self['value']
if value is not None:
    self.scale.set(value)

# Check keywords and initialize options
self.initialiseoptions(Gauge)

def _setGauge(self, value):
    self.canvas.delete('gauge')
    ival = self.scale.get()
    ticks = self['max'] - self['min']
    arc = (360.0/ticks) * ival
    xy = 3,3,self['size'],self['size']
    start = 90-arc
    if start < 0:
        start = 360 + start
    self.canvas.create_arc(xy, start=start, extent=arc-.001,
                           fill=self['fill'], tags=('gauge',))

Pmw.forwardmethods(Gauge, Scale, 'scale')

root = Tk()
root.option_readfile('optionDB')
root.title('Gauge')
Pmw.initialise()

g1 = Gauge(root, fill='red', value=56, min=0, max=255)
g1.pack(side=LEFT, padx=1, pady=10)

g2 = Gauge(root, fill='green', value=60, min=0, max=255)
g2.pack(side=LEFT, padx=1, pady=10)

g3 = Gauge(root, fill='blue', value=36, min=0, max=255)
g3.pack(side=LEFT, padx=1, pady=10)

root.mainloop()

Code comments

1 Options for the megawidget are specified by a three-element sequence of the option name, default value and a final argument. The final argument can be either a callback function, Pmw.INITOPT or None. If it is Pmw.INITOPT then the option may only be provided as an initialization option and it cannot be set by calling configure. Calling self.defineoptions includes keyword arguments passed in the widget’s constructor. These values may override any default values.

2 Having set the options we call the constructor of the base class, passing the parent widget as the single argument.

3 By convention, Pmw defines an interior attribute which is the container for components.