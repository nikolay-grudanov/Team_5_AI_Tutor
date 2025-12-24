---
source_image: page_445.png
page_number: 445
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.92
tokens: 8589
characters: 2065
timestamp: 2025-12-24T00:44:14.501829
finish_reason: stop
---

Binding and virtual events

Table A.78  Bind and event methods

<table>
  <tr>
    <th>Tk</th>
    <th>Tkinter</th>
  </tr>
  <tr>
    <td>bind tag</td>
    <td>widget.bind()</td>
  </tr>
  <tr>
    <td>bind tag sequence</td>
    <td>widget.bind('sequence')</td>
  </tr>
  <tr>
    <td>bind tag sequence script</td>
    <td>widget.bind('sequence', script)</td>
  </tr>
  <tr>
    <td>bindtags window [tagList]</td>
    <td>window.bindtags([tagList])</td>
  </tr>
  <tr>
    <td>event add <<virtual>> sequence [sequence ...]</td>
    <td>window.event_add(virtual, sequence [, sequence ...])</td>
  </tr>
  <tr>
    <td>event delete <<virtual>> [sequence ...]</td>
    <td>window.event_delete(virtual [, sequence ...])</td>
  </tr>
  <tr>
    <td>event generate window event [-when when] [option value ...]</td>
    <td>window.event_generate(sequence [, option=value ...])</td>
  </tr>
</table>

Geometry management

The pack command

Table A.79  Pack methods

<table>
  <tr>
    <th>Tk</th>
    <th>Tkinter</th>
  </tr>
  <tr>
    <td>pack [configure] slave [slave ...] [options]</td>
    <td>slave.pack([option=value ...])</td>
  </tr>
  <tr>
    <td>pack forget slave [slave ...]</td>
    <td>slave.pack_forget()</td>
  </tr>
  <tr>
    <td>pack info slave</td>
    <td>slave.pack_info()</td>
  </tr>
  <tr>
    <td>pack propagate master [boolean]</td>
    <td>master.pack_propagate([boolean])</td>
  </tr>
  <tr>
    <td>pack slaves master</td>
    <td>master.pack_slaves()</td>
  </tr>
</table>

The place command

Table A.80  Place options

<table>
  <tr>
    <th>Tk</th>
    <th>Tkinter</th>
  </tr>
  <tr>
    <td>-anchor anchor</td>
    <td>anchor=anchor</td>
  </tr>
  <tr>
    <td>-bordemode inside|outside|ignore</td>
    <td>bordemode='inside'|'outside'|'ignore'</td>
  </tr>
  <tr>
    <td>-height size</td>
    <td>height=size</td>
  </tr>
  <tr>
    <td>-in master</td>
    <td>in=master</td>
  </tr>
  <tr>
    <td>-relheight size</td>
    <td>relheight=size</td>
  </tr>
  <tr>
    <td>-relwidth size</td>
    <td>relwidth=size</td>
  </tr>
</table>