---
source_image: page_341.png
page_number: 341
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.59
tokens: 7447
characters: 1059
timestamp: 2025-12-24T02:49:14.990414
finish_reason: stop
---

6H   6
7H   7
8H   8
9H   9
10H  10
JH   10
KH   10
QH   10
dtype: int64

Исходя из сказанного выше, сдать пять карт из колоды можно следующим образом:

In [122]: def draw(deck, n=5):
    ....:     return deck.sample(n)
In [123]: draw(deck)
Out[123]:
4D   4
QH   10
8S   8
7D   7
9C   9
dtype: int64

Пусть требуется выбрать по две случайные карты из каждой масти. Поскольку масть обозначается последним символом названия карты, то можно произвести по ней группировку и воспользоваться методом apply:

In [124]: def get_suit(card):
    ....:     # последняя буква обозначает масть
    ....:     return card[-1]

In [125]: deck.groupby(get_suit).apply(draw, n=2)
Out[125]:
C   6C   6
    KC   10
D   7D   7
    3D   3
H   7H   7
    9H   9
S   2S   2
    QS   10
dtype: int64

Можно было бы вместо этого передать параметр group_keys=False, чтобы отбросить внешний индекс мастей, оставив только выбранные карты:

In [126]: deck.groupby(get_suit, group_keys=False).apply(draw, n=2)
Out[126]:
AC   1
3C   3
5D   5
4D   4
10H  10
7H   7
QS   10
7S   7
dtype: int64