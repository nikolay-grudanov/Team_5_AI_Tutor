---
source_image: page_106.png
page_number: 106
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.52
tokens: 8271
characters: 1624
timestamp: 2025-12-24T00:34:18.824009
finish_reason: stop
---

Packing from the top of the frame generates the result shown in figure 5.4. Note that the Packer centers the widgets in the available space since no further options are supplied and since the window is stretched to fit the widest widget.

Figure 5.4 Packing from the top side

Example_5_2a.py

Button(fm, text='Top').pack(side=TOP)
Button(fm, text='This is the Center button').pack(side=TOP)
Button(fm, text='Bottom').pack(side=TOP)

Combining side options in the Packer list may achieve the desired effect (although more often than not you’ll end up with an effect you did not plan on!). Figure 5.5 illustrates how unusual layouts may be induced.

Figure 5.5 Combining sides

In all of these examples we have seen that the Packer negotiates the overall size of containers to fit the required space. If you want to control the size of the container, you will have to use geometry options, because attempting to change the Frame size (see example_5_4.py) has no effect as shown in figure 5.6.

Figure 5.6 Effect of changing frame size

Example_5_4.py

fm = Frame(master, width=300, height=200)
Button(fm, text='Left').pack(side=LEFT)

Sizing windows is often a problem when programmers start to work with Tkinter (and most other toolkits, for that matter) and it can be frustrating when there is no response as width and height options are added to widget specifications.

To set the size of the window, we have to make use of the wm.geometry option. Figure 5.7 shows the effect of changing the geometry for the root window.

Figure 5.6 Assigning the geometry of the Toplevel shell

Example_5_5.py

master.geometry("300x200")