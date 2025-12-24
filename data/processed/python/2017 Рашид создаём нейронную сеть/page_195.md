---
source_image: page_195.png
page_number: 195
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.69
tokens: 6650
characters: 1373
timestamp: 2025-12-24T02:13:57.632993
finish_reason: stop
---

Мы распакуем эти данные точно так же, как и предыдущие, поскольку они имеют аналогичную структуру.

Прежде чем создавать цикл для перебора всех тестовых записей, посмотрим, что произойдет, если мы вручную выполним одиночный тест. Ниже представлены результаты опроса уже обученной нейронной сети, выполненного с использованием первой записи тестового набора данных.

In [2]: # загрузить в список тестовый набор данных CSV-файла набора MNIST
   test_data_file = open("mnist_dataset/mnist_test_10.csv", 'r')
   test_data_list = test_data_file.readlines()
   test_data_file.close()

In [3]: # получить первую тестовую запись
   all_values = test_data_list[0].split(',')
   # вывести маркер
   print(all_values[0])
   7

In [4]: image_array = numpy.asfarray(all_values[1:]).reshape((28,28))
   matplotlib.pyplot.imshow(image_array, cmap='Greys', interpolation='None')

Out[4]: <matplotlib.image.AxesImage at 0x8c6e080>

![Изображение цифры 7](https://i.imgur.com/7zZzZzZ.png)

In [5]: n.query((numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01)
Out[5]: array([[ 0.03305615],
   [ 0.00522053],
   [ 0.01038686],
   [ 0.07915526],
   [ 0.0167299 ],
   [ 0.02322546],
   [ 0.00498213],
   [ 0.79226727],
   [ 0.01799863],
   [ 0.01735059]])

Как видите, в качестве маркера первой записи тестового набора сеть определила символ "7". Именно этого ответа мы ожидали, опрашивая ее.