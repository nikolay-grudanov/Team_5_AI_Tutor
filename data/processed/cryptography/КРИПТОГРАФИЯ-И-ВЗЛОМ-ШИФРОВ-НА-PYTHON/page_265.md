---
source_image: page_265.png
page_number: 265
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.70
tokens: 7415
characters: 1607
timestamp: 2025-12-24T08:52:32.286911
finish_reason: stop
---

Enter D if done, anything else to continue hacking:
> d
Copying hacked message to clipboard:
"A computer would deserve to be called intelligent if it could deceive a human into believing that it was human." -Alan Turing

Проанализируем работу программы более подробно.

Импорт модулей, настройка констант и функция main()

Программа для взлома аффинного шифра состоит всего лишь из 60 строк, поскольку значительная часть кода уже написана нами. В строке 4 импортируются модули, созданные в предыдущих главах.

1. # Программа для взлома аффинного шифра
2. # https://www.nostarch.com/crackingcodes/ (BSD Licensed)
3.
4. import pyperclip, affineCipher, detectEnglish, cryptomath
5.
6. SILENT_MODE = False

Запустив программу, вы увидите, что в процессе перебора всех возможных вариантов дешифрования она выводит очень много информации. Это сильно замедляет ее работу. Если хотите ускорить процесс, отключите вывод диагностических сообщений, установив для константы SILENT_MODE в строке 6 значение True.

Далее создается функция main().

8. def main():
9.     # Этот текст можно скопировать из
10.    # файла примера (см. введение)
11.    myMessage =
        """5QG9o13La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RN"Q-5!1RQP36ARu"""
12.
13.    hackedMessage = hackAffine(myMessage)

Шифротекст, подлежащий взлому, хранится в строке myMessage, которая передается функции hackAffine() (ее мы рассмотрим в следующем разделе). Эта функция возвращает либо строку исходного сообщения, если шифротекст удалось взломать, или значение None, если взлом не удался.