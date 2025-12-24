---
source_image: page_260.png
page_number: 260
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.25
tokens: 7525
characters: 1113
timestamp: 2025-12-24T02:47:06.815543
finish_reason: stop
---

In [33]: frame
Out[33]:
    a   b   c   d
0   0   7 one  0
1   1   6 one  1
2   2   5 one  2
3   3   4 two  0
4   4   3 two  1
5   5   2 two  2
6   6   1 two  3

Метод set_index объекта DataFrame создает новый DataFrame, используя в качестве индекса один или несколько столбцов:

In [34]: frame2 = frame.set_index(["c", "d"])

In [35]: frame2
Out[35]:
    a   b
c   d
one 0   7
    1   6
    2   5
two 0   3   4
    1   4   3
    2   5   2
    3   6   1

По умолчанию столбцы удаляются из DataFrame, хотя их можно и оставить, передав методу set_index аргумент drop=False:

In [36]: frame.set_index(["c", "d"], drop=False)
Out[36]:
    a   b   c   d
c   d
one 0   7 one  0
    1   6 one  1
    2   5 one  2
two 0   3   4 two  0
    1   4   3 two  1
    2   5   2 two  2
    3   6   1 two  3

Есть также метод reset_index, который делает прямо противоположное set_index; уровни иерархического индекса перемещаются в столбцы:

In [37]: frame2.reset_index()
Out[37]:
    c   d   a   b
0   one  0   0   7
1   one  1   1   6
2   one  2   2   5
3   two  0   3   4
4   two  1   4   3
5   two  2   5   2
6   two  3   6   1