---
source_image: page_396.png
page_number: 396
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.15
tokens: 8378
characters: 2112
timestamp: 2025-12-24T00:42:43.038602
finish_reason: stop
---

However, you may not be willing or able to use a thread or you may be running on a system which does not support threads. In this case, using createfilehandler provides a convenient mechanism.

As an illustration, we’re going to look at a simple client/server which implements a time server. This might be used as some kind of monitor to make sure that critical components in an application are operating. Every minute, the server sends a timestamp on a given port. The client just displays this information in the example. To keep the code shorter, I’ve implemented the client and server in the same file:

client_server.py

from Tkinter import *
import sys, socket, time

class Server:
    def __init__(self):
        host = socket.gethostbyname(socket.gethostname())
        addr = host, 5000
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind('', 0)
        while 1:
            time.sleep(60.0)
            s.sendto(time.asctime(time.localtime(time.time())), addr)

class GUIClient:
    def __init__(self, master=None):
        self.master      = master
        self.master.title('Time Service Client')
        self.frame = Frame(master, relief=RAISED, borderwidth=2)
        self.text = Text(self.frame, height=26, width=50)
        self.scroll = Scrollbar(self.frame, command=self.text.yview)
        self.text.configure(yscrollcommand=self.scroll.set)
        self.text.pack(side=LEFT)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.frame.pack(padx=4, pady=4)
        Button(master, text='Close', command=self.master.quit).pack(side=TOP)

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind('', 5000)

        tkinter.createfilehandler(self.socket, READABLE, self.ihandler)

        self.master.after(5000, self.doMark)

    def ihandler(self, sock, mask):
        data, addr = sock.recvfrom(256)
        self.text.insert(END, '%s\n' % data)

    def doMark(self):
        self.text.insert(END, 'waiting...\n')
        self.master.after(5000, self.doMark)

if len(sys.argv) < 2:
    print 'select -s (server) or -c (client)'