---
source_image: page_026.png
page_number: 26
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.13
tokens: 7611
characters: 2009
timestamp: 2025-12-24T02:21:52.222878
finish_reason: stop
---

каждый из элементов здесь представляет собой количество вхождений соответствующего слова в предложение (корпус). TF-представление слова \( w \) мы будем обозначать \( TF(w) \).

Пример 1.1. Генерация свернутого унитарного или бинарного представления с помощью библиотеки scikit-learn (рис. 1.4)

from sklearn.feature_extraction.text import CountVectorizer
import seaborn as sns

corpus = ['Time flies flies like an arrow.',
           'Fruit flies like a banana.']
vocab=['an','arrow','banana','flies','fruit','like','time']
one_hot_vectorizer = CountVectorizer(binary=True)
one_hot = one_hot_vectorizer.fit_transform(corpus).toarray()
sns.heatmap(one_hot, annot=True,
            cbar=False, xticklabels=vocab,
            yticklabels=['Предложение 2'])

<table>
  <tr>
    <th rowspan="2">Предложение</th>
    <th colspan="7">слова</th>
  </tr>
  <tr>
    <th>an</th>
    <th>arrow</th>
    <th>banana</th>
    <th>flies</th>
    <th>fruit</th>
    <th>like</th>
    <th>time</th>
  </tr>
  <tr>
    <td>Предложение 1</td>
    <td>1</td>
    <td>1</td>
    <td>0</td>
    <td>1</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Предложение 2</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>0</td>
  </tr>
</table>

Рис. 1.4. Свернутое унитарное представление, сгенерированное в примере 1.1

Представление TF-IDF

Рассмотрим набор патентных документов. Вероятно, в большинстве из них встречаются такие слова, как *claim*, *system*, *method*, *procedure* и т. д., зачастую по нескольку раз. В TF-представлении веса слов пропорциональны частоте, с которой они встречаются в документе. Однако такие распространенные слова, как *claim*, не вносят никакого вклада в наше понимание конкретного патента. Проще говоря, когда редкое слово (например, «тетрафторэтилен») попадается не так часто, но, вероятно, ясно свидетельствует о сущности патентного документа, то имеет смысл присвоить ему больший вес в представлении. Эвристический алго-