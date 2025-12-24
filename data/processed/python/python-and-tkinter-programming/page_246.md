---
source_image: page_246.png
page_number: 246
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.87
tokens: 8228
characters: 1258
timestamp: 2025-12-24T00:38:10.490597
finish_reason: stop
---

Figure 9.11 Steps to generate rotated selector images

Note As I began to develop this example, I encountered a problem with the serial communications to the multimeter. While investigating this problem I wanted to continue developing the GUI. I did this by building a simple test harness to simulate input from the device. I am going to present development of this example by showing the test version first and then adding serial communications later. This technique is valuable to get an application started, since it is possible to simulate input from devices even if they are not available for your use (or too expensive for your boss to sign a purchase requisition so that you can get your hands on one!).

Here is the code to implement the test version of the multimeter. First, we begin with the data file, defining the meter’s ranges, control tables, labels, and other key data.

Example_9_1_data.py

# Tag    Run   RFlag   Units   Key
PRIMARY_DATA = [
    ('DI', 1, 'OL', 'mV', 'di'),
    ('DI', 0, '', 'mV', 'di'),
    ('OH', 1, 'OL.', 'Ohm', 'oh200o'),
    ('OH', 0, '4', 'Ohm', 'oh200o'),
    ('OH', 1, '.OL', 'KOhm', 'oh2ko'),
    ('OH', 0, '2', 'KOhm', 'oh2ko'),
    ('OH', 1, 'O.L', 'KOhm', 'oh20ko'),
    ...
    ('CA', 0, '2', 'nF', 'calo'),