---
source_image: page_040.png
page_number: 40
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.86
tokens: 8464
characters: 2253
timestamp: 2025-12-24T00:32:36.570347
finish_reason: stop
---

Parent widgets (usually referred to as *master* widgets) are explicit in Tkinter:

<table>
  <tr>
    <th>Tcl/Tk</th>
    <th>Tkinter</th>
  </tr>
  <tr>
    <td>label .screen.for</td>
    <td>label = Label(form) (screen is form’s parent)</td>
  </tr>
</table>

For configuration options, Tk uses keyword arguments followed by values or configure commands; Tkinter uses either keyword arguments or a dictionary reference to the option of the configure method in the target widget.

<table>
  <tr>
    <th>Tcl/Tk</th>
    <th>Tkinter</th>
  </tr>
  <tr>
    <td>label .myLabel -bg blue</td>
    <td>myLabel = Label(master, bg="blue")</td>
  </tr>
  <tr>
    <td>.myLabel configure -bg blue</td>
    <td>myLabel["bg"] = "blue"<br>myLabel.configure(bg = "blue")</td>
  </tr>
</table>

Since the Tkinter widget object has methods, you invoke them directly, adding arguments as appropriate.

<table>
  <tr>
    <th>Tcl/Tk</th>
    <th>Tkinter</th>
  </tr>
  <tr>
    <td>pack label -side left -fill y</td>
    <td>label.pack(side=LEFT, fill=Y)</td>
  </tr>
</table>

The following illustration demonstrates how we access an inherited method *pack* from the Packer. This style of programming contributes to the compact nature of Tkinter applications and their ease of maintenance and reuse.
Full mappings of Tk to Tkinter are provided in “Mapping Tk to Tkinter” on page 383.

2.3 *Win32 and UNIX GUIs*

As I mentioned earlier, it is reasonable to develop Tkinter applications for use in Win32, UNIX and Macintosh environments. Tcl/Tk is portable and can be built on the specific platform, as can Python, with its _tkinter C module. Using *Pmw* (Python MegaWidgets), which provides a portable set of composite widgets and is 100% Python code, it is possible to use the bytecode generated on a UNIX system on a Win32 or Macintosh system. What you cannot control is the use of fonts and, to a lesser extent, the color schemes imposed by the operating system.

* Pmw—Python MegaWidgets provide complex widgets, constructed from fundamental Tkinter widgets, which extend the available widgets to comboboxes, scrolled frames and button boxes, to name a few. Using these widgets gives GUI developers a rich palette of available input devices to use in their designs.