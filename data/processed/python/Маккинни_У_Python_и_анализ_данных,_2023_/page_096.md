---
source_image: page_096.png
page_number: 96
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.39
tokens: 7650
characters: 1852
timestamp: 2025-12-24T02:42:28.613624
finish_reason: stop
---

Чтобы поведение на разных платформах было одинаковым, рекомендуется явно передавать кодировку (например, широко используемую кодировку encoding="utf-8") при открытии файлов.

Метод seek изменяет позицию в файле на указанную:

In [247]: f1.seek(3)
Out[247]: 3

In [248]: f1.read(1)
Out[248]: 'ñ'

In [249]: f1.tell()
Out[249]: 5

Наконец, не забудем закрыть файлы:

In [250]: f1.close()
In [251]: f2.close()

Для записи текста в файл служат методы write или writelines. Например, можно было бы создать вариант файла examples/segismundo.txt без пустых строк:

In [252]: path
Out[252]: 'examples/segismundo.txt'

In [253]: with open("tmp.txt", mode="w") as handle:
.....:     handle.writelines(x for x in open(path) if len(x) > 1)

In [254]: with open("tmp.txt") as f:
.....:     lines = f.readlines()

In [255]: lines
Out[255]:
['Sueña el rico en su riqueza,\n',
 'que más cuidados le ofrece;\n',
 'sueña el pobre que padece\n',
 'su miseria y su pobreza;\n',
 'sueña el que a medrar empieza,\n',
 'sueña el que afana y pretende,\n',
 'sueña el que agravia y ofende,\n',
 'y en el mundo, en conclusión,\n',
 'todos sueñan lo que son,\n',
 'aunque ninguno lo entiende.\n']

В табл. 3.4 приведены многие из наиболее употребительных методов работы с файлами.

Таблица 3.4. Наиболее употребительные методы и атрибуты для работы с файлами в Python

<table>
  <tr>
    <th>Метод</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>read([size])</td>
    <td>Возвращает прочитанные из файла данные в виде строки. Необязательный аргумент size говорит, сколько байтов читать</td>
  </tr>
  <tr>
    <td>readable()</td>
    <td>Возвращает True, если файл поддерживает операции read</td>
  </tr>
  <tr>
    <td>readlines([size])</td>
    <td>Возвращает список прочитанных из файла строк. Необязательный аргумент size говорит, сколько строк читать</td>
  </tr>
</table>