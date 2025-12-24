---
source_image: page_125.png
page_number: 125
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.36
tokens: 7373
characters: 1767
timestamp: 2025-12-24T02:24:23.305480
finish_reason: stop
---

Пример 5.2. Решение задачи на аналогию с помощью вложений слов

Input[0]

import numpy as np
from annoy import AnnoyIndex

class PreTrainedEmbeddings(object):
    """ Продолжение реализации из предыдущего примера """
    def get_embedding(self, word):
        """
        Аргументы:
            word (str)
        Возвращает
            вложение (numpy.ndarray)
        """
        return self.word_vectors[self.word_to_index[word]]

    def get_closest_to_vector(self, vector, n=1):
        """ Возвращает n ближайших соседей заданного вектора
        Аргументы:
            vector (np.ndarray): размер его должен соответствовать размеру векторов в индексе Annoy
            n (int): требуемое число соседей
        Возвращает:
            [str, str, ...]: ближайшие к заданному вектору слова
                По расстоянию эти слова не упорядочиваются
        """
        nn_indices = self.index.get_nns_by_vector(vector, n)
        return [self.index_to_word[neighbor]
                for neighbor in nn_indices]

    def compute_and_print_analogy(self, word1, word2, word3):
        """ Выводит в консоль решения задачи на аналогию,
            с помощью вложений слов
        word1 по отношению к word2 аналогично word3 по отношению к __
        Данный метод выводит в консоль: word1 : word2 :: word3 : word4
        Аргументы:
            word1 (str)
            word2 (str)
            word3 (str)
        """
        vec1 = self.get_embedding(word1)
        vec2 = self.get_embedding(word2)
        vec3 = self.get_embedding(word3)

        # Простая гипотеза: аналогия представляет собой пространственную связь
        spatial_relationship = vec2 - vec1
        vec4 = vec3 + spatial_relationship

        closest_words = self.get_closest_to_vector(vec4, n=4)