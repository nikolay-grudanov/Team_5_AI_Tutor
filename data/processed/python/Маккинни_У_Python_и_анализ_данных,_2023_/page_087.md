---
source_image: page_087.png
page_number: 87
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.34
tokens: 7316
characters: 1258
timestamp: 2025-12-24T02:42:03.103280
finish_reason: stop
---

Вот как выглядит результат:

In [195]: clean_strings(states)
Out[195]:
['Alabama',
'Georgia',
'Georgia',
'Georgia',
'Florida',
'South Carolina',
'West Virginia']

Другой подход, который иногда бывает полезен, — составить список операций, которые необходимо применить к набору строк:

def remove_punctuation(value):
    return re.sub("[!#?]", "", value)

clean_ops = [str.strip, remove_punctuation, str.title]

def clean_strings(strings, ops):
    result = []
    for value in strings:
        for func in ops:
            value = func(value)
        result.append(value)
    return result

Далее поступаем следующим образом:

In [197]: clean_strings(states, clean_ops)
Out[197]:
['Alabama',
'Georgia',
'Georgia',
'Georgia',
'Florida',
'South Carolina',
'West Virginia']

Подобный функциональный подход позволяет задать способ модификации строк на очень высоком уровне. Степень общности и повторной используемости функции clean_strings определенно возросла!

Функции можно передавать в качестве аргументов другим функциям, например встроенной функции map, которая применяет переданную функцию к последовательности:

In [198]: for x in map(remove_punctuation, states):
    ....:     print(x)
Alabama
Georgia
Georgia
georgia
FlOrIda
south carolina
West virginia