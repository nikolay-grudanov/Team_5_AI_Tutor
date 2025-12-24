---
source_image: page_055.png
page_number: 55
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.63
tokens: 7510
characters: 1855
timestamp: 2025-12-24T00:52:55.450367
finish_reason: stop
---

In[14]: %%file mprun_demo.py
    def sum_of_lists(N):
        total = 0
        for i in range(5):
            L = [j ^ (j >> i) for j in range(N)]
        total += sum(L)
        del L # Удалить ссылку на L
        return total

Overwriting mprun_demo.py

Теперь мы можем импортировать новую версию нашей функции и запустить построчный профилировщик памяти:

In[15]: from mprun_demo import sum_of_lists
    %mprun -f sum_of_lists sum_of_lists(1000000)

Результат, выведенный в пейджер, представляет собой отчет об использовании памяти этой функцией и выглядит следующим образом:

Filename: ./mprun_demo.py

Line #    Mem usage    Increment    Line Contents
==================================================
     4    71.9 MiB      0.0 MiB    L = [j ^ (j >> i) for j in range(N)]

Filename: ./mprun_demo.py

Line #    Mem usage    Increment    Line Contents
==================================================
     1    39.0 MiB      0.0 MiB    def sum_of_lists(N):
     2    39.0 MiB      0.0 MiB    total = 0
     3    46.5 MiB      7.5 MiB    for i in range(5):
     4    71.9 MiB     25.4 MiB    L = [j ^ (j >> i)
                                    for j in range(N)]
     5    71.9 MiB      0.0 MiB    total += sum(L)
     6    46.5 MiB    -25.4 MiB    del L # Удалить ссылку на L
     7    39.1 MiB     -7.4 MiB    return total

Здесь столбец Increment сообщает нам, насколько каждая строка отражается в общем объеме памяти. Обратите внимание, что при создании и удалении списка L, помимо фонового использования памяти самим интерпретатором языка Python, использование памяти увеличивается примерно на 25 Мбайт.

Для получения дополнительной информации о «магических» функциях %memit и %mprun, а также о доступных для них параметрах воспользуйтесь справочной функциональностью оболочки IPython (то есть наберите %memit? в командной строке IPython).