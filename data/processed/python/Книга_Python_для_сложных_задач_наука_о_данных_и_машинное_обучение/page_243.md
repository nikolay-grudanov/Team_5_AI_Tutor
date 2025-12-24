---
source_image: page_243.png
page_number: 243
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.05
tokens: 7596
characters: 2023
timestamp: 2025-12-24T00:57:44.072355
finish_reason: stop
---

Верхний график представляет поведение по умолчанию: в выходные дни1 значения равны NA и отсутствуют на графике. Нижний график демонстрирует различия между двумя методиками заполнения пропусков: интерполяцией вперед (forward-fill interpolation) и интерполяцией назад (back-fill interpolation).

Временные сдвиги

Еще одна распространенная операция с временными рядами — сдвиг данных во времени. В библиотеке Pandas есть два родственных метода для подобных вычислений: shift() и tshift(). Разница между ними заключается в том, что shift() выполняет сдвиг данных, а tshift() — сдвиг индекса. В обоих случаях сдвиг задается кратным периоду.

В следующем фрагменте кода мы сдвигаем как данные, так и индекс на 900 дней (рис. 3.8):

In[31]: fig, ax = plt.subplots(3, sharey=True)

# задаем периодичность данных
goog = goog.asfreq('D', method='pad')

goog.plot(ax=ax[0])
goog.shift(900).plot(ax=ax[1])
goog.tshift(900).plot(ax=ax[2])

# Легенды и пояснения
local_max = pd.to_datetime('2007-11-05')
offset = pd.Timedelta(900, 'D')

ax[0].legend(['input'], loc=2)
ax[0].get_xticklabels()[4].set(weight='heavy', color='red')
ax[0].axvline(local_max, alpha=0.3, color='red')

ax[1].legend(['shift(900)'], loc=2)
ax[1].get_xticklabels()[4].set(weight='heavy', color='red')
ax[1].axvline(local_max + offset, alpha=0.3, color='red')

ax[2].legend(['tshift(900)'], loc=2)
ax[2].get_xticklabels()[1].set(weight='heavy', color='red')
ax[2].axvline(local_max + offset, alpha=0.3, color='red');

Видим, что shift(900) сдвигает данные на 900 дней, перемещая часть из них за пределы графика (и оставляя NA-значения с другой стороны), в то время как tshift(900) сдвигает на 900 дней значения индекса.

Такую разновидность сдвигов часто используют для вычисления изменений с течением времени. Например, мы воспользовались сдвинутыми значениями, чтобы вычислить прибыль за год от вложений в акции Google по всему набору данных (рис. 3.9):

1 В данном случае имеются в виду конкретно так называемые банковские выходные дни, когда банки не работают.