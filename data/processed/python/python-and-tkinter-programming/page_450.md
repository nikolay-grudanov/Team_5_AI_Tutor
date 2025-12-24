---
source_image: page_450.png
page_number: 450
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.29
tokens: 8138
characters: 1404
timestamp: 2025-12-24T00:44:02.961147
finish_reason: stop
---

APPENDIX B

Tkinter reference

About this appendix

The information presented in this appendix has been largely generated using Python programs that use the Tkinter module dictionary and the Tk man pages, which were parsed and edited to correspond to Python use and stored in a huge dictionary. The programs produced a large ASCII file which contained headings, text and tables ready for importing into FrameMaker, which was used to produce this book. Some of the information required manual adjustment, but the bulk of data required only formatting in FrameMaker. The scripts did not take long to develop.

You will find references to both Tcl and Tk. I have left them in the text, where appropriate, since it is worth remembering that Tkinter is, ultimately, just an interface to them and it is Tcl/Tk that determines whether supplied arguments are valid and appropriate.

Common options

Many widgets accept options which are common with other widgets. There may be small differences in the absolute values, but they are similar enough for them to be documented as a group here. In general, many of the descriptions are derived from the Tk man pages, since Tkinter provides a simple interface to the underlying Tk widgets where options are considered. However, since Tkinter provides an object-oriented wrapper to Tk, some of the descriptions required considerable modification to the Tkinter context.