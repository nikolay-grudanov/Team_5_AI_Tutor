---
source_image: page_165.png
page_number: 165
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.99
tokens: 7631
characters: 1662
timestamp: 2025-12-24T02:44:27.553694
finish_reason: stop
---

Ohio      1   0   0   0
Colorado  1   5   6   7
Utah      5   5   5   5
New York  1  13  14  15

In [176]: data.loc[data["four"] > 5] = 3

In [177]: data
Out[177]:
    one  two  three  four
Ohio   1    0     0     0
Colorado  3   3     3     3
Utah    5   5     5     5
New York  3   3     3     3

Типичная ошибка начинающих пользователей pandas — сцеплять операции выборки при присваивании, например:

In [177]: data.loc[data.three == 5]["three"] = 6
<ipython-input-11-0ed1cf2155d5>:1: SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

В зависимости от данных может быть напечатано специальное предупреждение SettingWithCopyWarning, в котором говорится, что вы пытаетесь модифицировать временное значение (непустой результат data.loc[data.three == 5]), а не данные data исходного объекта DataFrame, как, вероятно, намеревались. В данном случае data не изменилось:

In [179]: data
Out[179]:
    one  two  three  four
Ohio   1    0     0     0
Colorado  3   3     3     3
Utah    5   5     5     5
New York  3   3     3     3

В таких случаях нужно переписать цепное присваивание, заменив его одной операцией loc:

In [180]: data.loc[data.three == 5, "three"] = 6

In [181]: data
Out[181]:
    one  two  three  four
Ohio   1    0     0     0
Colorado  3   3     3     3
Utah    5   5     6     5
New York  3   3     3     3

Рекомендуется вообще избегать цепного индексирования при выполнении присваиваний. Есть и другие ситуации, связанные с цепным индексированием, когда pandas выдает предупреждение SettingWithCopyWarning. Отсылаю вас к онлайновой документации.