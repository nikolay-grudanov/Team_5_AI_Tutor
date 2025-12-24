---
source_image: page_063.png
page_number: 63
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.01
tokens: 7410
characters: 1243
timestamp: 2025-12-24T02:41:28.259689
finish_reason: stop
---

for value in collection:
    # что-то сделать с value

Ключевое слово continue позволяет сразу перейти к следующей итерации цикла, не доходя до конца блока. Рассмотрим следующий код, который суммирует целые числа из списка, пропуская значения None:

sequence = [1, 2, None, 4, None, 5]
total = 0
for value in sequence:
    if value is None:
        continue
    total += value

Ключевое слово break осуществляет выход из самого внутреннего цикла, объёмлющие циклы продолжают работать:

In [134]: for i in range(4):
    ....:     for j in range(4):
    ....:         if j > i:
    ....:             break
    ....:         print((i, j))
    ....:

(0, 0)
(1, 0)
(1, 1)
(2, 0)
(2, 1)
(2, 2)
(3, 0)
(3, 1)
(3, 2)
(3, 3)

Как мы вскоре увидим, если элементы коллекции или итераторы являются последовательностями (например, кортежем или списком), то их можно распаковать в переменные, воспользовавшись циклом for:

for a, b, c in iterator:
    # что-то сделать

Циклы while
Цикл while состоит из условия и блока кода, который выполняется до тех пор, пока условие не окажется равным False или не произойдет выход из цикла в результате предложения break:

x = 256
total = 0
while x > 0:
    if total > 500:
        break
    total += x
    x = x // 2