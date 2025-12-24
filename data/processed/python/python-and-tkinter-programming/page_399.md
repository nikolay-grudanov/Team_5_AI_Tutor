---
source_image: page_399.png
page_number: 399
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.22
tokens: 8127
characters: 1110
timestamp: 2025-12-24T00:42:26.180487
finish_reason: stop
---

CHAPTER 19

Distributing Tkinter applications

19.1 General issues in distributing applications 374
19.2 Distributing Unix applications 375
19.3 Distributing Win32 applications 376
19.4 Python distribution tools 379

If you follow the Python news group for a few weeks, you will see at least one question being raised repeatedly: “How do I distribute Python applications?”. In this chapter we will look at some options for UNIX and Win32. UNIX is relatively easy to handle, but Win32 has several possible solutions.

19.1 General issues in distributing applications

The main issue in distributing and installing a Python application is making sure that the end user has all of the components that are required for the application to run. You have several alternatives in deciding how to achieve this, but you first have to make sure that most of these components are present on the end user’s system:

1 Python executable (python, python.exe).
2 Launcher for your application (xxx script for UNIX, xxx.bat for Win32).
3 Python shared-object files (xxx.so) for UNIX, dynamic load libraries (xxx.dll) for Win32.