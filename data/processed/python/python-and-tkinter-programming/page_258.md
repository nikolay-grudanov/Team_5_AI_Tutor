---
source_image: page_258.png
page_number: 258
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.06
tokens: 8290
characters: 1632
timestamp: 2025-12-24T00:38:37.848138
finish_reason: stop
---

9.6.1 And now for something completely different...
#10 The Example

I’m sorry! I had to use that title. The last example is going to illustrate just how unusual a user interface can become. Readers who are familiar with popular computer games such as Myst and Riven will share with me their love of ray-traced user interfaces. This is a simplistic version of such an interface. I’m not going to detail the development of ray-traced images, as many texts cover the subject. Let’s start with the basic image shown in figure 9.15.

![Base scene generated with POV-Ray](./images/figure_9_15.png)

Figure 9.15 Base scene generated with POV-Ray

The figure looks best in color, so you may want to obtain the image online. Since you may wish to solve the simple puzzle presented by this example, I will present only a fragment of the code for the application. We are using the overlay techniques presented in this chapter to bind functionality to the two “buttons” in the display. This requires special handling, since the two “buttons” need to take focus, show a highlight when they have focus, and receive button-down events. The following code excerpt manages these buttons.

Example_9_3.py

class Machine:
    def __init__(self, master):
        self.root = master
        ...
        self.b1 = self.canvas.create_oval(216,285, 270,340, fill="", outline='#226644', width=3, tags='b_1')
        self.canvas.tag_bind(self.b1, "<Any-Enter>", self.mouseEnter)
        self.canvas.tag_bind(self.b1, "<Any-Leave>", self.mouseLeave)
        self.b2 = self.canvas.create_oval(216,355, 270,410, fill="", outline='#772244', width=3, tags='b_2')