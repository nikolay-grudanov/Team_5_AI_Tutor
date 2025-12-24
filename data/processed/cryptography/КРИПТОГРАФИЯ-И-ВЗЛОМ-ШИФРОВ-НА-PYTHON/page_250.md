---
source_image: page_250.png
page_number: 250
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.78
tokens: 7395
characters: 1730
timestamp: 2025-12-24T08:52:06.271071
finish_reason: stop
---

Программа импортирует четыре модуля, предоставляющих следующие функции:
■ модуль sys — функция exit();
■ модуль pyperclip — функция copy() для копирования сообщения в буфер обмена;
■ модуль cryptomath (см. главу 13) — функции gcd() и findModInverse();
■ модуль random — функция randint() для генерирования случайных ключей.
Строка, хранящаяся в переменной SYMBOLS, — это символьный набор, содержащий список всех символов, которые могут быть зашифрованы.

5. SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

Если в сообщении встречается какой-либо символ, не входящий в набор SYMBOLS, то он остается незашифрованным. В частности, в приведенном выше примере кавычки и дефис остались незашифрованными, поскольку они не входят в определенный нами символьный набор.
В строке 8 начинается определение функции main(), которое оказывается почти таким же, как и в программах для работы с перестановочным шифром. В строках 9–11 присваиваются значения переменным myMessage, myKey и myMode.

8. def main():
9.     myMessage = """A computer would deserve to be called intelligent if it could deceive a human into believing that it was human."
    -Alan Turing"""
10.    myKey = 2894
11.    myMode = 'encrypt' # задать 'encrypt' или 'decrypt'

Значение, сохраненное в переменной myMode, определяет, шифруется или дешифруется сообщение.

13.    if myMode == 'encrypt':
14.        translated = encryptMessage(myKey, myMessage)
15.    elif myMode == 'decrypt':
16.        translated = decryptMessage(myKey, myMessage)

Если переменная myMode равна 'encrypt', то выполняется строка 14, и значение, возвращаемое функцией encryptMessage(), сохраняется в переменной translated. Если же переменная myMode равна 'decrypt',