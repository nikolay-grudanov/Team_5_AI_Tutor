---
source_image: page_325.png
page_number: 325
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.54
tokens: 7421
characters: 1717
timestamp: 2025-12-24T08:54:06.280958
finish_reason: stop
---

8. def main():
9.     # Этот текст можно скопировать из файла примера (см. введение)
10.    myMessage = """Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist.""""
11.    myKey = 'ASIMOV'
12.    myMode = 'encrypt'  # задать 'encrypt' или 'decrypt'
13.
14.    if myMode == 'encrypt':
15.        translated = encryptMessage(myKey, myMessage)
16.    elif myMode == 'decrypt':
17.        translated = decryptMessage(myKey, myMessage)
18.
19.    print('%sed message:' % (myMode.title()))
20.    print(translated)
21.    pyperclip.copy(translated)
22.    print()
23.    print('The message has been copied to the clipboard.')
24.
25.
26. def encryptMessage(key, message):
27.    return translateMessage(key, message, 'encrypt')
28.
29.
30. def decryptMessage(key, message):
31.    return translateMessage(key, message, 'decrypt')
32.
33.
34. def translateMessage(key, message, mode):
35.    translated = []  # хранит зашифрованное/дешифрованное сообщение
36.
37.    keyIndex = 0
38.    key = key.upper()
39.
40.    for symbol in message:  # цикл по символам строки message
41.        num = LETTERS.find(symbol.upper())
42.        if num != -1:  # symbol.upper() найден в строке LETTERS
43.            if mode == 'encrypt':
44.                num += LETTERS.find(key[keyIndex])  # добавить в случае шифрования
45.            elif mode == 'decrypt':
46.                num -= LETTERS.find(key[keyIndex])  # вычесть в случае дешифрования
47.
48.        num %= len(LETTERS)  # обработка "завертывания"
49.
50.        # Добавить зашифрованный/дешифрованный символ в конец
51.        if symbol.isupper():
52.            translated.append(LETTERS[num])
53.        elif symbol.islower():