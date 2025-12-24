---
source_image: page_485.png
page_number: 485
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.86
tokens: 7212
characters: 962
timestamp: 2025-12-24T01:03:36.472106
finish_reason: stop
---

# Маркируем изображение целевыми значениями
ax.text(0, 7, str(digits.target[i]))

![Визуальное представление данных по рукописным цифрам](../images/5.78.png)

Рис. 5.78. Визуальное представление данных по рукописным цифрам

Быстро классифицировать цифры с помощью случайного леса можно следующим образом (рис. 5.79):

In[14]:
from sklearn.cross_validation import train_test_split

Xtrain, Xtest, ytrain, ytest = train_test_split(digits.data, digits.target,
                                              random_state=0)
model = RandomForestClassifier(n_estimators=1000)
model.fit(Xtrain, ytrain)
ypred = model.predict(Xtest)

Взглянем на отчет о классификации для данного классификатора:

In[15]: from sklearn import metrics
print(metrics.classification_report(ypred, ytest))

precision    recall    f1-score    support
0            1.00      0.97       0.99       38
1            1.00      0.98       0.99       44
2            0.95      1.00       0.98       42