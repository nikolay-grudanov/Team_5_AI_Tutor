---
source_image: page_627.png
page_number: 627
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.76
tokens: 8228
characters: 1672
timestamp: 2025-12-24T00:49:33.095538
finish_reason: stop
---

hull
This acts as the body for the entire megawidget. Other components are created as children of the hull to further specialize the widget.

label
If the labelfpos option is not None, this component is created as a text label for the megawidget. See the labelfpos option for details. Note that to set, for example, the text option of the label, you need to use the label_text component option.

text
The text widget which is scrolled by the scrollbars. If the borderframe option is true, this is created with a borderwidth of 0 to overcome a known problem with text widgets: if a widget inside a text widget extends across one of the edges of the text widget, then the widget obscures the border of the text widget. Therefore, if the text widget has no border, then this overlapping does not occur.

vertscrollbar
The vertical scrollbar. Its component group is Scrollbar.

Methods

bbox(index)
This method is explicitly forwarded to the text component’s bbox() method. Without this explicit forwarding, the bbox() method (aliased to grid_bbox()) of the hull would be invoked, which is probably not what the programmer intended.

clear()
Deletes all text from the text component.

exportfile(fileName)
Writes the contents of the text component to the file fileName.

get(first = None, last = None)
This is the same as the get() method of the text component, except that if neither first nor last are specified the entire contents of the text widget are returned.

importfile(fileName, where = 'end')
Reads the contents of the file fileName into the text component at the position given by where.

settext(text)
Replaces the entire contents of the text component with text.