---
source_image: page_047.png
page_number: 47
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 63.71
tokens: 8890
characters: 3547
timestamp: 2025-12-24T00:33:15.053098
finish_reason: stop
---

Вот текст программы с комментариями, объясняющими основные моменты:

```python
side=RIGHT, expand=YES, fill=BOTH)

class Key(Button):
    def __init__(self, master, font=('arial', 8, 'bold'),
                 fg='white', width=5, borderwidth=5, **kw):
        kw['font'] = font
        kw['fg'] = fg
        kw['width'] = width
        kw['borderwidth'] = borderwidth
        apply(Button.__init__, (self, master), kw)
        self.pack(side=LEFT, expand=NO, fill=NONE)

class Calculator(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, bg='gray40')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Tkinter Toolkit TT-42')
        self.master.iconname('Tk-42')
        self.calc = Evaluator()      # This is our evaluator
        self.buildCalculator()        # Build the widgets

        # This is an incomplete dictionary - a good exercise!
        self.actionDict = {
            'second': self.doThis, 'mode': self.doThis,
            'delete': self.doThis, 'alpha': self.doThis,
            'stat': self.doThis, 'math': self.doThis,
            'matrix': self.doThis, 'program': self.doThis,
            'vars': self.doThis, 'clear': self.clearall,
            'sin': self.doThis, 'cos': self.doThis,
            'tan': self.doThis, 'up': self.doThis,
            'X1': self.doThis, 'X2': self.doThis,
            'log': self.doThis, 'ln': self.doThis,
            'store': self.doThis, 'off': self.turnoff,
            'neg': self.doThis, 'enter': self.doEnter,
        }
        self.current = ""

    def doThis(self, action):
        print '"%s" has not been implemented' % action

    def turnoff(self, *args):
        self.quit()

    def clearall(self, *args):
        self.current = ""
        self.display.component('text').delete(1.0, END)

    def doEnter(self, *args):
        self.display.insert(END, '\n')
        result = self.calc.runpython(self.current)
        if result:
            self.display.insert(END, '%s\n' % result, 'ans')
        self.current = ""

    def doKeypress(self, event):
        key = event.char
        if key != '\b':
            self.current = self.current + key
```

Комментарии к ключевым частям кода:

2. Класс `Key` наследует от `Button` и определяет метод `__init__`, который принимает параметры `master`, `font`, `fg`, `width` и `borderwidth`. Метод `apply` используется для передачи этих параметров в конструктор `Button`.

3. Класс `Calculator` наследует от `Frame` и определяет метод `__init__`, который создает окно, устанавливает титул и иконку, создает объект `Evaluator` и вызывает метод `buildCalculator` для построения виджетов.

4. В словаре `actionDict` определены методы для различных команд, например, 'delete', 'alpha', 'math', 'vars', 'clear', 'sin', 'cos', 'tan', 'X1', 'X2', 'log', 'ln', 'store', 'off', 'neg', 'enter'. Метод `doThis` выводит сообщение о том, что команда не реализована. Метод `clearall` очищает текстовое поле. Метод `doEnter` вычисляет результат и выводит его в текстовое поле.

5. Метод `doEnter` вызывается при нажатии клавиши Enter. Он добавляет новую строку в текстовое поле, вызывает метод `runpython` для вычисления результата и выводит его в текстовое поле.

6. Если результат вычисления не пустой, метод `doEnter` выводит его в текстовое поле с помощью форматирования.

7. Метод `doKeypress` вызывается при нажатии клавиши. Если это не клавиша Backspace, он добавляет нажатую клавишу к текущей строке.

8. Метод `doKeypress` вызывается при нажатии клавиши. Если это клавиша Backspace, он ничего не делает.