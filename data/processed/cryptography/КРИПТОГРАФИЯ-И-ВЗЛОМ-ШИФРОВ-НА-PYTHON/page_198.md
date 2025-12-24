---
source_image: page_198.png
page_number: 198
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.39
tokens: 7407
characters: 1937
timestamp: 2025-12-24T08:50:55.584257
finish_reason: stop
---

34. if word in ENGLISH_WORDS:
35.     matches += 1
36. return float(matches) / len(possibleWords)
37.
38.
39. def removeNonLetters(message):
40.     lettersOnly = []
41.     for symbol in message:
42.         if symbol in LETTERS_AND_SPACE:
43.             lettersOnly.append(symbol)
44.     return ''.join(lettersOnly)
45.
46.
47. def isEnglish(message, wordPercentage=20, letterPercentage=85):
48.     # По умолчанию 20% слов должны быть в файле словаря,
49.     # а 85% символов сообщения должны быть буквами или
50.     # пробелами (а не знаками препинания или числами)
51.     wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
52.     numLetters = len(removeNonLetters(message))
53.     messageLettersPercentage = float(numLetters) / len(message) * 100
54.     lettersMatch = messageLettersPercentage >= letterPercentage
55.     return wordsMatch and lettersMatch

Применение модуля Detect English

Программа detectEnglish.py не будет выполняться сама по себе. Вместо этого другие программы шифрования будут импортировать ее, чтобы можно было вызвать функцию detectEnglish.isEnglish(), которая возвращает True, если строка определяется как текст на английском языке. Вот почему в файле detectEnglish.py нет функции main(). Другие функции, включенные в файл detectEnglish.py, являются вспомогательными и вызываются функцией isEnglish(). То, что мы сделаем в этой главе, позволит любой программе импортировать модуль detectEnglish с помощью инструкции import и использовать содержащиеся в нем функции.

Вы также сможете использовать этот модуль в интерактивной оболочке, для того чтобы проверить, представляет ли собой отдельная строка текст на английском языке.

>>> import detectEnglish
>>> detectEnglish.isEnglish('Is this sentence English text?')
True

В этом примере функция определила, что строка 'Is this sentence English text?' действительно представляет текст на английском языке, и поэтому вернула значение True.