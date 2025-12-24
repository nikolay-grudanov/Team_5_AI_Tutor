---
source_image: page_642.png
page_number: 642
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.68
tokens: 8370
characters: 1352
timestamp: 2025-12-24T00:50:05.147295
finish_reason: stop
---

APPENDIX E

Events and keysyms

The tables in this appendix document the modifiers, event types and keysyms recognized by Tkinter (strictly Tk). Translation of keycodes is highly implementation-dependent so it is important to note that not all keys can be detected consistently across multiple architectures.
    The generalized format of events is as follows:

< [ modifier [ ‘|’- modifier ...] ‘|’- ] [[ type [ qualifier ] | qualifier ] >

Modifiers

<table>
  <tr>
    <th>Modifier</th>
    <th>Alt. 1</th>
    <th>Alt. 2</th>
    <th>Mask</th>
  </tr>
  <tr>
    <td>Control</td>
    <td></td>
    <td></td>
    <td>ControlMask</td>
  </tr>
  <tr>
    <td>Shift</td>
    <td></td>
    <td></td>
    <td>ShiftMask</td>
  </tr>
  <tr>
    <td>Lock</td>
    <td></td>
    <td></td>
    <td>LockMask</td>
  </tr>
  <tr>
    <td>Meta</td>
    <td>M</td>
    <td></td>
    <td>META_MASK</td>
  </tr>
  <tr>
    <td>Alt</td>
    <td></td>
    <td></td>
    <td>ALT_MASK</td>
  </tr>
  <tr>
    <td>B1</td>
    <td>Button1</td>
    <td></td>
    <td>Button1Mask</td>
  </tr>
  <tr>
    <td>B2</td>
    <td>Button2</td>
    <td></td>
    <td>Button2Mask</td>
  </tr>
  <tr>
    <td>B3</td>
    <td>Button3</td>
    <td></td>
    <td>Button3Mask</td>
  </tr>
  <tr>
    <td>B4</td>
    <td>Button4</td>
    <td></td>
    <td>Button4Mask</td>
  </tr>
</table>