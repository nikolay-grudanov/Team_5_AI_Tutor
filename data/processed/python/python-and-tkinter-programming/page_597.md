---
source_image: page_597.png
page_number: 597
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.14
tokens: 8346
characters: 1841
timestamp: 2025-12-24T00:48:51.050577
finish_reason: stop
---

MenuBar

Description
This class creates a manager widget for containing menus. There are methods to add menu buttons and menus to the menu bar and for adding menu items to the menus. Menu buttons may be added to the left or right of the widget. Each menu button and menu item may have help text to be displayed by a Pmw.Balloon widget.

Inheritance
MenuBar inherits from Pmw.MegaWidget.

MenuBar options

<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
    <th>Units</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>balloon</td>
    <td>Specifies the Pmw.Balloon widget to display the help text for menu buttons and menu items. If None, no help is displayed.</td>
    <td>widget</td>
    <td>None</td>
  </tr>
  <tr>
    <td>hotkeys</td>
    <td>Specifies if the menu is to support “hot keys”, otherwise known as “accelerators”. If true, the user may select menu items using the underlined character in the item’s text.</td>
    <td>boolean</td>
    <td>1</td>
  </tr>
  <tr>
    <td>padx</td>
    <td>Specifies a padding distance to leave between each menu button in the x direction and also between the menu buttons and the outer edge of the menu bar.</td>
    <td>distance</td>
    <td>0</td>
  </tr>
</table>

Components
hull
This acts as the body for the entire megawidget. Other components are created as children of the hull to further specialize the widget.

Methods
addcascademenu(menuName, submenu, help = "", traverseSpec = None, ** kw)
Adds a cascade submenu which is named submenu-menu to menu menuName. submenu must not already exist. If help is defined it is used for balloonHelp. If traverseSpec is defined it defines the underline character within the cascade which may be used as a keyboard accelerator. traverseSpec may be defined either as the character or the integer index of the character to be underlined.