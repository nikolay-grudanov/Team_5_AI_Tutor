---
source_image: page_465.png
page_number: 465
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.07
tokens: 8319
characters: 2207
timestamp: 2025-12-24T00:44:49.515866
finish_reason: stop
---

tkraise(aboveThis=None) [lift(aboveThis=None)]
If the aboveThis argument is omitted then the method raises self so that it is above all of its siblings in the stacking order (it will not be obscured by any siblings and will obscure any siblings that overlap it). If aboveThis is specified then it must be the identity of a window that is either a sibling of the window or the descendant of a sibling of the window. In this case the raise method will insert self into the stacking order just above aboveThis (or the ancestor of aboveThis that is a sibling of the window); this could end up either raising or lowering the window.

unbind(sequence, funcid=None)
Removes any bindings for the given sequence. If the event handler funcid is given bindings for sequence, that handler alone will be removed.

unbind_all(sequence)
Removes all bindings for the supplied sequence at the application level.

unbind_class(className, sequence)
Removes all bindings for the supplied sequence for the specified class className.

update()
Processes all pending events on the event list. In particular, completes all geometry negotiation and redraws widgets as necessary. Use this method with care, since it can be a source of problems, not only by consuming CPU cycles but also by setting up potential race conditions.

update_idletasks()
Processes all pending idle events on the event list.

wait_variable(name='PY_VAR')
Waits for the value of the supplied Tkinter variable, name, to change. Note that the method enters a local event loop until the variable changes, so the application’s mainloop continues.

wait_visibility(window=None)
Waits for the specified window to become visible. Note that the method enters a local event loop until the variable changes, so the application’s mainloop continues.

wait_window(window=None)
Waits for the specified window to be destroyed. Note that the method enters a local event loop until the variable changes, so the application’s mainloop continues.

Winfo methods

winfo_atom(name, displayof=0)
Returns an integer giving the integer identifier for the atom whose name is name. If no atom exists with the name name then a new one is created. If the displayof option is given then