---
source_image: page_094.png
page_number: 94
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.15
tokens: 7592
characters: 1991
timestamp: 2025-12-24T02:42:25.905369
finish_reason: stop
---

функция pandas.read_csv. Однако важно понимать основы работы с файлами в Python. По счастью, здесь все очень просто, и именно поэтому Python так часто выбирают, когда нужно работать с текстом или файлами.

Чтобы открыть файл для чтения или для записи, пользуйтесь встроенной функцией open, которая принимает относительный или абсолютный путь:

In [233]: path = "examples/segismundo.txt"

In [234]: f = open(path, encoding="utf-8")

По умолчанию файл открывается только для чтения — в режиме 'r'. Далее описатель файла f можно рассматривать как список и перебирать строки:

for line in f:
    print(line)

У строк, прочитанных из файла, сохраняется признак конца строки (EOL), поэтому часто можно встретить код, который удаляет концы строк:

In [235]: lines = [x.rstrip() for x in open(path, encoding="utf-8")]

In [236]: lines
Out[236]:
['Sueña el rico en su riqueza,',
 'que más cuidados le ofrece;',
 '',
 'sueña el pobre que padece',
 'su miseria y su pobreza;',
 '',
 'sueña el que a medrar empieza,',
 'sueña el que afana y pretende,',
 'sueña el que agravia y ofende,',
 '',
 'y en el mundo, en conclusión,',
 'todos sueñan lo que son,',
 'aunque ninguno lo entiende.',
 '']

Если для создания объекта файла использовалась функция open, то следует явно закрывать файл по завершении работы с ним. Закрытие файла возвращает ресурсы операционной системе:

In [237]: f.close()

Упростить эту процедуру позволяет предложение with:

In [238]: with open(path) as f:
     .....:     lines = [x.rstrip() for x in f]

В таком случае файл f автоматически закрывается по выходе из блока with. Если не позаботиться о закрытии файлов, то в небольших скриптах может и не произойти ничего страшного, но в программах, работающих с большим количеством файлов, возможны проблемы.

Если бы мы написали f = open(path, 'w'), то был бы создан новый файл examples/segismundo.txt (будьте осторожны!), а старый был бы перезаписан. Существует также режим 'x', в котором создается допускающий запись файл, но лишь