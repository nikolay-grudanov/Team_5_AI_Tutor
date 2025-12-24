---
source_image: page_140.png
page_number: 140
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 8.79
tokens: 7038
characters: 570
timestamp: 2025-12-24T02:24:32.213617
finish_reason: stop
---

Возвращает:
    final_embeddings (numpy.ndarray): матрица вложений
"""
word_to_idx, glove_embeddings = load_glove_from_file(glove_filepath)
embedding_size = glove_embeddings.shape[1]
final_embeddings = np.zeros((len(words), embedding_size))

for i, word in enumerate(words):
    if word in word_to_idx:
        final_embeddings[i, :] = glove_embeddings[word_to_idx[word]]
    else:
        embedding_i = torch.ones(1, embedding_size)
        torch.nn.init.xavier_uniform_(embedding_i)
        final_embeddings[i, :] = embedding_i

return final_embeddings

NewsClassifier