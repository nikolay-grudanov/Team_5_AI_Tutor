---
source_image: page_591.png
page_number: 591
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.07
tokens: 8350
characters: 2012
timestamp: 2025-12-24T00:48:44.360091
finish_reason: stop
---

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>labelpos</td>
    <td>Specifies where to place the label component. If not None, it should be a concatenation of one or two of the letters N, S, E and W. The first letter specifies on which side of the megawidget to place the label. If a second letter is specified, it indicates where on that side to place the label. For example, if labelpos is W, the label is placed in the center of the left-hand side; if it is WN, the label is placed at the top of the left-hand side; if it is WS, the label is placed at the bottom of the left-hand side.</td>
    <td>anchor</td>
    <td>None</td>
  </tr>
</table>

Components

hull
This acts as the body for the entire megawidget. Other components are created as children of the hull to further specialize the widget.

label
If the labelpos option is not None, this component is created as a text label for the megawidget. See the labelpos option for details. Note that to set, for example, the text option of the label, you need to use the label_text component option.

labelchildsite
The frame which can contain other widgets to be labelled.

Methods

interior()
Returns the frame within which the programmer may create widgets. This is the same as component('labelchildsite').

MegaArchetype

Description
This class is the basis for all Pmw megawidgets. It provides methods to manage options and component widgets.
This class is normally used as a base class for other classes. If the hullClass argument is specified, such as in the Pmw.MegaWidget and Pmw.MegaToplevel classes, a container widget is created to act as the parent of all other component widgets. Classes derived from these subclasses create other component widgets and options to implement megawidgets that can be used in applications.
If no hullClass argument is given to the constructor, no container widget is created and only the option configuration functionality is available.