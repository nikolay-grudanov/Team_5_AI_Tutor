---
source_image: page_041.png
page_number: 41
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.52
tokens: 8241
characters: 1736
timestamp: 2025-12-24T00:32:22.514731
finish_reason: stop
---

Take a look at figure 2.2. This application uses Pmw combobox widgets along with Tkinter button and entry widgets arranged within frames. The font for this example is Arial, bold and 16 point. Apart from the obvious Win32 controls in the border, there is little to distinguish this window from the one shown in figure 2.3, which was run on UNIX. In this case, the font is Helvetica, bold and 16 point. The window is slightly larger because the font has slightly different kerning rules and stroke weight, and since the size of the widget is dependent on the font, this results in a slightly different layout. If precise alignment and sizing is an absolute requirement, it is possible to detect the platform on which the application is running and make adjustments for known differences. In general, it is better to design an application that is not sensitive to small changes in layout.

If you look closely, you may also notice a difference in the top and bottom highlights for the Execute and Close buttons, but not for the buttons on the Pmw widgets. This is because Tk is drawing Motif decorations for UNIX and Windows SDK decorations for Win32.

In general, as long as your application does not make use of very platform-specific fonts, it will be possible to develop transportable code.

2.4 Tkinter class hierarchy

Unlike many windowing systems, the Tkinter hierarchy is really quite simple; in fact, there really isn’t a hierarchy at all. The WM, Misc, Pack, Place and Grid classes are mixins to each of the widget classes. Most programmers only need to know about the lowest level in the tree to perform everyday operations and it is often possible to ignore the higher levels. The notional “hierarchy” is shown in figure 2.4.