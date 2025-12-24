---
source_image: page_166.png
page_number: 166
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.56
tokens: 7592
characters: 2284
timestamp: 2025-12-24T02:25:42.432080
finish_reason: stop
---

if len(y_pred.size()) == 3:
    y_pred = y_pred.contiguous().view(-1, y_pred.size(2))
if len(y_true.size()) == 2:
    y_true = y_true.contiguous().view(-1)
return y_pred, y_true

def sequence_loss(y_pred, y_true, mask_index):
    y_pred, y_true = normalize_sizes(y_pred, y_true)
    return F.cross_entropy(y_pred, y_true, ignore_index=mask_index)

На основе этой модифицированной функции вычисления потерь создадим процедуру обучения, аналогичную той, что приводилась во всех прочих примерах книги. Она начинается с прохода в цикле по обучающему набору данных, по одному мини-пакету за раз. Выходные данные модели вычисляются на основе входных для каждого из мини-пакетов. А поскольку на каждом временнóм шаге выполняются предсказания, выходные данные модели представляют собой трехмерный тензор. С помощью вышеописанного метода sequence_loss и оптимизатора вычисляется сигнал рассогласования для предсказаний модели, на основе которого обновляются ее параметры.

Большая часть гиперпараметров модели определяется размером символьного словаря. Он равен количеству дискретных токенов, потенциально наблюдаемых на входе модели, и количеству классов в выходной классификации на каждом временнóм шаге. Кроме этого, к гиперпараметрам модели относятся размер вложений символов и размер внутреннего скрытого состояния RNN. Эти гиперпараметры и параметры обучения приведены в примере 7.6.

Пример 7.6. Гиперпараметры для генерации фамилий

args = Namespace(
    # Информация о данных и путях
    surname_csv="data/surnames/surnames_with_splits.csv",
    vectorizer_file="vectorizer.json",
    model_state_file="model.pth",
    save_dir="model_storage/ch7/model1_unconditioned_surname_generation",
    # или: save_dir="model_storage/ch7/model2_conditioned_surname_generation",
    # Гиперпараметры модели
    char_embedding_size=32,
    rnn_hidden_size=32,
    # Гиперпараметры обучения
    seed=1337,
    learning_rate=0.001,
    batch_size=128,
    num_epochs=100,
    early_stopping_criteria=5,
    # Настройки времени выполнения не приводятся для экономии места
)

И хотя мера эффективности модели — точность предсказаний в пересчете на символ, в данном примере лучше будет выполнить качественную оценку, внимательно просмотрев генерируемые моделью фамилии. Напишем код для прохода в новом