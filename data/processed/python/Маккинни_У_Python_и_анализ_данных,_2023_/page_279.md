---
source_image: page_279.png
page_number: 279
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.79
tokens: 7432
characters: 1089
timestamp: 2025-12-24T02:47:37.795804
finish_reason: stop
---

In [137]: data2.unstack()
Out[137]:
    a   b   c   d   e
one  0   1   2   3  <NA>
two  <NA>  <NA>  4   5   6

In [138]: data2.unstack().stack()
Out[138]:
one   a   0
      b   1
      c   2
      d   3
two   c   4
      d   5
      e   6
dtype: Int64

In [139]: data2.unstack().stack(dropna=False)
Out[139]:
one   a   0
      b   1
      c   2
      d   3
      e  <NA>
two   a  <NA>
      b  <NA>
      c   4
      d   5
      e   6
dtype: Int64

В случае обратного поворота DataFrame поворачиваемый уровень становится самым нижним уровнем результирующего объекта:

In [140]: df = pd.DataFrame({"left": result, "right": result + 5},
.....: columns=pd.Index(["left", "right"], name="side"))

In [141]: df
Out[141]:
   side   left  right
state number
Ohio   one     0     5
       two     1     6
       three   2     7
Colorado   one   3     8
           two   4     9
           three  5    10

In [142]: df.unstack(level="state")
Out[142]:
   side   left  right
state Ohio Colorado Ohio Colorado
number
one     0     3     5     8
two     1     4     6     9
three   2     5     7    10