---
source_image: page_249.png
page_number: 249
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.05
tokens: 7411
characters: 1452
timestamp: 2025-12-24T08:52:06.401369
finish_reason: stop
---

70.
71. def getRandomKey():
72.    while True:
73.        keyA = random.randint(2, len(SYMBOLS))
74.        keyB = random.randint(2, len(SYMBOLS))
75.        if cryptomath.gcd(keyA, len(SYMBOLS)) == 1:
76.            return keyA * len(SYMBOLS) + keyB .
77.
78.
79. # Если файл affineCipher.py выполняется как программа
80. # (а не импортируется как модуль), вызвать функцию main()
81. if __name__ == '__main__':
82.    main()

Пример выполнения программы Affine Cipher

Запустите программу, нажав клавишу <F5>. Вы должны получить следующий результат.

Ключ: 2894
Encrypted text:
"5QG9o13La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RN"Q-5!1RQP36ARu
Full encrypted text copied to clipboard.

В программе аффинного шифрования сообщение "A computer would deserve to be called intelligent if it could deceive a human into believing that it was human." -Alan Turing было преобразовано в шифротекст с помощью ключа 2894. Чтобы дешифровать этот шифротекст, скопируйте его в переменную myMessage в строке 9 и присвойте переменной myMode в строке 11 кода значение 'decrypt'.

Импорт модулей, настройка констант и функция main()

В строках 1 и 2 программы содержатся комментарии, описывающие ее назначение. Далее следует инструкция импорта необходимых модулей.

1. # Программа аффинного шифрования
2. # https://www.nostarch.com/crackingcodes/ (BSD Licensed)
3.
4. import sys, pyperclip, cryptomath, random