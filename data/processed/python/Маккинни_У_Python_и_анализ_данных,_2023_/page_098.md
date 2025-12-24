---
source_image: page_098.png
page_number: 98
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.30
tokens: 7612
characters: 2043
timestamp: 2025-12-24T02:42:31.456228
finish_reason: stop
---

Зная кодировку текста, вы можете декодировать байты в объект str самостоятельно, но только в том случае, когда последовательность байтов корректна и полна:

In [263]: data.decode("utf-8")
Out[263]: 'Sueña el '

In [264]: data[:4].decode("utf-8")
---------------------------------------------------------------------------
UnicodeDecodeError                       Traceback (most recent call last)
<ipython-input-264-846a5c2fed34> in <module>
----> 1 data[:4].decode("utf-8")
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc3 in position 3: unexpected end of data

Текстовый режим в сочетании с параметром encoding функции open — удобный способ преобразовать данные из одной кодировки Unicode в другую:

In [265]: sink_path = "sink.txt"

In [266]: with open(path) as source:
.....:     with open(sink_path, "x", encoding="iso-8859-1") as sink:
.....:         sink.write(source.read())

In [267]: with open(sink_path, encoding="iso-8859-1") as f:
.....:     print(f.read(10))
Sueña el r

Будьте осторожны, вызывая метод seek для файла, открытого не в двоичном режиме. Если указанная позиция окажется в середине последовательности байтов, образующих один символ Unicode, то последующие операции чтения завершатся ошибкой:

In [269]: f = open(path, encoding='utf-8')

In [270]: f.read(5)
Out[270]: 'Sueca'

In [271]: f.seek(4)
Out[271]: 4

In [272]: f.read(1)
---------------------------------------------------------------------------
UnicodeDecodeError                       Traceback (most recent call last)
<ipython-input-272-5a354f952aa4> in <module>
----> 1 f.read(1)
/miniconda/envs/book-env/lib/python3.10/codecs.py in decode(self, input, final)
    320     # decode input (taking the buffer into account)
    321     data = self.buffer + input
--> 322     (result, consumed) = self._buffer_decode(data, self.errors, final)
    323     # keep undecoded input until the next call
    324     self.buffer = data[consumed:]
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb1 in position 0: invalid start byte

In [273]: f.close()