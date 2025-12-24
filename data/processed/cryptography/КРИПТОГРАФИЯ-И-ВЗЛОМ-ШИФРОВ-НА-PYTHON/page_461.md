---
source_image: page_461.png
page_number: 461
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.57
tokens: 7344
characters: 1673
timestamp: 2025-12-24T08:57:44.278698
finish_reason: stop
---

encrypted_file.txt, находится в том же каталоге, что и файл publicKeyCipher.py.
На этот раз программа дешифрует зашифрованное сообщение, хранящееся в файле encrypted_file.txt, и результат будет примерно таким.

Reading from encrypted_file.txt and decrypting...
Decrypted text:
Journalists belong in the gutter because that is where the ruling classes throw their guilty secrets. Gerald Priestland. The Founding Fathers gave the free press the protection it must have to bare the secrets of government and inform the people. Hugo Black.

Учтите, что программа publicKeyCipher.py способна шифровать и дешифровать только простые текстовые файлы.
Теперь перейдем к более тщательному рассмотрению исходного кода программы.

Начало программы

В шифрах с открытым ключом используются числа, поэтому мы преобразуем строку сообщения в целое число. Оно вычисляется на основании индексов символов в наборе, который хранится в константе SYMBOLS (строка 10).

1. # Шифрование с открытым ключом
2. # https://www.nostarch.com/crackingcodes/ (BSD Licensed)
3.
4. import sys, math
5.
6. # Открытый и закрытый ключи для этой программы создаются
7. # программой makePublicPrivateKeys.py. Программа должна
8. # выполняться в той же папке, в которой находятся файлы ключей.
9.
10. SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

Как программа определяет, что ей делать: шифровать или дешифровать

Чтобы программа publicKeyCipher.py могла определить, какую именно операцию — шифрование или дешифрование — следует выполнить и какой файл ключа следует использовать, мы сохраняем определенные значения в соответствующих переменных, которые задаются в функции main().