---
source_image: page_209.png
page_number: 209
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.44
tokens: 7626
characters: 1687
timestamp: 2025-12-24T00:56:45.271449
finish_reason: stop
---

In[28]: print(df2); print(df2.groupby(str.lower).mean())

df2
key   data1   data2
A      0       5
B      1       0
C      2       3
A      3       3
B      4       7
C      5       9

df2.groupby(str.lower).mean()
    data1   data2
a     1.5     4.0
b     2.5     3.5
c     3.5     6.0

Список допустимых ключей. Можно комбинировать любые из предыдущих вариантов ключей для группировки по мультииндексу:

In[29]: df2.groupby([str.lower, mapping]).mean()

Out[29]:
    data1   data2
a vowel   1.5     4.0
b consonant   2.5     3.5
c consonant   3.5     6.0

Пример группировки

В качестве примера соберем все это вместе в нескольких строках кода на языке Python и подсчитаем количество открытых планет по методу открытия и десятилетию:

In[30]: decade = 10 * (planets['year'] // 10)
decade = decade.astype(str) + 's'
decade.name = 'decade'
planets.groupby(['method', decade])\
    ['number'].sum().unstack().fillna(0)

Out[30]: decade
         1980s  1990s  2000s  2010s
method
Astrometry        0.0    0.0    0.0    2.0
Eclipse Timing Variations  0.0    0.0    5.0   10.0
Imaging           0.0    0.0   29.0   21.0
Microlensing      0.0    0.0   12.0   15.0
Orbital Brightness Modulation  0.0    0.0    0.0    5.0
Pulsar Timing     0.0    9.0    1.0    1.0
Pulsation Timing Variations  0.0    0.0    1.0    0.0
Radial Velocity   1.0   52.0  475.0  424.0
Transit           0.0    0.0   64.0  712.0
Transit Timing Variations  0.0    0.0    0.0    9.0

Это демонстрирует возможности комбинирования нескольких из вышеописанных операций применительно к реальным наборам данных. Мы мгновенно получили представление о том, когда и как открывались экзопланеты в последние несколько десятилетий!