---
source_image: page_291.png
page_number: 291
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.89
tokens: 7512
characters: 2206
timestamp: 2025-12-24T03:08:31.683534
finish_reason: stop
---

Задание времени ожидания и работа с ним

При написании кода, который запускает довольно долго выполняющиеся процессы, желательно указывать разумное время ожидания по умолчанию. Проще всего экспериментировать с этой возможностью с помощью команды sleep Unix. Вот пример команды sleep, выполнение которой завершается до истечения времени ожидания в командной оболочке IPython. Она возвращает объект CompletedProcess:

In [1]: subprocess.run(["sleep", "3"], timeout=4)
Out[1]: CompletedProcess(args=['sleep', '3'], returncode=0)

А это вторая версия, генерирующая исключение. В большинстве случаев лучше как-нибудь это исключение обработать:

----> 1 subprocess.run(["sleep", "3"], timeout=1)
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/subprocess.py
    in run(input, capture_output, timeout, check, *popenargs, **kwargs)
        477         stdout, stderr = process.communicate()
        478         raise TimeoutExpired(process.args, timeout, output=stdout,
--> 479                         stderr=stderr)
        480     except:  # Including KeyboardInterrupt, communicate handled that.
        481         process.kill()
TimeoutExpired: Command '[''sleep'', '3'']' timed out after 1 seconds

Наиболее разумный подход — перехватить это исключение TimeoutExpired, после чего занести информацию о нем в журнал и реализовать код для освобождения памяти:

import logging
import subprocess

try:
    subprocess.run(["sleep", "3"], timeout=4)
except subprocess.TimeoutExpired:
    logging.exception("Sleep command timed out")

Журналирование исключений жизненно необходимо при создании систем профессионального уровня. Отследить ошибку при развертывании кода на множестве машин будет невозможно без централизованной системы журналирования с возможностью поиска. Профессионалам в сфере DevOps чрезвычайно важно следовать этому паттерну и рассказывать всем о его полезности.

Проблема с потоками выполнения Python

Возможно, в детстве у вас был приятель, с которым ваши родители не советовали водиться. Если так, видимо, они пытались помочь вам избежать плохих решений. Потоки выполнения Python во многом схожи с таким скверным другом. Если с ними связаться, ни к чему хорошему это не приведет.