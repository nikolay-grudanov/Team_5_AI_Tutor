---
source_image: page_129.png
page_number: 129
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.16
tokens: 11873
characters: 2178
timestamp: 2025-12-24T01:40:39.414217
finish_reason: stop
---

Проблемы кодирования и декодирования

b'S\xe3o Paulo'
>>> city.encode('cp437')  # 1
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "/.../lib/python3.4/encodings/cp437.py", line 12, in encode
        return codecs.charmap_encode(input,errors,encoding_map)
UnicodeEncodeError: 'charmap' codec can't encode character '\xe3' in position 1: character maps to <undefined>
>>> city.encode('cp437', errors='ignore')  # 2
b'So Paulo'
>>> city.encode('cp437', errors='replace')  # 3
b'S?o Paulo'
>>> city.encode('cp437', errors='xmlcharrefreplace')  # 4
b'S&#227;o Paulo'

1 Кодировки 'utf_?' справляются с любой строкой str.
2 'iso8859_1' также работает для строки 'São Paulo'.
3 'cp437' не может закодировать букву 'ã' («а» с тильдой). Обработчик ошибок по умолчанию — 'strict' — возбуждает исключение UnicodeEncodeError.
4 Обработчик error='ignore' молча пропускает некодируемые символы, обычно это не слишком удачная идея.
5 Обработчик error='replace' заменяет некодируемые символы знаком '?'; данные теряются, но пользователь хотя бы знает, что какая-то часть информации утрачена.
6 'xmlcharrefreplace' заменяет некодируемые символы XML-компонентом.

Механизм обработки ошибок в модуле codecs расширяемый. Можно зарегистрировать дополнительные значения аргумента errors, передав строку и функцию обработки ошибок функции codecs.register_error. См. документацию по codecs.register_error (http://bit.ly/1Vm83DZ).

Обработка UnicodeDecodeError

Не каждый байт содержит допустимый символ ASCII, и не каждая последовательность байтов является допустимой в кодировке UTF-8 или UTF-16. Если при декодировании двоичной последовательности встретится неожиданный байт, то возникнет исключение UnicodeDecodeError.

С другой стороны, многие унаследованные 8-разрядные кодировки, например 'cp1252', 'iso8859_1' и 'koi8_r' могут декодировать произвольный поток байтов, в т. ч. случайный шум, без ошибок. Поэтому, если ваша программа ошибется в предположении о том, какая 8-разрядная кодировка используется, то будет молча декодировать мусор.

В примере 4.7 показано, как неправильно выбранный кодек может порождать крокозябры или исключение UnicodeDecodeError.