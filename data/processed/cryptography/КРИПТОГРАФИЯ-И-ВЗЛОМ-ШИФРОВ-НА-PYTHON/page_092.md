---
source_image: page_092.png
page_number: 92
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.26
tokens: 7416
characters: 1748
timestamp: 2025-12-24T08:48:11.573162
finish_reason: stop
---

31.
32.    # Обработать "завертывание", если необходимо
33.    if translatedIndex >= len(SYMBOLS):
34.        translatedIndex = translatedIndex - len(SYMBOLS)
35.    elif translatedIndex < 0:
36.        translatedIndex = translatedIndex + len(SYMBOLS)
37.
38.    translated = translated + SYMBOLS[translatedIndex]
39.    else:
40.        # Присоединить символ без шифрования/дешифрования
41.        translated = translated + symbol
42.
43. # Вывод преобразованной строки
44. print(translated)
45. pyperclip.copy(translated)

Пример выполнения программы Caesar Cipher

Выполнив программу caesarCipher.py, вы должны получить следующий результат:

guv6Jv6Jz!J6rp5r7Jzr66ntrM

Это строка 'This is my secret message.', зашифрованная шифром Цезаря с ключом 13. Программа шифрования, которую вы только что выполнили, автоматически копирует зашифрованную строку в буфер обмена, чтобы ее можно было вставить в электронное письмо или текстовый файл. Таким образом, вы сможете легко переслать зашифрованный текст другому человеку.

При выполнении программы возможно появление следующего сообщения об ошибке.

Traceback (most recent call last):
  File "C:\caesarCipher.py", line 4, in <module>
    import pyperclip
ImportError: No module named pyperclip

Если вы столкнетесь с таким сообщением, то это, вероятно, будет означать, что модуль pyperclip.py не был помещен в нужную папку. Если же файл pyperclip.py действительно находится в одной папке с файлом caesarCipher.py, но модуль почему-то не работает, закомментируйте код в строках 4 и 45 (содержащих ссылки на модуль pyperclip) программы caesarCipher.py, поместив перед ними символ #. Это заставит Python игнорировать код, который зависит от модуля pyperclip.py, и позволит программе успешно выполниться.