---
source_image: page_527.png
page_number: 527
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.40
tokens: 7312
characters: 1296
timestamp: 2025-12-24T01:04:45.177433
finish_reason: stop
---

В силу того что алгоритм \( k \)-средних ничего не знает о сущности кластеров, метки 0–9 могут оказаться перепутаны местами. Исправить это можно, задав соответствие всех полученных меток кластеров имеющимся в них фактическим меткам:

In[14]: from scipy.stats import mode

    labels = np.zeros_like(clusters)
    for i in range(10):
        mask = (clusters == i)
        labels[mask] = mode(digits.target[mask])[0]

Теперь можно проверить, насколько точно кластеризация без учителя определила подобие цифр в наших данных:

In[15]: from sklearn.metrics import accuracy_score
    accuracy_score(digits.target, labels)

Out[15]: 0.79354479688369506

С помощью простого алгоритма \( k \)-средних мы определили правильную группировку для почти 80 % исходных цифр! Посмотрим на матрицу различий (рис. 5.119):

In[16]: from sklearn.metrics import confusion_matrix
    mat = confusion_matrix(digits.target, labels)
    sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
                xticklabels=digits.target_names,
                yticklabels=digits.target_names)
    plt.xlabel('true label')
    plt.ylabel('predicted label');

![Матрица различий для классификатора методом k-средних](https://i.imgur.com/3Q5z5QG.png)

Рис. 5.119. Матрица различий для классификатора методом k-средних