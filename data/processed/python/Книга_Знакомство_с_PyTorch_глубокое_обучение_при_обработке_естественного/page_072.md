---
source_image: page_072.png
page_number: 72
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.40
tokens: 7498
characters: 2193
timestamp: 2025-12-24T02:22:59.856732
finish_reason: stop
---

""" Создает экземпляр ReviewVectorizer на основе сериализуемого словаря

Аргументы:
    contents (dict): сериализуемый словарь
Возвращает:
    экземпляр класса ReviewVectorizer
"""
review_vocab = Vocabulary.from_serializable(contents['review_vocab'])
rating_vocab = Vocabulary.from_serializable(contents['rating_vocab'])
return cls(review_vocab=review_vocab, rating_vocab=rating_vocab)

def to_serializable(self):
    """ Создает сериализуемый словарь для кэширования

Возвращает:
    contents (dict): сериализуемый словарь
    """
    return {'review_vocab': self.review_vocab.to_serializable(),
            'rating_vocab': self.rating_vocab.to_serializable()}

Класс DataLoader

Последняя фаза конвейера преобразования текста в векторизованный мини-пакет — собственно группировка векторизованных точек данных. Поскольку группировка в мини-пакеты играет столь важную роль в обучении нейронных сетей, фреймворк PyTorch предоставляет для координации этого процесса встроенный класс DataLoader. Для создания экземпляра класса DataLoader необходимо передать какой-либо объект Dataset PyTorch (например, описанный нами для этого примера ReviewDataset), batch_size и несколько других поименованных аргументов. В результате получается объект, представляющий собой Python-итератор, группирующий и свертывающий содержащиеся в объекте Dataset точки данных1. В примере 3.17 мы создадим для DataLoader адаптер в виде функции generate_batches() — генератора для удобного выбора (switch) данных между CPU и GPU.

Пример 3.17. Генерация мини-пакетов на основе набора данных

def generate_batches(dataset, batch_size, shuffle=True,
                     drop_last=True, device="cpu"):
    """
    Функция-генератор — адаптер для объекта DataLoader фреймворка PyTorch.
    Гарантирует размещение всех тензоров на нужном устройстве.
    """
    dataloader = DataLoader(dataset=dataset, batch_size=batch_size,
                            shuffle=shuffle, drop_last=drop_last)

1 Напомним, что для наследования класса Dataset PyTorch разработчик должен реализовать методы __getitem__() и __len__(), благодаря чему класс DataLoader сможет пройти в цикле по набору данных путем итерации по индексам из этого набора.