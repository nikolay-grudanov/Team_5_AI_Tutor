---
source_image: page_400.png
page_number: 400
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.98
tokens: 8525
characters: 3147
timestamp: 2025-12-24T00:42:50.153602
finish_reason: stop
---

4 Extension libraries (Python/Lib/lib-dynload/xxx.[so|dll]).
5 Python library files (Python/Lib/xxx.py).
6 Application-specific Python library files (appropriate location).
7 Tcl/Tk runtime (Tcl/bin, Tcl/lib, Tk/bin, /Tk/lib etc.).
8 Pmw (Python/Lib/Pmw).
9 Any other extensions, data files, or databases that your application requires.

One decision you will have to make is whether you will handle the distribution of Python and/or Tcl/Tk separately, either leaving it to the end user to install these items independently, or distributing them with your application. In general, the latter method is preferable, since Python is still expanding in popularity and currently will not be installed on many of the end users’ systems. Of course, we fully expect this to change in the future!

If you do decide to distribute Python and Tcl/Tk with your application, you have another decision to make—whether to install them publicly so that the end user has easy access to Python and/or Tcl/Tk, or locally so that they are accessed through your application. It is usually possible to install them publicly, although for Win32 it is often easier to use a local installation.

Finally, you must consider the architectures that your application is going to support. If you are targeting Win32 exclusively, then your task is quite simple. However, there are multiple UNIX architectures, which are normally supported by building from source. You probably do not want to be responsible for these builds, so you will have to consider supplying binaries for specific platforms. This is a totally different problem which requires careful consideration of both business and technical issues. It is beyond the scope of a short section such as this one..

19.2 Distributing UNIX applications

Supporting your application is usually a simple task once you have access to a built Python and Tcl/Tk. In general, UNIX end users are capable of building and installing both of these so you may be able to simply require your end users to take care of them. Then your application installation may be as simple as extracting files from a tar file and editing the users’ environments appropriately. For the moment, let’s assume that this is the case, so we will concentrate on getting your application up and running.

First, we need an executable to start your application. Our aim here is to use a minimal Python script to get into your application’s main module (remember that a Python script will be interpreted every time you invoke it, so you want to keep the script simple; see “Everyday speedups” on page 348).

Here is an example of a minimal script:

#!/usr/bin/env python
import myapplication
myapplication.main()

There are some cases where you cannot use #!/usr/bin/env python, so you might have to give an explicit path such as /usr/local/bin/python. One small reminder: the space in the first form is meant to be there; it is not uncommon for UNIX folks to unconsciously translate the space into a slash. Next, you might need to add a little bit more to make this work. The script assumes that the environment variable PYTHONPATH has been set and it includes