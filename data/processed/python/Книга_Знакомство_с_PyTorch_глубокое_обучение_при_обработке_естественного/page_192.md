---
source_image: page_192.png
page_number: 192
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.93
tokens: 7538
characters: 2627
timestamp: 2025-12-24T02:26:11.795917
finish_reason: stop
---

Пример 8.7. Класс NMTDecoder служит для формирования целевого предложения из кодированного исходного предложения

class NMTDecoder(nn.Module):
    def __init__(self, num_embeddings, embedding_size, rnn_hidden_size,
                 bos_index):
        """
        Аргументы:
            num_embeddings (int): число вложений; также число уникальных слов в целевом словаре
            embedding_size (int): размер вектора вложения
            rnn_hidden_size (int): размер скрытого состояния RNN
            bos_index(int): индекс BEGIN-OF-SEQUENCE
        """
        super(NMTDecoder, self).__init__()
        self._rnn_hidden_size = rnn_hidden_size
        self.target_embedding = nn.Embedding(num_embeddings=num_embeddings,
                                             embedding_dim=embedding_size,
                                             padding_idx=0)
        self.gru_cell = nn.GRUCell(embedding_size + rnn_hidden_size,
                                   rnn_hidden_size)
        self.hidden_map = nn.Linear(rnn_hidden_size, rnn_hidden_size)
        self.classifier = nn.Linear(rnn_hidden_size * 2, num_embeddings)
        self.bos_index = bos_index

    def _init_indices(self, batch_size):
        """ возвращает вектор индексов BEGIN-OF-SEQUENCE """
        return torch.ones(batch_size, dtype=torch.int64) * self.bos_index

    def _init_context_vectors(self, batch_size):
        """ возвращает нулевой вектор для инициализации контекста """
        return torch.zeros(batch_size, self._rnn_hidden_size)

    def forward(self, encoder_state, initial_hidden_state, target_sequence):
        """ Прямой проход модели
        Аргументы:
            encoder_state (torch.Tensor): выходные данные NMTEncoder
            initial_hidden_state (torch.Tensor): последнее скрытое состояние в NMTEncoder
            target_sequence (torch.Tensor): целевой тензор текстовых данных
            sample_probability (float): параметр плановой выборки
                вероятность использования предсказаний модели
                на каждом шаге декодировщика
        Возвращает:
            output_vectors (torch.Tensor): векторы предсказаний
                на каждом из шагов
        """
        # Здесь мы предполагаем, что пакет находится в первом измерении
        # Входные данные: (Пакет, Последовательность)
        # Мы хотим пройти в цикле по последовательности и переставить
        # измерения местами, чтобы получилось (Последовательность, Пакет)
        target_sequence = target_sequence.permute(1, 0)

        # Используем в качестве начального скрытого состояния
        # переданное скрытое состояние кодировщика