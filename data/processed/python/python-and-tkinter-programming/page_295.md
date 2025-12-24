---
source_image: page_295.png
page_number: 295
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.90
tokens: 8360
characters: 1904
timestamp: 2025-12-24T00:39:40.078859
finish_reason: stop
---

marshal.dump(len(keys), fd)
for key in keys:
    startx, starty, lastx, lasty, prevx, prevy, func, \
        fg, bg, fill, lwid , ld= self.objects[key]
    cfunc = self.transFunc[func]
    marshal.dump((key, startx, starty, lastx, lasty, prevx, \
        prevy, cfunc, fg, bg, fill, lwid , ld), fd)
    fd.close()

def initData(self):
    self.curFunc = self.drawLine
    self.growFunc = None
    self.curObject = None
    self.selObj = None
    self.lineData= []
    self.savedWidth = 1
    self.savedCursor = None
    self.objects = {}   # Now a dictionary
    self.foreground = 'black'
    self.background = 'white'
    self.fillStyle = None
    self.lineWidth = 1
    self.serial = 1000
    self.regular = FALSE
    self.inGrab = FALSE
    self.releaseGrab = TRUE
    self.currentName = 'Untitled'

# --- Code Removed ---------------------------------------------------------------

Code comments (continued)

To load an existing file, we use the standard tkFileDialog dialogs to obtain the filename. We then unmarshal* the contents of the file to obtain the stored object dictionary and then simply redraw the screen.

    fd = open(ofile)
    items = marshal.load(fd)
    for i in range(items):
        self.uniqueID, x1,y1,x2,y2,px,py, cfunc, \
            fg,bg,fill,lwid,ld = marshal.load(fd)
        self.storeObject(x1,y1,x2,y2,px,py, self.func[cfunc], \
            fg,bg,fill,lwid,ld)

Because it is not possible to marshal member functions of classes (self.func), we store the key to the function and use the reverse-lookup created in 3 to obtain the corresponding method.

* Marshaling is a method of serializing arbitrary Python data in a form that may be written and read to simple files. Not all Python types can be marshaled and other methods such as pickle or shelve (to store a database object) may be used. It is adequate to provide persistence for our relatively simple dictionary.