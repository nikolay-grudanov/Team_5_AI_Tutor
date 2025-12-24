---
source_image: page_085.png
page_number: 85
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.66
tokens: 7526
characters: 2045
timestamp: 2025-12-24T08:48:11.588279
finish_reason: stop
---

сообщения. Таким образом, по мере перемещения i как индекса от конца строки сообщения к ее началу строка message[i] добавляется в конец строки translated. Именно так и получается, что символы строки сообщения сохраняются в переменной translated в обратном порядке. Когда i в конечном счете станет равно -1 (это произойдет, когда в сообщении будет достигнут индекс 0), условие цикла станет равно False, после чего выполнение перейдет к строке 12.

12. print(translated)

В строке 12 (последняя в программе) мы выводим содержимое переменной translated (т.е. строку '.daed era meht fo owt fi ,terces a peek nac eerhT') на экран. Благодаря этому пользователь сможет увидеть, что собой представляет обращенная строка.

Если вам все еще не удается понять, каким образом код, выполняющийся в цикле while, обращает строку, добавьте в блок цикла следующую новую строку (выделена полужирным шрифтом).

8. while i >= 0:
9.    translated = translated + message[i]
10.   print('i is', i, ', message[i] is', message[i],
         ', translated is', translated)
11.   i = i - 1
12.
13.  print(translated)

В строке 10 на экран выводятся значения i, message[i] и translated при каждом прохождении цикла (т.е. на каждой его итерации). На этот раз мы используем вместо конкатенации строк нечто новое. Запятые сообщают функции print() о том, что мы выводим шесть различных элементов, поэтому функция добавляет пробелы между ними. Теперь, запустив программу, вы сможете наблюдать за процессом "наращивания" строки, хранящейся в переменной translated. Вывод будет выглядеть примерно так.

i is 48 , message[i] is . , translated is .
i is 47 , message[i] is d , translated is .d
i is 46 , message[i] is a , translated is .da
i is 45 , message[i] is e , translated is .dae
i is 44 , message[i] is d , translated is .daed
i is 43 , message[i] is , translated is .daed
i is 42 , message[i] is e , translated is .daed e
i is 41 , message[i] is r , translated is .daed er
i is 40 , message[i] is a , translated is .daed era
i is 39 , message[i] is , translated is .daed era