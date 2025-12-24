---
source_image: page_107.png
page_number: 107
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.07
tokens: 8172
characters: 1132
timestamp: 2025-12-24T00:34:09.840963
finish_reason: stop
---

5.2.1 Using the expand option

The expand option controls whether the Packer expands the widget when the window is resized. All the previous examples have accepted the default of expand=NO. Essentially, if expand is true, the widget may expand to fill the available space within its parcel; whether it does expand is controlled by the fill option (see “Using the fill option” on page 82).

![Figure 5.7 Expand without fill options](https://i.imgur.com/3Q5z5QG.png)

Figure 5.7 Expand without fill options

Example_5_6.py

Button(fm, text='Left').pack(side=LEFT, expand=YES)
Button(fm, text='Center').pack(side=LEFT, expand=YES)
Button(fm, text='Right').pack(side=LEFT, expand=YES)

Figure 5.7 shows the effect of setting expand to true (YES) without using the fill option (see Example_5_6.py). The vertical orientation in the second screen is similar to side=TOP (see Example_5_2a.py).

5.2.2 Using the fill option

Example_5_7.py illustrates the effect of combining fill and expand options; the output is shown in figure 5.9(1)

![Figure 5.8 Using the fill option](https://i.imgur.com/3Q5z5QG.png)

Figure 5.8 Using the fill option