---
source_image: page_159.png
page_number: 159
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.94
tokens: 7401
characters: 1934
timestamp: 2025-12-24T02:25:22.162998
finish_reason: stop
---

он должен возвращать последовательность целочисленных значений для целей предсказания, как показано в примере 7.1. Этот метод обращается к векторизатору для вычисления последовательности целых чисел, играющих роль входных данных (from_vector), и последовательности целых чисел, играющих роль выходных данных (to_vector). Реализация метода vectorize() описана в следующем подразделе.

Пример 7.1. Метод SurnameDataset.__getitem__() для задачи предсказания последовательностей

class SurnameDataset(Dataset):
    @classmethod
    def load_dataset_and_make_vectorizer(cls, surname_csv):
        """ Загружает набор данных и создает с нуля новый векторизатор

        Аргументы:
            surname_csv (str): местоположение набора данных
        Возвращает:
            экземпляр SurnameDataset
        """
        surname_df = pd.read_csv(surname_csv)
        return cls(surname_df, SurnameVectorizer.from_dataframe(surname_df))

    def __getitem__(self, index):
        """ Основной метод — точка входа для наборов данных PyTorch

        Аргументы:
            index (int): индекс точки данных
        Возвращает:
            словарь, содержащий точку данных: (x_data, y_target, class_index)
        """
        row = self._target_df.iloc[index]

        from_vector, to_vector = \
            self._vectorizer.vectorize(row.surname, self._max_seq_length)

        nationality_index = \
            self._vectorizer.nationality_vocab.lookup_token(row.nationality)

        return {'x_data': from_vector,
                'y_target': to_vector,
                'class_index': nationality_index}

Структуры данных для векторизации

Как и в предыдущих примерах, для преобразования последовательностей символов фамилий в векторизованную форму используются три основные структуры данных: SequenceVocabulary — для отображения токенов в целые числа, SurnameVectorizer — для общего согласования этих отображений и DataLoader — для группировки