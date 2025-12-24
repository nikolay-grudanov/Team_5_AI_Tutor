---
source_image: page_262.png
page_number: 262
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.38
tokens: 8151
characters: 1128
timestamp: 2025-12-24T00:38:33.254484
finish_reason: stop
---

CHAPTER 10

Drawing blobs and rubber lines

10.1 Drawing on a canvas 238
10.2 A more complete drawing program 244
10.3 Scrolled canvases 251
10.4 Ruler-class tools 254
10.5 Stretching canvas objects 258
10.6 Some finishing touches 262
10.7 Speed drawing 271
10.8 Summary 275

Despite the title, this chapter covers some of the techniques used to build drawing tools and interfaces which allow the user to create and move objects around in a GUI. The chapter is not meant to be a complete guide to developing a new “paint” tool, but I will provide you with some useful templates for drawing objects on a canvas, using rubber lines and rearranging objects on a canvas. You have already seen the effect of drawing items on a canvas in earlier chapters—this chapter reveals a little more detail on how to create and maintain drawn objects.

Some of the examples are Tkinter adaptations of Tk demonstration programs; they may be used as an additional guide to converting Tcl/Tk scripts to Tkinter. I have avoided the temptation to completely rework the code, since a side-by-side comparison would reveal how well Tkinter supports Tk.