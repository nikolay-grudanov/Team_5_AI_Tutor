---
source_image: page_421.png
page_number: 421
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.43
tokens: 7323
characters: 1318
timestamp: 2025-12-24T01:02:01.744431
finish_reason: stop
---

![Данные для демонстрации кривых обучения](https://i.imgur.com/3Q5z5QG.png)

Рис. 5.30. Данные для демонстрации кривых обучения

Повторим вышеприведенный код для построения графика кривой обучения для этого большего набора данных. Для сравнения выведем поверх и предыдущие результаты (рис. 5.31):

In[16]:
degree = np.arange(21)
train_score2, val_score2 = validation_curve(PolynomialRegression(), X2, y2,
    'polynomialfeatures__degree',
    degree, cv=7)

plt.plot(degree, np.median(train_score2, 1), color='blue',
    label='training score')
plt.plot(degree, np.median(val_score2, 1), color='red',
    label='validation score')
plt.plot(degree, np.median(train_score, 1), color='blue', alpha=0.3,
    linestyle='dashed')
plt.plot(degree, np.median(val_score, 1), color='red', alpha=0.3,
    linestyle='dashed')
plt.legend(loc='lower center')
plt.ylim(0, 1)
plt.xlabel('degree')
plt.ylabel('score');

Сплошные линии показывают новые результаты, а более бледные штриховые линии — результаты предыдущего меньшего набора данных. Из кривой проверки ясно, что этот больший набор данных позволяет использовать намного более сложную модель: максимум, вероятно, возле степени 6, но даже модель со степенью 20 не выглядит сильно переобученной — оценки эффективности для проверки и обучения остаются очень близки друг к другу.