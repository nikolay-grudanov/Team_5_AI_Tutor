---
source_image: page_189.png
page_number: 189
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.74
tokens: 7526
characters: 2318
timestamp: 2025-12-24T02:26:08.390238
finish_reason: stop
---

decoded_states = self.decoder(encoder_state=encoder_state,
    initial_hidden_state=final_hidden_states,
    target_sequence=target_sequence)
return decoded_states

Пример 8.5. Кодировщик выполняет вложения исходных слов и извлекает признаки с помощью bi-GRU

class NMTEncoder(nn.Module):
    def __init__(self, num_embeddings, embedding_size, rnn_hidden_size):
        """
        Аргументы:
            num_embeddings (int): размер исходного словаря
            embedding_size (int): размер векторов вложений
            rnn_hidden_size (int): размер векторов скрытого состояния RNN
        """
        super(NMTEncoder, self).__init__()

        self.source_embedding = nn.Embedding(num_embeddings, embedding_size,
            padding_idx=0)
        self.birnn = nn.GRU(embedding_size, rnn_hidden_size, bidirectional=True,
            batch_first=True)

    def forward(self, x_source, x_lengths):
        """
        Прямой проход модели

        Аргументы:
            x_source (torch.Tensor): тензор входных данных
                Значение x_source.shape равно (batch, seq_size)
            x_lengths (torch.Tensor): вектор длин всех элементов пакета
        Возвращает:
            кортеж: x_unpacked (torch.Tensor), x_birnn_h (torch.Tensor)
                x_unpacked.shape = (batch, seq_size, rnn_hidden_size * 2)
                x_birnn_h.shape = (batch, rnn_hidden_size * 2)
        """
        x_embedded = self.source_embedding(x_source)
        # создает PackedSequence; x_packed.data.shape=(number_items,
        #                 embedding_size)
        x_lengths = x_lengths.detach().cpu().numpy()
        x_packed = pack_padded_sequence(x_embedded, x_lengths,
            batch_first=True)

        # x_birnn_h.shape = (num_rnn, batch_size, feature_size)
        x_birnn_out, x_birnn_h = self.birnn(x_packed)
        # перестановка в (batch_size, num_rnn, feature_size)
        x_birnn_h = x_birnn_h.permute(1, 0, 2)
        # свертываем признаки; изменяем форму
        # на (batch_size, num_rnn * feature_size)
        # (напомним: -1 охватывает оставшиеся позиции,
        # свертывая два скрытых вектора RNN в 1)
        x_birnn_h = x_birnn_h.contiguous().view(x_birnn_h.size(0), -1)

        x_unpacked, _ = pad_packed_sequence(x_birnn_out, batch_first=True)
        return x_unpacked, x_birnn_h