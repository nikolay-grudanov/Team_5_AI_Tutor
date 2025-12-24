---
source_image: page_118.png
page_number: 118
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 51.47
tokens: 7898
characters: 2276
timestamp: 2025-12-24T03:04:22.345252
finish_reason: stop
---

def timing(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        ts = time()
        result = f(*args, **kwargs)
        te = time()
        print(f"fun: {f.__name__}, args: [{args}, {kwargs}] took: {te-ts} sec")
        return result
    return wrap

Далее добавим¹ декоратор numba.jit с ключевым аргументом nopython, равным True. Благодаря этому код будет выполняться JIT, а не обычным Python:

@timing
@numba.jit(nopython=True)
def expmean_jit(rea):
    """Вычисляет средние значения"""

    val = rea.mean() ** 2
    return val

При его запуске вы увидите как jit, так и обычную версию, запущенные посредством утилиты командной строки:

$ python nuclearcli.py jit-test
Running NO JIT
func:'expmean' args:[(array([[1.0000e+00, 4.2080e+05, 2350e+05, ...,
                                 1.0543e+06, 1.0485e+06, 1.0444e+06],
                            [2.0000e+00, 5.4240e+05, 5.4670e+05, ...,
                                 1.5158e+06, 1.5199e+06, 1.5253e+06],
                            [3.0000e+00, 7.0900e+04, 7.1200e+04, ...,
                                 1.1380e+05, 1.1350e+05, 1.1330e+05],
                            ...,
                            [1.5277e+04, 9.8900e+04, 9.8100e+04, ...,
                                 2.1980e+05, 2.2000e+05, 2.2040e+05],
                            [1.5280e+04, 8.6700e+04, 8.7500e+04, ...,
                                 1.9070e+05, 1.9230e+05, 1.9360e+05],
                            [1.5281e+04, 2.5350e+05, 2.5400e+05, ...,
                                 7.8360e+05, 7.7950e+05, 7.7420e+05]], dtype=float32)), {}] took: 0.0007 sec
$ python nuclearcli.py jit-test --jit
Running with JIT
func:'expmean_jit' args:[(array([[1.0000e+00, 4.2080e+05, 4.2350e+05, ...,
                                 0543e+06, 1.0485e+06, 1.0444e+06],
                            [2.0000e+00, 5.4240e+05, 5.4670e+05, ...,
                                 1.5158e+06, 1.5199e+06,
                                 1.5253e+06],
                            [3.0000e+00, 7.0900e+04, 7.1200e+04, ...,
                                 1.1380e+05, 1.1350e+05,
                                 1.1330e+05],
                            ...

¹ Не забудьте перед этим установить пакет numba, а затем импортировать его в коде. — Примеч. пер.