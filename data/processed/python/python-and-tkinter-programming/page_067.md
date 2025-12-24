---
source_image: page_067.png
page_number: 67
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.33
tokens: 8226
characters: 1408
timestamp: 2025-12-24T00:33:02.624037
finish_reason: stop
---

def makeDisabledMenu():
    Dummy_button = Menubutton(mBar, text='Disabled Menu', underline=0)
    Dummy_button.pack(side=LEFT, padx='2m')
    Dummy_button["state"] = DISABLED
    return Dummy_button

Documentation for the Menu widget starts on page 501.
Documentation for the Menubutton widget starts on page 506.
Documentation for the OptionMenu class starts on page 510.

![Screenshot of a menu window showing various menu options and radiobuttons](./images/menu_radiobuttons.png)

Figure 4.16 Menu: Radiobuttons

4.1.9 Message

The Message widget provides a convenient way to present multi-line text. You can use one font and one foreground/background color combination for the complete message. An example using this widget is shown in figure 4.17.
    The widget has the standard widget methods.

Message(root, text="Exactly. It's my belief that these sheep are laborin' "
    "under the misapprehension that they're birds. Observe their "
    "be'avior. Take for a start the sheeps' tendency to 'op about "
    "the field on their 'ind legs. Now witness their attempts to "
    "fly from tree to tree. Notice that they do not so much fly "
    "as...plummet.", bg='royalblue', fg='ivory',
    relief=GROOVE).pack(padx=10, pady=10)

Documentation for the Message widget starts on page 508.

![Screenshot of a message window with multi-line text](./images/message_widget.png)

Figure 4.17 Message widget