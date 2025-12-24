---
source_image: page_108.png
page_number: 108
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.21
tokens: 8195
characters: 1217
timestamp: 2025-12-24T00:34:13.994263
finish_reason: stop
---

Example_5_7.py

Button(fm, text='Left').pack(side=LEFT, fill=X, expand=YES)
Button(fm, text='Center').pack(side=LEFT, fill=X, expand=YES)
Button(fm, text='Right').pack(side=LEFT, fill=X, expand=YES)

If the fill option alone is used in Example_5_7.py, you will obtain a display similar to figure 5.9(2). By using fill and expand we see the effect shown in figure 5.9(3).
Varying the combination of fill and expand options may be used for different effects at different times. If you mix expand options, such as in example_5_8.py, you can allow some of the widgets to react to the resizing of the window while others remain a constant size. Figure 5.10 illustrates the effect of stretching and squeezing the screen.

Figure 5.9 Allowing widgets to expand and fill independently

Example_5_8.py

Button(fm, text='Left').pack(side=LEFT, fill=X, expand=NO)
Button(fm, text='Center').pack(side=LEFT, fill=X, expand=NO)
Button(fm, text='Right').pack(side=LEFT, fill=X, expand=YES)

Using fill=BOTH allows the widget to use all of its parcel. However, it might create some rather ugly effects, as shown in figure 5.11. On the other hand, this behavior may be exactly what is needed for your GUI.

Figure 5.10 Using fill=BOTH