---
source_image: page_553.png
page_number: 553
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.97
tokens: 8510
characters: 2456
timestamp: 2025-12-24T00:47:36.938206
finish_reason: stop
---

ciated widget. For example, if first is 0.2 and last is 0.4, it means that the first part of the document visible in the window is 20% of the way through the document, and the last visible part is 40% of the way through.

Text

![A screenshot of a text widget with several lines of text](./images/text_widget.png)

Description

The Text class defines a new window and creates an instance of a text widget. Additional options, described below, may be specified in the method call or in the option database to configure aspects of the text such as its default background color and relief. The text method returns the path name of the new window.

A text widget displays one or more lines of text and allows that text to be edited. Text widgets support four different kinds of annotations on the text: tags, marks, embedded windows and embedded images. Tags allow different portions of the text to be displayed with different fonts and colors. In addition, Tcl commands can be associated with tags so that scripts are invoked when particular actions such as keystrokes and mouse button presses occur in particular ranges of the text.

The second form of annotation consists of marks, which are floating markers in the text. Marks are used to keep track of various interesting positions in the text as it is edited.
The third form of annotation allows arbitrary windows to be embedded in a text widget.
The fourth form of annotation allows Tk images to be embedded in a text widget.
Many of the widget commands for texts take one or more indices as arguments. An index is a string used to indicate a particular place within a text, such as a place to insert characters or one endpoint of a range of characters to delete.

Inheritance

Text inherits from Widget.)

Shared options

<table>
  <tr>
    <th>Option (alias)</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>background (bg)</td>
    <td>SystemWindow</td>
  </tr>
  <tr>
    <td>borderwidth (bd)</td>
    <td>2</td>
  </tr>
  <tr>
    <td>cursor</td>
    <td>xterm</td>
  </tr>
  <tr>
    <td>font</td>
    <td>(('MS', 'Sans', 'Serif'), '8')</td>
  </tr>
  <tr>
    <td>foreground (fg)</td>
    <td>SystemWindowText</td>
  </tr>
  <tr>
    <td>height</td>
    <td>24</td>
  </tr>
  <tr>
    <td>highlightbackground</td>
    <td>SystemButtonFace</td>
  </tr>
  <tr>
    <td>highlightcolor</td>
    <td>SystemWindowFrame</td>
  </tr>
  <tr>
    <td>highlightthickness</td>
    <td>0</td>
  </tr>
</table>