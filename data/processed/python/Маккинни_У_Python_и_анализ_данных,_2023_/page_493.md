---
source_image: page_493.png
page_number: 493
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.82
tokens: 7595
characters: 1727
timestamp: 2025-12-24T02:53:54.963552
finish_reason: stop
---

Говоря о непрерывной организации памяти, мы имеем в виду, что элементы массива хранятся в памяти в том порядке, в котором видны в массиве, организованном по столбцам (как в Fortran) или по строкам (как в C). По умолчанию массивы в NumPy создаются C-непрерывными. О массиве, хранящемся по столбцам, например транспонированном C-непрерывном массиве, говорят, что он Fortran-непрерывный. Эти свойства можно явно опросить с помощью атрибута flags объекта ndarray:

In [228]: arr_c = np.ones((100, 10000), order='C')

In [229]: arr_f = np.ones((100, 10000), order='F')

In [230]: arr_c.flags
Out[230]:
    C_CONTIGUOUS : True
    F_CONTIGUOUS : False
    OWNDATA : True
    Advanced NumPy | 505
    WRITEABLE : True
    ALIGNED : True
    WRITEBACKIFCOPY : False
    UPDATEIFCOPY : False

In [231]: arr_f.flags
Out[231]:
    C_CONTIGUOUS : False
    F_CONTIGUOUS : True
    OWNDATA : True
    WRITEABLE : True
    ALIGNED : True
    WRITEBACKIFCOPY : False
    UPDATEIFCOPY : False

In [232]: arr_f.flags.f_contiguous
Out[232]: True

В данном случае суммирование строк массива теоретически должно быть быстрее для arr_c, чем для arr_f, поскольку строки хранятся в памяти непрерывно. Я проверил это с помощью функции %timeit в IPython (на вашей машине результаты могут отличаться):

In [233]: %timeit arr_c.sum(1)
444 us +- 60.5 us per loop (mean +- std. dev. of 7 runs, 1000 loops each)

In [234]: %timeit arr_f.sum(1)
581 us +- 8.16 us per loop (mean +- std. dev. of 7 runs, 1000 loops each)

Часто именно в этом направлении имеет смысл прикладывать усилия, стремясь выжать всю возможную производительность из NumPy. Если массив размещен в памяти не так, как нужно, можно скопировать его методом copy, передав параметр 'C' или 'F':