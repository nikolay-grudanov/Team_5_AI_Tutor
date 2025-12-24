---
source_image: page_169.png
page_number: 169
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.76
tokens: 7567
characters: 2410
timestamp: 2025-12-24T02:25:43.709214
finish_reason: stop
---

Для контекстно обусловленной SurnameGenerationModel мы модифицируем функцию sample_from_model() так, чтобы она принимала на входе список индексов национальностей вместо количества выборок. В примере 7.10 эта модифицированная функция на основе индексов и вложений национальностей формирует начальное скрытое состояние GRU. Дальнейшая процедура выборки выглядит точно так же, как и в контекстно не обусловленной модели.

Пример 7.10. Выборка из модели последовательности

def sample_from_model(model, vectorizer, nationalities, sample_size=20, temperature=1.0):
    """ Выборка последовательности индексов из модели

    Аргументы:
        model (SurnameGenerationModel): обученная модель
        vectorizer (SurnameVectorizer): соответствующий векторизатор
        nationalities (list): список соответствующих национальностям целых чисел
        sample_size (int): максимальная длина выборки
        temperature (float): подчеркивает или сворачивает распределение
            При 0.0 < temperature < 1.0 максимумы заостряются
            temperature > 1.0 делает распределение более равномерным
    Возвращает:
        indices (torch.Tensor): матрица индексов
            форма: (num_samples, sample_size)
    """
    num_samples = len(nationalities)
    begin_seq_index = [vectorizer.char_vocab.begin_seq_index for _ in range(num_samples)]
    begin_seq_index = torch.tensor(begin_seq_index, dtype=torch.int64).unsqueeze(dim=1)
    indices = [begin_seq_index]
    nationality_indices = torch.tensor(nationalities, dtype=torch.int64).unsqueeze(dim=0)
    h_t = model.nation_emb(nationality_indices)

    for time_step in range(sample_size):
        x_t = indices[time_step]
        x_emb_t = model.char_emb(x_t)
        rnn_out_t, h_t = model.rnn(x_emb_t, h_t)
        prediction_vector = model.fc(rnn_out_t.squeeze(dim=1))
        probability_vector = F.softmax(prediction_vector / temperature, dim=1)
        indices.append(torch.multinomial(probability_vector, num_samples=1))
    indices = torch.stack(indices).squeeze().permute(1, 0)
    return indices

Выборка с использованием контекстного вектора позволяет влиять на генерируемые выходные данные. В примере 7.11 мы проходим в цикле по индексам национальностей и производим выборку из каждого. Для экономии места мы покажем лишь небольшую часть результатов. Из них видно, что модель действительно улавливает некоторые орфографические особенности фамилий.