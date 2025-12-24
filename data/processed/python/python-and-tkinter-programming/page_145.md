---
source_image: page_145.png
page_number: 145
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.12
tokens: 8159
characters: 1277
timestamp: 2025-12-24T00:35:16.174348
finish_reason: stop
---

CHAPTER 7

Using classes, composites and special widgets

7.1 Creating a Light Emitting Diode class  120
7.2 Building a class library  129
7.3 Summary  139

The Object-Oriented Programming (OOP) capabilities of Python position the language as an ideal platform for developing prototypes and, in most cases, complete applications. One problem of OOP is that there is much argument over the methodologies (Object-Oriented Analysis and Design—OOAD) which lead to OOP, so many developers simply avoid OOP altogether and stay with structured programming (or unstructured programming in some case). There is nothing really magical about OOP; for really simple problems, it might not be worth the effort. However, in general, OOP in Python is an effective approach to developing applications. In this chapter, we are making an assumption that the reader is conversant with OOP in C++, Java or Python, so the basic concepts should be understood. For an extended discussion of this subject, Harms’ & McDonald’s Quick Python or Lutz and Ascher’s Learning Python.

7.1 Creating a Light Emitting Diode class

The following example introduces an LED class to define Light Emitting Diode objects. These objects have status attributes of on, off, warn and alarm (corresponding to typical net-