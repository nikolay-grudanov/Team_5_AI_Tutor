---
source_image: page_076.png
page_number: 76
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.35
tokens: 7430
characters: 1973
timestamp: 2025-12-24T02:23:07.053829
finish_reason: stop
---

вызове функции generate_batches() в основном цикле обучения, так что данные и модель будут располагаться на одном устройстве.

Осталось создать еще два компонента — функцию потерь и оптимизатор. В этом примере используется функция потерь BCEWithLogitsLoss() (как упоминалось в подразделе «Классификатор-перцептрон» на с. 88, наиболее подходящей функцией потерь для бинарной классификации является бинарная функция потерь на основе перекрестной энтропии, и с точки зрения численной устойчивости лучше использовать функцию BCEWithLogitsLoss() и модель, в которой к выходным значениям не применяется сигма-функция, чем функцию BCELoss() и модель, в которой к выходным значениям сигма-функция применяется). Мы также используем оптимизатор Adam. В целом оптимизатор Adam, по сравнению с другими, является вполне конкурентоспособным, и на момент написания книги отсутствуют убедительные аргументы, по которым предпочтительнее какой-то другой оптимизатор. Мы призываем вас проверить этот факт самостоятельно, попробовав другие оптимизаторы и сравнив их эффективность.

Пример 3.20. Создание набора данных, модели, функции потерь, оптимизатора и состояния обучения

import torch.optim as optim

def make_train_state(args):
    return {'epoch_index': 0,
            'train_loss': [],
            'train_acc': [],
            'val_loss': [],
            'val_acc': [],
            'test_loss': -1,
            'test_acc': -1}

train_state = make_train_state(args)

if not torch.cuda.is_available():
    args.cuda = False
args.device = torch.device("cuda" if args.cuda else "cpu")

# Набор данных и векторизатор
dataset = ReviewDataset.load_dataset_and_make_vectorizer(args.review_csv)
vectorizer = dataset.get_vectorizer()

# Модель
classifier = ReviewClassifier(num_features=len(vectorizer.review_vocab))
classifier = classifier.to(args.device)

# Функция потерь и оптимизатор
loss_func = nn.BCEWithLogitsLoss()
optimizer = optim.Adam(classifier.parameters(), lr=args.learning_rate)