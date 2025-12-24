---
source_image: page_460.png
page_number: 460
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.65
tokens: 8357
characters: 2543
timestamp: 2025-12-24T00:44:40.003344
finish_reason: stop
---

clipboard_clear()
Claims ownership of the clipboard on the window’s display and removes any previous contents.

configure(option=None)
Queries or modifies the configuration options of the widget. If no option is specified, returns a dictionary describing all of the available options for the widget. If one or more option-value pairs are specified, then the method modifies the given widget option(s) to have the given value(s); in this case the method returns None.

destroy()
Destroys the widget and removes all references from namespace.

event_add(virtual, *sequences)
Associates the virtual event virtual with the physical event sequence(s) given by the sequence arguments, so that the virtual event will trigger whenever any one of the sequences occurs. Virtual may be any string value and sequence may have any of the values allowed for the sequence argument to the bind method. If virtual is already defined, the new physical event sequences add to the existing sequences for the event.

event_delete(virtual, *sequences)
Deletes each of the sequences from those associated with the virtual event given by virtual. Virtual may be any string value and sequence may have any of the values allowed for the sequence argument to the bind method. Any sequences not currently associated with virtual are ignored. If no sequence argument is provided, all physical event sequences are removed for virtual, so that the virtual event will not trigger anymore.

event_generate(sequence, option=value...)
Generates a window event and arranges for it to be processed just as if it had come from the window system. Sequence provides a basic description of the event, such as <Shift-Button-2>. Sequence may have any of the forms allowed for the sequence argument of the bind method except that it must consist of a single event pattern, not a sequence. Option-value pairs may be used to specify additional attributes of the event, such as the x and y mouse position.

event_info(virtual=None)
Returns information about virtual events. If the virtual argument is omitted, the return value is a tuple of all the virtual events that are currently defined. If virtual is specified then the return value is a tuple whose elements are the physical event sequences currently defined for the given virtual event; if the virtual event is not defined then None is returned.

focus_displayof()
Returns the name of the focus window on the display containing the widget. If the focus window for widget’s display isn’t in this application, the return value is None.