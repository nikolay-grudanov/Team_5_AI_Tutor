---
source_image: page_065.png
page_number: 65
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.52
tokens: 8305
characters: 1655
timestamp: 2025-12-24T00:33:07.520233
finish_reason: stop
---

CmdBtn.pack(side=LEFT, padx="2m")
CmdBtn.menu = Menu(CmdBtn)

CmdBtn.menu.add_command(label="Undo")
CmdBtn.menu.entryconfig(0, state=DISABLED)

CmdBtn.menu.add_command(label='New...', underline=0, command=new_file)
CmdBtn.menu.add_command(label='Open...', underline=0, command=open_file)
CmdBtn.menu.add_command(label='Wild Font', underline=0,
    font=('Tempus Sans ITC', 14), command=stub_action)
CmdBtn.menu.add_command(bitmap="@bitmaps/RotateLeft")
CmdBtn.menu.add('separator')
CmdBtn.menu.add_command(label='Quit', underline=0,
    background='white', activebackground='green',
    command=CmdBtn.quit)

CmdBtn['menu'] = CmdBtn.menu
return CmdBtn

Figure 4.14 shows the appearance of Cascade menu entries.

![Screenshot of a Cascade menu showing nested menu options](https://i.imgur.com/3Q5z5QG.png)

Figure 4.14 Menu: Cascade

def makeCascadeMenu():
    CasBtn = Menubutton(mBar, text='Cascading Menus', underline=0)
    CasBtn.pack(side=LEFT, padx="2m")
    CasBtn.menu = Menu(CasBtn)

    CasBtn.menu.choices = Menu(CasBtn.menu)
    CasBtn.menu.choices.wierdones = Menu(CasBtn.menu.choices)

    CasBtn.menu.choices.wierdones.add_command(label='Stockbroker')
    CasBtn.menu.choices.wierdones.add_command(label='Quantity Surveyor')
    CasBtn.menu.choices.wierdones.add_command(label='Church Warden')
    CasBtn.menu.choices.wierdones.add_command(label='BRM')
    CasBtn.menu.choices.add_command(label='Wooden Leg')
    CasBtn.menu.choices.add_command(label='Hire Purchase')
    CasBtn.menu.choices.add_command(label='Dead Crab')
    CasBtn.menu.choices.add_command(label='Tree Surgeon')
    CasBtn.menu.choices.add_command(label='Filing Cabinet')