---
source_image: page_612.png
page_number: 612
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.56
tokens: 8234
characters: 1659
timestamp: 2025-12-24T00:49:10.531661
finish_reason: stop
---

Components

hull
This acts as the body for the entire megawidget. Other components are created as children of the hull to further specialize the widget.

Methods

add(name, ** kw)
Adds a pane to the end of the paned widget using the component name name. This is equivalent to calling insert() with before set to the current number of panes. The method returns the name component widget.

configurepane(name, ** kw)
Configures the pane specified by name, where name is either an integer, specifying the index of the pane, or a string, specifying the name of the pane. The keyword arguments specify the new values for the options for the pane. These options are described in the Pane options section.

insert(name, before = 0, ** kw)
Adds a pane just before (that is, to the left of or above) the pane specified by before, where before is either an integer, specifying the index of the pane, or a string, specifying the name of the pane. The keyword arguments specify the initial values for the options for the new pane. These options are described in the Pane options section. To add a pane to the end of the paned widget, use add().

pane(name)
Returns the Frame pane widget for the pane specified by name, where name is either an integer, specifying the index of the pane, or a string, specifying the name of the pane.

panes()
Returns a list of the names of the panes, in display order.

remove(name)
Removes the pane specified by name, where name is either an integer, specifying the index of the pane, or a string, specifying the name of the pane.

PromptDialog

Description
A PromptDialog is a convenience dialog window that requests input from the user.