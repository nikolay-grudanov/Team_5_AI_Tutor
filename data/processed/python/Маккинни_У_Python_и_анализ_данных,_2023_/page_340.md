---
source_image: page_340.png
page_number: 340
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.03
tokens: 7634
characters: 1712
timestamp: 2025-12-24T02:49:20.054056
finish_reason: stop
---

10.3. Метод apply: общий принцип разделения–применения–объединения

Nevada    0.960416
California 0.359244
Idaho      0.960416
dtype: float64

Или, возможно, требуется подставлять вместо отсутствующих значений фиксированные, но зависящие от группы. Поскольку у групп есть автоматически устанавливаемый атрибут name, мы можем воспользоваться им:

In [117]: fill_values = {"East": 0.5, "West": -1}

In [118]: def fill_func(group):
.....:     return group.fillna(fill_values[group.name])

In [119]: data.groupby(group_key).apply(fill_func)
Out[119]:
Ohio        0.329939
New York   0.981994
Vermont     0.500000
Florida    -1.613716
Oregon      1.561587
Nevada     -1.000000
California  0.359244
Idaho      -1.000000
dtype: float64

Пример: случайная выборка и перестановка
Предположим, что требуется произвести случайную выборку (с возвращением или без) из большого набора данных для моделирования методом Монте-Карло или какой-то другой задачи. Существуют разные способы выборки, одни более эффективны, другие — менее; здесь мы воспользуемся методом sample для объекта Series.

Для демонстрации сконструируем колоду игральных карт:

# Hearts (черви), Spades (пики), Clubs (трефы), Diamonds (бубны)
suits = ["H", "S", "C", "D"]
card_val = (list(range(1, 11)) + [10] * 3) * 4
base_names = ["A"] + list(range(2, 11)) + ["J", "K", "Q"]
cards = []
for suit in suits:
    cards.extend(str(num) + suit for num in base_names)

deck = pd.Series(card_val, index=cards)

Теперь у нас есть объект Series длины 52, индекс которого содержит названия карт, а значения — ценность карт в блэкджеке и других играх (для простоты я присвоил тузу значение 1).

In [121]: deck.head(13)
Out[121]:
AH    1
2H    2
3H    3
4H    4
5H    5