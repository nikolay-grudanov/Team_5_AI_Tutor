---
source_image: page_191.png
page_number: 191
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.84
tokens: 7495
characters: 1699
timestamp: 2025-12-24T02:26:03.603776
finish_reason: stop
---

Output[0]
Type: torch.FloatTensor
Shape/size: torch.Size([3, 4])
Values:
tensor([[1., 2., 3., 4.],
        [5., 6., 7., 0.],
        [8., 0., 0., 0.]])
Input[1]
lengths = [4, 3, 1]
packed_tensor = pack_padded_sequence(padded_tensor, lengths, batch_first=True)
packed_tensor
Output[1]
PackedSequence(data=tensor([1., 5., 8., 2., 6., 3., 7., 4.]), batch_sizes=tensor([3, 2, 2, 1]))
Input[2]
unpacked_tensor, unpacked_lengths = \
    pad_packed_sequence(packed_tensor, batch_first=True)
describe(unpacked_tensor)
describe(unpacked_lengths)
Output[2]
Type: torch.FloatTensor
Shape/size: torch.Size([3, 4])
Values:
tensor([[1., 2., 3., 4.],
        [5., 6., 7., 0.],
        [8., 0., 0., 0.]])
Type: torch.LongTensor
Shape/size: torch.Size([3])
Values:
tensor([4, 3, 1])

Как описано в предыдущем подразделе, сортировка производится при генерации мини-пакетов. Далее, как показано в примере 8.5, вызывается функция pack_padded_sequence() фреймворка PyTorch и ей передаются вложенные последовательности, их длины и булев флаг, указывающий, что первое измерение содержит пакет. Эта функция возвращает объект PackedSequence, который служит входными данными bi-GRU с целью создания векторов состояния для расположенного далее по конвейеру декодировщика. Результаты работы bi-GRU распаковываются в полный тензор с помощью еще одного булева флага, указывающего, что пакет находится в первом измерении. В результате операции распаковки (рис. 8.11) на всех маскированных позициях¹ оказываются нулевые векторы, что гарантирует целостность вычислений далее по конвейеру.

¹ Все позиции за пределами известной длины последовательности, начиная слева направо в измерении последовательности, считаются маскированными.