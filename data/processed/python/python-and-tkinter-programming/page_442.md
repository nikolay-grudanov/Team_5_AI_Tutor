---
source_image: page_442.png
page_number: 442
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 45.02
tokens: 8869
characters: 2800
timestamp: 2025-12-24T00:44:19.957356
finish_reason: stop
---

Table A.75  PhotolImage methods

<table>
  <tr>
    <th>Tk</th>
    <th>Tkinter</th>
  </tr>
  <tr>
    <td>image blank</td>
    <td>image.blank()</td>
  </tr>
  <tr>
    <td>image copy sourceImage [option value ...]</td>
    <td>image.copy()</td>
  </tr>
  <tr>
    <td>image copy sourceImage [-zoom x y]</td>
    <td>image.zoom(xscale [, yscale])</td>
  </tr>
  <tr>
    <td>image copy sourceImage [-subsample x y]</td>
    <td>image.subsample(xscale [, yscale])</td>
  </tr>
  <tr>
    <td>image get x y</td>
    <td>image.get(x, y)</td>
  </tr>
  <tr>
    <td>image put data [-to x1 y1 x2 y2]</td>
    <td>image.put(data [, 'to' x1 y1 x2 y2])</td>
  </tr>
  <tr>
    <td>image read file [option value ...]</td>
    <td>No mapping</td>
  </tr>
  <tr>
    <td>image redither</td>
    <td>No mapping</td>
  </tr>
  <tr>
    <td>image write fileName [option value ...]</td>
    <td>image.write(fileName [, formatName] [, (x1, y1, x2, y2)])</td>
  </tr>
</table>

Window information

Table A.76  Winfo methods

<table>
  <tr>
    <th>Tk</th>
    <th>Tkinter</th>
  </tr>
  <tr>
    <td>winfo allmapped window</td>
    <td>No mapping</td>
  </tr>
  <tr>
    <td>winfo atom [-displayof window] name</td>
    <td>window.winfo_atom(name, [, win])</td>
  </tr>
  <tr>
    <td>winfo atomname [-displayof window] id</td>
    <td>window.winfo_atomname(id [, win])</td>
  </tr>
  <tr>
    <td>winfo cells window</td>
    <td>window.winfo_cells()</td>
  </tr>
  <tr>
    <td>winfo children window</td>
    <td>window.winfo_children()</td>
  </tr>
  <tr>
    <td>winfo class window</td>
    <td>window.winfo_class()</td>
  </tr>
  <tr>
    <td>winfo_colormapfull window</td>
    <td>window.winfo_colormapfull()</td>
  </tr>
  <tr>
    <td>winfo containing [-displayof window] rootX rootY</td>
    <td>window.winfo_containing(rootX, rootY [, win])</td>
  </tr>
  <tr>
    <td>winfo depth window</td>
    <td>window.winfo_depth()</td>
  </tr>
  <tr>
    <td>winfo exists window</td>
    <td>window.winfo_exists()</td>
  </tr>
  <tr>
    <td>winfo fpixels window number</td>
    <td>window.winfo_fpixels(bumber)</td>
  </tr>
  <tr>
    <td>winfo geometry window</td>
    <td>window.winfo_geometry()</td>
  </tr>
  <tr>
    <td>winfo height window</td>
    <td>window.winfo_height()</td>
  </tr>
  <tr>
    <td>winfo id window</td>
    <td>window.winfo_id()</td>
  </tr>
  <tr>
    <td>winfo interps [-displayof window]</td>
    <td>window.winfo_interps([win])</td>
  </tr>
  <tr>
    <td>winfo ismapped window</td>
    <td>window.winfo_ismapped()</td>
  </tr>
  <tr>
    <td>winfo manager window</td>
    <td>window.winfo_manager()</td>
  </tr>
  <tr>
    <td>winfo name window</td>
    <td>window.winfo_name()</td>
  </tr>
  <tr>
    <td>winfo parent window</td>
    <td>window.winfo_parent()</td>
  </tr>
</table>