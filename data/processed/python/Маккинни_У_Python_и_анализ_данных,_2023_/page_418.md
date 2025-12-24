---
source_image: page_418.png
page_number: 418
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.94
tokens: 7473
characters: 1636
timestamp: 2025-12-24T02:51:40.680787
finish_reason: stop
---

Мы видим, что уже среди первых 10 часовых поясов встречаются неизвестные (пустые). Их можно было бы тоже отфильтровать, но я пока оставлю. Я покажу два способа подсчитать количество часовых поясов: трудный (в котором используется только стандартная библиотека Python) и легкий (с помощью pandas). Для подсчета можно завести словарь для хранения счетчиков и обойти весь список часовых поясов:

def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

Воспользовавшись более продвинутыми средствами из стандартной библиотеки Python, можно записать то же самое короче:

from collections import defaultdict
def get_counts2(sequence):
    counts = defaultdict(int) # values will initialize to 0
    for x in sequence:
        counts[x] += 1
    return counts

Чтобы можно было повторно воспользоваться этим кодом, я поместил его в функцию. Чтобы применить его к часовым поясам, достаточно передать этой функции список time_zones:

In [20]: counts = get_counts(time_zones)

In [21]: counts["America/New_York"]
Out[21]: 1251

In [22]: len(time_zones)
Out[22]: 3440

Чтобы получить только первые 10 часовых поясов со счетчиками, можно построить список кортежей (count, timezone) и отсортировать его:

def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

В результате получим:

In [24]: top_counts(counts)
Out[24]:
[(33, 'America/Sao_Paulo'),
 (35, 'Europe/Madrid'),
 (36, 'Pacific/Honolulu'),
 (37, 'Asia/Tokyo'),