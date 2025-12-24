---
source_image: page_163.png
page_number: 163
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.39
tokens: 7444
characters: 2060
timestamp: 2025-12-24T02:25:26.654597
finish_reason: stop
---

rnn_hidden_size, batch_first=True, padding_idx=0,
dropout_p=0.5):
"""
Аргументы:
    char_embedding_size (int): размер вложений символов
    char_vocab_size (int): количество символов для создания вложений
    rnn_hidden_size (int): размер скрытого состояния RNN
    batch_first (bool): указывает, будут ли в нулевом измерении входных тензоров располагаться данные пакета или последовательности
    padding_idx (int): индекс для дополнения тензора;
        см. torch.nn.Embedding
    dropout_p (float): вероятность обнуления при использовании метода дропаута
"""
super(SurnameGenerationModel, self).__init__()

self.char_emb = nn.Embedding(num_embeddings=char_vocab_size,
                            embedding_dim=char_embedding_size,
                            padding_idx=padding_idx)
self.rnn = nn.GRU(input_size=char_embedding_size,
                  hidden_size=rnn_hidden_size,
                  batch_first=batch_first)
self.fc = nn.Linear(in_features=rnn_hidden_size,
                    out_features=char_vocab_size)
self._dropout_p = dropout_p

def forward(self, x_in, apply_softmax=False):
    """ Прямой проход модели

    Аргументы:
        x_in (torch.Tensor): тензор входных данных
            Значение x_in.shape должно быть (batch, input_dim)
        apply_softmax (bool): флаг для многомерной логистической функции активации во время обучения должен равняться 0
    Возвращает:
        итоговый тензор. Значение tensor.shape должно быть (batch, output_dim)
    """
    x_embedded = self.char_emb(x_in)
    y_out, _ = self.rnn(x_embedded)
    batch_size, seq_size, feat_size = y_out.shape
    y_out = y_out.contiguous().view(batch_size * seq_size, feat_size)
    y_out = self.fc(F.dropout(y_out, p=self._dropout_p))

    if apply_softmax:
        y_out = F.softmax(y_out, dim=1)

    new_feat_size = y_out.shape[-1]
    y_out = y_out.view(batch_size, seq_size, new_feat_size)

    return y_out

Основное различие между задачами классификации последовательностей из главы 6 и задачами предсказания последовательностей из этой главы — обработка