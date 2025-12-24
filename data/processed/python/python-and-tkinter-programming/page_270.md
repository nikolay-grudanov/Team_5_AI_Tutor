---
source_image: page_270.png
page_number: 270
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.71
tokens: 8341
characters: 1984
timestamp: 2025-12-24T00:38:52.550539
finish_reason: stop
---

4 A refresh option to repaint the screen.
5 Balloon help (provided through AppShell, which was introduced on page 155).

Here is the source to support the functionality:

draw3.py

from Tkinter import *
import Pmw, AppShell, math, time, string

class ToolBarButton(Label):
    def __init__(self, top, parent, tag=None, image=None, command=None,
                 statushelp='', balloonhelp='', height=21, width=21,
                 bd=1, activebackground='lightgrey', padx=0, pady=0,
                 state='normal', bg='grey'):
        Label.__init__(self, parent, height=height, width=width,
                       relief='flat', bd=bd, bg=bg)
        self.bg = bg
        self.activebackground = activebackground
        if image != None:
            if string.split(image, '.')[1] == 'bmp':
                self.Icon = BitmapImage(file='icons/%s' % image)
            else:
                self.Icon = PhotoImage(file='icons/%s' % image)
        else:
            self.Icon = PhotoImage(file='icons/blank.gif')
        self.config(image=self.Icon)

        self.tag = tag
        self.icommand = command
        self.command = self.activate
        self.bind("<Enter>", self.buttonEnter)
        self.bind("<Leave>", self.buttonLeave)
        self.bind("<ButtonPress-1>", self.buttonDown)
        self.bind("<ButtonRelease-1>", self.buttonUp)
        self.pack(side='left', anchor=NW, padx=padx, pady=pady)

        if balloonhelp or statushelp:
            top.balloon().bind(self, balloonhelp, statushelp)
            self.state = state

    def activate(self):
        self.icommand(self.tag)

    def buttonEnter(self, event):
        if self.state != 'disabled':
            self.config(relief='raised', bg=self.bg)

    def buttonLeave(self, event):
        if self.state != 'disabled':
            self.config(relief='flat', bg=self.bg)

    def buttonDown(self, event):
        if self.state != 'disabled':
            self.config(relief='sunken', bg=self.activebackground)