---
source_image: page_074.png
page_number: 74
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.56
tokens: 8456
characters: 2849
timestamp: 2025-12-24T00:33:32.253573
finish_reason: stop
---

4.2.4 Setting application-wide default fonts and colors

When designing an application, you may find that the default colors, fonts and font-sizes supplied by the system are not appropriate for the particular layout that you have in mind. At such times you must set their values explicitly. The values could be put right in the code (you will see several examples in the book where this has been done). However, this prevents end users or system administrators from tailoring an application to their particular requirements or business standards. In this case the values should be set in an external option database. For X window programmers this is equivalent to the resource database which is usually tailored using a .Xdefaults file. In fact the format of the Tk option database is exactly like the .Xdefaults file:

*font:                Verdana 10
*Label*font:           Verdana 10 bold
*background:           Gray80
*Entry*background:     white
*foreground:           black
*Listbox*foreground:    RoyalBlue

The purpose of these entries is to set the font for all widgets except Labels to Verdana 10 (regular weight) and Labels to Verdana 10 bold. Similarly we set the default colors for background and foreground, modifying Entry backgrounds and Listbox foregrounds. If we place these entries in a file called optionDB, we can apply the values using an option_readfile call:

root = Tk()
root.option_readfile('optionDB')

This call should be made early in the code to ensure that all widgets are created as intended.

4.3 Pmw Megawidget tour

Python megawidgets, Pmw, are composite widgets written entirely in Python using Tkinter widgets as base classes. They provide a convenient way to add functionality to an application without the need to write a lot of code. In particular, the ComboBox is a useful widget, along with the Entry field with several built-in validation schemes.

In a similar fashion to the Tkinter tour, above, the following displays show typical Pmw widget appearance and usage. The code is kept short and it illustrates some of the options available for the widgets. If you need to look up a particular method or option, refer to appendix C. Each widget also has references to the corresponding section in the appendix.

Pmw comes with extensive documentation in HTML format. Consequently this chapter will not repeat this information here. Additionally, there is example code for all of the widgets in the demos directory in the Pmw distribution. Most of the examples shown are simplifications derived from that code.

With the exception of the first example, the code examples have been stripped of the boilerplate code necessary to import and initialize Tkinter. The common code which is not shown in any sequences after the first is shown in bold. The full source code for all of the displays is available online.