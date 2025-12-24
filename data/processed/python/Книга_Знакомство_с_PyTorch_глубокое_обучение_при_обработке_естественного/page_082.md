---
source_image: page_082.png
page_number: 82
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.58
tokens: 7253
characters: 1279
timestamp: 2025-12-24T02:23:11.356155
finish_reason: stop
---

Просмотр весов модели

Наконец, последний способ выяснить, хорошо ли работает модель после окончания обучения, — просмотреть веса модели и принять решение, правильно ли они выглядят. Как демонстрирует пример 3.24, в случае перцептрона и свернутого унитарного кодирования эта задача достаточно проста, поскольку каждому весу модели соответствует ровно одно слово из словаря.

Пример 3.24. Просматриваем полученные в результате обучения модели веса

Input[0]
# Сортировка весов
fc1_weights = classifier.fc1.weight.detach()[0]
_, indices = torch.sort(fc1_weights, dim=0, descending=True)
indices = indices.numpy().tolist()

# Топ-20 позитивных слов
print("Influential words in Positive Reviews:")
print("-------------------------------")
for i in range(20):
    print(vectorizer.review_vocab.lookup_index(indices[i]))

Output[0]
Influential words in Positive Reviews:
-------------------------------
great
awesome
amazing
love
friendly
delicious
best
excellent
definitely
perfect
fantastic
wonderful
vegas
favorite
loved
yummy
fresh
reasonable
always
recommend

Input[1]
# Топ-20 негативных слов
print("Influential words in Negative Reviews:")
print("-------------------------------")
indices.reverse()
for i in range(20):
    print(vectorizer.review_vocab.lookup_index(indices[i]))