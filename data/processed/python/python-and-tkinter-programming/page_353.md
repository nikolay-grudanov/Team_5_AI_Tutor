---
source_image: page_353.png
page_number: 353
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.13
tokens: 8299
characters: 1538
timestamp: 2025-12-24T00:41:19.378408
finish_reason: stop
---

class Dictionary:
    def __init__(self, name=None):
        self.dictionary = {
            'Graham Chapman': (1941, 1989, 'Leicester', 'Medicine'),
            'John Cleese': (1939, -1, 'Weston-Super-Mare', 'Law'),
            'Eric Idle': (1943, -1, 'South Shields', 'English'),
            'Terry Jones': (1942, -1, 'Colwyn Bay', 'English'),
            'Michael Palin': (1943, -1, 'Sheffield', 'History'),
            'Terry Gilliam': (1940, -1, 'Minneapolis', 'Political Science'),
        }

4 Then we get the reference to self.dictionary and store it for later use.

5 PyDict_GetItemString(rDict, who) is equivalent to the statement:
    tuple = self.dictionary[who]

6 This is a bit of paranoid code: we check that we really retrieved a tuple.

7 Finally, we unpack the tuple using the format string.

To compile and link you would use something like this (on Win32):

cl -c dictionary.c -I\pystuff\python-1.5.2\Include \
    -I\pystuff\python-1.5.2\PC -I.
link dictionary.obj \pystuff\python-1.5.2\PCbuild\python15.lib \
    -out:dict.exe

If you run dict.exe, you’ll see output similar to figure 14.1.

Figure 14.1 Python embedded in a C application

14.8 Summary

You may never need to build a Python extension or embed Python in an application, but in some cases it is the only way to interface with a particular system or develop code economically. Although the information contained in this chapter is accurate at the time of writing, I suggest that you visit www.python.org to obtain information about the current release.