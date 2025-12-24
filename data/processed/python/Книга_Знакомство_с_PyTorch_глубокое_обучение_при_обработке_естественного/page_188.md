---
source_image: page_188.png
page_number: 188
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.18
tokens: 7548
characters: 2701
timestamp: 2025-12-24T02:26:08.670371
finish_reason: stop
---

модели кодировщик сначала отображает каждую из исходных последовательностей в последовательность векторов состояния с помощью bi-GRU (см. раздел «Захватываем больше информации из последовательности: двунаправленные рекуррентные модели» на с. 207). Далее декодировщик использует скрытые состояния кодировщика в качестве своего начального скрытого состояния и применяет механизм внимания (см. раздел «Захватываем больше информации из последовательности: внимание» на с. 209), выбирая различную информацию из исходной последовательности для генерации выходной последовательности. В оставшейся части подраздела мы рассмотрим этот процесс во всех подробностях.

Пример 8.4. Класс NMTModel инкапсулирует кодировщик и декодировщик в одном методе forward() и согласовывает их работу

class NMTModel(nn.Module):
    """ Модель для нейронного машинного перевода """
    def __init__(self, source_vocab_size, source_embedding_size,
                 target_vocab_size, target_embedding_size, encoding_size,
                 target_bos_index):
        """
        Аргументы:
            source_vocab_size (int): число уникальных слов в исходном языке
            source_embedding_size (int): размер исходных векторов вложений
            target_vocab_size (int): число уникальных слов в целевом языке
            target_embedding_size (int): размер целевых векторов вложений
            encoding_size (int): размер RNN кодировщика
            target_bos_index (int): индекс токена BEGIN-OF-SEQUENCE
        """
        super(NMTModel, self).__init__()
        self.encoder = NMTEncoder(num_embeddings=source_vocab_size,
                                  embedding_size=source_embedding_size,
                                  rnn_hidden_size=encoding_size)
        decoding_size = encoding_size * 2
        self.decoder = NMTDecoder(num_embeddings=target_vocab_size,
                                  embedding_size=target_embedding_size,
                                  rnn_hidden_size=decoding_size,
                                  bos_index=target_bos_index)

    def forward(self, x_source, x_source_lengths, target_sequence):
        """ Прямой проход модели

        Аргументы:
            x_source (torch.Tensor): тензор исходных текстовых данных
                Значение x_source.shape должно быть (batch, vectorizer.max_source_length)
            x_source_lengths torch.Tensor): длины последовательностей в x_source
            target_sequence (torch.Tensor): тензор целевых текстовых данных
        Возвращает:
            decoded_states (torch.Tensor): векторы предсказаний на каждом из выходных шагов
        """
        encoder_state, final_hidden_states = self.encoder(x_source, x_source_lengths)