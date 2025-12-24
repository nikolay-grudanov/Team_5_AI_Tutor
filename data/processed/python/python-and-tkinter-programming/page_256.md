---
source_image: page_256.png
page_number: 256
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.66
tokens: 8400
characters: 2175
timestamp: 2025-12-24T00:38:33.932312
finish_reason: stop
---

d['parity']    = serial.NoParity
d['dataBits']  = serial.WordLength7
d['stopBits']  = serial.TwoStopBits

Note the somewhat unusual format and slow communication speed. However, the meter is a quite simple device, and not very expensive, so we can make an exception here.

5 The read is blocking, which is unusual for a GUI. Since there are no user controls on the display, we do not need to worry about exposing the event loop. So, if the meter failed to respond to a request for data, we might lock up for a second or so.

6 This is where the meter’s unusual handshaking protocol is handled. This is the reason I constructed the test version of the code, because I could not get the device to respond to the poll request initially. I had to use a software datascope to monitor the control lines on the serial interface to determine what the device needed to communicate. Unusually, it required Request-To-Send (RTS) to go low before it would send anything. The serial module, as obtained from the Python FTP site, has RTS strapped high. A simple change fixes this problem. Here we force RTS low.

d['rtsSignal'] = 'C'

7 The meter has to be polled to get the current value measured.

line = self.fd.write('D\r')

8 If the poll times out, we assume that the multimeter is switched off and we fabricate a message to show an appropriate value on the display.

return 'XX Off '

The minimal changes to serial.py are shown here:

serial.py (changes only)

def __init__(self):
    self._dict = {}
...
    self._dict['rspType'] = RSP_BEST EFFORT
    self._dict['rspFixedLen'] = 0
    self._dict['rtsSignal'] = 'S'
    self._dict['dtrSignal'] = 'S'
...
    def __setitem__(self, key, value):
...
        elif key == 'debug' or key == 'cmdsEchoed':
            if type(value) != IntType:
                raise AttributeError, 'must be a boolean value'
        elif key == 'rtsSignal':
            if not value[:1] in 'CS':
                raise AttributeError, 'Illegal rtsSignal value'
        elif key == 'dtrSignal':
            if not value[:1] in 'CS':
                raise AttributeError, 'Illegal dtrSignal value'
        self._dict[key] = value
...
    def open(self, cfg):