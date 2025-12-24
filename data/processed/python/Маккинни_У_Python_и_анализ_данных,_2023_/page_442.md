---
source_image: page_442.png
page_number: 442
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.20
tokens: 7394
characters: 1271
timestamp: 2025-12-24T02:52:13.795927
finish_reason: stop
---

13.3. Имена, которые давали детям в США за период с 1880 по 2010 год

1884   39   16

In [144]: diversity.plot(title="Number of popular names in top 50%")

![График зависимости разнообразия от года](https://i.imgur.com/3Q5z5QG.png)

Рис. 13.7. График зависимости разнообразия от года

Как видим, девочкам всегда давали более разнообразные имена, чем мальчикам, и со временем эта тенденция проявляется все ярче. Анализ того, что именно является причиной разнообразия, например рост числа вариантов написания одного и того же имени, оставляю читателю.

Революция «последней буквы»
В 2007 году исследовательница детских имен Лаура Уоттенберг (Laura Wattenberg) отметила на своем сайте (http://www.babynamewizard.com), что распределение имен мальчиков по последней букве за последние 100 лет существенно изменилось. Чтобы убедиться в этом, я сначала агрегирую данные полного набора обо всех родившихся по году, полу и последней букве:

def get_last_letter(x):
    return x[-1]

last_letters = names["name"].map(get_last_letter)
last_letters.name = "last_letter"

table = names.pivot_table("births", index=last_letters,
                          columns=["sex", "year"], aggfunc=sum)

Затем выберу из всего периода три репрезентативных года и напечатаю первые несколько строк: