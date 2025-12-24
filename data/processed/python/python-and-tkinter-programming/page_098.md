---
source_image: page_098.png
page_number: 98
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.23
tokens: 8278
characters: 1665
timestamp: 2025-12-24T00:34:09.371579
finish_reason: stop
---

title='Sketch',
defaultbutton=0,
label_text='The Hospital')
dialog.insert(END, sketch)
dialog.configure(text_state='disabled')
dialog.activate()
dialog.tkraise()

Documentation for the TextDialog widget starts on page 605.

4.3.29 TimeCounter

The TimeCounter widget implements a device to set hours, minutes and seconds using up and down arrows. The widget may be configured to autorepeat so that holding down a button will slew the value displayed in the widget. Figure 4.51 shows the widget’s appearance.

![Pmw TimeCounter widget](./images/timecounter.png)

Figure 4.51 Pmw TimeCounter widget

time = Pmw.TimeCounter(root, labelpos=W, label_text='HH:MM:SS',
    min='00:00:00', max='23:59:59')
time.pack(padx=10, pady=5)

Documentation for the TimeCounter widget starts on page 607.

4.4 Creating new megawidgets

In addition to supplying useful widgets, Pmw provides a simple mechanism to allow you to develop new megawidgets. The documentation supplied with Pmw describes the process of coding a megawidget. This description is an adaptation of that material.

4.4.1 Description of the megawidget

This widget will implement a simple gauge which tracks an integer value supplied by a Scale widget, which selects a number from a range. The gauge indicates the setting as a percentage of the range. The completed megawidget will look like the one shown in figure 4.52.

The scale widget will be a component of the megawidget since the range may be set by the programmer; the size and color of the gauge may similarly be changed, as appropriate for the application, so we make this a component, too.

![Gauge widget](./images/gauge.png)

Figure 4.52 Gauge widget