---
source_image: page_077.png
page_number: 77
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.37
tokens: 7485
characters: 1717
timestamp: 2025-12-24T03:02:56.637606
finish_reason: stop
---

XML позволяет использовать пространства имен (группировать данные с помощью тегов). В XML перед тегами в скобках указываются пространства имен. Если структура иерархии известна, можно искать элементы на основе их путей. Для удобства можно передать ассоциативный массив с описанием пространств имен:

In [108]: ns = {'default':'http://www.w3.org/2005/Atom'}
In [106]: authors = root.findall("default:entry/default:author/default:name", ns)

In [107]: for author in authors:
    ...:     print(author.text)
    ...:
Nat Torkington
VM Brasseur
Adam Jacob
Roger Magoulas
Pete Skomoroch
Adrian Cockcroft
Ben Lorica
Nat Torkington
Alison McCauley
Tiffani Bell
Arun Gupta

Вы можете столкнуться также с необходимостью работы с данными в виде значений, отделенных друг от друга запятыми (CSV). Этот формат часто применяется для данных в электронных таблицах. Чтобы было удобно их читать, можно воспользоваться модулем csv Python:

In [16]: import csv
In [17]: file_path = '/Users/kbehrman/Downloads/registered_user_count_ytd.csv'

In [18]: with open(file_path, newline='') as csv_file:
    ...:     off_reader = csv.reader(csv_file, delimiter=',')
    ...:     for _ in range(5):
    ...:         print(next(off_reader))
    ...:
['Date', 'PreviousUserCount', 'UserCountTotal', 'UserCountDay']
['2014-01-02', '61', '5336', '5275']
['2014-01-03', '42', '5378', '5336']
['2014-01-04', '26', '5404', '5378']
['2014-01-05', '65', '5469', '5404']

Объект csv.reader проходит в цикле CSV-файл построчно, благодаря чему можно обрабатывать данные по одной строке за раз. Такой способ обработки файлов особенно удобен для больших CSV-файлов, которые нежелательно полностью загружать в оперативную память. Конечно, если нужно выполнять