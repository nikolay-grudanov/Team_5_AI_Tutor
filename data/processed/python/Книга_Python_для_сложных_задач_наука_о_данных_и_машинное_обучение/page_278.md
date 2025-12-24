---
source_image: page_278.png
page_number: 278
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.18
tokens: 7267
characters: 1169
timestamp: 2025-12-24T00:58:34.173556
finish_reason: stop
---

• plt.xlabel() → ax.set_xlabel();
• plt.ylabel() → ax.set_ylabel();
• plt.xlim() → ax.set_xlim();
• plt.ylim() → ax.set_ylim();
• plt.title() → ax.set_title().

В объектно-ориентированном интерфейсе построения графиков вместо того, чтобы вызывать эти функции по отдельности, удобнее воспользоваться методом ax.set(), чтобы задать значения всех этих параметров за один раз (рис. 4.19):

In[16]: ax = plt.axes()
    ax.plot(x, np.sin(x))
    ax.set(xlim=(0, 10), ylim=(-2, 2),
        xlabel='x', ylabel='sin(x)',
        title='A Simple Plot'); # Простая диаграмма

![Простая диаграмма](../images/ch4_19.png)

Рис. 4.19. Пример использования метода ax.set() для задания значения нескольких параметров за один вызов

Простые диаграммы рассеяния

Еще один часто используемый тип графиков — диаграммы рассеяния, родственные линейным графикам. В них точки не соединяются отрезками линий, а представлены по отдельности точками, кругами или другими фигурами на графике. Начнем с настройки блокнота для построения графиков и импорта нужных нам функций:

In[1]: %matplotlib inline
    import matplotlib.pyplot as plt
    plt.style.use('seaborn-whitegrid')
    import numpy as np