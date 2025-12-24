---
source_image: page_123.png
page_number: 123
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.33
tokens: 7369
characters: 1716
timestamp: 2025-12-24T02:24:20.046330
finish_reason: stop
---

Пример 5.1. Использование предобученных вложений слов¹

Input[0]

import numpy as np
from annoy import AnnoyIndex

class PreTrainedEmbeddings(object):
    def __init__(self, word_to_index, word_vectors):
        """
        Аргументы:
            word_to_index (dict): отображение слов
            в целочисленные значения
            word_vectors (список массивов numpy)
        """
        self.word_to_index = word_to_index
        self.word_vectors = word_vectors
        self.index_to_word = \
            {v: k for k, v in self.word_to_index.items()}
        self.index = AnnoyIndex(len(word_vectors[0]),
            metric='euclidean')
        for _, i in self.word_to_index.items():
            self.index.add_item(i, self.word_vectors[i])
        self.index.build(50)

    @classmethod
    def from_embeddings_file(cls, embedding_file):
        """
        Создаем экземпляр на основе файла векторов,
        заранее полученных в результате обучения

        Формат файла векторов должен быть следующим:
            word0 x0_0 x0_1 x0_2 x0_3 ... x0_N
            word1 x1_0 x1_1 x1_2 x1_3 ... x1_N

        Аргументы:
            embedding_file (str): местоположение файла
        Возвращает:
            экземпляр PretrainedEmbeddings
        """
        word_to_index = {}
        word_vectors = []
        with open(embedding_file) as fp:

¹ При выполнении примера 5.1 может возникнуть ошибка кодировки из-за содержащихся в наборе Glove символов не из таблицы ASCII. Простейший способ решения этой проблемы — воспользоваться в методе from_embeddings_file функцией open из пакета io, указав кодировку UTF, вот так:
import io
...
    with io.open(embedding_file, encoding='utf-8') as fp:
... — Примеч. пер.