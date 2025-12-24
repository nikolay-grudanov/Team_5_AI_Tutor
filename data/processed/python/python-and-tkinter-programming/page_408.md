---
source_image: page_408.png
page_number: 408
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.35
tokens: 8144
characters: 1336
timestamp: 2025-12-24T00:42:45.295749
finish_reason: stop
---

APPENDIX A

Mapping Tk to Tkinter

This appendix details the mapping of Tk commands and arguments into Tkinter methods and options. The order of the mappings somewhat follows the sequence presented in a reference guide published by Paul Raines and Jeff Trainer for Tcl/Tk (Tcl/Tk is a Nutshell: A Desktop Quick Reference is published by O’Reilly and Associates, Inc.). The mappings do not contain any Tcl information, however. I assume that you want to directly translate Tk directives into Tkinter. In many cases, there may be better means of implementing a Tcl/Tk code sequence in Tkinter. Tkinter implements many of the Tk commands as inherited widget methods, which may cause some initial confusion for Tcl/Tk programmers.

General Tk widget information

All widgets are created with:

    widget = Widget(master [, option=value [, option=value]])

where Widget is the Tkinter class of widget desired (such as Button) and widget is the instance. Widget configuration options may be passed as arguments to the creation call. Options begin with a keyword and are always followed by a value or a string. After creation, options may be changed using the configure method and accessed using the cget method. Optionally, access may be references to the dictionary keys in the widget (value = widget['option'] or widget['option'] = value).