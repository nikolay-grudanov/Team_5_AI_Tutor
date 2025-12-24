---
source_image: page_217.png
page_number: 217
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.55
tokens: 6413
characters: 997
timestamp: 2025-12-24T02:14:20.274853
finish_reason: stop
---

https://github.com/makeyourownneuralnetwork/makeyourownneuralnetwork/blob/master/part3_load_own_images.ipynb

Нам нужно создать версию программы, использовавшейся ранее для создания базовой нейронной сети и ее обучения с помощью набора данных MNIST, но теперь мы будем тестировать программу с использованием набора данных, созданного на основе наших изображений.

Новая программа доступна на сайте GitHub по следующему адресу:

https://github.com/makeyourownneuralnetwork/makeyourownneuralnetwork/blob/master/part3_neural_network_mnist_and_own_data.ipynb

Работает ли она? Конечно, работает! Следующая иллюстрация демонстрирует результаты опроса сети с использованием наших изображений.

![Изображения с цифрами и их распознавание](https://github.com/makeyourownneuralnetwork/makeyourownneuralnetwork/blob/master/part3_load_own_images.ipynb)

Как видите, нейронной сети удалось распознать все изображения, включая намеренно поврежденную цифру "3". Не удалось распознать лишь зашумленную цифру "6".