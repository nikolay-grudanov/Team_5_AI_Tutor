---
source_image: page_242.png
page_number: 242
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.58
tokens: 7321
characters: 1360
timestamp: 2025-12-24T00:57:33.420032
finish_reason: stop
---

goog.asfreq('BA').plot(style='--');
plt.legend(['input', 'resample', 'asfreq'],
    loc='upper left');

Обратите внимание на различие: в каждой точке resample выдает среднее значение за предыдущий год, а asfreq — значение на конец года.

В случае повышающей дискретизации методы resample() и asfreq() в значительной степени идентичны, хотя доступных для использования параметров у resample() гораздо больше. В данном случае оба этих метода по умолчанию оставляют значения интерполированных точек пустыми, то есть заполненными значениями NA. Аналогично обсуждавшейся выше функции pd.fillna() метод asfreq() принимает аргумент method, определяющий, откуда будут браться значения для таких точек. Здесь мы передискретизируем данные по рабочим дням с периодичностью обычного дня, то есть включая выходные дни (рис. 3.7):

In[30]: fig, ax = plt.subplots(2, sharex=True)
    data = goog.iloc[:10]

    data.asfreq('D').plot(ax=ax[0], marker='o')

    data.asfreq('D', method='bfill').plot(ax=ax[1], style='-o')
    data.asfreq('D', method='ffill').plot(ax=ax[1], style='--o')
    ax[1].legend(["back-fill", "forward-fill"]);

![Сравнение интерполяции вперед (forward-fill interpolation) и назад (backward-fill interpolation)](https://i.imgur.com/3Q5z5QG.png)

Рис. 3.7. Сравнение интерполяции вперед (forward-fill interpolation) и назад (backward-fill interpolation)