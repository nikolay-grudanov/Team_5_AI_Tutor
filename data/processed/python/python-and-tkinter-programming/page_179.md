---
source_image: page_179.png
page_number: 179
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.99
tokens: 8397
characters: 2413
timestamp: 2025-12-24T00:36:29.805526
finish_reason: stop
---

In this case, we are just loading three values into the combo’s list. Typically data may be either loaded from databases or calculated.

2 We do not intend for the values selected in this ComboBox to be editable, so we need to disable the entry field component of the widget.

    entry_width=12, entry_state="disabled",
    self.combo1.component('entry').config(bg='gray80')

We set the background of the Entry widget to be similar to the background to give the user a clear indication that the field is not editable.

3 This one is an unusual one. Frequently, fields on a screen are dependent on the values contained within other fields on the same screen (on other screens in some cases). So, if you change the value in the combobox, you ripple the values within other widgets. (Ripple is a term that I invented, but it somewhat conveys the effect you can see as the new values ripple through the interface.)

    selectioncommand = self.ripple)

Note Careless use of the ripple technique can be dangerous! Using ripple must be considered carefully, since it is quite easy to design a system which results in constant value modification if several fields are dependent on each other. Some sort of control flag is necessary to prevent a continuous loop of selectioncommand callbacks consuming CPU cycles.
See “Tkinter performance” on page 350 for other important factors you should consider when designing an application.

4 We select default value from the lists or else the entry would be displayed as blank, which is probably not appropriate for a non-editable combobox.

    self.combo1.selectitem("Upper")

5 This is our ripple callback function. The selectioncommand callback returns the value of the item selected as an argument. We use this to look up the list to be applied to the second combobox:

    def ripple(self, value):
        lookup = {'Upper': ("ANIMAL", "VEGETABLE", "MINERAL"),
                  'Lower': ("animal", "vegetable", "mineral"),
                  'Mixed': ("Animal", "Vegetable", "Mineral")}
        items = lookup[value]

6 The list obtained from the lookup replaces the current list.

    self.combo2.setlist(items)
    self.combo2.selectitem(items[0])
    As before, you need to select one of the values in the lists to be displayed in the widget.

If you run Example_8_6.py, you will see this simple example of rippled widgets. Part of the effect can be seen in figure 8.6.