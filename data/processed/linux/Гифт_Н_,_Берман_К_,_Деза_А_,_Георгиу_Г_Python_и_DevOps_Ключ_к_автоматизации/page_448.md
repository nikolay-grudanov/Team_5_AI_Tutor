---
source_image: page_448.png
page_number: 448
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.93
tokens: 7451
characters: 1528
timestamp: 2025-12-24T03:12:38.618605
finish_reason: stop
---

linearRegression(
    (linear): Linear(in_features=1, out_features=1, bias=True)
)

Создаем объекты для стохастического градиентного спуска и функции потерь:

In[0]:

criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learningRate)

А теперь обучаем модель:

In[0]:

for epoch in range(epochs):
    inputs = Variable(torch.from_numpy(x_train).cuda())
    labels = Variable(torch.from_numpy(y_train).cuda())
    optimizer.zero_grad()
    outputs = model(inputs)
    loss = criterion(outputs, labels)
    print(loss)
    # получаем градиенты относительно параметров
    loss.backward()
    # обновление параметров
    optimizer.step()
    print('epoch {}, loss {}'.format(epoch, loss.item()))

Вывод от 1000 итераций сокращен ради экономии места.

Out[0]:

tensor(29221.6543, device='cuda:0', grad_fn=<MseLossBackward>)
epoch 0, loss 29221.654296875
tensor(266.7252, device='cuda:0', grad_fn=<MseLossBackward>)
epoch 1, loss 266.72515869140625
tensor(106.6842, device='cuda:0', grad_fn=<MseLossBackward>)
epoch 2, loss 106.6842269897461
....сокращено....
epoch 998, loss 105.7930908203125
tensor(105.7931, device='cuda:0', grad_fn=<MseLossBackward>)
epoch 999, loss 105.7930908203125

График соотношения предсказанного и истинного роста. А теперь построим график соотношения предсказанного и истинного роста (рис. 14.5), как в предыдущей простой модели.

In[0]:

with torch.no_grad():
    predicted = model(Variable(torch.from_numpy(x_test).cuda())).cpu().\
        data.numpy()
    print(predicted)