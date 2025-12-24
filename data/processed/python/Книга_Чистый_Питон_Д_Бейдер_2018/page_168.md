---
source_image: page_168.png
page_number: 168
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.29
tokens: 7304
characters: 1185
timestamp: 2025-12-24T02:31:04.863229
finish_reason: stop
---

bytearray — изменяемые массивы одиночных байтов

Тип bytearray представляет собой изменяемую последовательность целых чисел в диапазоне \(0 \leq x \leq 255\). Они тесно связаны с объектами bytes, при этом главное их отличие в том, что объекты bytearray можно свободно изменять — вы можете переписывать элементы, удалять существующие элементы или добавлять новые. Объект bytearray будет соответствующим образом расти и сжиматься.

Объекты bytearray могут быть преобразованы обратно в неизменяемые объекты bytes, но это влечет за собой копирование абсолютно всех хранящихся в них данных — весьма медленная операция, занимающая \(O(n)\) времени.

>>> arr = bytearray((0, 1, 2, 3))
>>> arr[1]
1

# Метод repr для bytearray:
>>> arr bytearray(b'x00x01x02x03')

# Байтовые массивы bytearray изменяемы:
>>> arr[1] = 23
>>> arr
bytearray(b'x00x17x02x03')

>>> arr[1]
23

# Байтовые массивы bytearray могут расти и сжиматься в размере:
>>> del arr[1]
>>> arr
bytearray(b'x00x02x03')

>>> arr.append(42)
>>> arr
bytearray(b'x00x02x03*')

# Байтовые массивы bytearray могут содержать только "байты"

1 См. документацию Python «bytearray»: https://docs.python.org/3/library/stdtypes.html#bytearray