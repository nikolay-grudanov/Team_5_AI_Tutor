---
source_image: page_176.png
page_number: 176
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.69
tokens: 8268
characters: 1782
timestamp: 2025-12-24T00:36:17.822489
finish_reason: stop
---

15 The modifiedcommand in the previous code fragment binds a function to the widget to be called whenever the content of the widget changes (a valuechanged callback). This allows us to implement one form of validation or, in this case, to change each character to upper case:

    upname = string.upper(self.userName.get())
    if upname:
        self.userName.setentry(upname)

16 Finally, we create the root shell and populate it with the subcomponents of the form:

    shell=Shell(title='Example 8-4')
    shell.root.geometry("%dx%d" % (400,350))
    shell.doBaseForm(shell.root)
    shell.doDataForm()
    shell.doInfoForm()
    shell.root.mainloop()

Note that we delay calling the doBaseForm, doDataForm and doInfoForm methods to allow us flexibility in exactly how the form is created from the base classes.

If you run Example_8_4.py, you will see screens similar to the one in figure 8.4. Notice how the ScrolledText widget automatically adds scroll bars as necessary. In fact, the overall layout changes slightly to accommodate several dimension changes. The title to the ScrolledText widget, for example, adds a few pixels to its containing frame; this has a slight effect on the layout of the entry fields. This is one reason why user interfaces need to be completely tested.

Note Automatic scroll bars can introduce some bothersome side effects. In figure 8.4, the vertical scroll bar was added because the number of lines exceeded the height of the widget. The horizontal scroll bar was added because the vertical scroll bar used space needed to display the longest line. If I had resized the window about 10 pixels wider, the horizontal scroll bar would not have been displayed.

![Figure 8.4 Single-shot form](../images/figure_8_4.png)

Figure 8.4 Single-shot form