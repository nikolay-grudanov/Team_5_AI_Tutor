---
source_image: page_641.png
page_number: 641
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.88
tokens: 8098
characters: 1045
timestamp: 2025-12-24T00:49:51.953699
finish_reason: stop
---

12 Move python.exe, pythonw.exe, python15.dll and _tkinter.pyd to the directory you wish to run Python from (see “Distributing Tkinter applications” on page 374 for further details).

Building for MacOS

I have to admit that I do not build the MacOS version of Tcl/Tk or Python. I have been informed that you do not need to build Tcl/Tk for MacOS; the standard installer contains a complete Tcl/Tk installation.

Visit www.python.org and find the latest version of Python (you will usually find a reference to the current version in the Topics panel). This should point you to the source distribution page; at the time of writing, it is www.cwi.nl/~jack/macpython.html. There you will find Stuffit and BinHex versions of the source. The source for the MacOS distribution is almost identical to the UNIX distribution, although you will retrieve the Stuffit or binhex version. Retrieve the Python distribution and copy the file to the location you have chosen.

Once you have retrieved the files, follow the instructions included with the release.