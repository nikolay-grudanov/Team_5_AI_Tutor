---
source_image: page_149.png
page_number: 149
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.94
tokens: 7409
characters: 1863
timestamp: 2025-12-24T02:25:03.983934
finish_reason: stop
---

вектора индексов

"""
indices = [self.char_vocab.begin_seq_index]
indices.extend(self.char_vocab.lookup_token(token)
    for token in surname)
indices.append(self.char_vocab.end_seq_index)

if vector_length < 0:
    vector_length = len(indices)

out_vector = np.zeros(vector_length, dtype=np.int64)
out_vector[:len(indices)] = indices
out_vector[len(indices):] = self.char_vocab.mask_index

return out_vector, len(indices)

@classmethod
def from_dataframe(cls, surname_df):
    """ Создает экземпляр векторизатора на основе объекта DataFrame набора данных

Аргументы:
    surname_df (pandas.DataFrame): набор данных фамилий
Возвращает:
    экземпляр SurnameVectorizer
"""
char_vocab = SequenceVocabulary()
nationality_vocab = Vocabulary()

for index, row in surname_df.iterrows():
    for char in row.surname:
        char_vocab.add_token(char)
    nationality_vocab.add_token(row.nationality)

return cls(char_vocab, nationality_vocab)

Модель SurnameClassifier

Модель SurnameClassifier состоит из слоя вложений, RNN Элмана и линейного слоя. Мы предполагаем, что ее входными данными служат токены, представленные в виде набора целочисленных значений, после их отображения в целые числа с помощью SequenceVocabulary. Модель сначала выполняет вложение этих целых чисел с помощью соответствующего слоя вложений. Затем с применением RNN вычисляются векторы представления последовательности. Они соответствуют скрытым состояниям для каждого из символов фамилии. Поскольку задача — классифицировать фамилии, извлекается вектор, соответствующий позиции завершающего символа в каждой из фамилий. Его можно рассматривать как результат прохода по всей входной последовательности, а значит, сводный вектор для фамилии. Путем передачи этих сводных векторов через линейный слой вычисляется вектор предсказаний. Далее либо этот вектор предсказаний используется при вычислении