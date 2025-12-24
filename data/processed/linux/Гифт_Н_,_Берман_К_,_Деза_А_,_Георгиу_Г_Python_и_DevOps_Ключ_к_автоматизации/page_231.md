---
source_image: page_231.png
page_number: 231
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.07
tokens: 7496
characters: 1962
timestamp: 2025-12-24T03:07:03.083937
finish_reason: stop
---

Среда DEVEL прекрасно работает, и для смены ее на среду промышленной эксплуатации достаточно всего одной переменной среды:

$ APP_ENVIRON='PRODUCTION' pecan serve config.py
Starting server in PID 2832
serving on 0.0.0.0:8080, view at http://127.0.0.1:8080
2019-08-12 08:15:46,552 [PRODUCTION][INFO    ] [pecan.commands.serve] GET / 200

Распространенные паттерны

Модуль журналирования включает несколько неплохих паттернов, на первый взгляд неочевидных, но заслуживающих как можно более частого применения. Один из них — использование вспомогательной функции logging.exception. Обычная схема выглядит вот так:

try:
    return expensive_operation()
except TypeError as error:
    logging.error("Running expensive_operation caused error: %s" % str(error))

Она неудачна по нескольким причинам: сначала «съедает» исключение и лишь потом отображает его строковое представление. Если исключение неочевидное либо генерируется в неочевидном месте, то оповещать о TypeError бессмысленно. Если замена исключения на строковое значение завершилась неудачей, вы получите ошибку ValueError, но она мало чем поможет, если код скрывает трассу вызовов:

[ERROR] Running expensive_operation caused an error:
    TypeError: not all arguments converted during string formatting

Где возникла эта ошибка? Мы знаем, что она произошла при вызове expensive_operation(), но где именно? В каких функции, классе или файле? Подобное журналирование не помогает, а только приводит разработчика в бешенство! С помощью модуля журналирования можно занести в журнал полную трассу исключения:

try:
    return expensive_operation()
except TypeError:
    logging.exception("Running expensive_operation caused error")

Вспомогательная функция logging.exception как по волшебству помещает в журнал полную трассу исключения. В реализации не нужно заботиться о перехвате ошибки, как раньше, или даже пытаться извлечь из исключения полезную информацию. Модуль журналирования позаботится обо всем сам.