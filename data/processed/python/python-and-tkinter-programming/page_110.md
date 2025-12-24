---
source_image: page_110.png
page_number: 110
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.52
tokens: 8333
characters: 1692
timestamp: 2025-12-24T00:34:25.489554
finish_reason: stop
---

packed a slave using side=TOP, the remaining space is below the slave, so you cannot pack alongside existing parcels.

Example_5_12.py

```python
fm = Frame(master)
Button(fm, text='Top').pack(side=TOP, anchor=W, fill=X, expand=YES)
Button(fm, text='Center').pack(side=TOP, anchor=W, fill=X, expand=YES)
Button(fm, text='Bottom').pack(side=TOP, anchor=W, fill=X, expand=YES)
Button(fm, text='Left').pack(side=LEFT)
Button(fm, text='This is the Center button').pack(side=LEFT)
Button(fm, text='Right').pack(side=LEFT)
fm.pack()
```

![Screenshot of Example 12 showing four buttons arranged in a single row](example_12.png)

Figure 5.14 Abusing the Packer

All we have to do is to pack the two columns of widgets in separate frames and then pack the frames side by side. Here is the modified code:

Example_5_13.py

```python
fm = Frame(master)
Button(fm, text='Top').pack(side=TOP, anchor=W, fill=X, expand=YES)
Button(fm, text='Center').pack(side=TOP, anchor=W, fill=X, expand=YES)
Button(fm, text='Bottom').pack(side=TOP, anchor=W, fill=X, expand=YES)
fm.pack(side=LEFT)
fm2 = Frame(master)
Button(fm2, text='Left').pack(side=LEFT)
Button(fm2, text='This is the Center button').pack(side=LEFT)
Button(fm2, text='Right').pack(side=LEFT)
fm2.pack(side=LEFT, padx=10)
```

Figure 5.16 shows the effect achieved by running Example_5_13.py.
This is an important technique which will be seen in several examples throughout the book. For an example which uses several embedded frames, take a look at Examples/chapter17/Example_16_9.py, which is available online.

![Screenshot of Example 13 showing two columns of widgets with hierarchical packing](example_13.png)

Figure 5.15 Hierarchical packing