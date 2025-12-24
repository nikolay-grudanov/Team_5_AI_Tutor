---
source_image: page_326.png
page_number: 326
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.67
tokens: 7340
characters: 1368
timestamp: 2025-12-24T08:54:02.857473
finish_reason: stop
---

54. translated.append(LETTERS[num].lower())
55.
56. keyIndex += 1 # перейти к следующей букве ключа
57. if keyIndex == len(key):
58.     keyIndex = 0
59. else:
60.     # Присоединить символ без шифрования/дешифрования
61.     translated.append(symbol)
62.
63. return ''.join(translated)
64.
65.
66. # Если файл vigenereCipher.py выполняется как программа
67. # (а не импортируется как модуль), вызвать функцию main()
68. if __name__ == '__main__':
69.     main()

Пример выполнения программы Vigenere Cipher

Выполнив программу, вы должны получить следующий результат.

Encrypted message:
Adiz Avtzqeci Tmzubb wsa m Pmilqev halpqavtakuoi, lgouqdaf, kdmktsvmztstl, izr xoexghzr kkusitaaf.

The message has been copied to the clipboard.

Программа отображает зашифрованное сообщение и копирует шифротекст в буфер обмена.

Импорт модулей, настройка констант и функция main()

Программа начинается со стандартных комментариев, описывающих ее назначение. С помощью инструкции import подключается модуль pyperclip, а в переменной LETTERS хранится строка, содержащая все буквы алфавита в верхнем регистре. Функция main() имеет примерно ту же структуру, что и в остальных программах. Она начинается с определения переменных для хранения сообщения, ключа и режима работы.

1. # Шифр Виженера
2. # https://www.nostarch.com/crackingcodes/ (BSD Licensed)
3.
4. import pyperclip
5.