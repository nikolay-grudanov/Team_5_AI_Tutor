---
source_image: page_295.png
page_number: 295
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.27
tokens: 7413
characters: 1258
timestamp: 2025-12-24T02:48:01.142834
finish_reason: stop
---

In [42]: ticks = ax.set_xticks([0, 250, 500, 750, 1000])

In [43]: labels = ax.set_xticklabels(["one", "two", "three", "four", "five"],
    ....:                                 rotation=30, fontsize=8)

Аргумент rotation устанавливает угол наклона меток рисок к оси x равным 30 градусов. Наконец, метод set_xlabel именует ось x, а метод set_title задает название подграфика (см. окончательный результат на рис. 9.9):

In [44]: ax.set_xlabel("Stages")

Out[44]: Text(0.5, 6.666666666666652, 'Stages')
In [45]: ax.set_title("My first matplotlib plot")

![Простой график для иллюстрации рисок](../images/fig_9_9.png)

Рис. 9.9. Простой график для иллюстрации рисок

Модификация оси y производится точно так же с заменой x на y. В классе оси имеется метод set, позволяющий задавать сразу несколько свойств графика. Так, предыдущий пример можно было записать в следующем виде:

ax.set(title="My first matplotlib plot", xlabel="Stages")

Добавление пояснительных надписей
Пояснительная надпись – еще один важный элемент оформления графика. Добавить ее можно двумя способами. Проще всего передать аргумент label при добавлении каждого нового графика:

In [46]: fig, ax = plt.subplots()

In [47]: ax.plot(np.random.randn(1000).cumsum(), color="black", label="one");