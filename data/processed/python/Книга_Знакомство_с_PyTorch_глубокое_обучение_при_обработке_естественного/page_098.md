---
source_image: page_098.png
page_number: 98
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.56
tokens: 7502
characters: 2206
timestamp: 2025-12-24T02:23:41.216459
finish_reason: stop
---

перекрестной энтропии, с которой мы познакомились в разделе «Функции потерь» на с. 64. Напомним, что функция потерь на основе перекрестной энтропии лучше всего подходит для многоклассовой классификации, но вычисление многомерной логистической функции во время обучения — напрасная трата ресурсов. Кроме того, во многих случаях она может приводить к численной неустойчивости.

Пример 4.7. Реализация класса SurnameClassifier с помощью MLP

import torch.nn as nn
import torch.nn.functional as F

class SurnameClassifier(nn.Module):
    """ Многослойный перцептрон с двумя слоями для классификации фамилий """
    def __init__(self, input_dim, hidden_dim, output_dim):
        """
        Аргументы:
            input_dim (int): размер входных векторов
            hidden_dim (int): размер выходных векторов первого линейного слоя
            output_dim (int): размер выходных векторов второго линейного слоя
        """
        super(SurnameClassifier, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x_in, apply_softmax=False):
        """
        Прямой проход классификатора

        Аргументы:
            x_in (torch.Tensor): входной тензор данных
                Значение x_in.shape должно быть (batch, input_dim)
            apply_softmax (bool): флаг для многомерной логистической функции активации. При использовании функции потерь на основе перекрестной энтропии должен равняться false
        Возвращает:
            итоговый тензор. Значение tensor.shape должно быть (batch, output_dim).
        """
        intermediate_vector = F.relu(self.fc1(x_in))
        prediction_vector = self.fc2(intermediate_vector)

        if apply_softmax:
            prediction_vector = F.softmax(prediction_vector, dim=1)

        return prediction_vector

Процедура обучения

Хотя в этом примере мы используем другую модель, набор данных и функцию потерь, процедура обучения не отличается от описанной в предыдущей главе. Поэтому в примере 4.8 мы приведем только args и основные различия процедуры обучения между этим примером и примером из раздела «Пример: классификация тональностей обзоров ресторанов» на с. 76.