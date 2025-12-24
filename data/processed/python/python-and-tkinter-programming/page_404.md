---
source_image: page_404.png
page_number: 404
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.60
tokens: 8151
characters: 1313
timestamp: 2025-12-24T00:42:34.756534
finish_reason: stop
---

Clearly, there are other ways to achieve this effect, and if you scan the Python news group (see “Python News Group” on page 626) you will find other suggestions on how to do this quite frequently.

19.4 Python distribution tools

A number of tools are available to an application developer and more are being developed. I am not going to cover these tools here, since there are such wide application targets to be covered.

One of the tools worth looking at is freeze, which wraps your Python application and all of the necessary support modules in an embedded C-program. To date, I have not found a need to use it, but I am certain that it may be a solution for some of you.

Another tool is SqueezeTool, which squeezes a Python application and all of its support modules into a single, compressed package. You can find more details in the “References” section (see “PythonWorks” on page 626).

There is also a Distutils special interest group (SIG) for people who are working to develop tools to distribute Python applications, both with and without C extensions, to all platforms. By the time this book is available, the early versions of these tools will have undergone considerable testing. Take a look at http://www.python.org/sigs/distutils-sig/ for the latest information on this interesting development.