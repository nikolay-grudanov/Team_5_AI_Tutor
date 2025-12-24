---
source_image: page_029.png
page_number: 29
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.65
tokens: 8529
characters: 3093
timestamp: 2025-12-24T00:32:28.766799
finish_reason: stop
---

This chapter is really not necessary for most readers, then, since the material will already be familiar. Its purpose is to provide a refresher course for readers who worked with Python in the early days and a map for Tcl/Tk programmers and those readers experienced with other languages.

Readers unfamiliar with object-oriented programming (OOP) may find section 1.3 useful as an introduction to OOP as it is implemented in Python. C++ or Java programmers who need to see how Python’s classes operate will benefit as well.

I’m not going to explain the reasons why Python was developed or when, since this information is covered in every other Python book very well. I will state that Guido van Rossum, Python’s creator, has been behind the language since he invented it at Stichting Mathematisch Centrum (CWI) in Amsterdam, The Nederlands, around 1990; he is now at the Corporation for National Research Initiatives (CNRI), Reston, Virginia, USA. The fact that one person has taken control of the growth of the language has had a great deal to do with its stability and elegance, although Guido will be the first to thank all of the people who have contributed, in one way or another, to the language’s development.

Perhaps more important than any of the above information is the name of the language. This language has nothing to do with snakes. Python is named after Monty Python’s Flying Circus, the BBC comedy series which was produced from 1969 to 1974. Like many university students around 1970, I was influenced by Monty Python, so when I started writing this book I could not resist the temptation to add bits of Python other than the language. Now, all of you that skipped the boring beginning bit of this book, or decided that you didn’t need to read this paragraph are in for a surprise. Scattered through the examples you’ll find bits of Python. If you have never experienced Monty Python, then I can only offer the following advice: if something about the example looks weird, it’s probably Python. As my Yugoslavian college friend used to say “You find that funny”?

1.1.1 Why Python?

Several key features make Python an ideal language for a wide range of applications. Adding Tkinter to the mix widens the possibilities dramatically. Here are some of the highlights that make Python what it is:

• Automatic compile to bytecode
• High-level data types and operations
• Portability across architectures
• Wide (huge) range of supported extensions
• Object-oriented model
• Ideal prototyping system
• Readable code with a distinct C-like quality supports maintenance
• Easy to extend in C and C++ and embed in applications
• Large library of contributed applications and tools
• Excellent documentation

You might notice that I did not mention an interpreter explicitly. One feature of Python is that it is a bytecode engine written in C. The extension modules are written in C. With a little care in the way you design your code, most of your code will run using compiled C since many operations are built into the system. The remaining code will run in the bytecode engine.