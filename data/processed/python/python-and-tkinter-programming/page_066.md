---
source_image: page_066.png
page_number: 66
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.34
tokens: 8410
characters: 1751
timestamp: 2025-12-24T00:33:16.431262
finish_reason: stop
---

CasBtn.menu.choices.add_command(label='Goldfish')
CasBtn.menu.choices.add_cascade(label='Is it a...',
menu=CasBtn.menu.choices.wierdones)
CasBtn.menu.add_cascade(label='Scipts', menu=CasBtn.menu.choices)
CasBtn['menu'] = CasBtn.menu
return CasBtn

Check buttons may be used within a menu, as shown in figure 4.15.

![Screenshot of a menu window showing checkbuttons](./images/figure_4.15.png)

Figure 4.15 Menu: Checkbuttons

def makeCheckbuttonMenu():
    ChkBttn = Menubutton(mBar, text='Checkbutton Menus', underline=0)
    ChkBttn.pack(side=LEFT, padx='2m')
    ChkBttn.menu = Menu(ChkBttn)

    ChkBttn.menu.add_checkbutton(label='Doug')
    ChkBttn.menu.add_checkbutton(label='Dinsdale')
    ChkBttn.menu.add_checkbutton(label="Stig O'Tracy")
    ChkBttn.menu.add_checkbutton(label='Vince')
    ChkBttn.menu.add_checkbutton(label='Gloria Pules')

    ChkBttn.menu.invoke(ChkBttn.menu.index('Dinsdale'))
    ChkBttn['menu'] = ChkBttn.menu
    return ChkBttn

An alternative is to use Radiobuttons in a menu, as illustrated in figure 4.16.

def makeRadiobuttonMenu():
    RadBttn = Menubutton(mBar, text='Radiobutton Menus', underline=0)
    RadBttn.pack(side=LEFT, padx='2m')
    RadBttn.menu = Menu(RadBttn)

    RadBttn.menu.add_radiobutton(label='metonymy')
    RadBttn.menu.add_radiobutton(label='zeugmatists')
    RadBttn.menu.add_radiobutton(label='synechdotists')
    RadBttn.menu.add_radiobutton(label='axiomists')
    RadBttn.menu.add_radiobutton(label='anagogists')
    RadBttn.menu.add_radiobutton(label='catachresis')
    RadBttn.menu.add_radiobutton(label='periphrastic')
    RadBttn.menu.add_radiobutton(label='litotes')
    RadBttn.menu.add_radiobutton(label='circumlocutors')

    RadBttn['menu'] = RadBttn.menu
    return RadBttn