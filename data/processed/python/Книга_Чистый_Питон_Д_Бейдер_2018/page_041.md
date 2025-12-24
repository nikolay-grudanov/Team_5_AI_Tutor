---
source_image: page_041.png
page_number: 41
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.81
tokens: 7333
characters: 1541
timestamp: 2025-12-24T02:28:17.470385
finish_reason: stop
---

>>> with ManagedFile('hello.txt') as f:
...     f.write('привет, мир!')
...     f.write('а теперь, пока!')

Python вызывает __enter__, когда поток исполнения входит в контекст инструкции with и наступает момент получения ресурса. Когда поток исполнения снова покидает контекст, Python вызывает __exit__, чтобы высвободить этот ресурс.

Написание менеджера контекста на основе класса не является единственным способом поддержки инструкции with в Python. Служебный модуль contextlib1 стандартной библиотеки обеспечивает еще несколько абстракций, надстроенных поверх базового протокола менеджера контекста. Он может слегка облегчить вашу жизнь, если ваши варианты применения совпадают с тем, что предлагается модулем contextlib.

Например, вы можете применить декоратор contextlib.contextmanager, чтобы определить для ресурса фабричную функцию на основе генератора, которая затем будет автоматически поддерживать инструкцию with. Вот как выглядит пример нашего контекстного менеджера ManagedFile, переписанный в соответствии с этим приемом:

from contextlib import contextmanager

@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()

>>> with managed_file('hello.txt') as f:
...     f.write('привет, мир!')
...     f.write('а теперь, пока!')

В данном случае managed_file() является генератором, который сначала получает ресурс. После этого он временно приостанавливает собственное

1 См. документацию Python «contextlib»: https://docs.python.org/3/library/contextlib.html