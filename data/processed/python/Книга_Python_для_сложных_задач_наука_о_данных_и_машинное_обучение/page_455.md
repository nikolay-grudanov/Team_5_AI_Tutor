---
source_image: page_455.png
page_number: 455
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.98
tokens: 7390
characters: 1281
timestamp: 2025-12-24T01:02:58.438556
finish_reason: stop
---

In[18]:
    def hours_of_daylight(date, axis=23.44, latitude=47.61):
        """Рассчитываем длительность светового дня для заданной даты"""
        days = (date - pd.datetime(2000, 12, 21)).days
        m = (1. - np.tan(np.radians(latitude))
             * np.tan(np.radians(axis))
             * np.cos(days * 2 * np.pi / 365.25)))
        return 24. * np.degrees(np.arccos(1 - np.clip(m, 0, 2))) / 180.

daily['daylight_hrs'] = list(map(hours_of_daylight, daily.index))
daily[['daylight_hrs']].plot();

![Визуализация длительности светового дня в Сиэтле](https://i.imgur.com/3Q5z5QG.png)

Дата

Рис. 5.51. Визуализация длительности светового дня в Сиэтле

Мы также добавим к данным среднюю температуру и общее количество осадков. Помимо количества дюймов осадков, добавим еще и флаг для обозначения засушливых дней (с нулевым количеством осадков):

In[19]: # Температуры указаны в десятых долях градуса Цельсия;
    # преобразуем в градусы
    weather['TMIN'] /= 10
    weather['TMAX'] /= 10
    weather['Temp (C)'] = 0.5 * (weather['TMIN'] + weather['TMAX'])

    # Осадки указаны в десятых долях миллиметра; преобразуем в дюймы
    weather['PRCP'] /= 254
    weather['dry day'] = (weather['PRCP'] == 0).astype(int)

daily = daily.join(weather[['PRCP', 'Temp (C)', 'dry day']])