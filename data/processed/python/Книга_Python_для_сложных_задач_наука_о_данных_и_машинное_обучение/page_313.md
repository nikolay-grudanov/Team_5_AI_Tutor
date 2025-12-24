---
source_image: page_313.png
page_number: 313
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.83
tokens: 7463
characters: 1632
timestamp: 2025-12-24T00:59:29.832587
finish_reason: stop
---

Функция plt.GridSpec: более сложные конфигурации

При выходе за пределы обычной сетки графиков к субграфикам, занимающим много строк и столбцов, наилучшим инструментом считается plt.GridSpec. Сам по себе объект plt.GridSpec не создает графиков, это просто удобный интерфейс, понятный команде plt.subplot(). Например, вызов GridSpec для сетки из двух строк и трех столбцов с заданными значениями ширины и высоты будет выглядеть следующим образом:

In[8]: grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3)

Затем мы можем задать местоположение и размеры субграфиков с помощью обычного синтаксиса срезов языка Python (рис. 4.65):

In[9]: plt.subplot(grid[0, 0])
    plt.subplot(grid[0, 1:])
    plt.subplot(grid[1, :2])
    plt.subplot(grid[1, 2]);

![Создание субграфиков неодинаковой формы с помощью функции plt.GridSpec](https://i.imgur.com/465.png)

Рис. 4.65. Создание субграфиков неодинаковой формы с помощью функции plt.GridSpec

Подобное гибкое выравнивание сетки находит множество различных применений. Я чаще всего использую его при создании графиков гистограмм с несколькими системами координат (рис. 4.66):

In[10]: # Создаем нормально распределенные данные
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 3000).T

# Задаем системы координат с помощью функции GridSpec
fig = plt.figure(figsize=(6, 6))
grid = plt.GridSpec(4, 4, hspace=0.2, wspace=0.2)
main_ax = fig.add_subplot(grid[:-1, 1:])
y_hist = fig.add_subplot(grid[:-1, 0], xticklabels=[], sharey=main_ax)
x_hist = fig.add_subplot(grid[-1, 1:], yticklabels=[], sharex=main_ax)

# Распределяем точки по основной системе координат