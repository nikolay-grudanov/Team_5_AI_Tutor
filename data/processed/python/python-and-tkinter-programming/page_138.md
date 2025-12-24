---
source_image: page_138.png
page_number: 138
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.86
tokens: 8398
characters: 2337
timestamp: 2025-12-24T00:35:15.960115
finish_reason: stop
---

Code comments

1 The date field uses the built-in date validator, specifying the format of the data and the separators:

    validate = {'validator': 'date',
                'format': 'mdy', 'separator': '/'})

2 The time field sets maximum and minimum options along with minstrict and maxstrict:

    validate = {'validator': 'time',
                'min': '00:00:00', 'max': '23:59:59',
                'minstrict': 0, 'maxstrict': 0})

Setting minstrict and maxstrict to False (zero) allows values outside of the min and max range to be set. The background will be colored to indicate an error. If they are set to True, values outside the range cannot be input.

3 The Social Security field uses a user-supplied validator:

    validate = self.validateSSN, value = '')

4 Pmw provides a convenience method to align labels. This helps to reduce the need to set up additional formatting in the geometry managers.

    Pmw.alignlabels(fields)
    self._date.component('entry').focus_set()

It is always a good idea to set input focus to the first editable field in a data-entry screen.

5 The validateSSN method is simple; it looks for three groups or characters separated by dashes.

6 Since the entry is cumulative, the string.split call will fail until the third group has been entered.

7 We set the Tk options database to override fonts and colors in all components used in the Pmw widgets.

    root.option_add('*Font', 'Verdana 10 bold')
    root.option_add('*EntryField.Entry.Font', 'Courier 10')
    root.option_add('*EntryField.errorbackground', 'yellow')
    Pmw.initialise(root, useTkOptionDb=1)

This construct will be seen in many examples. However, this is a less-frequently used option to Pmw.initialise to force the use of the Tk option database.

Running Example_6_7 displays a screen similar to figure 6.2. Notice how the date and Social Security fields have a shaded background to indicate that they contain an invalid format.

Although validation of this kind is provided automatically by the Pmw Entryfield widget, it has some drawbacks.

1 There is no indication of the actual validation error. The user is required to determine the cause of the error himself.

2 Data which is valid, when complete, is indicated as being in error as it is being entered (the Social Security field in figure 6.2 is a good example).