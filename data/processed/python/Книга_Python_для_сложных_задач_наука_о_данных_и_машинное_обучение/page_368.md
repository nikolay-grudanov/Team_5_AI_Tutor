---
source_image: page_368.png
page_number: 368
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.09
tokens: 7565
characters: 1718
timestamp: 2025-12-24T01:01:00.239774
finish_reason: stop
---

![Гистограмма как частный случай графика факторов](https://i.imgur.com/3Q5z5QG.png)

Рис. 4.124. Гистограмма как частный случай графика факторов

Мы можем узнать больше, если посмотрим на метод, с помощью которого была открыта каждая из этих планет, как показано на рис. 4.125:

In[21]: with sns.axes_style('white'):
    g = sns.factorplot("year", data=planets, aspect=4.0, kind='count',
        hue='method', order=range(2001, 2015))
    g.set_ylabels('Number of Planets Discovered')
    # Количество обнаруженных планет

Дополнительную информацию о построении графиков с помощью библиотеки Seaborn можно найти в документации, справочном руководстве и галерее Seaborn.

Пример: время прохождения марафона

В этом разделе мы рассмотрим использование библиотеки Seaborn для визуализации и анализа данных по времени прохождения марафонской дистанции. Эти данные я собрал из различных интернет-источников, агрегировал, убрал все идентифицирующие данные и поместил на GitHub, откуда их можно скачать (если вас интересует использование языка Python для веб-скрапинга, рекомендую книгу Web Scraping with Python¹ (http://shop.oreilly.com/product/0636920034391.do) Райана Митчелла. Начнем со скачивания данных из Интернета и загрузки их в Pandas:

In[22]: # !curl -O https://raw.githubusercontent.com/jakevdp/marathon-data/
# master/marathon-data.csv

In[23]: data = pd.read_csv('marathon-data.csv')
data.head()

Out[23]:    age  gender   split   final
      0   33       M  01:05:38  02:08:51
      1   32       M  01:06:26  02:09:28
      2   31       M  01:06:49  02:10:42
      3   38       M  01:06:16  02:13:45
      4   31       M  01:06:32  02:13:59

¹ Райан М. Сcraping сайтов с помощью Python. — М.: ДМК-Пресс, 2016.