---
source_image: page_600.png
page_number: 600
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.83
tokens: 8352
characters: 1749
timestamp: 2025-12-24T00:48:59.614799
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
    <td colspan="4">
      {
        'systemerror' : (5, 10, 2, 1),
        'usererror'   : (4, 5, 1, 0),
        'busy'        : (3, 0, 0, 0),
        'systemevent' : (2, 5, 0, 0),
        'userevent'   : (2, 5, 0, 0),
        'help'        : (1, 5, 0, 0),
        'state'       : (0, 0, 0, 0),
      }
    </td>
  </tr>
  <tr>
    <td>silent</td>
    <td>If true, no audible bells will sound, regardless of the value for bells defined in the messagetypes option.</td>
    <td>boolean</td>
    <td>0</td>
  </tr>
</table>

Components

entry
The widget where the messages are displayed. Long messages may be scrolled horizontally by dragging with the middle mouse button.

hull
This acts as the body for the entire megawidget. Other components are created as children of the hull to further specialize the widget.

label
If the labelfpos option is not None, this component is created as a text label for the megawidget. See the labelfpos option for details. Note that to set, for example, the text option of the label, you need to use the label_text component option.

Methods

helpmessage(text)
A convenience method that displays text in the message bar according to the characteristics defined by the help message type. Equivalent to message('help', text).

message(type, text)
Displays text in the message bar according to the characteristics defined by the type message type, as discussed under messagetypes.

resetmessages(type)
Clears the type message and all message types with a lower priority, except permanent messages, such as state. This is useful for clearing the busy message and any outstanding event and help messages.