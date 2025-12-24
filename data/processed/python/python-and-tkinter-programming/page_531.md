---
source_image: page_531.png
page_number: 531
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.07
tokens: 8347
characters: 2234
timestamp: 2025-12-24T00:46:55.844088
finish_reason: stop
---

unpost()
Unmaps the window so that it is no longer displayed. If a lower-level cascaded menu is posted, unpost that menu. Returns an empty string. This method does not work on Windows and Macintosh, as those platforms have their own way of unposting menus.

yposition(index)
Returns an integer giving the y-coordinate within the menu window of the top-most pixel in the entry specified by index.

Menubutton

![Screenshot of a menubutton widget showing a dropdown menu with various options](images/menubutton.png)

Description
The Menubutton class defines a new window and creates an instance of a menubutton widget. Additional options, described below, may be specified in the method call or in the option database to configure aspects of the menubutton such as its colors, font, text, and initial relief. The menubutton method returns the identity of the new widget. At the time this method is invoked, the menubutton’s parent must exist.

A menubutton is a widget that displays a textual string, bitmap, or image and is associated with a menu widget. If text is displayed, it must all be in a single font, but it can occupy multiple lines on the screen (if it contains newlines or if wrapping occurs because of the wrapLength option) and one of the characters may optionally be underlined using the underline option.

In normal usage, pressing mouse button 1 over the menubutton causes the associated menu to be posted just underneath the menubutton. If the mouse is moved over the menu before releasing the mouse button, the button release causes the underlying menu entry to be invoked. When the button is released, the menu is unposted. Menubuttons are typically organized into groups called menu bars that allow scanning: if the mouse button is pressed over one menubutton (causing it to post its menu) and the mouse is moved over another menubutton in the same menu bar without releasing the mouse button, then the menu of the first menubutton is unposted and the menu of the new menubutton is posted instead.

There are several interactions between menubuttons and menus; see the menu entry for information on various menu configurations, such as pulldown menus and option menus.

Inheritance
Menubutton inherits from Widget.