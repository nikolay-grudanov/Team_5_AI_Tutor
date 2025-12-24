---
source_image: page_599.png
page_number: 599
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.82
tokens: 8474
characters: 2557
timestamp: 2025-12-24T00:49:04.089329
finish_reason: stop
---

**MessageBar**

**Description**
This class creates a single-line message display area. Messages of several different types may be displayed. Messages are cleared after a period defined for each message type. Each message type has a priority so that if the application attempts to display more than one message at a time, the message with the highest priority will be displayed. Messages may be accompanied by a number of audible bells.

**Inheritance**
MessageBar inherits from Pmw.MegaWidget.

**MessageBar options**

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>labelmargin</td>
    <td>If the labelpos option is not None, this specifies the distance between the label component and the rest of the megawidget.</td>
    <td>distance</td>
    <td>0</td>
  </tr>
  <tr>
    <td>labelpos</td>
    <td>Specifies where to place the label component. If not None, it should be a concatenation of one or two of the letters N, S, E and W. The first letter specifies on which side of the megawidget to place the label. If a second letter is specified, it indicates where on that side to place the label. For example, if labelpos is W, the label is placed in the center of the left-hand side; if it is WN, the label is placed at the top of the left-hand side; if it is WS, the label is placed at the bottom of the left-hand side.</td>
    <td>anchor</td>
    <td>None</td>
  </tr>
  <tr>
    <td>messagetypes</td>
    <td>This defines what message types are supported by the message bar and the characteristics of those message types. It is a dictionary where the key is a string specifying a message type and the value is a tuple of four integers (priority, showtime, bells, logmessage), where priority is the rank of the message type, showtime is the number of seconds to display messages of this message type, bells is the number of audible bells to ring and logmessage is a boolean specifying whether this message should be logged for retrieval later. Messages with a higher priority are displayed in preference to those with lower priority. If a high priority message times out (because it has been displayed for showtime seconds), then a lower priority message may be displayed. A showtime of 0 means that the message will never time out and it is useful for displaying messages describing the current state of the application as opposed to messages describing events. Logging is not currently implemented. The default is:</td>
    <td>dictionary</td>
    <td></td>
  </tr>
</table>