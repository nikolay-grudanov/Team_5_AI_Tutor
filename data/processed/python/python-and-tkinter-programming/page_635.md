---
source_image: page_635.png
page_number: 635
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.73
tokens: 8148
characters: 1313
timestamp: 2025-12-24T00:49:48.566572
finish_reason: stop
---

APPENDIX D

Building and installing Python, Tkinter

In general, you will not need to build Python or its components from source; binary distributions are readily available from www.python.org for several UNIX variants, Win32, and MacOS. However, if you intend to build extensions to Python you will need to obtain the sources for Python and sometimes for Tcl and Tk.

If you do decide to build Python, you may also want to build Tcl/Tk. The information presented here is for Python 1.5.2 and Tcl/Tk 8.0.5, which were the stable releases at the time of writing. For newer releases, you should visit the respective web pages for up-to-date information.

We will look at building everything for UNIX, Win32, and MacOS in turn.

Building for UNIX

Building Python and Tkinter for UNIX is probably the most straightforward process when compared to the other architectures. Personally, I’ve had only two UNIX systems that have given me trouble and the problems can be attributed to the fact that they were new systems.

Before starting, you will need to obtain the appropriate source distributions.

Obtaining source distributions

Before collecting any source, decide where you are going to store the source files. You are going to have three directories (Python, Tcl and Tk) each with their revision as a suffix. You