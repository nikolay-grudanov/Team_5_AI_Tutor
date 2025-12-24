---
source_image: page_067.png
page_number: 67
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.41
tokens: 7401
characters: 1489
timestamp: 2025-12-24T03:02:43.521913
finish_reason: stop
---

'-rwxr-xr-x   1 root    wheel    23984 Mar 20 23:10 killall',
'-rwxr-xr-x   1 root    wheel    30512 Mar 20 23:10 pkill']

Из всего этого можно сделать вывод, что IPython — идеальная среда для всяких экспериментов с маленькими сценариями командной оболочки.

«Магические» команды IPython

Если вы привыкнете работать с Python, то должны научиться использовать встроенные «магические» команды. По сути, они представляют собой сокращенные формы записи, заключающие в себе огромный потенциал. Перед «магическими» командами ставятся символы %%. Вот пример написания в Python встраиваемой команды bash. Конечно, это всего лишь одна команда, но точно так же можно написать и целый сценарий bash:

In [13]: %%bash
    ...: uname -a
    ...:
    ...:
Darwin nogibjj.local 18.5.0 Darwin Kernel Version 18.5.0: Mon Mar ...

Очень интересна команда %%writefile, позволяющая писать и тестировать сценарии Python или bash прямо во время работы и выполнять их с помощью IPython:

In [16]: %%writefile print_time.py
    ...: #!/usr/bin/env python
    ...: import datetime
    ...: print(datetime.datetime.now().time())
    ...:
    ...:
    ...:
Writing print_time.py

In [17]: cat print_time.py
#!/usr/bin/env python
import datetime
print(datetime.datetime.now().time())

In [18]: !python print_time.py
19:06:00.594914

Еще одна удобная команда, %who, демонстрирует загруженные в памяти интерактивные переменные. Она очень полезна при длительной работе в терминале:

In [20]: %who
df      ls      var_ls