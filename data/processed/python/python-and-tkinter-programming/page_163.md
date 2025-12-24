---
source_image: page_163.png
page_number: 163
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.31
tokens: 8276
characters: 1685
timestamp: 2025-12-24T00:35:54.410608
finish_reason: stop
---

expand=YES,
padx=2,
pady=6)

if __name__ == '__main__':
    TestComposite().mainloop()

You can see from this example that the test code is beginning to exceed the size of the code needed to construct the widget; this is not an unusual situation when building Python code! If you run Example_7_6.py the following switches shown in figure 7.6 are displayed:

![Figure 7.6 Composite Switch/Indicator Widgets](./images/figure_7_6.png)

Figure 7.6 Composite Switch/Indicator Widgets

Note The two switches on the left are US switches while the two on the right are UK switches. American and British readers may be equally confused with this if they have never experienced switches on the opposite side of the Atlantic Ocean.

In the preceding examples we have simplified the code by omitting to save the instances of the objects that we have created. This would not be very useful in real-world applications. In future examples we will save the instance in the class or a local variable. Changing our code to save the instance has a side effect that requires us to separate the instantiation and the call to the Packer in our examples. For example, the following code:

for top, mount, state, mode in switches:
    SwitchIndicator(frame, mount=mount, outside=20, metal=Color.CHROME,
        mode=mode, bg="gray80", top=top,
        status=state).frame.pack(side=LEFT,
            expand=YES, padx=2, pady=6)

becomes:

idx = 0
for top, mount, state, mode in switches:
    setattr(self, 'swin%d' % idx, None)
    var = getattr(self, 'swin%d' % idx)
    var = SwitchIndicator(frame,
        mount=mount,
        outside=20,
        metal=Color.CHROME,
        mode=mode,
        bg="gray80",