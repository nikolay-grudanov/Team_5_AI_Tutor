---
source_image: page_137.png
page_number: 137
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.49
tokens: 8496
characters: 2042
timestamp: 2025-12-24T00:35:20.719269
finish_reason: stop
---

Вот текст программы с комментариями и объяснениями:

```python
self._time = Pmw.EntryField(master,
    labelfpos = 'w', label_text = 'Time (24hr clock):',
    value = '8:00:00',
    validate = {'validator':'time',
        'min':'00:00:00', 'max':'23:59:59',
        'minstrict':0, 'maxstrict':0})

self._real = Pmw.EntryField(master,
    labelfpos = 'w',value = '127.2',
    label_text = 'Real (50.0 to 1099.0):',
    validate = {'validator':'real',
        'min':50, 'max':1099,
        'minstrict':0},
    modifiedcommand = self.valueChanged)

self._ssn = Pmw.EntryField(master,
    labelfpos = 'w', label_text = 'Social Security #:',
    validate = self.validateSSN, value = '')  # 3

fields = (self._date, self._time, self._real, self._ssn)
for field in fields:
    field.pack(fill='x', expand=1, padx=12, pady=8)

Pmw.alignlabels(fields)
self._date.component('entry').focus_set()  # 4

def valueChanged(self):
    print 'Value changed, value is', self._real.get()

def validateSSN(self, contents):
    result = -1
    if '-' in contents:
        ssnf = string.split(contents, '-')
        try:
            if len(ssnf[0]) == 3 and \
                len(ssnf[1]) == 2 and \
                len(ssnf[2]) == 4:
                result = 1
        except IndexError:
            result = -1
    elif len(contents) == 9:
        result = 1
    return result

if __name__ == '__main__':
    root = Tk()
    root.option_add('*Font', 'Verdana 10 bold')
    root.option_add('*EntryField.Entry.Font', 'Courier 10')
    root.option_add('*EntryField.errorbackground', 'yellow')
    Pmw.initialise(root, useTkOptionDb=1)

    root.title('Pmw EntryField Validation')
    quit = Button(root, text='Quit', command=root.destroy)
    quit.pack(side = 'bottom')
    top = EntryValidation(root)
    root.mainloop()
```

Комментарии к номерам:

2. Установка поля для вещественного числа.
3. Установка поля для номера社会保险安全号。
4. Выравнивание меток полей.
5. Функция проверки номера社会保险安全号.
6. Функция обновления значения.
7. Настройка окна и запуск приложения.