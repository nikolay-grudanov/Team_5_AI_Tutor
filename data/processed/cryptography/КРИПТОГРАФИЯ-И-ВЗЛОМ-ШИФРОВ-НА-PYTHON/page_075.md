---
source_image: page_075.png
page_number: 75
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.68
tokens: 7236
characters: 1065
timestamp: 2025-12-24T08:47:44.648546
finish_reason: stop
---

В этой главе...

• Функция len()
• Цикл while
• Булев тип данных
• Операторы сравнения
• Условия
• Блоки

Исходный код программы Reverse Cipher

Выберите в IDLE пункты меню File⇒New Window для создания нового окна редактора файлов. Введите приведенный ниже код (естественно, без номеров строк), сохраните его в файле reverseCipher.py и выполните, нажав клавишу <F5>.

reverseCipher.py

1. # Программа обратного шифрования
2. # https://www.nostarch.com/crackingcodes/ (BSD Licensed)
3.
4. message = 'Three can keep a secret, if two of them are dead.'
5. translated = ''
6.
7. i = len(message) - 1
8. while i >= 0:
9.     translated = translated + message[i]
10.    i = i - 1
11.
12. print(translated)

Пробный запуск программы Reverse Cipher

Выполнив программу reverseCipher.py, вы должны получить следующий результат:

.daed era meht fo owt fi ,terces a peek nac eerhT

Чтобы дешифровать это сообщение, скопируйте текст .daed era meht fo owt fi ,terces a peek nac eerhT в буфер обмена, выделив сообщение и нажав комбинацию клавиш <Ctrl+C> (Windows/Linux) или <⌘+C>