---
source_image: page_087.png
page_number: 87
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.29
tokens: 7377
characters: 1576
timestamp: 2025-12-24T03:03:07.860887
finish_reason: stop
---

ними. Как уже упоминалось, модуль os стремится к кросс-платформенному поведению, и подмодуль os.path не исключение. Он интерпретирует пути в соответствии с действующей операционной системой с использованием прямых косых черт для разделения каталогов в Unix-подобных системах и обратных — в Windows. Благодаря этому программа может формировать подходящие для любой операционной системы пути на лету. Возможность удобного разбиения и «склеивания» путей — вероятно, чаще всего применяемая функциональность подмодуля os.path. Для разбиения путей используются три метода — split, basename и dirname:

In [1]: import os

In [2]: cur_dir = os.getcwd() ①

In [3]: cur_dir
Out[3]: '/Users/kbehrman/Google-Drive/projects/python-devops/samples/chapter4'

In [4]: os.path.split(cur_dir) ②
Out[4]: ('/Users/kbehrman/Google-Drive/projects/python-devops/samples',
        'chapter4')

In [5]: os.path.dirname(cur_dir) ③
Out[5]: '/Users/kbehrman/Google-Drive/projects/python-devops/samples'

In [6]: os.path.basename(cur_dir) ④
Out[6]: 'chapter4'

① Получаем текущий рабочий каталог.

② os.path.split отделяет конечный уровень пути от родительского пути.

③ os.path.dirname возвращает родительский путь.

④ os.path.basename возвращает название конечного каталога.

os.path.dirname удобно использовать для обхода дерева каталогов:

In [7]: while os.path.basename(cur_dir):
    ...:     cur_dir = os.path.dirname(cur_dir)
    ...:     print(cur_dir)
    ...:
/Users/kbehrman/projects/python-devops/samples
/Users/kbehrman/projects/python-devops
/Users/kbehrman/projects
/Users/kbehrman
/Users
/