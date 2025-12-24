---
source_image: page_109.png
page_number: 109
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.32
tokens: 8248
characters: 1702
timestamp: 2025-12-24T00:34:19.049141
finish_reason: stop
---

5.2.3 Using the padx and pady options

The padx and pady options allow the widget to be packed with additional space around it. Figure 5.12 shows the effect of adding padx=10 to the pack request for the center button. Padding is applied to the specified left/right or top/bottom sides for padx and pady respectively. This may not achieve the effect you want, since if you place two widgets side by side, each with a padx=10, there will be 20 pixels between the two widgets and 10 pixels to the left and right of the pair. This can result in some unusual spacing.

5.2.4 Using the anchor option

The anchor option is used to determine where a widget will be placed within its parcel when the available space is larger than the size requested and none or one fill direction is specified. Figure 5.13 illustrates how a widget would be packed if an anchor is supplied. The option anchor=CENTER positions the widget at the center of the parcel. Figure 5.14 shows how this looks in practice.

Figure 5.12 Anchoring a widget within the available space

Figure 5.13 Using the anchor option to place widgets

5.2.5 Using hierarchical packing

While it is relatively easy to use the Packer to lay out simple screens, it is usually necessary to apply a hierarchical approach and employ a design which packs groups of widgets within frames and then packs these frames either alongside one other or inside other frames. This allows much more control over the layout, particularly if there is a need to fill and expand the widgets.

Figure 5.15 illustrates the result of attempting to lay out two columns of widgets. At first glance, the code appears to work, but it does not create the desired layout. Once you have