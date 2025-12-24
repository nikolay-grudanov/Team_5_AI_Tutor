---
source_image: page_266.png
page_number: 266
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.52
tokens: 7222
characters: 905
timestamp: 2025-12-24T00:58:04.548228
finish_reason: stop
---

266 Глава 4 • Визуализация с помощью библиотеки Matplotlib

![Простейший пример построения графиков](../images/ch04_01.png)
Рис. 4.1. Простейший пример построения графиков

Сохранение рисунков в файл

Умение сохранять рисунки в файлы различных форматов — одна из возможностей библиотеки Matplotlib. Например, сохранить предыдущий рисунок в файл PNG можно с помощью команды savefig():

In[5]: fig.savefig('my_figure.png')

В текущем рабочем каталоге появился файл с названием my_figure.png:

In[6]: !ls -lh my_figure.png

-rw-r--r--  1 jakevdp  staff   16K Aug 1110:59 my_figure.png

Чтобы убедиться, что содержимое этого файла соответствует нашим ожиданиям, воспользуемся объектом Image оболочки IPython для отображения его содержимого (рис. 4.2):

In[7]: from IPython.display import Image
    Image('my_figure.png')

![Простой график в виде PNG](../images/ch04_02.png)
Рис. 4.2. Простой график в виде PNG