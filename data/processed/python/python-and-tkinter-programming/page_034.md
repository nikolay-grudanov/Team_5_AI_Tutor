---
source_image: page_034.png
page_number: 34
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.81
tokens: 8316
characters: 2120
timestamp: 2025-12-24T00:32:22.514764
finish_reason: stop
---

1.3 Classes

I’m including a short section on Python classes largely for C++ programmers who may need to learn some of the details of Python’s implementation and for Python programmers who have yet to discover OOP in Python.

1.3.1 How do classes describe objects?

A class provides the following object descriptions:

• The attributes (data-members) of the object
• The behavior of the object (methods)
• Where behavior is inherited from other classes (superclasses)

Having said all that, C++ programmers will probably be tuning out at this point—but hold on for a little longer. There are some valuable features of Python classes, some of which may come as a bit of a surprise for someone who is not fully up to speed with Python OOP.

Most of the examples of applications in this book rely heavily on building class libraries to create a wide range of objects. The classes typically create instances with multiple formats (see LEDs and Switches in chapter 7). Before we start building these objects, let’s review the rules and features that apply to Python classes.

1.3.2 Defining classes

A Python class is a user-defined data type which is defined with a class statement:

class AClass:
    statements

Statements are any valid Python statements defining attributes and member functions. In fact, any Python statement can be used, including a pass statement, as we will see in the next section. Calling the class as a function creates an instance of the class:

anInstanceOfAClass = AClass()

1.3.3 Neat Python trick #10

A class instance can be used like a C structure or Pascal record. However, unlike C and Pascal, the members of the structure do not need to be declared before they are used—they can be created dynamically. We can use this ability to access arbitrary data objects across modules; examples using class instances to support global data will be shown later.

class DummyClass:
    pass

Colors = DummyClass()
Colors.alarm    = 'red'
Colors.warning = 'orange'
Colors.normal   = 'green'

If the preceding lines are stored in a file called programdata.py, the following is a possible code sequence.