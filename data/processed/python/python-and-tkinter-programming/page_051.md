---
source_image: page_051.png
page_number: 51
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.82
tokens: 8406
characters: 2456
timestamp: 2025-12-24T00:32:53.109317
finish_reason: stop
---

vscrollmode='dynamic', hull_relief='sunken',
hull_background='gray40', hull_borderwidth=10,
text_background='honeydew4', text_width=16,

Notice how the attributes for the hull (the container for the subordinate widgets within Pmw widgets) and the text widget are accessed by prefixing the widget.

11 We define a text tag which is used to differentiate output from input in the calculator’s screen.
    self.display.tag_config('ans', foreground='white')
    We saw this tag in use earlier in the text insert method.

12 Again, we must use a lambda expression to bind our callback function.

13 Python exceptions are quite flexible and allow simple control of errors. In the calculator’s evaluator (runpython), we first run eval.
    try:
        return `eval(code, self.myNameSpace, self.myNameSpace)`
    This is used mainly to support direct calculator math. eval cannot handle code sequences, however, so when we attempt to eval a code sequence, a SyntaxError exception is raised.

14 We trap the exception:
    except SyntaxError:
        try:
            exec code in self.myNameSpace, self.myNameSpace
        except:
            return 'Error'
and then the code is exec’ed in the except clause. Notice how this is enclosed by another try... except clause.

Figure 3.2 shows the results of clicking keys on the calculator to calculate simple math equations. Unlike many calculators, this displays the input and output in different colors. The display also scrolls to provide a history of calculations, not unlike a printing calculator. If you click on the display screen, you may input data directly. Here is the surprise: you can enter Python and have exec run the code.

Figure 3.3 shows how you can import the sys module and access built-in functions within Python. Technically, you could do almost anything from this window (within the constraint of a very small display window). However, I don’t think that this calculator is the much-sought Interactive Development Environment (IDE) for Python! (Readers who subscribe to the Python news group will understand that there has been a constant demand for an IDE for Python. Fortunately, Guido Van Rossum has now released IDLE with Python.)

When you press ENTER after dir(), you will see output similar to figure 3.4. This list of built-in symbols has scrolled the display over several lines (the widget is only 16 characters wide, after all).

Figure 3.3 Python input

Figure 3.4 Output from dir()