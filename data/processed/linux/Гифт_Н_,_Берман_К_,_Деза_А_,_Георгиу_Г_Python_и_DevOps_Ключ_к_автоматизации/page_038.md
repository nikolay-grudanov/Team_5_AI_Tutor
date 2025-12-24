---
source_image: page_038.png
page_number: 38
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.89
tokens: 7164
characters: 776
timestamp: 2025-12-24T03:01:42.474497
finish_reason: stop
---

8
10
12
14
16
18
>>>

В этом примере блок кода имеет следующий вид:

...    x = i*2
...    print(x)

Этот код выполняется десять раз, причем переменной i каждый раз присваивается следующий элемент последовательности целых чисел из диапазона 0–9. Циклы for подходят для обхода любых типов последовательностей Python, как вы увидите далее в этой главе.

continue

Оператор continue позволяет пропустить один шаг в цикле и перейти сразу к очередному элементу последовательности:

>>> for i in range(6):
...    if i == 3:
...        continue
...    print(i)
...
...
0
1
2
4
5
>>>

Циклы while

Цикл while повторяет выполнение блока кода до тех пор, пока условное выражение равно True:

>>> count = 0
>>> while count < 3:
...    print(f"The count is {count}")
...    count += 1
...