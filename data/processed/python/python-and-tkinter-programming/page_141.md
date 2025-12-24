---
source_image: page_141.png
page_number: 141
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.29
tokens: 8392
characters: 2218
timestamp: 2025-12-24T00:35:24.817422
finish_reason: stop
---

root.option_add('*Font', 'Verdana 10 bold')
root.option_add('*Entry.Font', 'Courier 10')
root.title('Entry Validation')

top = EntryValidation(root)
quit = Button(root, text='Quit', command=root.destroy)
quit.pack(side = 'bottom')

root.mainloop()

Code comments

① The grid geometry manager sometimes needs a little help to lay out a screen. We use an empty first and last column in this example:

    Label(frame, text='    ').grid(row=0, column=0, sticky=W)
    Label(frame, text='    ').grid(row=0, column=3, sticky=W)

You cannot use the Grid manager’s minsize option if the column (or row) is empty; you have to use the technique shown here. As an alternative, you can pack the gridded widget inside a Frame and use padding to add space at the sides.

② Since we are using native Tkinter widgets, we have to create a Label and Entry widget for each row of the form and place them in the appropriate columns. We use the createField method to do this.

③ We create a dictionary to define a variable used to store the contents of each widget.

    self._wDict = {self._ipaddr: ('_ipAddrV', validIP),
                   self._crdprt: ('_crdprtV', validCP),
                   self._lname:  ('_lnameV',   validLName) }

Using the dictionary enables us to use bindings to a single event-handler with multiple validators, which simplifies the code.

④ The bindings for validation are when the cursor leaves the widget and when focus is lost (tabbing out of the field). We also bind the activate function called when the ENTER key is pressed.

    id.bind('<Any-Leave>', valid)
    id.bind('<FocusOut>', valid)
    id.bind('<Return>', enter)

⑤ One of the complications of using this type of validation scheme is that whenever a field loses focus, its validator is called—including when we return to a field to allow the user to correct an error. We provide a mechanism to ignore one event:

    if self._ignoreEvent:
        self._ignoreEvent = 0

⑥ We get the variable and validator for the widget creating the event:

    var, validator = self._wDict[event.widget]
    nValue, replace, valid = validator(currentValue)
and call the validator to check the widget’s contents—possibly editing the content, as appropriate.