---
source_image: page_306.png
page_number: 306
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.73
tokens: 7663
characters: 2144
timestamp: 2025-12-24T08:53:42.876628
finish_reason: stop
---

>>> simpleSubHacker.addLettersToMapping(letterMapping1, 'OLQIHXIRCKGNZ', candidates[0])
>>> letterMapping1
{'A': [], 'C': ['T'], 'B': [], 'E': [], 'D': [], 'G': ['B'], 'F': [], 'I': ['O'], 'H': ['M'], 'K': ['A'], 'J': [], 'M': [], 'L': ['N'], 'O': ['U'], 'N': ['L'], 'Q': ['C'], 'P': [], 'S': [], 'R': ['R'], 'U': [], 'T': [], 'W': [], 'V': [], 'Y': [], 'X': ['F'], 'Z': ['E']}

Как показывает анализ словаря letterMapping1, буквы шифрослова 'OLQIHXIRCKGNZ' транслируются в буквы слова 'UNCOMFORTABLE' следующим образом: 'O' — ['U'], 'L' — ['N'], 'Q' — ['C'] и т.д.

Но поскольку шифрослово 'OLQIHXIRCKGNZ' может быть также дешифровано в слово 'UNCOMFORTABLY', необходимо и его добавить в словарь. Введите в интерактивной оболочке следующие инструкции.

>>> simpleSubHacker.addLettersToMapping(letterMapping1, 'OLQIHXIRCKGNZ', candidates[1])
>>> letterMapping1
{'A': [], 'C': ['T'], 'B': [], 'E': [], 'D': [], 'G': ['B'], 'F': [], 'I': ['O'], 'H': ['M'], 'K': ['A'], 'J': [], 'M': [], 'L': ['N'], 'O': ['U'], 'N': ['L'], 'Q': ['C'], 'P': [], 'S': [], 'R': ['R'], 'U': [], 'T': [], 'W': [], 'V': [], 'Y': [], 'X': ['F'], 'Z': ['E', 'Y']}

Обратите внимание на то, что содержимое словаря letterMapping1 почти не изменилось, за исключением того, что теперь шифробукве 'Z' соответствует не только буква 'E', но и 'Y'. Это объясняется тем, что функция addLettersToMapping() добавляет букву в список только в том случае, если до этого она в нем отсутствовала.

Итак, мы получили словарь шифробукв для первого из трех шифрослов. Теперь необходимо построить словарь для второго шифрослова, 'PLQRZKBZB', повторив весь процесс.

>>> letterMapping2 = simpleSubHacker.getBlankCipherletterMapping()
>>> wordPat = makeWordPatterns.getWordPattern('PLQRZKBZB')
>>> candidates = wordPatterns.allPatterns[wordPat]
>>> candidates
['CONVERSES', 'INCREASES', 'PORTENDED', 'UNIVERSES']
>>> for candidate in candidates:
...     simpleSubHacker.addLettersToMapping(letterMapping2, 'PLQRZKBZB', candidate)
...
>>> letterMapping2
{'A': [], 'C': [], 'B': ['S', 'D'], 'E': [], 'D': [], 'G': [], 'F': [], 'I': [], 'H': [], 'K': ['R', 'A', 'N'], 'J': [], 'M': [], 'L': ['O',