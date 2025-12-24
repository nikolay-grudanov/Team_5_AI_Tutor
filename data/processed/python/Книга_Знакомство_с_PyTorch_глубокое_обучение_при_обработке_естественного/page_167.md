---
source_image: page_167.png
page_number: 167
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.24
tokens: 7601
characters: 2543
timestamp: 2025-12-24T02:25:42.603438
finish_reason: stop
---

цикле по модифицированной версии шагов из метода forward() и вычисления предсказаний на каждом из временных шагов, которые затем послужат входными данными для следующего временного шага. Соответствующий код показан в примере 7.7. На выходе модели на каждом временном шаге получается вектор предсказаний, который преобразуется в распределение вероятности с помощью многомерной логистической функции. С этим распределением вероятности мы можем воспользоваться функцией выборки torch.multinomial(), выбирающей индексы с пропорциональной их вероятности частотой. Выборка представляет собой стохастическую процедуру, результаты которой каждый раз новые.

Пример 7.7. Выборка из контекстно не обусловленной модели генерации

def sample_from_model(model, vectorizer, num_samples=1, sample_size=20, temperature=1.0):
    """ Выборка последовательности индексов из модели

    Аргументы:
        model (SurnameGenerationModel): обученная модель
        vectorizer (SurnameVectorizer): соответствующий векторизатор
        num_samples (int): число выборок
        sample_size (int): максимальная длина выборки
        temperature (float): подчеркивает или сворачивает распределение
            При 0.0 < temperature < 1.0 максимумы заостряются
            temperature > 1.0 делает распределение более равномерным
    Возвращает:
        indices (torch.Tensor): матрица индексов
            форма: (num_samples, sample_size)
    """
    begin_seq_index = [vectorizer.char_vocab.begin_seq_index for _ in range(num_samples)]
    begin_seq_index = torch.tensor(begin_seq_index, dtype=torch.int64).unsqueeze(dim=1)
    indices = [begin_seq_index]
    h_t = None

    for time_step in range(sample_size):
        x_t = indices[time_step]
        x_emb_t = model.char_emb(x_t)
        rnn_out_t, h_t = model.rnn(x_emb_t, h_t)
        prediction_vector = model.fc(rnn_out_t.squeeze(dim=1))
        probability_vector = F.softmax(prediction_vector / temperature, dim=1)
        indices.append(torch.multinomial(probability_vector, num_samples=1))
    indices = torch.stack(indices).squeeze().permute(1, 0)
    return indices

Необходимо преобразовать полученные из функции sample_from_model выборки индексов в строковое значение, удобное для чтения человеком. Как демонстрирует пример 7.8, мы воспользуемся для этого SequenceVocabulary, который служил для векторизации фамилий. При создании строкового значения станем использовать только индексы, предшествующие индексу END-OF-SEQUENCE. А значит, модель теперь будет «понимать», где должны заканчиваться фамилии.