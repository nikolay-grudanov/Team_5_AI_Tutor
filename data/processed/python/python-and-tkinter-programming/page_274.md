---
source_image: page_274.png
page_number: 274
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.82
tokens: 8578
characters: 2156
timestamp: 2025-12-24T00:39:14.131711
finish_reason: stop
---

self.lastx = self.startx + delta
    self.lasty = self.starty + delta
    self.curFunc(self.startx, self.starty, self.lastx,
        self.lasty, self.prevx, self.prevy, self.foreground,
        self.background, self.fillStyle, self.lineWidth,
        self.lineData)
    self.storeObject()
else:
    if self.selObj:
        self.canvas.itemconfig(self.selObj,
            width=self.savedWidth)

def drawLine(self,x,y,x2,y2,x3,y3,fg,bg,fillp,wid,ld):
    self.canvas.delete(self.curObject)
    self.curObject = self.canvas.create_line(x,y,x2,y2,fill=fg,
        tags='drawing',stipple=fillp,width=wid)

def drawFree(self,x,y,x2,y2,x3,y3,fg,bg,fillp,wid,ld):
    self.drawFreeSmooth(x,y,x2,y2,x3,y3,FALSE,fg,bg,fillp,wid,ld)

def drawSmooth(self,x,y,x2,y2,x3,y3,fg,bg,fillp,wid, ld):
    self.drawFreeSmooth(x,y,x2,y2,x3,y3,TRUE,fg,bg,fillp,wid,ld)

def drawFreeSmooth(self,x,y,x2,y2,x3,y3,smooth,fg,bg,fillp,
    wid,ld):
    if not ld:
        for coord in [[x3, y3, x2, y2], [x2, y2]][smooth]:
            self.lineData.append(coord)
            ild = self.lineData
    else:
        ild = ld
    if len(ild) > 2:
        self.curObject = self.canvas.create_line(ild, fill=fg,
            stipple=fillp, tags='drawing', width=wid, smooth=smooth)

def drawRect(self,x,y,x2,y2,x3,y3,fg,bg,fillp,wid,ld):
    self.drawFilledRect(x,y,x2,y2,x3,y3,fg,'',fillp,wid,ld)

def drawFilledRect(self,x,y,x2,y2,x3,y3,fg,bg,fillp,wid,ld):
    self.canvas.delete(self.curObject)
    self.curObject = self.canvas.create_rectangle(x,y,x2,y2,
        outline=fg, tags='drawing',fill=bg,
        stipple=fillp,width=wid)

def drawOval(self,x,y,x2,y2,x3,y3,fg,bg,fillp,wid,ld):
    self.drawFilledOval(x,y,x2,y2,x3,y3,fg,'',fillp,wid,ld)

def drawFilledOval(self,x,y,x2,y2,x3,y3,fg,bg,fillp,wid,ld):
    self.canvas.delete(self.curObject)
    self.curObject = self.canvas.create_oval(x,y,x2,y2,outline=fg,
        fill=bg,tags='drawing',stipple=fillp,width=wid)

Code comments (continued)
6 Each of the select callbacks uses the tag attached to each of the toolbar buttons to look up the function, line width, or other property of a button (Some of the code has been removed).