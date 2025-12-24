---
source_image: page_131.png
page_number: 131
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.04
tokens: 7416
characters: 1861
timestamp: 2025-12-24T02:24:34.529747
finish_reason: stop
---

index (int): индекс точки данных
Возвращает:
    словарь с признаками (x_data) и меткой (y_target) точки данных
"""
row = self._target_df.iloc[index]

    context_vector = \
        self._vectorizer.vectorize(row.context, self._max_seq_length)
    target_index = self._vectorizer.cbow_vocab.lookup_token(row.target)

    return {'x_data': context_vector,
            'y_target': target_index}

Классы Vocabulary, Vectorizer и DataLoader

В задаче классификации CBOW конвейер преобразования текста в векторизованный мини-пакет не отличается ничем особенным: классы Vocabulary и DataLoader функционируют точно так же, как и в примере с классификацией тональностей обзоров ресторанов. Однако, в отличие от векторизаторов из глав 3 и 4, векторизатор в данном случае не формирует унитарные векторы. Вместо этого он формирует и возвращает вектор целых чисел, представляющих индексы контекста. Код функции vectorize() приведен в примере 5.8.

Пример 5.8. Векторизатор для данных CBOW

class CBOWVectorizer(object):
    """ Векторизатор, приводящий словари в соответствие друг другу и использующий их"""
    def vectorize(self, context, vector_length=-1):
        """
        Аргументы:
            context (str): строка разделенных пробелами слов
            vector_length (int): аргумент, жестко задающий длину вектора индексов
        """
        indices = \
            [self.cbow_vocab.lookup_token(token) for token in context.split(' ')]
        if vector_length < 0:
            vector_length = len(indices)

        out_vector = np.zeros(vector_length, dtype=np.int64)
        out_vector[:len(indices)] = indices
        out_vector[len(indices):] = self.cbow_vocab.mask_index

        return out_vector

Обратите внимание, что, если число токенов в контексте меньше максимальной длины, оставшиеся записи заполняются нулями. Это можно назвать дополнением нулями.