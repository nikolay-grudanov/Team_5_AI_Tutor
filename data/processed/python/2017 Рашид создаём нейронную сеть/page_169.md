---
source_image: page_169.png
page_number: 169
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.55
tokens: 6543
characters: 1479
timestamp: 2025-12-24T02:13:20.677707
finish_reason: stop
---

self.lr = learningrate

# использование сигмоиды в качестве функции активации
self.activation_function = lambda x: scipy.special.expit(x)

pass

# тренировка нейронной сети
def train() :
    pass

# опрос нейронной сети
def query(self, inputs_list):
    # преобразовать список входных значений
    # в двухмерный массив
    inputs = numpy.array(inputs_list, ndmin=2).T

    # рассчитать входящие сигналы для скрытого слоя
    hidden_inputs = numpy.dot(self.wih, inputs)
    # рассчитать исходящие сигналы для скрытого слоя
    hidden_outputs = self.activation_function(hidden_inputs)

    # рассчитать входящие сигналы для выходного слоя
    final_inputs = numpy.dot(self.who, hidden_outputs)
    # рассчитать исходящие сигналы для выходного слоя
    final_outputs = self.activation_function(final_inputs)

    return final_outputs

Но это только определение класса, перед которым в первой ячейке блокнота IPython следует поместить код, импортирующий модули numpy и scipy.special.

import numpy
# библиотека scipy.special с сигмоидой expit()
import scipy.special

Попутно отмечу, что функции query() в качестве входных данных потребуются только входные сигналы input_list. Ни в каких других входных данных она не нуждается.

Мы достигли значительного прогресса и теперь можем вернуться к недостающему фрагменту — функции train(). Вспомните, что тренировка включает две фазы: первая — это расчет выходного сигнала, что и делает функция query(), а вторая — обратное распространение