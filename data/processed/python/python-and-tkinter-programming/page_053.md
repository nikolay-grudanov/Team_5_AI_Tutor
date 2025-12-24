---
source_image: page_053.png
page_number: 53
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.03
tokens: 8254
characters: 1627
timestamp: 2025-12-24T00:32:48.120807
finish_reason: stop
---

...
create widgets
...
Calculator.mainloop()

<table>
  <tr>
    <th>imported modules</th>
  </tr>
  <tr>
    <td>'global' data</td>
  </tr>
  <tr>
    <td>Helper Classes and Functions</td>
  </tr>
  <tr>
    <td>Main Class</td>
  </tr>
  <tr>
    <td>GUI Init</td>
  </tr>
  <tr>
    <td>Main Class Instantiation</td>
  </tr>
  <tr>
    <td>Test Code</td>
  </tr>
</table>

Figure 3.7 Application structure

Calling Calculator.mainloop() creates a calculator instance and starts the mainloop.

As we develop more applications, you will see this structure repeatedly. For those of us that tend to think spatially, the diagram shown in figure 3.7 may help.

All we have to do is fill in the blocks and we’re finished! Well, nearly finished. I believe that the most important block in the structure is the last one: “Test Code.” The purpose of this section is to allow you to test a module that is part of a suite of modules without the whole application structure being in place. Writing Python code this way will save a great deal of effort in integrating the components of the application. Of course, this approach applies to any implementation.

3.4 Extending the application

I leave you now with an exercise to extend the calculator and complete the functions that have been left undefined. It would be a simple task to modify the keys list to remove unnecessary keys and produce a rather more focused calculator. It would also be possible to modify the keys to provide a business or hex calculator.

In subsequent examples, you will see more complex manifestations of the application structure illustrated by this example.