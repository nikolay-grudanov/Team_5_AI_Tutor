---
source_image: page_032.png
page_number: 32
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 13.14
tokens: 7084
characters: 438
timestamp: 2025-12-24T02:21:42.423402
finish_reason: stop
---

В PyTorch также реализованы высокоэффективные операции линейной алгебры: умножение, вычисление обратного элемента и следа тензора (второго ранга. — Примеч. пер.), как показано в примере 1.14.

Пример 1.14. Операции линейной алгебры над тензорами

Input[0]
import torch
x1 = torch.arange(6).view(2, 3)
describe(x1)

Output[0]
Type: torch.FloatTensor
Shape/size: torch.Size([2, 3])
Values:
tensor([[ 0.,  1.,  2.],
        [ 3.,  4.,  5.]])