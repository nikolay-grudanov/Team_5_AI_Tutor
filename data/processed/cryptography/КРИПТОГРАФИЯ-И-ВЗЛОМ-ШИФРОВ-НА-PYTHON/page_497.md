---
source_image: page_497.png
page_number: 497
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.72
tokens: 7250
characters: 1004
timestamp: 2025-12-24T08:58:49.195506
finish_reason: stop
---

3. Напишите цикл for для вывода значений, содержащихся в следующем словаре.

spam = {'name': 'Zophie', 'species': 'cat', 'age': 8}

ОТВЕТ:
for key in spam:
    print(spam[key])

4. Что выведет следующий код?

print('Hello, world!'.split())

ОТВЕТ: ['Hello,', 'world!']

5. Что выведет следующий код?

def spam(eggs=42):
    print(eggs)
spam()
spam('Hello')

ОТВЕТ:
42
Hello

6. Каков процент слов английского языка в следующем предложении?

"Whether it's flobulllar in the mind to quarfalog the slings and arrows of outrageous guuuuuuuuuur."

ОТВЕТ: 80% (12 из 15 слов: 12 / 15 = 0,8, т.е. 80%).

Глава 12

1. Какой результат вернет приведенное ниже выражение?

' Hello world'.strip()

ОТВЕТ: 'Hello world'

2. Какие символы являются пробельными?

ОТВЕТ: символы пробела, табуляции и перехода на новую строку.

3. Почему вызов 'Hello world'.strip('o') возвращает строку, которая по-прежнему содержит букву 'o'?

ОТВЕТ: потому что метод strip() удаляет лишь символы, находящиеся в начале и в конце строки.