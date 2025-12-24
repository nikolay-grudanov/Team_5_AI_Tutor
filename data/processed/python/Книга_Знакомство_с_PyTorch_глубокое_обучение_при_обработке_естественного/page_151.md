---
source_image: page_151.png
page_number: 151
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.54
tokens: 7434
characters: 1844
timestamp: 2025-12-24T02:25:06.062932
finish_reason: stop
---

используемые для поиска завершающих векторов последовательностей
apply_softmax (bool): флаг для многомерной логистической функции активации. При использовании функции потерь на основе перекрестной энтропии должен равняться false
Возвращает:
    out (torch.Tensor); `out.shape = (batch, num_classes)`
"""
    x_embedded = self.emb(x_in)
    y_out = self.rnn(x_embedded)

    if x_lengths is not None:
        y_out = column_gather(y_out, x_lengths)
    else:
        y_out = y_out[:, -1, :]

    y_out = F.dropout(y_out, 0.5)
    y_out = F.relu(self.fc1(y_out))
    y_out = F.dropout(y_out, 0.5)
    y_out = self.fc2(y_out)

    if apply_softmax:
        y_out = F.softmax(y_out, dim=1)

    return y_out

Как вы увидите, для функции forward() требуются длины последовательностей. Они используются для извлечения завершающих векторов каждой из последовательностей в тензоре, возвращаемых из RNN функцией column_gather() (пример 6.5). Она проходит в цикле по индексам строк пакета и извлекает вектор, находящийся на позиции, которая соответствует длине последовательности.

Пример 6.5. Извлечение завершающего выходного вектора каждой из последовательностей с помощью метода column_gather()
def column_gather(y_out, x_lengths):
    """ Извлекает определенный вектор из каждой точки данных пакета в `y_out`.
    Аргументы:
        y_out (torch.FloatTensor, torch.cuda.FloatTensor)
            shape: (batch, sequence, feature)
        x_lengths (torch.LongTensor, torch.cuda.LongTensor)
            shape: (batch,)
    Возвращает:
        y_out (torch.FloatTensor, torch.cuda.FloatTensor)
            shape: (batch, feature)
    """
    x_lengths = x_lengths.long().detach().cpu().numpy() - 1

    out = []
    for batch_index, column_index in enumerate(x_lengths):
        out.append(y_out[batch_index, column_index])

    return torch.stack(out)