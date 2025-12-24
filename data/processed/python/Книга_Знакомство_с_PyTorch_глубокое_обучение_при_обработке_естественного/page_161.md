---
source_image: page_161.png
page_number: 161
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.79
tokens: 7397
characters: 1947
timestamp: 2025-12-24T02:25:24.218411
finish_reason: stop
---

довательности заполнялись (дополнялись) справа, поскольку пустые позиции меняют выходной вектор и хотелось бы, чтобы это произошло после просмотра последовательности.

Пример 7.2. Код метода SurnameVectorizer.vectorize() для задачи предсказания последовательности

class SurnameVectorizer(object):
    """ Векторизатор, приводящий словари в соответствие друг другу и использующий их"""
    def vectorize(self, surname, vector_length=-1):
        """ Векторизует фамилию в вектор наблюдений и целей

        Аргументы:
            surname (str): векторизуемая фамилия
            vector_length (int): аргумент, жестко задающий длину вектора индексов
        Возвращает:
            кортеж: (from_vector, to_vector)
                from_vector (numpy.ndarray): вектор наблюдений
                to_vector (numpy.ndarray): вектор целевых предсказаний
        """
        indices = [self.char_vocab.begin_seq_index]
        indices.extend(self.char_vocab.lookup_token(token)
            for token in surname)
        indices.append(self.char_vocab.end_seq_index)

        if vector_length < 0:
            vector_length = len(indices) - 1

        from_vector = np.zeros(vector_length, dtype=np.int64)
        from_indices = indices[:-1]
        from_vector[:len(from_indices)] = from_indices
        from_vector[len(from_indices):] = self.char_vocab.mask_index

        to_vector = np.empty(vector_length, dtype=np.int64)
        to_indices = indices[1:]
        to_vector[:len(to_indices)] = to_indices
        to_vector[len(to_indices):] = self.char_vocab.mask_index

        return from_vector, to_vector

    @classmethod
    def from_dataframe(cls, surname_df):
        """ Создает экземпляр векторизатора на основе объекта DataFrame набора данных

        Аргументы:
            surname_df (pandas.DataFrame): набор данных фамилий
        Возвращает:
            экземпляр SurnameVectorizer
        """
        char_vocab = SequenceVocabulary()