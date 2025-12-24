---
source_image: page_585.png
page_number: 585
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.14
tokens: 8488
characters: 2688
timestamp: 2025-12-24T00:48:28.928658
finish_reason: stop
---

will be displayed with a background color to indicate it is in error. An example of partially valid real text is ‘–.’, which may be the first two characters of the valid string ‘– .5’. Some validators, such as date, have a relaxed interpretation of partial validity, which allows the user flexibility in how he enters the text.

Validation is performed early, at each keystroke or other event which modifies the text. However, if partially valid text is permitted, the validity of the entered text can be checked just before it is to be used; this is a form of late validation.

Minimum and maximum values may be specified. Some validators also accept other specifications, such as date and time formats and separators.

Validation function return values

Validation is performed by a function which takes as its first argument the entered text and returns one of three standard values, indicating whether the text is valid:

• Pmw.OK    The text is valid.
• Pmw.ERROR    The text is invalid and is not acceptable for display. In this case the entry will be restored to its previous value.
• Pmw.PARTIAL    The text is partially valid and is acceptable for display. In this case the text will be displayed using the errorbackground color.

Inheritance

EntryField inherits from Pmw.MegaWidget.

EntryField options

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>command</td>
    <td>This specifies a function to call whenever the RETURN key is pressed or invoke() is called.</td>
    <td>function</td>
    <td>None</td>
  </tr>
  <tr>
    <td>errorbackground</td>
    <td>Specifies the background color to use when displaying invalid or partially valid text.</td>
    <td>color</td>
    <td>'pink'</td>
  </tr>
  <tr>
    <td>extravalidators</td>
    <td>This is a dictionary of extra validators. The keys are the names of validators which may be used in a future call to the validate option. Each value in the dictionary is a tuple of (validate_function, stringtovalue_function).<br>The validate_function is used to implement the validation and the stringtovalue_function is used to convert the entry input into a value which can be compared with the minimum and maximum limits. These functions are as described for the validate option.<br>If either of these is not given as a function, it is assumed to be the name of one of the other extra validators or one of the standard validators. The alias search is performed when the validate option is configured, not when the extravalidators option is configured or when the validate function is called.</td>
    <td>dictionary</td>
    <td>{ }</td>
  </tr>
</table>