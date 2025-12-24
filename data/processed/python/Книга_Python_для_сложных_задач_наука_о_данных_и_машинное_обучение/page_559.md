---
source_image: page_559.png
page_number: 559
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.59
tokens: 7512
characters: 2211
timestamp: 2025-12-24T01:05:40.599319
finish_reason: stop
---

Внутреннее устройство пользовательского оценивателя

Рассмотрим этот код и обсудим основные его особенности:

from sklearn.base import BaseEstimator, ClassifierMixin

class KDEClassifier(BaseEstimator, ClassifierMixin):
    """Байесовская порождающая классификация на основе метода KDE

    Параметры
    ----------
    bandwidth : float
        Ширина ядра в каждом классе
    kernel : str
        Название ядра, передаваемое функции KernelDensity
    """

Каждый оцениватель в библиотеке Scikit-Learn представляет собой класс, наследующий класс BaseEstimator, а также соответствующую примесь (mixin), которые обеспечивают стандартную функциональность. Например, помимо прочего, класс BaseEstimator включает логику, необходимую для клонирования/копирования оценивателя, чтобы использовать его в процедуре перекрестной проверки, а ClassifierMixin определяет используемый по умолчанию метод score(). Мы также задали docstring, который будет собран справочной системой языка Python (см. раздел «Справка и документация в оболочке Python» главы 1).

Вот метод инициализации нашего класса:

def __init__(self, bandwidth=1.0, kernel='gaussian'):
    self.bandwidth = bandwidth
    self.kernel = kernel

Это тот код, который фактически выполняется при создании объекта посредством конструктора KDEClassifier(). В библиотеке Scikit-Learn важно, чтобы в методе инициализации не содержалось никаких команд, кроме присваивания объекту self переданных значений по имени. Причина в том, что содержащаяся в классе BaseEstimator логика необходима для клонирования и модификации оценивателей для перекрестной проверки, поиска по сетке и других целей. Аналогично все аргументы метода __init__ должны быть объявлены явным образом, то есть следует избегать аргументов *args или **kwargs, так как они не могут быть корректно обработаны внутри процедур перекрестной проверки.

Дальше идет метод fit(), в котором мы обрабатываем обучающие данные:

def fit(self, X, y):
    self.classes_ = np.sort(np.unique(y))
    training_sets = [X[y == yi] for yi in self.classes_]
    self.models_ = [KernelDensity(bandwidth=self.bandwidth,
                                 kernel=self.kernel).fit(Xi)
                    for Xi in training_sets]