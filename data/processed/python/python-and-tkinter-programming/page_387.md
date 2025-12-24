---
source_image: page_387.png
page_number: 387
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.65
tokens: 8325
characters: 1797
timestamp: 2025-12-24T00:42:16.102055
finish_reason: stop
---

Using threads in a Python-only environment (without involving a GUI) can be quite straightforward. However, adding Tkinter (or CORBA or ILU) can introduce some special problems. Such systems rely on a mainloop to dispatch events received from a number of stimuli, and threads can complicate the design of your code dramatically.

18.1.1 Non-GUI threads

Let’s begin by looking at a simple example which does not involve a GUI, or at least not directly. This example is a skeleton for a server which accepts a number of requests to process data (the requests may come from a client with a GUI). In particular, the requestors do not expect to get data returned to them, or at most they accept a success/failure return code.

thread1.py

import thread, time

class Server:
    def __init__(self):
        self._dispatch = {}
        self._dispatch['a'] = self.serviceA
        self._dispatch['b'] = self.serviceB
        self._dispatch['c'] = self.serviceC
        self._dispatch['d'] = self.serviceD

    def service(self, which, qual):
        self._dispatch[which](qual)

    def serviceA(self, argin):
        thread.start_new_thread(self.engine, (argin,'A'))

    def serviceB(self, argin):
        thread.start_new_thread(self.engine, (argin,'B'))

    def serviceC(self, argin):
        thread.start_new_thread(self.engine, (argin,'C'))

    def serviceD(self, argin):
        thread.start_new_thread(self.engine, (argin,'D'))

    def engine(self, arg1, arg2):
        for i in range(500):
            print '%s%s%03d' % (arg1, arg2, i),
            time.sleep(0.0001)
        print

server = Server()

server.service('a', '88')      # These calls simulate receipt of
server.service('b', '12')      # requests for service.
server.service('c', '44')
server.service('d', '37')

time.sleep(30.0)