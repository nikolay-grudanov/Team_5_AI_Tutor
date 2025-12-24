---
source_image: page_035.png
page_number: 35
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.98
tokens: 7630
characters: 1989
timestamp: 2025-12-24T02:22:09.832903
finish_reason: stop
---

вать только для GPU производства NVIDIA¹. В PyTorch есть объекты-тензоры для CUDA, неотличимые на практике от обычных CPU-тензоров, за исключением внутреннего механизма выделения памяти.

PyTorch обеспечивает простоту создания этих CUDA-тензоров, поддерживая перемещение тензоров с CPU на GPU с сохранением их базового типа. В PyTorch рекомендуется применять аппаратно независимый подход и писать код, который бы работал как на CPU, так и на GPU. В примере 1.16 мы сначала проверяем, доступен ли GPU, с помощью функции torch.cuda.is_available() и извлекаем название устройства, вызвав метод torch.device(). Далее мы создаем все будущие тензоры и перемещаем их на нужное устройство с помощью метода .to(device).

Пример 1.16. Создание CUDA-тензоров

<table>
  <tr>
    <th>Input[0]</th>
    <td>import torch<br>print (torch.cuda.is_available())</td>
  </tr>
  <tr>
    <th>Output[0]</th>
    <td>True</td>
  </tr>
  <tr>
    <th>Input[1]</th>
    <td># предпочтительный метод: аппаратно-независимое<br># создание экземпляров тензоров<br>device = torch.device("cuda" if torch.cuda.is_available() else "cpu")<br>print (device)</td>
  </tr>
  <tr>
    <th>Output[1]</th>
    <td>cuda</td>
  </tr>
  <tr>
    <th>Input[2]</th>
    <td>x = torch.rand(3, 3).to(device)<br>describe(x)</td>
  </tr>
  <tr>
    <th>Output[2]</th>
    <td>Type: torch.cuda.FloatTensor<br>Shape/size: torch.Size([3, 3])<br>Values:<br>tensor([[ 0.9149,   0.3993,   0.1100],<br>        [ 0.2541,   0.4333,   0.4451],<br>        [ 0.4966,   0.7865,   0.6604]], device='cuda:0')</td>
  </tr>
</table>

Чтобы работать с CUDA- и не-CUDA-объектами, необходимо гарантировать, что они располагаются на одном устройстве. В противном случае попытка вычислений завершится ошибкой, как показано в примере 1.17. Подобная ситуация возникает,

¹ За прошедшее с момента написания книги время ситуация изменилась к лучшему. См. https://github.com/pytorch/pytorch/issues/488 и https://github.com/pytorch/pytorch/pull/6625. — Примеч. пер.