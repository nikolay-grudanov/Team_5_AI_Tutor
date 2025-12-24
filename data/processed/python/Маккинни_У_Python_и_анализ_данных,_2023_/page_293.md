---
source_image: page_293.png
page_number: 293
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.54
tokens: 7334
characters: 1185
timestamp: 2025-12-24T02:47:50.655968
finish_reason: stop
---

По умолчанию на линейных графиках соседние точки соединяются отрезками прямой, т. е. производится линейная интерполяция. Параметр drawstyle позволяет изменить этот режим:

In [34]: fig = plt.figure()

In [35]: ax = fig.add_subplot()

In [36]: data = np.random.standard_normal(30).cumsum()

In [37]: ax.plot(data, color="black", linestyle="dashed", label="Default");

In [38]: ax.plot(data, color="black", linestyle="dashed",
    ....:         drawstyle="steps-post", label="steps-post");

In [39]: ax.legend()

![Линейный график с различными значениями параметра drawstyle](https://i.imgur.com/3Q5z5QG.png)

Рис. 9.7. Линейный график с различными значениями параметра drawstyle

В данном случае мы передали функции plot аргумент label, поэтому можем с помощью метода plt.legend нанести на график надпись, описывающую каждую линию. Подробнее о надписях мы поговорим ниже.

Для создания надписи необходимо вызвать метод ax.legend вне зависимости от того, передавали вы аргумент label при построении графика или нет.

Риски, метки и надписи
Для доступа к большинству средств оформления графиков у объектов осей имеются специальные методы, в т. ч. xlim, xticks и xticklabels. Они управляют