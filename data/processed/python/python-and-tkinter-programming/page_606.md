---
source_image: page_606.png
page_number: 606
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.04
tokens: 8242
characters: 1627
timestamp: 2025-12-24T00:49:00.596550
finish_reason: stop
---

Components

hull
This acts as the body for the entire megawidget. Other components are created as children of the hull to further specialize the widget.

nbframe
By default, this component is a Canvas.

Methods

add(pagename, ** kw)
Adds a page at the end of the notebook. See the insert() method for full details.

initialise(e = None, w = 1, h = 1)

interior()
Returns the widget framing the interior space in which any children of this megawidget should be created. By default, this returns the hull component widget, if one was created, or None otherwise. A subclass should use the widget returned by interior() as the parent of any components or sub-widgets it creates. Megawidgets which can be further subclassed, such as Pmw.Dialog, should redefine this method to return the widget in which subclasses should create children. The overall containing widget is always available as the hull component.

lift(pagenameOrIndex)
If pagenameOrIndex is a string, it raises the pane with that name. If pagenameOrIndex is an integer, it raises the page with index.

pagecget(pagename, option)
Returns the value of option for the pane pagename.

pageconfigure(pagename, ** kw)
Configures the pane specified by pagename, where name is a string, specifying the name of the pane. The keyword arguments specify the new values for the options for the pane.

pages()
Returns a list of the panes currently defined in the notebook.

raised()
Returns the name of the pane that is currently at the top of the stack.

tkdelete(pagename)
Removes the pane and tab button for pane pagename.

tkraise(pagenameOrIndex)
tkraise is an alias for lift.