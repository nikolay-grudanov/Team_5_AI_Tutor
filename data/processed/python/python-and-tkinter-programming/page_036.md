---
source_image: page_036.png
page_number: 36
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.49
tokens: 8327
characters: 2314
timestamp: 2025-12-24T00:32:26.544552
finish_reason: stop
---

1.3.6 Private and public variables and methods

Unless you take special action, all variables and methods are public and virtual. If you make use of name mangling, however, you can emulate private variables and methods. You mangle the name this way: Any name which begins with a double-underscore (__ ) is private and is not exported to a containing environment. Any name which begins with a single underscore (_) indicates private by convention, which is similar to protected in C++ or Java. In fact, Python usually is more intuitive than C++ or other languages, since it is immediately obvious if a reference is being made to a private variable or method.

1.3.7 Inheritance

The rules of inheritance in Python are really quite simple:

• Classes inherit behavior from the classes specified in their header and from any classes above these classes.
• Instances inherit behavior from the class from which they are created and from all the classes above this class.

When Python searches for a reference it searches in the immediate namespace (the instance) and then in each of the higher namespaces. The first occurrence of the reference is used; this means that a class can easily redefine attributes and methods of its superclasses. If the reference cannot be found Python reports an error.

Note that inherited methods are not automatically called. To initialize the base class, a subclass must call the __init__ method explicitly.

1.3.8 Multiple inheritance

Multiple inheritance in Python is just an extension of inheritance. If more than one class is specified in a class’s header then we have multiple inheritance. Unlike C++, however, Python does not report errors if attributes of classes are multiple defined; the basic rule is that the first occurrence found is the one that is used.

1.3.9 Mixin classes

A class that collects a number of common methods and can be freely inherited by subclasses is usually referred to as a mixin class (some standard texts may use base, generalized or abstract classes, but that may not be totally correct). Such methods could be contained in a Python module, but the advantage of employing a mixin class is that the methods have access to the instance self and thus can modify the behavior of an instance. We will see examples of mixin classes throughout this book.