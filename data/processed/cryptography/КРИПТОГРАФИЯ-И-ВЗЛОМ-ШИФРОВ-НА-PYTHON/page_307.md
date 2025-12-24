---
source_image: page_307.png
page_number: 307
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.38
tokens: 7635
characters: 2094
timestamp: 2025-12-24T08:53:46.292769
finish_reason: stop
---

'N'], 'O': [], 'N': [], 'Q': ['N', 'C', 'R', 'I'], 'P': ['C', 'I', 'P', 'U'], 'S': [], 'R': ['V', 'R', 'T'], 'U': [], 'T': [], 'W': [], 'V': [], 'Y': [], 'X': [], 'Z': ['E']}

Вместо того чтобы четырежды вводить функцию addLettersToMapping() для каждого из четырех слов-кандидатов, мы организуем цикл for по словам-кандидатам в списке. Таким образом, мы получили словарь шифробукв для второго шифрослова.

Следующий шаг — создание пересечения словарей, сохраненных в переменных letterMapping1 и letterMapping2. Для этого мы передаем словари в функцию intersectMappings(). Введите в интерактивной оболочке следующие инструкции.

>>> intersectedMapping = simpleSubHacker.intersectMappings(letterMapping1, letterMapping2)
>>> intersectedMapping
{'A': [], 'C': ['T'], 'B': ['S', 'D'], 'E': [], 'D': [], 'G': ['B'], 'F': [], 'I': ['O'], 'H': ['M'], 'K': ['A'], 'J': [], 'M': [], 'L': ['N'], 'O': ['U'], 'N': ['L'], 'Q': ['C'], 'P': ['C', 'I', 'P', 'U'], 'S': [], 'R': ['R'], 'U': [], 'T': [], 'W': [], 'V': [], 'Y': [], 'X': ['F'], 'Z': ['E']}

Теперь список вариантов дешифрования для любой шифробуквы, входящей в объединенный словарь, должен содержать лишь варианты, общие для словарей letterMapping1 и letterMapping2. Например, список для ключа 'Z' включает лишь одну букву, ['E'], поскольку словарь letterMapping1 содержал список ['E', 'Y'], тогда как словарь letterMapping2 — только список ['E'].

Далее повторяем все то же самое для третьего шифрослова, 'MPBKSSIPLC'.

>>> letterMapping3 = simpleSubHacker.getBlankCipherletterMapping()
>>> wordPat = makeWordPatterns.getWordPattern('MPBKSSIPLC')
>>> candidates = wordPatterns.allPatterns[wordPat]
>>> for i in range(len(candidates)):
...    simpleSubHacker.addLettersToMapping(letterMapping3, 'MPBKSSIPLC', candidates[i])
...
>>> letterMapping3
{'A': [], 'C': ['Y', 'T'], 'B': ['M', 'S'], 'E': [], 'D': [], 'G': [], 'F': [], 'I': ['E', 'O'], 'H': [], 'K': ['I', 'A'], 'J': [], 'M': ['A', 'D'], 'L': ['L', 'N'], 'O': [], 'N': [], 'Q': [], 'P': ['D', 'I'], 'S': ['T', 'P'], 'R': [], 'U': [], 'T': [], 'W': [], 'V': [], 'Y': [], 'X': [], 'Z': []}