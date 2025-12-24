---
source_image: page_580.png
page_number: 580
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.58
tokens: 8372
characters: 2386
timestamp: 2025-12-24T00:48:19.520755
finish_reason: stop
---

• time  A time specification, as accepted by Pmw.timestringtoseconds(). This counter accepts a separator argument, which specifies the character used to separate the time fields. The default separator is ‘:’.
• date  A date specification, as accepted by Pmw.datestringtojdn(). This counter accepts a separator argument, which specifies the character used to separate the three date fields. The default is ‘/’. This counter also accepts a format argument, which is passed to Pmw.datestringtojdn() to specify the desired ordering of the fields. The default is ymd.

If counter is a function, then it will be called whenever the counter is incremented or decremented. The function is called with at least three arguments, the first three being (text, factor, increment), where text is the current contents of the entry field, factor is 1 when incrementing or -1 when decrementing, and increment is the value of the increment megawidget option.

The other arguments are keyword arguments made up of the fields of the datatype dictionary (excluding the counter field). The counter function should return a string representing the incremented or decremented value. It should raise a ValueError exception if the text is invalid. In this case the bell is rung and the entry text is not changed.

Components

downarrow
The arrow button used for decrementing the counter. Depending on the value of orient, it will appear on the left or below the entry field. Its component group is Arrow.

entryfield
The entry field widget where the text is entered, displayed and validated.

frame
If the label component has been created (that is, the labelfpos option is not None), the frame component is created to act as the container of the entry field and arrow buttons. If there is no label component, then no frame component is created and the hull component acts as the container. In either case the border around the container of the entry field and arrow buttons will be raised (but not around the label).

hull
This acts as the body for the entire megawidget. Other components are created as children of the hull to further specialize the widget.

label
If the labelfpos option is not None, this component is created as a text label for the megawidget. See the labelfpos option for details. Note that to set, for example, the text option of the label, you need to use the label_text component option.