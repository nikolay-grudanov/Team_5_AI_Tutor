---
source_image: page_156.png
page_number: 156
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.01
tokens: 8126
characters: 927
timestamp: 2025-12-24T00:35:25.043190
finish_reason: stop
---

7.2.1 Adding a hex nut to our class library

Now let’s make use of the color transformations to add some visual effects to a drawn object. In this example we are going to create hex nuts. As you’ll see later, these simple objects can be used in many different ways.

We will begin by extending some of the definitions in Common_7_1.py, which will be saved as Common_7_2.py:

Common_7_2.py

NUT_FLAT      = 0
NUT_POINT     = 1

Color.BRONZE   = '#7e5b41'
Color.CHROME   = '#c5c5b8'
Color.BRASS    = '#cdb800'

Here is the code for our HexNut class. This example is a little more complex and has options for instantiating a variety of nuts. The test routine illustrates some of the possible variations. Running this code displays the window shown in figure 7.4.

Example_7_4.py

from Tkinter           import *
from GUICommon_7_2     import *
from Common_7_2        import *

Figure 7.3 Transforming colors

Figure 7.4 Basic nuts