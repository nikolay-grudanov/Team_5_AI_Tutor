---
source_image: page_036.png
page_number: 36
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.35
tokens: 7699
characters: 2153
timestamp: 2025-12-24T02:40:54.949496
finish_reason: stop
---

Примеры кода
Примеры кода в большинстве случаев показаны так, как выглядят в оболочке IPython или Jupyter-блокнотах: ввод и вывод.

In [5]: КОД
Out[5]: РЕЗУЛЬТАТ

Это означает, что вы должны ввести код в блоке In в своей рабочей среде и выполнить его, нажав клавишу Enter (или Shift-Enter в Jupyter). Результат должен быть таким, как показано в блоке Out.

Я изменил параметры вывода на консоль, подразумеваемые по умолчанию в NumPy и pandas, ради краткости и удобочитаемости. Так, числовые данные печатаются с большей точностью. Чтобы при выполнении примеров результаты выглядели так же, как в книге, выполните следующий Python-код перед запуском примеров:

import numpy as np
import pandas as pd
pd.options.display.max_columns = 20
pd.options.display.max_rows = 20
pd.options.display.max_colwidth = 80
np.set_printoptions(precision=4, suppress=True)

Данные для примеров
Наборы данных для примеров из каждой главы находятся в репозитории на сайте GitHub: https://github.com/wesm/pydata-book (или его зеркале на Gitee по адресу https://gitee.com/wesmckinn/pydata-book, если у вас нет доступа к GitHub). Вы можете получить их либо с помощью командной утилиты системы управления версиями Git, либо скачав zip-файл репозитория с сайта. Если возникнут проблемы, заходите на мой сайт (https://wesmckinney.com/book), где выложены актуальные инструкции по получению материалов к книге.

Скачав zip-файл с примерами наборов данных, вы должны будете распаковать его в какой-нибудь каталог и перейти туда в терминале, прежде чем выполнять примеры:

$ pwd
/home/wesm/book-materials
$ ls
appa.ipynb ch05.ipynb ch09.ipynb ch13.ipynb README.md
ch02.ipynb ch06.ipynb ch10.ipynb COPYING requirements.txt
ch03.ipynb ch07.ipynb ch11.ipynb datasets
ch04.ipynb ch08.ipynb ch12.ipynb examples

Я стремился, чтобы в репозиторий попало все необходимое для воспроизведения примеров, но мог где-то ошибиться или что-то пропустить. В таком случае пишите мне на адрес book@wesmckinney.com. Самый лучший способ сообщить об ошибках, найденных в книге, — описать их на странице опечаток на сайте издательства O’Reilly (https://www.oreilly.com/catalog/errata.csp?isbn=0636920519829).