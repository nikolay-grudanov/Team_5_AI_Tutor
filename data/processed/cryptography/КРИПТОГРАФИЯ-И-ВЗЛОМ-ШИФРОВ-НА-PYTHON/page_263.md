---
source_image: page_263.png
page_number: 263
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.67
tokens: 7503
characters: 1744
timestamp: 2025-12-24T08:52:34.588859
finish_reason: stop
---

Исходный код программы Affine Hacker

Откройте в редакторе файлов новое окно, выбрав пункты меню File→New File. Введите в этом окне приведенный ниже код и сохраните его в файле affineHacker.py. Поскольку ввод строки для переменной myMessage вручную вряд ли доставит вам удовольствие, скопируйте ее из файла, доступного на сайте издательства (см. введение), чтобы сэкономить время. Убедитесь в том, что словарь dictionary.txt, а также файлы pyperclip.py, affineCipher.py, detectEnglish.py и cryptomath.py находятся в той же папке, что и файл affineHacker.py.

affineHacker.py

1. # Программа для взлома аффинного шифра
2. # https://www.nostarch.com/crackingcodes/ (BSD Licensed)
3.
4. import pyperclip, affineCipher, detectEnglish, cryptomath
5.
6. SILENT_MODE = False
7.
8. def main():
9.     # Этот текст можно скопировать из
10.    # файла примера (см. введение)
11.    myMessage =
12.        """5QG9o13La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQ
13.        ADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQII1
14.        iQX3o1RN"Q-5!1RQP36ARu""""
15.    hackedMessage = hackAffine(myMessage)
16.    if hackedMessage != None:
17.        # Вывод дешифрованного текста на экран;
18.        # для удобства копируем его в буфер обмена
19.        print('Copying hacked message to clipboard:')
20.        print(hackedMessage)
21.        pyperclip.copy(hackedMessage)
22.    else:
23.        print('Failed to hack encryption.')
24.
25. def hackAffine(message):
26.    print('Hacking...')
27.
28.    # Работу программы на Python можно в любой момент прервать,
29.    # нажав <Ctrl+C> (Windows) или <Ctrl+D> (macOS и Linux)
30.    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')
31.
32.    # Перебор всех возможных ключей методом грубой силы