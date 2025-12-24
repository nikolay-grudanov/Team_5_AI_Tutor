---
source_image: page_031.png
page_number: 31
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.98
tokens: 7076
characters: 467
timestamp: 2025-12-24T02:21:42.237656
finish_reason: stop
---

Обратите внимание, что тип индексов — LongTensor; таковы требования к доступу по индексу при использовании функций PyTorch. Можно также выполнять объединение тензоров с помощью встроенных функций конкатенации (пример 1.13), указывая тензоры и нужные измерения.

Пример 1.13. Конкатенация тензоров

import torch
x = torch.arange(6).view(2,3)
describe(x)

Type: torch.FloatTensor
Shape/size: torch.Size([2, 3])
Values:
tensor([[ 0.,  1.,  2.],
        [ 3.,  4.,  5.]])