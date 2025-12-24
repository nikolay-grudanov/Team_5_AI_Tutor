---
source_image: page_136.png
page_number: 136
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.82
tokens: 7499
characters: 2024
timestamp: 2025-12-24T02:24:50.911492
finish_reason: stop
---

Возвращает:
    экземпляр NewsDataset
"""
news_df = pd.read_csv(news_csv)
train_news_df = news_df[news_df.split=='train']
return cls(news_df, NewsVectorizer.from_dataframe(train_news_df))

def __getitem__(self, index):
    """ Основной метод — точка входа для наборов данных PyTorch

Аргументы:
    index (int): индекс точки данных
Возвращает:
    словарь с признаками (x_data) и меткой (y_target) точки данных
"""
row = self._target_df.iloc[index]

title_vector = \
    self._vectorizer.vectorize(row.title, self._max_seq_length)

category_index = \
    self._vectorizer.category_vocab.lookup_token(row.category)

return {'x_data': title_vector,
        'y_target': category_index}

Классы Vocabulary, Vectorizer и DataLoader

В этом примере появился класс SequenceVocabulary — подкласс стандартного класса Vocabulary, включающий четыре специальных токена, используемых для данных последовательности: токены UNK, MASK, BEGIN-OF-SEQUENCE и END-OF-SEQUENCE. Мы опишем их подробнее в главе 6, но, если говорить вкратце, они служат для трех различных целей. Благодаря токену UNK (сокращение от unknown — «неизвестный»), с которым мы сталкивались в главе 4, модель получает возможность обучаться представлениям для редких слов, а значит, обрабатывать во время контроля не встречавшиеся ей во время обучения слова. Токен MASK служит индикатором для слоев вложений и вычислений функций потерь в случае последовательностей переменной длины. Наконец токены BEGIN-OF-SEQUENCE и END-OF-SEQUENCE указывают нейронной сети на границы последовательности. Рисунок 5.3 демонстрирует результаты использования этих специальных токенов в конвейере векторизации.

Вторую часть конвейера для преобразования текста в векторизованный мини-пакет составляет векторизатор NewsVectorizer, в котором создается экземпляр и инкапсулируется применение SequenceVocabulary. В данном примере векторизатор следует паттерну, продемонстрированному в пункте «Класс Vectorizer» на с. 85: ограничению общего набора возможных слов путем подсчета вхождений и порого-