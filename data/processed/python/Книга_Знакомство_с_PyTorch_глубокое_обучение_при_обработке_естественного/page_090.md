---
source_image: page_090.png
page_number: 90
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.80
tokens: 7456
characters: 1849
timestamp: 2025-12-24T02:23:25.955589
finish_reason: stop
---

x_in (torch.Tensor): тензор входных данных
    Значение x_in.shape должно быть (batch, input_dim)
apply_softmax (bool): флаг для многомерной логистической функции активации. При использовании функции потерь на основе перекрестной энтропии должен равняться false
Возвращает:
    итоговый тензор. Значение tensor.shape должно быть (batch, output_dim)
"""
intermediate = F.relu(self.fc1(x_in))
output = self.fc2(intermediate)

if apply_softmax:
    output = F.softmax(output, dim=1)
return output

В примере 4.2 мы воплощаем MLP. Благодаря обобщенному характеру реализации MLP входные данные могут быть любого размера. Для демонстрации возьмем входные данные размерностью 3, выходные — размерностью 4, а скрытое представление — размерностью 100. Обратите внимание, как в выводимых оператором print результатах количества блоков в слоях выстраиваются таким образом, чтобы для входных данных размерностью 3 сгенерировать выходные данные размерностью 4.

Пример 4.2. Пример воплощения MLP

Input[0]
batch_size = 2 # число вводимых за один раз выборок
input_dim = 3
hidden_dim = 100
output_dim = 4

# Инициализация модели
mlp = MultilayerPerceptron(input_dim, hidden_dim, output_dim)
print(mlp)

Output[0]
MultilayerPerceptron(
    (fc1): Linear(in_features=3, out_features=100, bias=True)
    (fc2): Linear(in_features=100, out_features=4, bias=True)
    (relu): ReLU()
)

Для быстрой проверки работы модели мы можем передать в нее случайные входные данные, как показано в примере 4.3. Поскольку модель пока не обучена, выходные данные также носят случайный характер. Подобная предварительная проверка работоспособности полезна перед тем, как тратить время на обучение модели. Обратите внимание, как благодаря диалоговому режиму PyTorch все это можно сделать в режиме реального времени при разработке примерно так же, как при использовании NumPy и Pandas.