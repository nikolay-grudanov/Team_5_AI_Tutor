---
source_image: page_537.png
page_number: 537
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.95
tokens: 8524
characters: 2400
timestamp: 2025-12-24T00:47:09.534356
finish_reason: stop
---

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Typical</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>ipadx</td>
    <td>Amount specifies how much horizontal internal padding to leave on each side of the slave(s). Amount must be a valid screen distance, such as 2 or .5c.</td>
    <td>distance</td>
    <td>2</td>
    <td>0</td>
  </tr>
  <tr>
    <td>ipady</td>
    <td>Amount specifies how much vertical internal padding to leave on each side of the slave(s).</td>
    <td>distance</td>
    <td>1m</td>
    <td>0</td>
  </tr>
  <tr>
    <td>padx</td>
    <td>Amount specifies how much horizontal external padding to leave on each side of the slave(s).</td>
    <td>distance</td>
    <td>3</td>
    <td>0</td>
  </tr>
  <tr>
    <td>pady</td>
    <td>Amount specifies how much vertical external padding to leave on each side of the slave(s).</td>
    <td>distance</td>
    <td>'2m'</td>
    <td>0</td>
  </tr>
  <tr>
    <td>side</td>
    <td>Specifies which side of the master the slave(s) will be packed against. Must be LEFT, RIGHT, TOP, or BOTTOM.</td>
    <td>constant</td>
    <td>LEFT 'top' TOP</td>
    <td></td>
  </tr>
</table>

Methods

pack(option=value, ...)
The arguments consist of pairs of arguments that specify how to manage the slaves.

pack_forget()
Removes self from the packing order for its master and unmaps its windows. The slave will no longer be managed by the Packer.

pack_info()
Returns a dictionary whose elements are the current configuration state of self in the same option-value form that might be specified to pack_configure.

pack_propagate(flag=_noarg_)
If flag has a true boolean value such as 1 or ON then propagation is enabled for self. If flag has a FALSE boolean value then propagation is disabled for master. If flag is omitted then the command returns FALSE or TRUE to indicate whether propagation is currently enabled for master. Propagation is enabled by default.

pack_slaves()
Returns a list of IDs for all of the slaves in the packing order for master. The order of the slaves in the list is the same as their order in the packing order. If master has no slaves then None is returned.

PhotoImage class

Description
A photo is an image whose pixels can display any color or be transparent. A photo image is stored internally in full color (24 bits per pixel), and is displayed using dithering if necessary.