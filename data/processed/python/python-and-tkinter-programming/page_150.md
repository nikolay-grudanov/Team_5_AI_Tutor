---
source_image: page_150.png
page_number: 150
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.02
tokens: 8261
characters: 1840
timestamp: 2025-12-24T00:35:28.477595
finish_reason: stop
---

Code comments

1 We have some simple drawing constructs to draw a triangular area on the canvas.
2 The LED widget has a number of methods to change the appearance of the display, show several colors and turn blink on and off.
3 The selected state of the LED is updated:
    if self.status == STATUS_ON:
        self.canvas.itemconfig(self.light, fill=self.onColor)
4 We always flush the event queue to ensure that the widget is drawn with the current appearance.

Note Throughout this book I will encourage you to find ways to reduce the amount of code that you have to write. This does not mean that I am encouraging you to write obfuscated code, but there is a degree of elegance in well-constructed Python. The TestLEDs class in Example_7_1.py is a good example of code that illustrates Python economy. Here I intended to create a large number of LEDs, so I constructed two lists: one to contain the various statuses that I want to show and another to contain the LED shapes and attributes that I want to create. Put inside two nested loops, we create the LEDs with ease.

This technique of looping to generate multiple instances of objects will be exploited again in other examples. You can also expect to see other rather elegant ways of creating objects within loops, but more of that later.

Example_7_1.py produces the screen shown in figure 7.1. Although this might not seem to be very useful at this point, it illustrates the ability of Tkinter to produce some output that might be useful in an application.

Unfortunately, it is not possible to see the LEDs flashing on a printed page, so you will have to take my word that the four columns on the right flash on and off (you can obtain the examples online to see the example in action).

![LED example screenshot](./images/led_example.png)

Figure 7.2 LED example (shorter code)