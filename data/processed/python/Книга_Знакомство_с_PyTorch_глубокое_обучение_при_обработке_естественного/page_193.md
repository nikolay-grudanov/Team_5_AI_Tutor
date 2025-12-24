---
source_image: page_193.png
page_number: 193
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.64
tokens: 7507
characters: 2083
timestamp: 2025-12-24T02:26:15.977469
finish_reason: stop
---

h_t = self.hidden_map(initial_hidden_state)

batch_size = encoder_state.size(0)
# Инициализируем векторы контекста нулями
context_vectors = self._init_context_vectors(batch_size)
# Инициализируем первое y_t слово как BOS [BEGIN-OF-SEQUENCE]
y_t_index = self._init_indices(batch_size)

h_t = h_t.to(encoder_state.device)
y_t_index = y_t_index.to(encoder_state.device)
context_vectors = context_vectors.to(encoder_state.device)

output_vectors = []
# Перемещаем из GPU все закэшированные тензоры и сохраняем
# для последующего анализа
self._cached_p_attn = []
self._cached_ht = []
self._cached_decoder_state = encoder_state.cpu().detach().numpy()

output_sequence_size = target_sequence.size(0)
for i in range(output_sequence_size):

    # Шаг 1: выполняем вложение слова и его конкатенацию
    # с предыдущим контекстом
    y_input_vector = self.target_embedding(target_sequence[i])
    rnn_input = torch.cat([y_input_vector, context_vectors], dim=1)

    # Шаг 2: выполняем шаг GRU, получая новый скрытый вектор
    h_t = self.gru_cell(rnn_input, h_t)
    self._cached_ht.append(h_t.cpu().data.numpy())

    # Шаг 3: обращаем внимание на состояние кодировщика,
    # используя текущий скрытый вектор
    context_vectors, p_attn, _ = \
        verbose_attention(encoder_state_vectors=encoder_state,
                          query_vector=h_t)

    # вспомогательный: кэшируем вероятности внимания
    # для визуализации
    self._cached_p_attn.append(p_attn.cpu().detach().numpy())

    # Шаг 4: на основе текущего скрытого вектора
    # и вектора контекста генерируем предсказание
    # относительно следующего слова
    prediction_vector = torch.cat((context_vectors, h_t), dim=1)
    score_for_y_t_index = self.classifier(prediction_vector)

    # вспомогательный: получаем показатели эффективности
    # предсказания
    output_vectors.append(score_for_y_t_index)

После создания кодировщиком векторов состояния с помощью bi-GRU и упаковки-распаковки декодировщик проходит в цикле по временным шагам и генерирует выходную последовательность. Функционально этот цикл очень похож на