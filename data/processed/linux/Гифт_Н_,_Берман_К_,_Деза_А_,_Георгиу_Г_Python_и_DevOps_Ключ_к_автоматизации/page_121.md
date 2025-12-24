---
source_image: page_121.png
page_number: 121
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.39
tokens: 7222
characters: 1052
timestamp: 2025-12-24T03:03:52.208994
finish_reason: stop
---

@timing
def add_sum(rea):
    """Обычный цикл for"""

    x, _ = rea.shape
    total = 0
    for _ in numba.prange(x):
        total += rea.sum()
        print(total)

@cli.command()
@click.option('--threads/--no-jit', default=False)
def thread_test(threads):
    rea = real_estate_array()
    if threads:
        click.echo(click.style('Running with multicore threads', fg='green'))
        add_sum_threaded(rea)
    else:
        click.echo(click.style('Running NO THREADS', fg='red'))
        add_sum(rea)

Обратите внимание на ключевое отличие распараллеленной версии: потоки выполнения для итераций порождаются с помощью декоратора @numba.jit(parallel=True) и оператора numba.prange. Как видно из рис. 3.1, все ядра CPU на машине используются практически на 100 %, а когда практически тот же код выполняется без распараллеливания, задействуется только одно ядро:

$ python nuclearcli.py thread-test
$ python nuclearcli.py thread-test --threads

![Использование всех ядер CPU](../images/chapter_3/fig_3_1.png)

Рис. 3.1. Использование всех ядер CPU