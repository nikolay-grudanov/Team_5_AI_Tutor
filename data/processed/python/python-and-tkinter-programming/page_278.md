---
source_image: page_278.png
page_number: 278
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.20
tokens: 8386
characters: 1979
timestamp: 2025-12-24T00:39:08.118747
finish_reason: stop
---

def scrollEnter(self, event):
    id = self.canvas.find_withtag(CURRENT)[0]
    if 'text' in self.canvas.gettags(CURRENT):
        id = id-1
    self.canvas.itemconfigure(id, fill='SeaGreen1')

def scrollLeave(self, event):
    id = self.canvas.find_withtag(CURRENT)[0]
    if 'text' in self.canvas.gettags(CURRENT):
        id = id-1
    self.canvas.itemconfigure(id, fill=self.canvas['background'])

def scrollButton(self, event):
    ids = self.canvas.find_withtag(CURRENT)
    if ids:
        id = ids[0]
        if not 'text' in self.canvas.gettags(CURRENT):
            id = id+1
        print 'You clicked on %s' % \
            self.canvas.itemcget(id, 'text')

if __name__ == '__main__':
    root = Tk()
    root.option_add('*Font', 'Verdana 10')
    root.title('Scrolled Canvas')
    scroll = ScrolledCanvas(root)
    root.mainloop()

Code comments

① We create the canvas with a 61cm × 31cm scroll region which clearly will not fit in a 500×350 (pixels) window. The horizontal and vertical bars are created and bound directly to the position method of the canvas.

self.canvas = Canvas(master, relief=SUNKEN, borderwidth=2,
    scrollregion=(-11c', '-11c', '50c', '20c'))
self.hscroll = Scrollbar(master, orient=HORIZONTAL,
    command=self.canvas.xview)
self.vscroll = Scrollbar(master, command=self.canvas.yview)

② The scroll bars are set to track the canvas:

self.canvas.configure(xscrollcommand=self.hscroll.set,
    yscrollcommand=self.vscroll.set)

③ Setting up the bindings to pan the canvas when the right mouse button is clicked and dragged is surprisingly easy—we just bind the click to the scan_mark method and the drag to scan_dragto.

self.canvas.bind('<3>', lambda e, s=self: s.canvas.scan_mark(e.x, e.y))
self.canvas.bind('<B3-Motion>', lambda e, s=self: s.canvas.scan_dragto(e.x, e.y))

④ Finally, the ScrollButton callback is worthy of a brief note. It illustrates the ease of using tags to identify objects:

ids = self.canvas.find_withtag(CURRENT)