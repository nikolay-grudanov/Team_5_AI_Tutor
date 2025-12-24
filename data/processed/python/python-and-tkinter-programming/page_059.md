---
source_image: page_059.png
page_number: 59
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.16
tokens: 8285
characters: 1338
timestamp: 2025-12-24T00:32:58.116791
finish_reason: stop
---

iff.append(Frame(of[bdw], borderwidth=bdw, relief=relief))
    Label(iff[ifx], text=relief, width=10).pack(side=LEFT)
    iff[ifx].pack(side=LEFT, padx=7-bdw, pady=5+bdw)
    ifx = ifx+1
    of[bdw].pack()

![Frame Styles](https://i.imgur.com/3Q5z5QG.png)

Figure 4.3 Frame styles combining relief type with varying borderwidths

A common use of the GROOVE relief type is to provide a labelled frame (sometimes called a panel) around one or more widgets. There are several ways to do this; figure 4.4 illustrates just one example, using two frames. Note that the outer frame uses the Placer geometry manager to position the inner frame and label. The widgets inside the inner frame use the Packer geometry manager.

![Using a Frame widget to construct a panel](https://i.imgur.com/2Q5z5QG.png)

Figure 4.4 Using a Frame widget to construct a panel

f = Frame(root, width=300, height=110)
xf = Frame(f, relief=GROOVE, borderwidth=2)
Label(xf, text="You shot him!").pack(pady=10)
Button(xf, text="He's dead!", state=DISABLED).pack(side=LEFT, padx=5, pady=8)
Button(xf, text="He's completely dead!", command=root.quit).pack(side=RIGHT, padx=5, pady=8)
xf.place(relx=0.01, rely=0.125, anchor=NW)
Label(f, text='Self-defence against fruit').place(relx=.06, rely=0.125, anchor=W)
f.pack()

Documentation for the Frame widget starts on page 491.