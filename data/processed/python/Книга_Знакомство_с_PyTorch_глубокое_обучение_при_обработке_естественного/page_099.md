---
source_image: page_099.png
page_number: 99
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.87
tokens: 7475
characters: 2008
timestamp: 2025-12-24T02:23:36.579613
finish_reason: stop
---

Пример 4.8. Гиперпараметры и настройки программы для классификатора фамилий на основе MLP

args = Namespace(
    # Информация о данных и путях
    surname_csv="data/surnames/surnames_with_splits.csv",
    vectorizer_file="vectorizer.json",
    model_state_file="model.pth",
    save_dir="model_storage/ch4/surname_mlp",
    # Гиперпараметры модели
    hidden_dim=300
    # Гиперпараметры обучения
    seed=1337,
    num_epochs=100,
    early_stopping_criteria=5,
    learning_rate=0.001,
    batch_size=64,
    # Настройки времени выполнения не приводятся для экономии места
)

Наиболее заметное различие в обучении относится к выходным данным модели и используемой функции потерь. В этом примере выходные данные представляют собой вектор многоклассовых предсказаний, который можно преобразовать в вероятности. Для таких выходных данных подходят только функции потерь CrossEntropyLoss() и NLLLoss(). Воспользуемся первой.

В примере 4.9 приведено создание экземпляров набора данных, модели, функции потерь и оптимизатора. Они практически идентичны тем, что описывались в примере из главы 3. Собственно, это справедливо практически для всех примеров в последующих главах.

Пример 4.9. Создание экземпляров набора данных, модели, функции потерь и оптимизатора

dataset = SurnameDataset.load_dataset_and_make_vectorizer(args.surname_csv)
vectorizer = dataset.get_vectorizer()

classifier = SurnameClassifier(input_dim=len(vectorizer.surname_vocab),
    hidden_dim=args.hidden_dim,
    output_dim=len(vectorizer.nationality_vocab))

classifier = classifier.to(args.device)

loss_func = nn.CrossEntropyLoss(dataset.class_weights)
optimizer = optim.Adam(classifier.parameters(), lr=args.learning_rate)

Цикл обучения

Цикл обучения для этого примера практически идентичен описанному в пункте «Цикл обучения» на с. 92, за исключением названий переменных. А именно, из примера 4.10 видно, что для получения данных из batch_dict используются другие ключи. Помимо этого незначительного различия, функциональность цикла