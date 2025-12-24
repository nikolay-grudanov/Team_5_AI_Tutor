---
source_image: page_197.png
page_number: 197
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.39
tokens: 7595
characters: 2653
timestamp: 2025-12-24T02:26:30.685699
finish_reason: stop
---

Наконец, при условии if use_sample выполняется сама выборка. В примере 8.9 закомментированные строки демонстрируют использование предсказания максимума, а не закомментированные строки демонстрируют возможность выборки индексов пропорционально их вероятностям.

Пример 8.9. Декодировщик со встроенной процедурой выборки (выделено жирным шрифтом)
class NMTDecoder(nn.Module):
    def __init__(self, num_embeddings, embedding_size, rnn_size, bos_index):
        super(NMTDecoder, self).__init__()
        # ... остальной код инициализации ...

        # задается произвольно; подойдет любая небольшая константа
        self._sampling_temperature = 3

    def forward(self, encoder_state, initial_hidden_state, target_sequence,
                sample_probability=0.0):
        if target_sequence is None:
            sample_probability = 1.0
        else:
            # Здесь мы предполагаем, что пакет находится в первом измерении
            # Входные данные: (Пакет, Последовательность)
            # Мы хотим пройти в цикле по последовательности и переставить
            # измерения местами, чтобы получить (Последовательность, Пакет)

            target_sequence = target_sequence.permute(1, 0)
            output_sequence_size = target_sequence.size(0)

            # ... с предыдущей реализации ничего не поменялось

            output_sequence_size = target_sequence.size(0)
            for i in range(output_sequence_size):
                # новый код: вспомогательное булево значение
                # и "учитель" y_t_index
                use_sample = np.random.random() < sample_probability
                if not use_sample:
                    y_t_index = target_sequence[i]

                # Шаг 1: выполняем вложение слова и его конкатенацию
                # с предыдущим контекстом
                # ... код опущен для экономии места
                # Шаг 2: выполняем шаг GRU, получая новый скрытый вектор
                # ... код опущен для экономии места
                # Шаг 3: обращаем внимание на состояние кодировщика,
                # используя текущий скрытый вектор
                # ... код опущен для экономии места
                # Шаг 4: на основе текущего скрытого вектора
                # и вектора контекста генерируем предсказание
                # относительно следующего слова
                prediction_vector = torch.cat((context_vectors, h_t), dim=1)
                score_for_y_t_index = self.classifier(prediction_vector)
                # новый код: если булево значение истинно, производим выборку
                if use_sample:
                    # температура выборки обеспечивает заострение максимумов