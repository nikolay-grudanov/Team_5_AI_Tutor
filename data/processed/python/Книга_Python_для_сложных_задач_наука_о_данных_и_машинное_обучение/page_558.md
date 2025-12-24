---
source_image: page_558.png
page_number: 558
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.66
tokens: 7447
characters: 1948
timestamp: 2025-12-24T01:05:37.538752
finish_reason: stop
---

3. Вычисляем априорную вероятность принадлежности к классу (class prior), \( P(y) \), на основе количества экземпляров каждого класса в обучающей последовательности.

4. Для неизвестной точки \( x \) апостериорная вероятность принадлежности к классу равна \( P(y | x) \propto P(x | y) \, P(y) \). Метка каждой точки — класс, при котором достигается максимум этой апостериорной вероятности.

Данный алгоритм достаточно прост и интуитивно понятен. Несколько сложнее будет реализовать его с помощью фреймворка Scikit-Learn так, чтобы воспользоваться поиском по сетке и перекрестной проверкой.

Вот код, реализующий этот алгоритм на базе фреймворка Scikit-Learn, мы последовательно рассмотрим его блок за блоком:

In[16]: from sklearn.base import BaseEstimator, ClassifierMixin

class KDEClassifier(BaseEstimator, ClassifierMixin):
    """Байесовская порождающая классификация на основе метода KDE

Параметры
----------
bandwidth : float
    Ширина ядра в каждом классе
kernel : str
    Название ядра, передаваемое функции KernelDensity
    """
    def __init__(self, bandwidth=1.0, kernel='gaussian'):
        self.bandwidth = bandwidth
        self.kernel = kernel

    def fit(self, X, y):
        self.classes_ = np.sort(np.unique(y))
        training_sets = [X[y == yi] for yi in self.classes_]
        self.models_ = [KernelDensity(bandwidth=self.bandwidth,
                                      kernel=self.kernel).fit(Xi)
                        for Xi in training_sets]
        self.logpriors_ = [np.log(Xi.shape[0] / X.shape[0])
                           for Xi in training_sets]
        return self

    def predict_proba(self, X):
        logprobs = np.array([model.score_samples(X)
                             for model in self.models_]).T
        result = np.exp(logprobs + self.logpriors_)
        return result / result.sum(1, keepdims=True)

    def predict(self, X):
        return self.classes_[np.argmax(self.predict_proba(X), 1)]