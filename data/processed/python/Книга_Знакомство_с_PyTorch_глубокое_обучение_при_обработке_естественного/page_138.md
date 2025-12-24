---
source_image: page_138.png
page_number: 138
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.80
tokens: 7325
characters: 1872
timestamp: 2025-12-24T02:24:46.141079
finish_reason: stop
---

Пример 5.12. Реализация векторизатора для набора данных AG News

class NewsVectorizer(object):
    def vectorize(self, title, vector_length=-1):
        """
        Аргументы:
            title (str): строка разделенных пробелами слов
            vector_length (int): аргумент, жестко задающий длину вектора индексов
        Возвращает:
            векторизованный заголовок статьи (numpy.array)
        """
        indices = [self.title_vocab.begin_seq_index]
        indices.extend(self.title_vocab.lookup_token(token)
                        for token in title.split(" "))
        indices.append(self.title_vocab.end_seq_index)

        if vector_length < 0:
            vector_length = len(indices)

        out_vector = np.zeros(vector_length, dtype=np.int64)
        out_vector[:len(indices)] = indices
        out_vector[len(indices):] = self.title_vocab.mask_index

        return out_vector

    @classmethod
    def from_dataframe(cls, news_df, cutoff=25):
        """
        Создает экземпляр векторизатора на основе объекта DataFrame набора данных

        Аргументы:
            news_df (pandas.DataFrame): целевой набор данных
            cutoff (int): пороговое значение частоты вхождений для включения в словарь
        Возвращает:
            экземпляр NewsVectorizer
        """
        category_vocab = Vocabulary()
        for category in sorted(set(news_df.category)):
            category_vocab.add_token(category)

        word_counts = Counter()
        for title in news_df.title:
            for token in title.split(" "):
                if token not in string.punctuation:
                    word_counts[token] += 1

        title_vocab = SequenceVocabulary()
        for word, word_count in word_counts.items():
            if word_count >= cutoff:
                title_vocab.add_token(word)

        return cls(title_vocab, category_vocab)