---
source_image: page_435.png
page_number: 435
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.45
tokens: 11604
characters: 1498
timestamp: 2025-12-24T01:54:49.444387
finish_reason: stop
---

Класс Sentence, попытка № 2: классический вариант

Мы поступаем так, чтобы прояснить важнейшее различие между итерируемым объектом и итератором, а также показать, как они связаны между собой.

Пример 14.4. sentence_iter.py: класс Sentence, реализованный с помощью паттерна Итератор

import re
import reprlib

RE_WORD = re.compile(r'\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self): ①
        return SentenceIterator(self.words) ②

class SentenceIterator:

    def __init__(self, words):
        self.words = words ③
        self.index = 0 ④

    def __next__(self):
        try:
            word = self.words[self.index] ⑤
        except IndexError:
            raise StopIteration() ⑥
        self.index += 1 ⑦
        return word ⑧

    def __iter__(self): ⑨
        return self

① Метод __iter__ — единственное дополнение к предыдущей реализации Sentence. В этой версии нет метода __getitem__, тем самым мы хотим доказать, что класс является итерируемым, потому что реализует __iter__.
② __iter__ выполняет требования протокола итерируемого объекта — создает и возвращает итератор.
③ SentenceIterator хранит ссылку на список слов.
④ self.index используется для определения следующего слова.
⑤ Получаем слово с индексом self.index.
⑥ Если слова с индексом self.index не существует, возбуждаем исключение StopIteration.