---
source_image: page_255.png
page_number: 255
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.94
tokens: 8315
characters: 1711
timestamp: 2025-12-24T00:38:27.760343
finish_reason: stop
---

def open(self, cfg):
    self.debug = cfg['debug']
    self._trace('RS232.open')
    cfg['cmdsEchoed'] = FALSE
    cfg['cmdTerm'] = '\r'
    cfg['rspTerm'] = '\r'
    cfg['rspType'] = serial.RSP_TERMINATED
    serial.Port.open(self, cfg)

class MeterServer:
    def __init__(self):
        # Open up the serial port
        try:
            d = serial.PortDict()
            d['port'] = serial.COM1
            d['baud'] = serial.Baud1200
            d['parity'] = serial.NoParity
            d['dataBits'] = serial.WordLength7
            d['stopBits'] = serial.TwoStopBits
            d['timeOutMs'] = 1500
            d['rspTerm'] = IGNORE
            d['rtsSignal'] = 'C'
            d['debug'] = FALSE
            self.fd = RS232()
            self.fd.open(d)
        except:
            print 'Cannot open serial port (COM1)'
            sys.exit()

    def poll(self):
        try:
            line = self.fd.write('D\r')
            # OK, read the serial line (wait maximum of 1500 msec)
            inl = self.fd.readTerminated()
            return inl
        except:
            return 'XX Off'

Code comments

1 The serial module wraps the sio module, which is a dll.
from crilib import *
import sys, serial, time, string, os
crilib contains simple constants.

2 This time we have to initialize the UART (Universal Asynchronous Receiver Transmitter):
    def __init__(self):
        serial.Port.__init__(self)

3 The terminators for the serial protocol are defined. Although we are not turning debug on for this example, the necessary initializers are given to help you reuse the code.

4 The communication parameters for the UART are set.
    d['port'] = serial.COM1
    d['baud'] = serial.Baud1200