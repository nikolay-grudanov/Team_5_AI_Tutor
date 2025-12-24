---
source_image: page_119.png
page_number: 119
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.83
tokens: 7515
characters: 1662
timestamp: 2025-12-24T03:04:02.912299
finish_reason: stop
---

[1.5277e+04, 9.8900e+04, 9.8100e+04, ..., 2.1980e+05, 2.2000e+05,
    2.2040e+05],
[1.5280e+04, 8.6700e+04, 8.7500e+04, ..., 1.9070e+05, 1.9230e+05,
    1.9360e+05],
[1.5281e+04, 2.5350e+05, 2.5400e+05, ..., 7.8360e+05, 7.7950e+05,
@click.option('--jit/--no-jit', default=False)
    7.7420e+05]], dtype=float32),), {}] took: 0.2180 sec

Как этот код работает? Этот простой переключатель требует всего лишь нескольких строк кода:

@cli.command()
def jit_test(jit):
    rea = real_estate_array()
    if jit:
        click.echo(click.style('Running with JIT', fg='green'))
        expmean_jit(rea)
    else:
        click.echo(click.style('Running NO JIT', fg='red'))
        expmean(rea)

В некоторых случаях JIT-версия может ускорить выполнение кода в тысячи раз, но определять это нужно путем тестирования. Кроме того, стоит обратить внимание на следующую строку:

click.echo(click.style('Running with JIT', fg='green'))

Этот сценарий позволяет выводить в терминал текст различных цветов, что может оказаться очень удобно для сложных утилит.

Использование GPU с помощью CUDA Python

Еще один способ существенно ускорить выполнение кода — запуск его непосредственно на GPU. Для следующего примера вам понадобится компьютер с поддержкой CUDA. Код выглядит следующим образом:

@cli.command()
def cuda_operation():
    """Выполняет векторизованные операции на GPU"""

    x = real_estate_array()
    y = real_estate_array()

    print("Moving calculations to GPU memory")
    x_device = cuda.to_device(x)
    y_device = cuda.to_device(y)
    out_device = cuda.device_array(
        shape=(x_device.shape[0],x_device.shape[1]), dtype=np.float32)
    print(x_device)