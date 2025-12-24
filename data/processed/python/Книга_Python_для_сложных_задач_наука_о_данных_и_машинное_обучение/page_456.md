---
source_image: page_456.png
page_number: 456
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.43
tokens: 7735
characters: 1813
timestamp: 2025-12-24T01:03:20.952958
finish_reason: stop
---

Добавим счетчик, который будет увеличиваться, начиная с первого дня, и отмерять количество прошедших лет. Он позволит нам отслеживать ежегодные увеличения или уменьшения ежедневного количества проезжающих:

In[20]: daily['annual'] = (daily.index - daily.index[0]).days / 365.

Теперь наши данные приведены в полный порядок, и мы можем посмотреть на них:

In[21]: daily.head()

Out[21]:
      Total   Mon   Tue   Wed   Thu   Fri   Sat   Sun  holiday  daylight_hrs
Date
2012-10-03  3521   0    0     1     0     0     0     0       0      11.277359
2012-10-04  3475   0    0     0     1     0     0     0       0      11.219142
2012-10-05  3148   0    0     0     0     1     0     0       0      11.161038
2012-10-06  2006   0    0     0     0     0     1     0       0      11.103056
2012-10-07  2142   0    0     0     0     0     0     1       0      11.045208

      PRCP  Temp (C)  dry day  annual
Date
2012-10-03  0      13.35     1     0.000000
2012-10-04  0      13.60     1     0.002740
2012-10-05  0      15.30     1     0.005479
2012-10-06  0      15.85     1     0.008219
2012-10-07  0      15.85     1     0.010959

После этого можно выбрать нужные столбцы и обучить линейную регрессионную модель на наших данных. Зададим параметр fit_intercept = False, поскольку флаги для дней, по сути, выполняют подбор точек пересечения с осями координат по дням:

In[22]:
column_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'holiday',
                'daylight_hrs', 'PRCP', 'dry day', 'Temp (C)', 'annual']
X = daily[column_names]
y = daily['Total'] # Всего

model = LinearRegression(fit_intercept=False)
model.fit(X, y)
daily['predicted'] = model.predict(X)

Сравниваем общий и предсказанный моделью велосипедный трафик визуально (рис. 5.52):

In[23]: daily[['Total', 'predicted']].plot(alpha=0.5);