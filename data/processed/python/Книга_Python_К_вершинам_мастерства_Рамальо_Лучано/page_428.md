---
source_image: page_428.png
page_number: 428
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.60
tokens: 11600
characters: 1400
timestamp: 2025-12-24T01:54:14.890148
finish_reason: stop
---

Пример 14.1. sentence.py: объект Sentence как последовательность слов

import re
import reprlib

RE_WORD = re.compile(r'\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)  # 1

    def __getitem__(self, index):
        return self.words[index]  # 2

    def __len__(self):  # 3
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)  # 4

1 re.findall возвращает список всех непересекающихся подстрок, соответствующих регулярному выражению.
2 self.words содержит результат .findall, поэтому мы просто возвращаем слово с заданным индексом.
3 Чтобы выполнить требования протокола последовательности, мы реализуем метод __len__, — но для получения итерируемого объекта он не нужен.
4 Служебная функция reprlib.repr генерирует сокращенные строковые представления структур данных, которые могут быть очень велики3.

По умолчанию reprlib.repr ограничивает сгенерированную строку 30 символами. В примере 14.2 показано, как используется класс Sentence.

Пример 14.2. Итерирование объекта Sentence

>>> s = Sentence('»The time has come,» the Walrus said,')
>>> s
Sentence('"The time ha... Walrus said,')
>>> for word in s:  # 3
...     print(word)
The
time
has
come
the
Walrus
said

3 Впервые мы встретились с ней в разделе «Vector, попытка № 1: совместимость с Vector2d» главы 10.