---
source_image: page_447.png
page_number: 447
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.75
tokens: 8597
characters: 2007
timestamp: 2025-12-24T00:44:14.747363
finish_reason: stop
---

Table A.83  Grid methods

<table>
  <tr>
    <th>Tk</th>
    <th>Tkinter</th>
  </tr>
  <tr>
    <td>grid [configure] slave [slave ...] [option value ...]</td>
    <td>slave.grid([option=value ...])</td>
  </tr>
  <tr>
    <td>grid bbox master [column row [column2 row2]]</td>
    <td>master.grid_bbox([column, row [, column2, row2]])</td>
  </tr>
  <tr>
    <td>grid columnconfigure master columnList [options]</td>
    <td>master.grid_columnconfigure(columnList [, options])</td>
  </tr>
  <tr>
    <td>-minsize size</td>
    <td>minsize=size</td>
  </tr>
  <tr>
    <td>-pad amount</td>
    <td>pad=amount</td>
  </tr>
  <tr>
    <td>-weight int</td>
    <td>weight=int</td>
  </tr>
  <tr>
    <td>grid forget slave [slave ...]</td>
    <td>slave.grid_forget()</td>
  </tr>
  <tr>
    <td>grid info slave</td>
    <td>slave.grid_info()</td>
  </tr>
  <tr>
    <td>grid location master x y</td>
    <td>slave.grid_location(x, y)</td>
  </tr>
  <tr>
    <td>grid propagate master [boolean]</td>
    <td>master.grid_propagate([boolean])</td>
  </tr>
  <tr>
    <td>grid remove slave [slave ...]</td>
    <td>slave.grid_remove()</td>
  </tr>
  <tr>
    <td>grid rowconfigure master rowList [options]</td>
    <td>master.grid_rowconfigure(rowList, [, options])</td>
  </tr>
  <tr>
    <td>grid size master</td>
    <td>master.grid_size()</td>
  </tr>
  <tr>
    <td>grid slaves master [-row row] [-column column]</td>
    <td>master.grid_slaves([row] [, column])</td>
  </tr>
</table>

Fonts

Table A.84  Font options

<table>
  <tr>
    <th>Tk</th>
    <th>Tkinter</th>
  </tr>
  <tr>
    <td>-family name</td>
    <td>family=name</td>
  </tr>
  <tr>
    <td>-size size</td>
    <td>size=size</td>
  </tr>
  <tr>
    <td>-weight weight</td>
    <td>weight=weight</td>
  </tr>
  <tr>
    <td>-slant slant</td>
    <td>slant=slant</td>
  </tr>
  <tr>
    <td>-underline boolean</td>
    <td>underline=boolean</td>
  </tr>
  <tr>
    <td>-overstrike boolean</td>
    <td>overstrike=boolean</td>
  </tr>
</table>