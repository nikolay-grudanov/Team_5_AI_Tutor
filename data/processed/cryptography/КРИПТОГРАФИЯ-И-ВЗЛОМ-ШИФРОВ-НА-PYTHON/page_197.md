---
source_image: page_197.png
page_number: 197
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.03
tokens: 7395
characters: 1699
timestamp: 2025-12-24T08:50:49.729567
finish_reason: stop
---

будем идентифицировать сообщение как текст на английском языке. А раз так, то существует большая вероятность того, что мы успешно дешифровали шифротекст с корректным ключом.

Исходный код модуля Detect English

Откройте в редакторе файлов новое окно, выбрав пункты меню File⇒New File. Введите приведенный ниже код и сохраните его в файле detectEnglish.py. Убедитесь, что файл dictionary.txt находится в том же самом каталоге, иначе программа не будет работать. Запустите программу, нажав клавишу <F5>.

detectEnglish.py

1. # Модуль распознавания английского языка
2. # https://www.nostarch.com/crackingcodes/ (BSD Licensed)
3.
4. # Чтобы использовать данный модуль, введите следующий код:
5. # import detectEnglish
6. # detectEnglish.isEnglish(someString) # возвращает True или False
7. # В каталоге программы должен существовать файл dictionary.txt,
8. # содержащий по одному слову в строке. Файл доступен для загрузки
9. # на сайте издательства (см. введение).
10. UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
11. LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + '\t\n'
12.
13. def loadDictionary():
14.     dictionaryFile = open('dictionary.txt')
15.     englishWords = {}
16.     for word in dictionaryFile.read().split('\n'):
17.         englishWords[word] = None
18.     dictionaryFile.close()
19.     return englishWords
20.
21. ENGLISH_WORDS = loadDictionary()
22.
23.
24. def getEnglishCount(message):
25.     message = message.upper()
26.     message = removeNonLetters(message)
27.     possibleWords = message.split()
28.
29.     if possibleWords == []:
30.         return 0.0 # слова отсутствуют, поэтому возвращаем 0.0
31.
32.     matches = 0
33.     for word in possibleWords: