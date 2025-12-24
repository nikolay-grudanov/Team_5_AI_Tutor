---
source_image: page_598.png
page_number: 598
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.89
tokens: 8287
characters: 1890
timestamp: 2025-12-24T00:48:48.920436
finish_reason: stop
---

addmenu(menuName, balloonHelp, statusHelp = None, side = 'left', traverseSpec = None, ** kw)
Adds a menu button and its associated menu to the menu bar. Any keyword arguments present will be passed to the constructor when creating the menu button. If the text keyword argument is not given, the text option of the menu button defaults to menuName. Each menu button is packed into the menu bar using the given side, which should be either left or right.

If the balloon option has been defined, balloonHelp and statusHelp are passed to the balloon as the help strings for the menu button. See the bind() method of Pmw.Balloon for information on how these strings may be displayed.

The menu button is created as a component named menuName-button and the menu is created as a component named menuName-menu. The method returns the menu button component widget.

addmenuitem(menuName, type, help = '', traverseSpec = None, ** kw)
Adds a menu item to the menu given by menuName. The kind of menu item is given by type and it may be one of command, separator, checkbutton, radiobutton or cascade. Any keyword arguments present will be passed to the menu when creating the menu item. See Menu for the valid options for each type. When the mouse is moved over the menu item, the string given by help will be displayed by the balloon’s statuscommand.

deletemenu(menuName)
Deletes the menu named menuName. Subordinate cascade menus should be deleted before main menu items.

deletemenuitems(menuName, start = '0', end = None)
Deletes menu items from the menu named menuName. If start and end are defined it deletes items beginning at index start and ending at index end. If start is defined without end, it deletes the item at start. If neither start or end are defined it deletes all items in menuName.

disableall()
Disables all items in the menubar.

enableall()
Enables all items in the menubar.