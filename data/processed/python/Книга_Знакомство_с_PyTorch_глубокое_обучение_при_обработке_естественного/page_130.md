---
source_image: page_130.png
page_number: 130
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.38
tokens: 7576
characters: 2211
timestamp: 2025-12-24T02:24:37.923212
finish_reason: stop
---

набор задействуется не более одного раза, для повышения объективности оценки. В этом примере (как и в большинстве примеров книги) набор данных разбивается в соотношении 70 % на обучающий, 15 % на проверочный и 15% на контрольный набор данных.

Предварительно обработанное предложение

i pitied frankenstein my pity amounted to horror i abhorred myself

Окно 1
i pitied frankenstein my pity amounted to horror i abhorred myself

Окно 2
i pitied frankenstein my pity amounted to horror i abhorred myself

Окно 3
i pitied frankenstein my pity amounted to horror i abhorred myself

Окно 4
i pitied frankenstein my pity amounted to horror i abhorred myself

Рис. 5.2. Задача CBOW: предсказание слова по окружающему его контексту (с обеих сторон). Длина контекстных окон равна двум словам как слева, так и справа. В результате скольжения окна по тексту получается множество выборок с учителем, каждая со своим целевым словом (по центру). Окна, длина которых отличается от 2, дополняются пробелами до нужного размера. Например, для окна 3 по контекстам i pitied и my pity классификатор CBOW выдает предсказание frankenstein

Полученный набор данных с окнами и целями загружается с помощью объекта DataFrame библиотеки Pandas и индексируется в классе CBOWDataset. В примере 5.7 показан фрагмент кода метода __getitem__(), в котором используется векторизатор для преобразования контекста — правого и левого окон — в вектор. Целевое слово по центру окна преобразуется в целое число с помощью словаря.

Пример 5.7. Формирование класса набора данных для задачи CBOW

class CBOWDataset(Dataset):
    # ... существующая реализация из примера 3.15
    @classmethod
    def load_dataset_and_make_vectorizer(cls, cbow_csv):
        """Загружает набор данных и создает новый векторизатор с нуля

        Аргументы:
            cbow_csv (str): местоположение набора данных
        Возвращает:
            экземпляр CBOWDataset
        """
        cbow_df = pd.read_csv(cbow_csv)
        train_cbow_df = cbow_df[cbow_df.split=='train']
        return cls(cbow_df, CBOWVectorizer.from_dataframe(train_cbow_df))

    def __getitem__(self, index):
        """Основной метод — точка входа для наборов данных PyTorch

        Аргументы: