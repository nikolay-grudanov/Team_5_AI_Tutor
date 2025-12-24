---
source_image: page_128.png
page_number: 128
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.11
tokens: 8354
characters: 2214
timestamp: 2025-12-24T00:34:52.650862
finish_reason: stop
---

else:
    print 'command in:'

Of course, this does increase complexity, particularly if the function already has arguments, since you will have to determine if the first argument is an event object or a regular argument.

6.4 Lambda expressions

Oh no! Not the dreaded lambda again!* Although lambda has been mentioned earlier in the book, and has been used extensively in examples, before we go on to the next section we must take another look at the use of lambda.

The term lambda originally came from Alonzo Church’s lambda calculus and you will now find lambda used in several contexts—particularly in the functional programming disciplines. Lambda in Python is used to define an anonymous function which appears to be a statement to the interpreter. In this way you can put a single line of executable code where it would not normally be valid.

Take a look at this code fragment:

var = IntVar()
value = 10
...
btn.bind('Button-1', (btn.flash(), var.set(value)))

A quick glance at the bolded line might not raise any alarms, but the line will fail at runtime. The intent was to flash the button when it was clicked and set a variable with some pre-determined value. What is actually going to happen is that both of the calls will be called when the bind method executes. Later, when the button is clicked, we will not get the desired effect, since the callback list contains just the return values of the two method calls, in this case (None, None). Additionally, we would have missed the event object—which is always the first argument in the callback—and we could possibly have received a runtime error. Here is the correct way to bind this callback:

btn.bind('Button-1', lambda event, b=btn, v=var, i=value:
    (b.flash(), v.set(i)))

Notice the event argument (which is ignored in this code fragment).

6.4.1 Avoiding lambdas altogether

If you don’t like lambda expressions, there are other ways of delaying the call to your function. Timothy R. Evans posted a suggestion to the Python news group which defines a command class to wrap the function.

class Command:
    def __init__(self, func, *args, **kw):
        self.func = func
        self.args = args

* “Cardinal Fang! Bring me the lambda!”