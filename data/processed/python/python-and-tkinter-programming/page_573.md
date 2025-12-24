---
source_image: page_573.png
page_number: 573
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.22
tokens: 8306
characters: 2081
timestamp: 2025-12-24T00:48:07.793234
finish_reason: stop
---

Methods

add(name, **kw)
Adds a button to the end of the button box as a component named name. Any keyword arguments present will be passed to the constructor when creating the button. If the text keyword argument is not given, the text option of the button defaults to name. The method returns the name component widget.

alignbuttons(when = 'later')
Sets the widths of all the buttons to be the same as the width of the widest button. If when is later, this will occur when the interpreter next becomes idle; otherwise, the resizing will occur immediately.

delete(index)
Deletes the button given by index from the button box. index may have any of the forms accepted by the index() method.

index(index, forInsert = 0)
Returns the numerical index of the button corresponding to index. This may be specified in any of the following forms:
• number Specifies the button numerically, where 0 corresponds to the left (or top) button.
• end Indicates the right (or bottom) button.
• default Indicates the current default button.
• name Specifies the button named name.

If forInsert is true, end returns the number of buttons rather than the index of the last button.

insert(name, before = 0, **kw)
Adds a button just before the button specified by before, as a component named name. Any keyword arguments present will be passed to the constructor when creating the button. before may have any of the forms accepted by the index() method. To add a button to the end of the button box, use add(). The method returns the name component widget.

invoke(index = 'default', noFlash = 0)
Invokes the callback command associated with the button specified by index. Unless noFlash is true, flashes the button to indicate to the user that something happened. index may have any of the forms accepted by the index() method.

numbuttons()
Returns the number of buttons in the button box.

setdefault(index)
Sets the default button to the button given by index. This causes the specified button to be displayed with the platform-specific appearance for a default button. If index is None, there