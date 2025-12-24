---
source_image: page_305.png
page_number: 305
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.02
tokens: 7511
characters: 1735
timestamp: 2025-12-24T08:53:35.259672
finish_reason: stop
---

рослова. Для этого нам потребуется создать по одному словарю для каждого слова, а затем объединить словари.

Импортируем модуль simpleSubHacker.py в интерактивной оболочке:

>>> import simpleSubHacker

Затем вызовем функцию getBlankCipherletterMapping() для создания пустого словаря шифробукв и сохраним его в переменной letterMapping1.

>>> letterMapping1 = simpleSubHacker.getBlankCipherletterMapping()
>>> letterMapping1
{'A': [], 'C': [], 'B': [], 'E': [], 'D': [], 'G': [], 'F': [], 'I': [], 'H': [], 'K': [], 'J': [], 'M': [], 'L': [], 'O': [], 'N': [], 'Q': [], 'P': [], 'S': [], 'R': [], 'U': [], 'T': [], 'W': [], 'V': [], 'Y': [], 'X': [], 'Z': []}

Приступим к взлому первого шифрослова, 'OLQIHXIRCKGNZ'. Прежде всего, нужно получить для него шаблон, вызвав функцию getWordPattern() из модуля makeWordPatterns.

>>> import makeWordPatterns
>>> makeWordPatterns.getWordPattern('OLQIHXIRCKGNZ')
0.1.2.3.4.5.3.6.7.8.9.10.11

Чтобы определить, какие слова, содержащиеся в файле английского словаря, соответствуют шаблону 0.1.2.3.4.5.3.6.7.8.9.10.11 (т.е. являются словами-кандидатами шифрослова 'OLQIHXIRCKGNZ'), импортируем модуль wordPatterns и выполним поиск этого шаблона.

>>> import wordPatterns
>>> candidates = wordPatterns.allPatterns['0.1.2.3.4.5.3.6.7.8.9.10.11']
>>> candidates
['UNCOMFORTABLE', 'UNCOMFORTABLY']

Шаблону шифрослова 'OLQIHXIRCKGNZ' соответствуют только два английских слова: 'UNCOMFORTABLE' и 'UNCOMFORTABLY'. Они являются нашими кандидатами, поэтому сохраним их в переменной candidates в виде списка.

Далее следует сопоставить буквы этих слов с буквами шифрослова, используя функцию addLettersToMapping(). Сначала сопоставим слово 'UNCOMFORTABLE', обратившись к первому элементу списка кандидатов.