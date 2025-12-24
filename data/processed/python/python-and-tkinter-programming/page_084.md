---
source_image: page_084.png
page_number: 84
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.53
tokens: 8379
characters: 2034
timestamp: 2025-12-24T00:33:49.715891
finish_reason: stop
---

4.3.12 MenuBar

The MenuBar widget is a manager widget which provides methods to add menu buttons and menus to the menu bar and to add menu items to the menus. One important convenience is that it is easy to add balloon help to the menus and menu items. Almost all of the menu options available with Tkinter Menu widgets (see “Menu” on page 39) are available through the Pmw MenuBar. Figure 4.34 illustrates a similar menu to the one shown in figure 4.13 using discrete Tkinter widgets.

![Screenshot of a Pmw MenuBar widget showing a menu bar with options such as Buttons, Cascade, Checkbutton, Radiobutton, Close, and Exit](./images/figure_4.34.png)

Figure 4.34 Pmw MenuBar widget

balloon = Pmw.Balloon(root)
menuBar = Pmw.MenuBar(root, hull_relief=RAISED,hull_borderwidth=1,
    balloon=balloon)
menuBar.pack(fill=X)

menuBar.addmenu('Buttons', 'Simple Commands')
menuBar.addmenuitem('Buttons', 'command', 'Close this window',
    font=('StingerLight', 14), label='Close')
menuBar.addmenuitem('Buttons', 'command',
    bitmap="@bitmaps/RotateLeft", foreground='yellow')
menuBar.addmenuitem('Buttons', 'separator')
menuBar.addmenuitem('Buttons', 'command',
    'Exit the application', label='Exit')

menuBar.addmenu('Cascade', 'Cascading Menus')
menuBar.addmenu('Checkbutton', 'Checkbutton Menus')
menuBar.addmenu('Radiobutton', 'Radiobutton Menus')

Documentation for the MenuBar widget starts on page 572.

4.3.13 MessageBar

The MessageBar widget is used to implement a status area for an application. Messages in several discrete categories may be displayed. Each message is displayed for a period of time which is determined by its category. Additionally, each category is assigned a priority so the message with the highest priority is displayed first. It is also possible to specify the number of times that the bell should be rung on receipt of each message category. Figure 4.35 shows how a system error would appear.

messagebar = box = None
def selectionCommand():
    sels = box.getcurselection()
    if len(sels) > 0: