---
source_image: page_536.png
page_number: 536
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.73
tokens: 8419
characters: 1931
timestamp: 2025-12-24T00:47:03.259841
finish_reason: stop
---

Shared options
None.

Options specific to Widget
None.

Methods

OptionMenu(master, variable, value, *values)
Creates an instance of OptionMenu. master is the parent widget, and variable is the identity of the Tkinter variable. value is the default value and values is a list of values to be inserted in the optionmenu’s menu.

Pack geometry manager

Description
The pack method is used to communicate with the Packer, a geometry manager that arranges the children of a parent by packing them in order around the edges of the parent.

Inheritance
Inherits from None. Pack does not inherit from anything.

Shared options
None.

Options specific to Pack

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>after</td>
    <td>Value must be another window. Use its master as the master for the slaves, and insert the slaves just after other in the packing order.</td>
    <td>widget</td>
    <td>label</td>
    <td></td>
  </tr>
  <tr>
    <td>before</td>
    <td>Value must be another window. Use its master as the master for the slaves, and insert the slaves just before other in the packing order.</td>
    <td>widget</td>
    <td>self.entry</td>
    <td></td>
  </tr>
  <tr>
    <td>expand</td>
    <td>Specifies whether the slaves should be expanded to consume extra space in their master. Boolean may have any proper boolean value, such as 1 or NO.</td>
    <td>boolean</td>
    <td>YES</td>
    <td>0</td>
  </tr>
  <tr>
    <td>fill</td>
    <td>If a slave’s parcel is larger than its requested dimensions, this option may be used to stretch the slave.</td>
    <td>constant</td>
    <td>X 'both'</td>
    <td>NONE</td>
  </tr>
  <tr>
    <td>in_</td>
    <td>Insert the slave(s) at the end of the packing order for the master window given by value.</td>
    <td>widget</td>
    <td>container</td>
    <td>parent</td>
  </tr>
</table>