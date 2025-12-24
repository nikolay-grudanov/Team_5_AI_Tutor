---
source_image: page_064.png
page_number: 64
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.78
tokens: 8237
characters: 1445
timestamp: 2025-12-24T00:33:02.624146
finish_reason: stop
---

('Michael Palin',2,0,NORMAL), ('Terry Gilliam', 2,1,NORMAL)]:
    setattr(var, castmember, IntVar())
    Checkbutton(root, text=castmember, state=status, anchor=W,
                variable = getattr(var, castmember)).grid(row=row, col=col, sticky=W)

Documentation for the Checkbutton widget starts on page 481.

4.1.8 Menu

Menu widgets provide a familiar method to allow the user to choose operations within an application. Menus can be fairly cumbersome to construct, especially if the cascades walk out several levels (it is usually best to try design menus so that you do not need to walk out more than three levels to get to any functionality).

Tkinter provides flexibility for menu design, allowing multiple fonts, images and bitmaps, and checkbuttons and radiobuttons. It is possible to build the menu in several schemes. The example shown in figure 4.12 is one way to build a menu; you will find an alternate scheme to build the same menu online as altmenu.py.

Figure 4.12 Menu widget

Figure 4.13 illustrated adding Button commands to menu.

Figure 4.13 Menu: Button commands

mBar = Frame(root, relief=RAISED, borderwidth=2)
mBar.pack(fill=X)
CmdBtn = makeCommandMenu()
CasBtn = makeCascadeMenu()
ChkBtn = makeCheckbuttonMenu()
RadBtn = makeRadiobuttonMenu()
NoMenu = makeDisabledMenu()
mBar.tk_menuBar(CmdBtn, CasBtn, ChkBtn, RadBtn, NoMenu)
def makeCommandMenu():
    CmdBtn = Menubutton(mBar, text='Button Commands', underline=0)