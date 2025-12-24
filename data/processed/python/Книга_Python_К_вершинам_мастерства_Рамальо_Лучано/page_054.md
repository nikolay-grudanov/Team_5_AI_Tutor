---
source_image: page_054.png
page_number: 54
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 52.89
tokens: 11888
characters: 1878
timestamp: 2025-12-24T01:37:11.601280
finish_reason: stop
---

>>> s = 'bicycle'
>>> s[::3]
'bye'
>>> s[::1]
'elcycib'
>>> s[::2]
'eccb'

Еще один пример был приведен в главе 1, где мы использовали выражение deck[12::13] для выборки всех тузов из неперетасованной колоды:

>>> deck[12::13]
[Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]

Нотация a:b:c допустима только внутри квадратных скобок, когда используется в качестве оператора индексирования и порождает объект среза slice(a, b, c). В разделе «Как работает срезка» на стр. 311 мы увидим, что для вычисления выражения seq[start:stop:step] Python вызывает метод seq.__getitem__(slice(start, stop, step)). Даже если вы никогда не будете сами реализовывать типы последовательностей, знать об объектах среза полезно, потому что это позволяет присваивать срезам имена — по аналогии с именами диапазонов ячеек в электронных таблицах.

Пусть требуется разобрать плоский файл данных, например накладную, показанную в примере 2.11. Вместо того чтобы загромождать код «защитными» диапазонами, мы можем поименовать их. Посмотрим, насколько понятным становится при этом цикл for в конце примера.

Пример 2.11. Строки из файла накладной

>>> invoice = """
... 0......6........................................40.......52...55.......
... 1909 Pimoroni PiBrella $17.50 3 $52.50
... 1489 6mm Tactile Switch x20 $4.95 2 $9.90
... 1510 Panavise Jr. - PV-201 $28.00 1 $28.00
... 1601 PiTFT Mini Kit 320x240 $34.95 1 $34.95
... ""
>>> SKU = slice(0, 6)
>>> DESCRIPTION = slice(6, 40)
>>> UNIT_PRICE = slice(40, 52)
>>> QUANTITY = slice(52, 55)
>>> ITEM_TOTAL = slice(55, None)
>>> line_items = invoice.split('\n')[2:]
>>> for item in line_items:
...     print(item[UNIT_PRICE], item[DESCRIPTION])
...
$17.50    Pimoroni PiBrella
$4.95     6mm Tactile Switch x20
$28.00    Panavise Jr. - PV-201
$34.95    PiTFT Mini Kit 320x240