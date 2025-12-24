---
source_image: page_298.png
page_number: 298
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.33
tokens: 7530
characters: 1819
timestamp: 2025-12-24T08:53:25.519074
finish_reason: stop
---

Hacking...
Mapping:
{'A': ['E'], 'B': ['Y', 'P', 'B'], 'C': ['R'], 'D': [], 'E': ['W'], 'F': ['B', 'P'], 'G': ['B', 'Q', 'X', 'P', 'Y'], 'H': ['P', 'Y', 'K', 'X', 'B'], 'I': ['H'], 'J': ['T'], 'K': [], 'L': ['A'], 'M': ['L'], 'N': ['M'], 'O': ['D'], 'P': ['O'], 'Q': ['V'], 'R': ['S'], 'S': ['I'], 'T': ['U'], 'U': ['G'], 'V': [], 'W': ['C'], 'X': ['N'], 'Y': ['F'], 'Z': ['Z']}

Original ciphertext:
Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr srxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr srxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm

Copying hacked message to clipboard:
If a man is offered a fact which goes against his instincts, he will scrutinize it closely, and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even on the slightest evidence. The origin of maths is explained in this way. - Bertrand Russell

Исследуем код программы более подробно.

Импорт модулей и настройка констант

Рассмотрим начальные строки программы. В строке 4 импортируются семь модулей — больше, чем в любой из программ, которые мы обсуждали до этого. В строке 10 в глобальной переменной LETTERS сохраняется символьный набор, состоящий из букв алфавита в верхнем регистре.

1. # Программа взлома простого подстановочного шифра
2. # https://www.nostarch.com/crackingcodes/ (BSD Licensed)
3.
4. import os, re, copy, pyperclip, simpleSubCipher, wordPatterns, makeWordPatterns
--опущено--
10. LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'