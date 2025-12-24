---
source_image: page_097.png
page_number: 97
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.09
tokens: 7456
characters: 1907
timestamp: 2025-12-24T02:23:33.162256
finish_reason: stop
---

""" Векторизация передаваемой фамилии

Аргументы:
    surname (str): фамилия
Возвращает:
    one_hot (np.ndarray): свернутое унитарное представление
"""

vocab = self.surname_vocab
one_hot = np.zeros(len(vocab), dtype=np.float32)
for token in surname:
    one_hot[vocab.lookup_token(token)] = 1
return one_hot

@classmethod
def from_dataframe(cls, surname_df):
    """ Создает экземпляр векторизатора на основе объекта DataFrame набора данных

    Аргументы:
        surname_df (pandas.DataFrame): набор данных фамилий
    Возвращает:
        экземпляр SurnameVectorizer
    """
    surname_vocab = Vocabulary(unk_token="@")
    nationality_vocab = Vocabulary(add_unk=False)

    for index, row in surname_df.iterrows():
        for letter in row.surname:
            surname_vocab.add_token(letter)
        nationality_vocab.add_token(row.nationality)

    return cls(surname_vocab, nationality_vocab)

Модель SurnameClassifier

Класс SurnameClassifier (пример 4.7) — реализация MLP, представленного ранее в главе. Первый линейный слой отображает входные векторы в промежуточный вектор, к которому применяется нелинейность. Второй линейный слой отображает промежуточный вектор в вектор предсказаний.

На последнем шаге может применяться многомерная логистическая функция для приведения суммы выходных значений к 1, то есть их интерпретации как «вероятностей»1. Причина необходимости ее применения кроется в математической формулировке используемой функции потерь — функции потерь на основе

1 Мы намеренно написали слово «вероятностей» в кавычках, чтобы подчеркнуть, что это вовсе не настоящие вероятности в байесовском смысле, но поскольку сумма выходных значений равна 1, то это допустимое распределение, которое можно интерпретировать как вероятности. Это одно из самых занудных примечаний в данной книге, так что можете смело его игнорировать, просто закройте на это глаза и называйте их вероятностями.