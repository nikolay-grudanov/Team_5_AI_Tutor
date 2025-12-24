---
source_image: page_594.png
page_number: 594
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.57
tokens: 8453
characters: 2769
timestamp: 2025-12-24T00:48:51.170156
finish_reason: stop
---

megawidget or one of its base classes); or if it references, by name, a component of the megawidget; or if it references, by group, at least one component.
It also calls the configuration callback function for all configuration options.
This method is only effective when called by the constructor of the leaf class, that is, if myClass is the same as the class of the object being constructed. The method returns immediately when called by the constructors of base classes.

interior()
Returns the widget framing the interior space in which any children of this megawidget should be created. By default, this returns the hull component widget, if one was created, or None otherwise. A subclass should use the widget returned by interior() as the parent of any components or sub-widgets it creates. Megawidgets which can be further subclassed, such as Pmw.Dialog, should redefine this method to return the widget in which subclasses should create children. The overall containing widget is always available as the hull component.

isinitoption(option)
If option is an initialization option, returns true. Otherwise returns false (the option is a configuration option). The option argument must be an option of this megawidget, not an option of a component. Otherwise an exception is raised.

options()
Returns a sorted list of this megawidget’s options. Each item in the list is a 3-element tuple, (option, default, isinit), where option is the name of the option, default is its default value and isinit is true if the option is an initialization option.

MegaToplevel

Description
This class creates a megawidget contained within a toplevel window. It may be used directly to create a toplevel megawidget or it may be used as a base class for more specialized toplevel megawidgets, such as Pmw.Dialog. It creates a Toplevel component, named hull, to act as the container of the megawidget. The window class name for the hull widget is set to the most-specific class name for the megawidget. Derived classes specialize this widget by creating other widget components as children of the hull widget.

The megawidget may be used as either a normal toplevel window or as a modal dialog. Use show() and withdraw() for normal use and activate() and deactivate() for modal dialog use. If the window is deleted by the window manager while being shown normally, the default behavior is to destroy the window. If the window is deleted by the window manager while the window is active (such as when it is used as a modal dialog), the window is deactivated. Use the userdeletefunc() and usermodaldeletefunc() methods to override these behaviors. Do not call protocol() to set the WM_DELETE_WINDOW window manager protocol directly if you want to use this window as a modal dialog.