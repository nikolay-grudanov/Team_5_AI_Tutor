---
source_image: page_316.png
page_number: 316
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.07
tokens: 7621
characters: 2036
timestamp: 2025-12-24T00:59:42.726947
finish_reason: stop
---

При работе с данными подобным образом часто бывает полезно снабдить элементы графика пояснениями для привлечения к ним внимания читателя. Это можно сделать вручную с помощью команды plt.text/ax.text, которая поместит текст в месте, соответствующем конкретным значениям координат (x, y) (рис. 4.68):

In[4]: fig, ax = plt.subplots(figsize=(12, 4))
    births_by_date.plot(ax=ax)

    # Добавляем метки на график
    style = dict(size=10, color='gray')

    ax.text('2012-1-1', 3950, "New Year's Day", **style)
    ax.text('2012-7-4', 4250, "Independence Day", ha='center', **style)
    ax.text('2012-9-4', 4850, "Labor Day", ha='center', **style)
    ax.text('2012-10-31', 4600, "Halloween", ha='right', **style)
    ax.text('2012-11-25', 4450, "Thanksgiving", ha='center', **style)
    ax.text('2012-12-25', 3850, "Christmas ", ha='right', **style)

    # Добавляем метки для осей координат
    ax.set(title='USA births by day of year (1969-1988)',
           ylabel='average daily births')

    # Размещаем ось X центрированными метками для месяцев
    ax.xaxis.set_major_locator(mpl.dates.MonthLocator())
    ax.xaxis.set_minor_locator(mpl.dates.MonthLocator(bymonthday=15))
    ax.xaxis.set_major_formatter(plt.NullFormatter())
    ax.xaxis.set_minor_formatter(mpl.dates.DateFormatter('%h'));

Ежедневное количество новорожденных в зависимости от даты, США (1969–1988)

День труда
Хеллоуин
День Благодарения
Рождество
День Независимости
Новый год

Янв   Фев   Мар   Апр   Май   Июн   Июл   Авг   Сен   Окт   Ноя   Дек

Рис. 4.68. Ежедневное количество рожденных детей в зависимости от даты, с комментариями

Метод ax.text принимает на входе координату x, координату y, строковое значение и необязательные ключевые слова, задающие цвет, размер, стиль, выравнивание и другие свойства текста. В данном случае мы использовали значения ha='right' и ha='center', где ha — сокращение от horizontal alignment («выравнивание по горизонтали»). См. дальнейшую информацию об имеющихся настройках в docstring функций plt.text() и mpl.text.Text().