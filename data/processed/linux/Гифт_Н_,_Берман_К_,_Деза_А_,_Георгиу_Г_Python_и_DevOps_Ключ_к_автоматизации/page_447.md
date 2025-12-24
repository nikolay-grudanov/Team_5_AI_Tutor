---
source_image: page_447.png
page_number: 447
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.54
tokens: 7312
characters: 1350
timestamp: 2025-12-24T03:12:32.148260
finish_reason: stop
---

Регрессия с помощью PyTorch

Сначала преобразуем данные в тип float32:

In[0]:

# Обучающие данные
x_train = np.array(X_train, dtype=np.float32)
x_train = x_train.reshape(-1, 1)
y_train = np.array(y_train, dtype=np.float32)
y_train = y_train.reshape(-1, 1)

# Контрольные данные
x_test = np.array(X_test, dtype=np.float32)
x_test = x_test.reshape(-1, 1)
y_test = np.array(y_test, dtype=np.float32)
y_test = y_test.reshape(-1, 1)

Учите, что, если вы не используете блокноты Colab, возможно, вам придется установить PyTorch. Кроме того, если вы используете блокноты Colab, то можете бесплатно получить доступ к GPU NVIDIA и выполнить этот код на нем. В противном случае вам нужно будет выполнить этот код на платформе с GPU.

In[0]:

import torch
from torch.autograd import Variable

class linearRegression(torch.nn.Module):
    def __init__(self, inputSize, outputSize):
        super(linearRegression, self).__init__()
        self.linear = torch.nn.Linear(inputSize, outputSize)

    def forward(self, x):
        out = self.linear(x)
        return out

Теперь создайте модель с подключенным CUDA (если вы выполняете в блокноте Colab или на машине с GPU):

In[0]:

inputDim = 1      # для переменной 'x'
outputDim = 1     # для переменной 'y'
learningRate = 0.0001
epochs = 1000

model = linearRegression(inputDim, outputDim)
model.cuda()

Out[0]: