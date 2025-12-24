---
source_image: page_102.png
page_number: 102
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.49
tokens: 7567
characters: 2185
timestamp: 2025-12-24T02:23:51.624537
finish_reason: stop
---

Извлечение k наилучших предсказаний для новой фамилии

Часто бывает полезно взглянуть не только на одно лучшее предсказание. Например, в NLP стандартной практикой считается извлечение \( k \) наилучших предсказаний и повторное ранжирование их с помощью другой модели. Для получения этих предсказаний во фреймворке PyTorch есть удобная функция torch.topk() (пример 4.12).

Пример 4.12. Предсказание к лучше всего подходящих национальностей

def predict_topk_nationality(name, classifier, vectorizer, k=5):
    vectorized_name = vectorizer.vectorize(name)
    vectorized_name = torch.tensor(vectorized_name).view(1, -1)
    prediction_vector = classifier(vectorized_name, apply_softmax=True)
    probability_values, indices = torch.topk(prediction_vector, k=k)

    # Возвращаемый размер 1,k
    probability_values = probability_values.detach().numpy()[0]
    indices = indices.detach().numpy()[0]

    results = []
    for prob_value, index in zip(probability_values, indices):
        nationality = vectorizer.nationality_vocab.lookup_index(index)
        results.append({'nationality': nationality,
                        'probability': prob_value})

    return results

Регуляризация многослойных перцептронов: регуляризация весов и структурная регуляризация

В главе 3 мы объяснили, почему регуляризация является решением проблемы переобучения, и изучили два важных типа регуляризации весов — L1 и L2. Эти методы регуляризации весов применимы как к MLP, так и к сверточным нейронным сетям, которые мы рассмотрим в следующем разделе. Помимо регуляризации весов, для глубоких моделей (то есть моделей из нескольких слоев), таких как обсуждавшиеся в этой главе упреждающие сети, важнейшее значение имеет подход структурной регуляризации под названием dropout (dropout).

Попросту говоря, во время обучения дропаут отбрасывает на вероятностной основе связи между элементами из двух смежных слоев. В чем польза такого подхода? Начнем с интуитивно понятного (юмористического) объяснения Стивена Мерити (Stephen Merity):

Дропаут, попросту говоря, означает, что если у вас хорошо

1 Это определение взято из весьма забавной первоапрельской «статьи» Стивена Мерити (http://bit.ly/2Cq1FJR).