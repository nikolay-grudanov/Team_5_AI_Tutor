---
source_image: page_441.png
page_number: 441
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.07
tokens: 7243
characters: 1097
timestamp: 2025-12-24T01:02:27.279235
finish_reason: stop
---

In[12]:
from sklearn.metrics import confusion_matrix
mat = confusion_matrix(test.target, labels)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
    xticklabels=train.target_names, yticklabels=train.target_names)
plt.xlabel('true label')
plt.ylabel('predicted label');

![Матрица различий для полиномиального наивного байесовского классификатора текста](https://i.imgur.com/3Q5z5QG.png)

Рис. 5.41. Матрица различий для полиномиального наивного байесовского классификатора текста

Даже этот очень простой классификатор может легко отделять обсуждения космоса от дискуссий о компьютерах, но он путает обсуждения религии вообще и обсуждения христианства. Вероятно, этого следовало ожидать!

Хорошая новость состоит в том, что у нас теперь есть инструмент определения категории для любой строки с помощью метода predict() нашего конвейера. Следующий фрагмент кода описывает простую вспомогательную функцию, возвращающую предсказание для отдельной строки:

In[13]: def predict_category(s, train=train, model=model):
    pred = model.predict([s])
    return train.target_names[pred[0]]