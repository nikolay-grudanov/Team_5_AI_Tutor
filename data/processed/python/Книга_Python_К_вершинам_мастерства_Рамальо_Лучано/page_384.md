---
source_image: page_384.png
page_number: 384
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.96
tokens: 11808
characters: 2025
timestamp: 2025-12-24T01:52:25.661651
finish_reason: stop
---

Глава 12. Наследование: хорошо или плохо

1 Toplevel: класс окна верхнего уровня в приложении Tkinter.
2 Widget: суперкласс всех видимых объектов, которые можно разместить в окне.
3 Button: обычная кнопка.
4 Entry: односторочное редактируемое текстовое поле.
5 Text: многострочное редактируемое текстовое поле

Вот как выглядят MRO этих классов, напечатанные функцией print_mro из примера 12.8:

```python
>>> import tkinter
>>> print_mro(tkinter.Toplevel)
Toplevel, BaseWidget, Misc, Wm, object
>>> print_mro(tkinter.Widget)
Widget, BaseWidget, Misc, Pack, Place, Grid, object
>>> print_mro(tkinter.Button)
Button, Widget, BaseWidget, Misc, Pack, Place, Grid, object
>>> print_mro(tkinter.Entry)
Entry, Widget, BaseWidget, Misc, Pack, Place, Grid, XView, object
>>> print_mro(tkinter.Text)
Text, Widget, BaseWidget, Misc, Pack, Place, Grid, XView, YView, object
```

Стоит обратить внимание на то, как эти классы связаны друг с другом.

• Toplevel — единственный графический класс, не наследующий widget, потому что это окно верхнего уровня, и оно не ведет себя, как виджет, — например, его нельзя присоединить к окну или фрейму. Toplevel наследует классу Wm, который предоставляет функции прямого доступа к объемлющему оконному менеджеру, например, для установки заголовка окна и настройке его рамки.

• Widget наследует непосредственно BaseWidget, а также классам Pack, Place и Grid. Последние три класса — менеджеры компоновки, они отвечают за расположение виджетов в окне или фрейме. Каждый инкапсулирует свою стратегию и API размещения виджетов.

• Button, как и большинство виджетов, напрямую наследует только widget, а опосредованно — классу Misc, который предоставляет десятки методов каждому виджету.

• Entry является подклассом Widget и XView — класса, который реализует горизонтальную прокрутку.

• Text наследует Widget, XView и YView — классу, реализующему вертикальную прокрутку.

Далее мы обсудим некоторые рекомендации по использованию множественного наследования и посмотрим, согласуется ли с ними Tkinter.