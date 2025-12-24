---
source_image: page_592.png
page_number: 592
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.94
tokens: 8344
characters: 2286
timestamp: 2025-12-24T00:48:44.211280
finish_reason: stop
---

Inheritance
MegaArchetype inherits from None.

Methods

addoptions(optionDefs)
Adds additional options for this megawidget. The optionDefs argument is treated in the same way as the defineoptions() method. This method is used by derived classes. It is only used if a megawidget should conditionally define some options, perhaps depending on the value of other options. Usually, megawidgets unconditionally define all their options in the call to defineoptions() and do not need to use addoptions(). This method may be called after the call to defineoptions() and before the call to initialiseoptions().

cget(option)
Returns the current value of option (which should be in the format described in the Options section). This method is also available using object subscripting, for example myWidget['font']. Unlike Tkinter’s cget(), which always returns a string, this method returns the same value and type as used when the option was set (except where option is a component option and the component is a Tkinter widget, in which case it returns the string returned by Tcl/Tk).

component(name)
Returns the component widget whose name is name. This allows the user of a megawidget to access and configure component widgets directly.

componentaliases()
Returns the list of aliases for components. Each item in the list is a tuple whose first item is the name of the alias and whose second item is the name of the component or subcomponent it refers to.

componentgroup(name)
Returns the group of the component whose name is name or None if it does not have a group.

components()
Returns a sorted list of names of the components of this megawidget.

configure (option = None, ** kw)
Queries or configures the megawidget options. If no arguments are given, returns a tuple consisting of all megawidget options and values, each as a 5-element tuple (name, resourceName, resourceClass, default, value). This is in the same format as the value returned by the standard Tkinter configure() method, except that the resource name is always the same as the option name and the resource class is the option name with the first letter capitalized.
If one argument is given, it returns the 5-element tuple for option. Otherwise, it sets the configuration options specified by the keyword arguments.