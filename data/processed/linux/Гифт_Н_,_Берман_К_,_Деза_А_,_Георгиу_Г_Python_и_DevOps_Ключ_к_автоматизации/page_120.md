---
source_image: page_120.png
page_number: 120
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.44
tokens: 7676
characters: 1691
timestamp: 2025-12-24T03:04:09.395295
finish_reason: stop
---

print(x_device.shape)
print(x_device.dtype)

print("Calculating on GPU")
add_ufunc(x_device, y_device, out=out_device)

out_host = out_device.copy_to_host()
print(f"Calculations from GPU {out_host}")

Имеет смысл отметить, что если сначала переместить массив Numpy на GPU, то векторизованная функция выполняет вычисления на GPU. А после завершения задания данные перемещаются обратно из GPU. Использование GPU может радикально улучшить выполнение кода в зависимости от того, какие именно вычисления производятся. Вот результаты выполнения утилиты командной строки:

$ python nuclearcli.py cuda-operation
Moving calculations to GPU memory
<numba.cuda.cudadrv.devicearray.DeviceNDArray object at 0x7f01bf6ccac8>
(10015, 259)
float32
Calculating on GPU
Calculations from GPU [
[2.0000e+00 8.4160e+05 8.4700e+05 ... 2.1086e+06 2.0970e+06 2.0888e+06]
[4.0000e+00 1.0848e+06 1.0934e+06 ... 3.0316e+06 3.0398e+06 3.0506e+06]
[6.0000e+00 1.4180e+05 1.4240e+05 ... 2.2760e+05 2.2700e+05 2.2660e+05]
...
[3.0554e+04 1.9780e+05 1.9620e+05 ... 4.3960e+05 4.4000e+05 4.4080e+05]
[3.0560e+04 1.7340e+05 1.7500e+05 ... 3.8140e+05 3.8460e+05 3.8720e+05]
[3.0562e+04 5.0700e+05 5.0800e+05 ... 1.5672e+06 1.5590e+06 1.5484e+06]
]

Многоядерное многопоточное выполнение кода Python с помощью Numba

Одна из часто возникающих проблем с производительностью Python заключается в отсутствии подлинной многопоточности. Ее тоже можно решить с помощью Numba. Вот пример некоторых простейших операций:

@timing
@numba.jit(parallel=True)
def add_sum_threaded(rea):
    """Использует все ядра процессора"""

    x, _ = rea.shape
    total = 0
    for _ in numba.prange(x):
        total += rea.sum()
        print(total)