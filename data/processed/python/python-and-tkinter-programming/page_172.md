---
source_image: page_172.png
page_number: 172
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.07
tokens: 8521
characters: 2255
timestamp: 2025-12-24T00:36:20.458281
finish_reason: stop
---

Вот текст кода с комментариями и номерами строк, соответствующими меткам в правом верхнем углу:

```python
def doBaseForm(self, master):
    # Create the Balloon.
    self.balloon = Pmw.Balloon(master)

    self.menuBar = Pmw.MenuBar(master, hull_borderwidth=1,
        hull_relief = RAISED,
        hotkeys=1, balloon = self.balloon)
    self.menuBar.pack(fill=X)

    self.menuBar.addmenu('File', 'Exit')
    self.menuBar.addmenuitem('File', 'command',
        'Exit the application',
        label='Exit', command=self.exit)
    self.menuBar.addmenu('View', 'View status')
    self.menuBar.addmenuitem('View', 'command',
        'Get user status',
        label='Get status',
        command=self.getStatus)
    self.menuBar.addmenu('Help', 'About Example 8-4', side=RIGHT)
    self.menuBar.addmenuitem('Help', 'command',
        'Get information on application',
        label='About...', command=self.help)

    self.dataFrame = Frame(master)
    self.dataFrame.pack(fill=BOTH, expand=1)

    self.infoFrame = Frame(self.root,bd=1, relief='groove')
    self.infoFrame.pack(fill=BOTH, expand=1, padx = 10)

    self.statusBar = Pmw.MessageBar(master, entry_width = 40,
        entry_relief='groove',
        labelfpos = W,
        label_text = '')
    self.statusBar.pack(fill = X, padx = 10, pady = 10)

    # Add balloon text to statusBar
    self.balloon.configure(statuscommand = self.statusBar.helpmessage)

    # Create about dialog.
    Pmw.aboutversion('8.1')
    Pmw.aboutcopyright('Copyright My Company 1999'
        '\nAll rights reserved')
    Pmw.aboutcontact(
        'For information about this application contact:\n' +
        '    My Help Desk\n'
        '    Phone: 800 555-1212\n'
        '    email: help@my.company.com'
    )
    self.about = Pmw.AboutDialog(master,
        applicationname = 'Example 8-4')
    self.about.withdraw()

def exit(self):
    import sys
    sys.exit(0)
```

Комментарии и метки:
2. Создание объекта Balloon
3. Создание и настройка менюбар
4. Добавление пунктов меню "File" и "View"
5. Создание и настройка данных фрейма
6. Создание и настройка инфо фрейма
7. Создание и настройка статус бара
8. Настройка сообщений о баллоне
9. Создание и настройка диалога о программе
10. Функция выхода из программы