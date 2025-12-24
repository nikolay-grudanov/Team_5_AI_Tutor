---
source_image: page_071.png
page_number: 71
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.37
tokens: 7317
characters: 1622
timestamp: 2025-12-24T02:22:51.717581
finish_reason: stop
---

rating_vocab (Vocabulary): отображает метки классов в целочисленные значения
"""
self.review_vocab = review_vocab
self.rating_vocab = rating_vocab

def vectorize(self, review):
    """ Создает свернутый унитарный вектор для обзора

    Аргументы:
        review (str): обзор
    Возвращает:
        one_hot (np.ndarray): свернутое унитарное представление
    """
    one_hot = np.zeros(len(self.review_vocab), dtype=np.float32)

    for token in review.split(" "):
        if token not in string.punctuation:
            one_hot[self.review_vocab.lookup_token(token)] = 1
    return one_hot

@classmethod
def from_dataframe(cls, review_df, cutoff=25):
    """ Создает экземпляр векторизатора на основе объекта DataFrame набора данных

    Аргументы:
        review_df (pandas.DataFrame): набор данных обзоров
        cutoff (int): параметр для фильтрации по частоте вхождения
    Возвращает:
        экземпляр класса ReviewVectorizer
    """
    review_vocab = Vocabulary(add_unk=True)
    rating_vocab = Vocabulary(add_unk=False)

    # Добавить рейтинги
    for rating in sorted(set(review_df.rating)):
        rating_vocab.add_token(rating)

    # Добавить часто встречающиеся слова, если число вхождений больше указанного
    word_counts = Counter()
    for review in review_df.review:
        for word in review.split(" "):
            if word not in string.punctuation:
                word_counts[word] += 1

    for word, count in word_counts.items():
        if count > cutoff:
            review_vocab.add_token(word)
    return cls(review_vocab, rating_vocab)

@classmethod
def from_serializable(cls, contents):