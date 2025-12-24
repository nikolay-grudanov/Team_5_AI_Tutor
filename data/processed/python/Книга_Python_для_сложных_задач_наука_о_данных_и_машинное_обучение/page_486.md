---
source_image: page_486.png
page_number: 486
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.91
tokens: 7352
characters: 1110
timestamp: 2025-12-24T01:03:41.908052
finish_reason: stop
---

3      0.98      0.96      0.97      46
4      0.97      1.00      0.99      37
5      0.98      0.96      0.97      49
6      1.00      1.00      1.00      52
7      1.00      0.96      0.98      50
8      0.94      0.98      0.96      46
9      0.96      0.98      0.97      46

avg / total    0.98      0.98      0.98      450

В дополнение нарисуем матрицу различий (см. рис. 5.79):

In[16]: from sklearn.metrics import confusion_matrix
mat = confusion_matrix(ytest, ypred)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False)
plt.xlabel('true label')
plt.ylabel('predicted label');

![Матрица различий для классификации цифр с помощью случайных лесов](https://i.imgur.com/3Q5z5QG.png)

Рис. 5.79. Матрица различий для классификации цифр с помощью случайных лесов

Оказалось, что простой, не настроенный каким-то специальным образом случайный лес дает очень точную классификацию данных по рукописным цифрам.

Резюме по случайным лесам

В этом разделе мы познакомили вас с понятием ансамблей оценивателей (ensemble estimators) и, в частности, модели случайного леса — ансамбля случайных деревьев