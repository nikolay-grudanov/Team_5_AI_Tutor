---
source_image: page_027.png
page_number: 27
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.69
tokens: 7663
characters: 2092
timestamp: 2025-12-24T02:21:56.600264
finish_reason: stop
---

ритм учета обратной частотности документа (Inverse-Document-Frequency, IDF) именно так и работает.

IDF-представление специально снижает вес распространенных лексем и повышает вес редких в векторном представлении. Значение \( IDF(w) \) лексемы \( w \) учитывает корпус документов и равно:

\[
IDF(w) = \log \frac{N}{n_w},
\]

где \( n_w \) равно количеству документов, содержащих слово \( w \), а \( N \) — общее количество документов. Показатель TF-IDF равен просто \( TF(w) \cdot IDF(w) \). Во-первых, обратите внимание, что для очень распространенного слова, встречающегося во всех документах (то есть \( n_w = N \)), \( IDF(w) \) равно 0, а следовательно, и показатель TF-IDF равен 0, так что вес этого терма полностью аннулируется. Во-вторых, если терм встречается очень редко, скажем только в одном документе, то показатель IDF примет максимальное возможное значение, \( \log N \). Пример 1.2 демонстрирует генерацию TF-IDF-представления для списка предложений на английском языке с помощью библиотеки scikit-learn.

Пример 1.2. Генерация TF-IDF-представления с помощью библиотеки scikit-learn (рис. 1.5)

from sklearn.feature_extraction.text import TfidfVectorizer
import seaborn as sns

vocab=['an','arrow','banana','flies','fruit','like','time']
tfidf_vectorizer = TfidfVectorizer()
tfidf = tfidf_vectorizer.fit_transform(corpus).toarray()
sns.heatmap(tfidf, annot=True, cbar=False, xticklabels=vocab,
    yticklabels= ['Предложение 1', 'Предложение 2'])

<table>
  <tr>
    <th rowspan="2">Предложение</th>
    <th colspan="7">an arrow banana flies fruit like time</th>
  </tr>
  <tr>
    <td>0,43</td>
    <td>0,43</td>
    <td>0</td>
    <td>0,61</td>
    <td>0</td>
    <td>0,3</td>
    <td>0,43</td>
  </tr>
  <tr>
    <td>Предложение 1</td>
    <td>0</td>
    <td>0</td>
    <td>0,58</td>
    <td>0,41</td>
    <td>0,58</td>
    <td>0,41</td>
    <td>0</td>
  </tr>
  <tr>
    <td>Предложение 2</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>

Рис. 1.5. TF-IDF-представление, сгенерированное в примере 1.2