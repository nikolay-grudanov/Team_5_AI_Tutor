---
source_image: page_112.png
page_number: 112
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 63.48
tokens: 8984
characters: 3161
timestamp: 2025-12-24T00:35:01.392249
finish_reason: stop
---

self.oldpw = Entry(master, width = 16, show='*')
self.newpw1 = Entry(master, width = 16, show='*')
self.newpw2 = Entry(master, width = 16, show='*')

self.oldpw.grid(row=0, column=1, sticky=W)
self.newpw1.grid(row=1, column=1, sticky=W)
self.newpw2.grid(row=2, column=1, sticky=W)

Code comments

1 First, we create the labels. Since we do not need to preserve a reference to the label, we can apply the grid method directly. We specify the row number but allow the column to default (in this case to column 0). The sticky attribute determines where the widget will be attached within its cell in the grid. The sticky attribute is similar to a combination of the anchor and expand options of the Packer and it makes the widget look like a packed widget with an anchor=W option.

2 We do need a reference to the entry fields, so we create them separately.

3 Finally, we add the entry fields to the grid, specifying both row and column.

Let’s go back to the image editor example. If you plan the layout for the fields in a grid it is easy to see what needs to be done to generate the screen. Look at figure 5.19 to see how the areas are to be gridded. The important feature to note is that we need to span both rows and columns to set aside the space for each of the components. You may find it convenient to sketch out designs for complex grids before committing them to code. Here is the code for the image editor. I have removed some of the code, since I really want to focus on the layout and not the operation of the application. The full source code for this example is available online.

<table>
  <tr>
    <th>0</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th>
  </tr>
  <tr>
    <td>Image</td><td>Image</td><td>Image</td><td>Image</td><td>Image</td><td>label</td><td></td><td></td>
  </tr>
  <tr>
    <td>2</td><td></td><td></td><td></td><td></td><td>radiobutton</td><td></td><td></td>
  </tr>
  <tr>
    <td>3</td><td></td><td></td><td></td><td></td><td>radiobutton</td><td></td><td></td>
  </tr>
  <tr>
    <td>4</td><td></td><td></td><td></td><td></td><td>radiobutton</td><td></td><td></td>
  </tr>
  <tr>
    <td>5</td><td></td><td></td><td></td><td></td><td>label</td><td></td><td></td>
  </tr>
  <tr>
    <td>6</td><td></td><td></td><td></td><td></td><td>combobox</td><td></td><td></td>
  </tr>
  <tr>
    <td>7</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
  </tr>
  <tr>
    <td>8</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
  </tr>
  <tr>
    <td>9</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
  </tr>
  <tr>
    <td>10</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
  </tr>
  <tr>
    <td>11</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
  </tr>
  <tr>
    <td>12</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
  </tr>
  <tr>
    <td>13</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
  </tr>
  <tr>
    <td>14</td><td></td><td></td><td></td><td></td><td>button</td><td>button</td><td></td>
  </tr>
</table>

Figure 5.18 Designing the layout for a gridded display