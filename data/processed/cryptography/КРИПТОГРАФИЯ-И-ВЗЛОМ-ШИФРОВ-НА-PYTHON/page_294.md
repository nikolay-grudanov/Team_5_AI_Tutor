---
source_image: page_294.png
page_number: 294
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.74
tokens: 7438
characters: 1571
timestamp: 2025-12-24T08:53:16.700359
finish_reason: stop
---

Исходный код программы Simple Substitution Hacker

Откройте в редакторе файлов новое окно, выбрав пункты меню File→New File. Введите в этом окне приведенный ниже код и сохраните его в файле simpleSubHacker.py. Убедитесь в том, что файлы pyperclip.py, simpleSubCipher.py и wordPatterns.py находятся в той же самой папке. Запустите программу, нажав клавишу <F5>.

simpleSubHacker.py

1. # Программа взлома простого подстановочного шифра
2. # https://www.nostarch.com/crackingcodes/ (BSD Licensed)
3.
4. import os, re, copy, pyperclip, simpleSubCipher, wordPatterns, makeWordPatterns
5.
6.
7.
8.
9.
10. LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
11. nonLettersOrSpacePattern = re.compile('[^A-Z\s]')
12.
13. def main():
14.     message = 'Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrp x ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm'
15.
16.     # Определяем варианты дешифрования шифротекста
17.     print('Hacking...')
18.     letterMapping = hackSimpleSub(message)
19.
20.     # Выводим результаты
21.     print('Mapping:')
22.     print(letterMapping)
23.     print()
24.     print('Original ciphertext:')
25.     print(message)
26.     print()
27.     print('Copying hacked message to clipboard:')
28.     hackedMessage = decryptWithCipherletterMapping(message, letterMapping)