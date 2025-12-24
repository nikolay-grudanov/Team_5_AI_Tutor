---
source_image: page_228.png
page_number: 228
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.12
tokens: 7491
characters: 1977
timestamp: 2025-12-24T03:06:56.152613
finish_reason: stop
---

мешать. Как видите, настроек требуется довольно много и они сильно усложняются, если механизмов журналирования несколько. Для минимизации этого эффекта лучше создать отдельный модуль со вспомогательной функцией, которая будет задавать все эти опции. В качестве альтернативы подобному варианту конфигурации модуль logging предлагает конфигурацию на основе ассоциативного массива, в которой параметры конфигурации задаются в интерфейсе вида «ключ/значение». Далее приведена подобная конфигурация для того же примера.

Чтобы увидеть все это в действии, добавьте в конец файла несколько операций записи в журнал, выполняемых непосредственно с помощью Python, и сохраните его в файл log_test.py:

# Корневой механизм журналирования
logger = logging.getLogger()
logger.warning('this is an info message from the root logger')

app_logger = logging.getLogger('my-app')
app_logger.warning('an info message from my-app')

Корневой механизм журналирования является родительским, кроме того, здесь появляется новый механизм журналирования my-app. Если выполнить этот файл напрямую, в терминал, как и в файл application.log, будет выведено следующее:

$ python log_test.py
[root][WARNING] this is an info message from the root logger
[my-app][WARNING] an info message from my-app
$ cat application.log
[2019-09-08 12:28:25,190][root][WARNING] this is an info message from the root logger
[2019-09-08 12:28:25,190][my-app][WARNING] an info message from my-app

Выводимая информация дублируется, поскольку мы настроили оба механизма журналирования, но это вовсе не обязательно. Форматирование в файловом механизме журналирования отличается, чтобы было удобнее просматривать в консоли:

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {
        'BASE_FORMAT': {
            'format': '[%(name)s][%(levelname)-6s] %(message)s',
        },
        'FILE_FORMAT': {
            'format': '[%(asctime)s] [%(name)s][%(levelname)-6s] %(message)s',
        },
