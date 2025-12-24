---
source_image: page_586.png
page_number: 586
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.24
tokens: 8674
characters: 3126
timestamp: 2025-12-24T00:48:44.425633
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
    <td>invalidcommand</td>
    <td>If the name of one of the extra validators is the same as one of the standard validators, the extra validator takes precedence.</td>
    <td>function</td>
    <td>self.bell</td>
  </tr>
  <tr>
    <td>labelmargin</td>
    <td>This is executed when invalid text is entered and the text is restored to its previous value (that is, when the validate function returns Pmw.ERROR). It is also called if an attempt is made to set invalid text in a call to setentry().</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>labelpos</td>
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
    <td>modifiedcommand</td>
    <td>This is called whenever the content of the entry has been changed due to user action or by a call to setentry().</td>
    <td>function</td>
    <td>None</td>
  </tr>
  <tr>
    <td>validate</td>
    <td>Specifies what kind of validation should be performed on the entry input text. See below for details.</td>
    <td>constant</td>
    <td>None</td>
  </tr>
  <tr>
    <td>value</td>
    <td>Specifies the initial contents of the entry. If this text is invalid, it will be displayed with the errorbackground color and the invalidcommand function will be called. If both value and entry_textvariable options are specified in the constructor, value will take precedence.</td>
    <td>string</td>
    <td>''</td>
  </tr>
</table>

Validators

The most general way to specify the validate option is as a dictionary. The kind of validation is specified by the validator dictionary field, which may be the name of one of the standard validators described below, the name of a validator supplied by the extravalidators option, a function or None.

Any other dictionary fields specify other restrictions on the entered values. For all validators, the following fields may be specified:

• min Specifies the minimum acceptable value, or None if no minimum checking should be performed. The default is None.
• max Specifies the maximum acceptable value, or None if no maximum checking should be performed. The default is None.
• minstrict If true, then minimum checking is strictly enforced. Otherwise, the entry input may be less than min, but it will be displayed using the errorbackground color. The default is true.