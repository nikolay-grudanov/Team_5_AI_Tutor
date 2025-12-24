---
source_image: page_030.png
page_number: 30
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.94
tokens: 8455
characters: 2587
timestamp: 2025-12-24T00:32:22.038680
finish_reason: stop
---

The result is a system that may be used as a scripting language to develop anything from some system administration scripts all the way to a complex GUI-based application (using database, client/server, CORBA or other techniques).

1.1.2 Where can Python be used?

Knowing where Python can be used is best understood by learning where it might not be the best choice. Regardless of what I just said about the bytecode engine, Python has an interpretive nature, so if you can’t keep within the C-extensions, there has to be a performance penalty. Therefore, real-time applications for high-speed events would be a poor match. A set of extensions to Python have been developed specifically for numerical programming (see “NumPy” on page 626). These extensions help support compute-bound applications, but Python is not the best choice for huge computation-intensive applications unless time isn’t a factor. Similarly, graphics-intensive applications which involve real-time observation are not a good match (but see “Speed drawing” on page 271 for an example of what can be done).

1.2 Key data types: lists, tuples and dictionaries

Three key data types give Python the power to produce effective applications: two sequence classes—lists and tuples—and a mapping class—dictionaries. When they are used together, they can deliver surprising power in a few lines of code.

Lists and tuples have a lot in common. The major difference is that the elements of a list can be modified in place but a tuple is immutable: you have to deconstruct and then reconstruct a tuple to change individual elements. There are several good reasons why we should care about this distinction; if you want to use a tuple as the key to a dictionary, it’s good to know that it can’t be changed arbitrarily. A small advantage of tuples is that they are a slightly cheaper resource since they do not carry the additional operations of a list.

If you want an in-depth view of these data types take a look at chapters 6 and 8 of Quick Python.

1.2.1 Lists

Let’s look at lists first. If you are new to Python, remember to look at the tutorial that is available in the standard documentation, which is available at www.python.org.

Initializing lists
Lists are easy to create and use. To initialize a list:

lst = []                # Empty list
lst = ['a', 'b', 'c']    # String list
lst = [1, 2, 3, 4]       # Integer list
lst = [[1,2,3], ['a','b','c']]   # List of lists
lst = [(1,'a'),(2,'b'),(3,'c')]  # List of tuples

Appending to lists
Lists have an append method built in:

lst.append('e')
lst.append((5,'e'))