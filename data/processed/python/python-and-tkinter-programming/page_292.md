---
source_image: page_292.png
page_number: 292
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.18
tokens: 8593
characters: 2340
timestamp: 2025-12-24T00:39:43.197531
finish_reason: stop
---

self.canvas.itemconfig(self.selObj,
    width=self.savedWidth)
self.canvas.config(cursor='arrow')

def addGrabHandles(self, objectID, tag):
    self.canvas.delete("grabHandle")
    self.canvas.dtag("grabHandle")
    self.canvas.dtag("grab")
    self.canvas.dtag("grabbedObject")

    self.canvas.addtag("grab", "withtag", CURRENT)
    self.canvas.addtag("grabbedObject", "withtag", CURRENT)
    x1,y1,x2,y2 = self.canvas.bbox(tag)
    for x,y, curs, tagBx, tagBy, tagX, tagY in [
        (x1,y1,TLC,      'bx*1','by*1','x*1','y*1'),
        (x2,y1,TRC,      'bx*2','by*1','x*1','y*1'),
        (x1,y2,BLC,      'bx*1','by*2','x*1','y*1'),
        (x2,y2,BRC,      'bx*2','by*2','x*1','y*1'),
        (x1+((x2-x1)/2),y1,TS,  'bx*0','by*1','x*0','y*1'),
        (x2,y1+((y2-y1)/2),RS,  'bx*2','by*0','x*1','y*0'),
        (x1,y1+((y2-y1)/2),LS,  'bx*1','by*0','x*1','y*0'),
        (x1+((x2-x1)/2),y2,BS,  'bx*0','by*2','x*0','y*1')]:
        ghandle = self.canvas.create_rectangle(x-2,y-2,x+2,y+2,
            outline='black', fill='black', tags=('grab',
            'grabHandle', tagBx, tagBy, tagX,
            tagY,'%s'%objectID))
    self.canvas.tag_bind(ghandle, '<Any-Enter>',
        lambda e, s=self, c=curs: s.setCursor(e,c))
    self.canvas.tag_bind(ghandle, '<Any-Leave>',
        self.resetCursor)
    self.canvas.lift("grab")

# --- Code Removed ---------------------------------------------------------------

Code comments (continued)

4 Each of the objects drawn on the canvas is identified by a unique identity, which is attached to the object as a tag. Here we construct an identity:
    self.uniqueID = 'S*%d' % self.serial
    self.serial = self.serial + 1

5 Here we use the tags to get the identity of a drawn object from one of the grab handles or the object itself:
    for tag in tags:
        if tag[:2] == 'S*':
            objectID = tag
    Then, we determine if we have grabbed a grab handle (which all contain a grabhandle tag) or an object, in which case we change the cursor to indicate that the object is moveable.

6 This is where we parse the tags attached to the grab handles. The grab handles are encoded with information about their processing; this reduces the amount of code needed to support stretching the objects. The tags are attached in step 10 below.
    for tag in tags:
        if '*' in tag: