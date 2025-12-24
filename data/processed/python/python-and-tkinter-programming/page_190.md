---
source_image: page_190.png
page_number: 190
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.33
tokens: 8217
characters: 1453
timestamp: 2025-12-24T00:36:35.009978
finish_reason: stop
---

self.createButtons()
self.createMain()

If you run AppShell.py, you will see a shell similar to the one in figure 8.8. Look for the toggle menu item in the Help menu to enable or disable balloon help.

![AppShell—A standard application framework](./images/appshell.png)

Figure 8.8 AppShell—A standard application framework

8.3 Data dictionaries

The forms that I have presented as examples have been coded explicitly for the material to be displayed; this becomes cumbersome when several forms are required to support an application. The solution is to use a data dictionary which defines fields, labels, widget types and other information. In addition, it may provide translation from database to screen and back to database, and define validation requirements, editable status and other behavior. We will see some more complete examples in “Putting it all together...” on page 311. However, the examples presented here will certainly give you a clear indication of their importance in simplifying form design.

First let’s take a look at a simple data dictionary; in this case it really is a Python dictionary, but other data structures could be used.

datadictionary.py

LC = 1    # Lowercase Key
UC = 2    # Uppercase Key
XX = 3    # As Is
DT = 4    # Date Insert
ND = 5    # No Duplicate Keys
ZP = 6    # Pad Zeroes
ZZ = 7    # Do Not Display
ZS = 8    # Do Not display, but fill in with key if blank
BLANKOK = 0    # Blank is valid in this field