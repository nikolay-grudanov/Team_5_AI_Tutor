---
source_image: page_170.png
page_number: 170
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.13
tokens: 7246
characters: 1243
timestamp: 2025-12-24T02:25:26.149775
finish_reason: stop
---

Пример 7.11. Выборка из контекстно обусловленной модели SurnameGenerationModel (показаны не все результаты)

Input[0]
for index in range(len(vectorizer.nationality_vocab)):
    nationality = vectorizer.nationality_vocab.lookup_index(index)
    print("Sampled for {}: ".format(nationality))
    sampled_indices = sample_from_model(model=conditioned_model,
                                         vectorizer=vectorizer,
                                         nationalities=[index] * 3,
                                         temperature=0.7)
    for sampled_surname in decode_samples(sampled_indices, vectorizer):
        print("-   " + sampled_surname)

Output[0]
Sampled for Arabic:
- Khatso
- Salbwa
- Gadi
Sampled for Chinese:
- Lie
- Puh
- Pian
Sampled for German:
- Lenger
- Schanger
- Schumper
Sampled for Irish:
- Mcochin
- Corran
- O'Baintin
Sampled for Russian:
- Mahghatsunkov
- Juhin
- Karkovin
Sampled for Vietnamese:
- Lo
- Tham
- Tou

Полезные советы по обучению моделей последовательностей

Обучение моделей последовательностей — непростая задача, в процессе которой возникает множество проблем. В этом разделе мы приведем пару советов и опишем несколько приемов, которые пригодились нам в работе и встречались в литературе.