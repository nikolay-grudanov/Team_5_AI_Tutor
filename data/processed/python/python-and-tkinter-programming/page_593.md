---
source_image: page_593.png
page_number: 593
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.15
tokens: 8467
characters: 2884
timestamp: 2025-12-24T00:48:51.462449
finish_reason: stop
---

createcomponent(name, aliases, group, widgetClass, widgetArgs, ** kw)
Creates a component widget by calling widgetClass with the arguments given by widgetArgs and any keyword arguments. The name argument is the name by which the component will be known and must not contain the underscore character (_). The group argument specifies the group of the component. The aliases argument is a sequence of 2-element tuples, whose first item is an alias name and whose second item is the name of the component or subcomponent it is to refer to.

createlabel(parent, childCols = 1, childRows = 1)
Creates a Label component named label in the parent widget. This convenience method is used by several megawidgets that require an optional label. The widget must have options named labelfpos and labelmargin. If labelfpos is None, no label is created. Otherwise, a label is created and positioned according to the value of labelfpos and labelmargin. The label is added to the parent using the grid() method, with childCols and childRows indicating how many rows and columns the label should span. Note that all other child widgets of the parent must be added to the parent using the grid() method. The createlabel() method may be called by derived classes during megawidget construction.

defineoptions(keywords, optionDefs)
Creates options for this megawidget. The optionDefs argument defines the options. It is a sequence of 3-element tuples, (name, default, callback), where name is the name of the option, default is its default value and callback is the function to call when the value of the option is set by a call to configure(). The keywords argument should be the keyword arguments passed in to the constructor of a megawidget. The user may override the default value of an option by supplying a keyword argument to the constructor.
This should be called before the constructor of the base class, so that default values defined in a derived class override those in a base class.
If callback is Pmw.INITOPT, then the option is an initialization option.

destroycomponent(name)
Removes the megawidget component called name. This method may be called by derived classes to destroy a megawidget component. It destroys the component widget and then removes all record of the component from the megawidget.

hulldestroyed()
Returns true if the Tk widget corresponding to the hull component has been destroyed.

initialiseoptions(myclass)
Checks keyword arguments and calls option callback functions. This must be called at the end of a megawidget constructor with myClass set to the class being defined. It checks that all keyword arguments given to the constructor have been used. If not, it raises an error indicating which arguments were unused. A keyword is defined to be used if, during the construction of a megawidget, it is defined in a call to defineoptions() or addoptions() (by the