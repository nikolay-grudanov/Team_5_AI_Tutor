---
source_image: page_104.png
page_number: 104
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.35
tokens: 8172
characters: 1335
timestamp: 2025-12-24T00:34:06.993758
finish_reason: stop
---

5.2 Packer

The Packer positions slave widgets in the master by adding them one at a time from the outside edges to the center of the window. The Packer is used to manage rows, columns and combinations of the two. However, some additional planning may have to be done to get the desired effect.

The Packer works by maintaining a list of slaves, or the packing list, which is kept in the order that the slaves were originally presented to the Packer. Take a look at figure 5.1 (this figure is modeled after John Ousterhout’s description of the Packer).

Figure 5.1(1) shows the space available for placing widgets. This might be within a frame or the space remaining after placing other widgets. The Packer allocates a parcel for the next slave to be processed by slicing off a section of the available space. Which side is allocated is determined by the options supplied with the pack request; in this example, the side=LEFT and fill=Y options have been specified. The actual size allocated by the Packer is determined by a number of factors. Certainly the size of the slave is a starting point, but the available space and any optional padding requested by the slave must be taken into account. The allocated parcel is shown in figure 5.1(2).

![Packer operation diagram](https://i.imgur.com/3Q5z5QG.png)

Figure 5.1 Packer operation