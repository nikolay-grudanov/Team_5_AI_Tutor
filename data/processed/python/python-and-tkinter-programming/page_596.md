---
source_image: page_596.png
page_number: 596
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.25
tokens: 8252
characters: 1803
timestamp: 2025-12-24T00:48:40.820533
finish_reason: stop
---

• first + spec   It is assumed that the rest of the argument (after first) is a standard geometry specification. The window will be positioned using this specification the first time it is activated. On subsequent activations it will be positioned in the same position as the last time it was displayed, even if it has been moved by the user. For example, geometry = first+100+100 will initially display the window at position (100,100). Other calls to activate() will not change the previous position of the window.
• spec   This is a standard geometry specification. The window will be positioned using this specification.

If the BLT Tcl extension library is present, a clock cursor will be displayed until the window is deactivated.
    If the activatemethod option is callable, it is called just before the window begins to wait for the result.
    If master is not None, the window will become a transient window of master. The master should be another existing toplevel window.

MegaWidget

Description
This class creates a megawidget contained within a Frame window. The class acts as the base class for megawidgets that are not contained in their own toplevel window, such as Pmw.ButtonBox and Pmw.ComboBox. It creates a Frame component named hull to act as the container of the megawidget. The window class name for the hull widget is set to the most-specific class name for the megawidget. Derived classes specialize this widget by creating other widget components as children of the hull widget.

Inheritance
MegaWidget inherits from Pmw.MegaArchetype.

Components
hull
This acts as the body for the entire megawidget. Other components are created as children of the hull to further specialize the widget.

Methods
destroy()
Destroys the hull component widget, including all of its children.