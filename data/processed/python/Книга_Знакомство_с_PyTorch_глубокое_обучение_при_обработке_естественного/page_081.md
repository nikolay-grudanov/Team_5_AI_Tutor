---
source_image: page_081.png
page_number: 81
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.23
tokens: 7309
characters: 1576
timestamp: 2025-12-24T02:23:11.356077
finish_reason: stop
---

# вычисление точности
acc_batch = compute_accuracy(y_pred, batch_dict['y_target'])
running_acc += (acc_batch - running_acc) / (batch_index + 1)

train_state['test_loss'] = running_loss
train_state['test_acc'] = running_acc

print("Test loss: {:.3f}".format(train_state['test_loss']))
print("Test Accuracy: {:.2f}".format(train_state['test_acc']))

Test loss: 0.297
Test Accuracy: 90.55

Вывод и классификация новых точек данных

Еще один метод оценки эффективности модели — вывод на основе новых данных и анализ того, работает ли она. Рассмотрим пример 3.23.

Пример 3.23. Вывод в консоль предсказаний для образца обзора

def predict_rating(review, classifier, vectorizer,
    decision_threshold=0.5):
    """ Предсказание рейтинга обзора

    Аргументы:
        review (str): текст обзора
        classifier (ReviewClassifier): обученная модель
        vectorizer (ReviewVectorizer): соответствующий векторизатор
        decision_threshold (float): численная граница, разделяющая различные классы рейтинга
    """
    review = preprocess_text(review)
    vectorized_review = torch.tensor(vectorizer.vectorize(review))
    result = classifier(vectorized_review.view(1, -1))

    probability_value = F.sigmoid(result).item()

    index = 1
    if probability_value < decision_threshold:
        index = 0

    return vectorizer.rating_vocab.lookup_index(index)

    test_review = "this is a pretty awesome book"
    prediction = predict_rating(test_review, classifier, vectorizer)
    print("{} -> {}".format(test_review, prediction))

this is a pretty awesome book -> positive