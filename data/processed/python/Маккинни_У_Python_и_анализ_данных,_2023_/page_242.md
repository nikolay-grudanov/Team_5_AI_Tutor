---
source_image: page_242.png
page_number: 242
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.03
tokens: 7510
characters: 1667
timestamp: 2025-12-24T02:46:35.752951
finish_reason: stop
---

функция), но для отсутствующих значений они «грохнутся». Чтобы справиться с этой проблемой, в классе Series есть методы для операций со строками, которые пропускают отсутствующие значения. Доступ к ним производится через атрибут str; например, вот как можно было бы с помощью метода str.contains проверить, содержит ли каждый почтовый адрес подстроку 'gmail':

In [188]: data.str.contains("gmail")
Out[188]:
Dave    False
Steve   True
Rob     True
Wes     NaN
dtype: object

Обратите внимание, что результат этой операции имеет тип object. В pandas имеются расширенные типы для специализированной обработки строк, целых чисел и булевых данных; до недавнего времени работа с этими типами вызывала некоторые трудности, если часть данных отсутствовала:

In [189]: data_as_string_ext = data.astype('string')

In [190]: data_as_string_ext
Out[190]:
Dave    dave@google.com
Steve   steve@gmail.com
Rob     rob@gmail.com
Wes     <NA>
dtype: string

In [191]: data_as_string_ext.str.contains("gmail")
Out[191]:
Dave    False
Steve   True
Rob     True
Wes     <NA>
dtype: boolean

Расширенные типы более подробно обсуждаются в разделе 7.3 выше.
Регулярные выражения тоже можно так использовать, равно как и их флаги типа IGNORECASE:

In [192]: pattern = r"([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})"

In [193]: data.str.findall(pattern, flags=re.IGNORECASE)
Out[193]:
Dave    [(dave, google, com)]
Steve   [(steve, gmail, com)]
Rob     [(rob, gmail, com)]
Wes     NaN
dtype: object

Существует два способа векторной выборки элементов: str.get или доступ к атрибуту str по индексу:

In [194]: matches = data.str.findall(pattern, flags=re.IGNORECASE).str[0]

In [195]: matches