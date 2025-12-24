---
source_image: page_035.png
page_number: 35
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.48
tokens: 8312
characters: 2092
timestamp: 2025-12-24T00:32:22.524876
finish_reason: stop
---

from programdata import Colors
...
Button(parent, bg=Colors.alarm, text='Pressure\nVessel',
    command=evacuateBuilding)

Alternately, if you apply a little knowledge about how Python manages data internally, you can use the following construction.

class Record:
    def __init__(self, **kw):
        self.__dict__.update(kw)
Colors = Record(alarm='red', warning='orange', normal='green')

1.3.4 Initializing an instance

Fields (instance variables) of an instance may be initialized by including an __init__ method in the class body. This method is executed automatically when a new instance of the class is created. Python passes the instance as the first argument. It is a convention to name it self (it’s called this in C++). In addition, methods may be called to complete initialization. The __init__ methods of inherited classes may also be called, when necessary.

class ASX200(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        Pack.config(self)
        self.state = NORMAL
        self.set_hardware_data(FORE)
        self.createWidgets()
    ...
    ...
switch = ASX200()

Note To use instance variables you must reference the containing object (in the previous example it is switch.state, not self.state). If you make a reference to a variable by itself, it is to a local variable within the executing function, not an instance variable.

1.3.5 Methods

We have already encountered the __init__ method that is invoked when an instance is created. Other methods are defined similarly with def statements. Methods may take arguments: self is always the first or only argument.

You will see plenty of examples of methods, so little discussion is really necessary. Note that Python accepts named arguments, in addition to positional arguments, in both methods and function calls. This can make supplying default values for methods very easy, since omission of an argument will result in the default value being supplied. Take care when mixing positional and named arguments as it is very easy to introduce problems in class libraries this way.