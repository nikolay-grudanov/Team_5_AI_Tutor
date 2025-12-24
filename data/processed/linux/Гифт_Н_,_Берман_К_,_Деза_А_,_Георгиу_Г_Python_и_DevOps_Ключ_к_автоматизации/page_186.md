---
source_image: page_186.png
page_number: 186
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.07
tokens: 7555
characters: 2126
timestamp: 2025-12-24T03:05:57.084159
finish_reason: stop
---

• hello-world.service - hello world pecan service
    Loaded: loaded (/etc/systemd/system/hello-world.service; disabled; )
    Active: active (running) since Tue 2019-04-23 13:44:20 EDT; 5s ago
    Main PID: 23980 (pecan)
        Tasks: 1 (limit: 4915)
        Memory: 20.1M
        CGroup: /system.slice/hello-world.service
            └─23980 /opt/http/bin/python /opt/http/bin/pecan serve config.py

Apr 23 13:44:20 huando systemd[1]: Started hello world pecan service.

Сервис запущен и находится в полностью рабочем состоянии. Вновь проверьте на порте 8080, что фреймворк запущен, работает и реагирует на запросы:

$ curl localhost:8080
Hello, World!

Если остановить наш сервис с помощью команды systemctl stop hello-world, команда curl снова начнет сообщать об ошибке соединения.

Пока что мы создали и установили юнит, проверили, что он работает, запустив и остановив сервис, а также проверили, что фреймворк Pecan реагирует на запросы на его порте по умолчанию. Хотелось бы, чтобы этот сервис запускался и работал при перезагрузке сервера, и в этом нам поможет раздел Install. Активируем (enable) сервис:

$ systemctl enable hello-world
Created symlink hello-world.service → /etc/systemd/system/hello-world.service.

В случае перезагрузки сервера наш маленький сервис HTTP API снова запустится и будет работать.

Управление журналами

Благодаря тому что речь идет о сконфигурированном сервисе с настройками журналирования (весь вывод stdout и stderr направляется прямиком в systemd), управление журналами происходит без всяких усилий с нашей стороны. Не требуется настраивать файлы журналов, их циклическую замену или даже задавать окончание срока действия. systemd предоставляет несколько интересных и очень удобных возможностей для работы с журналами, например ограничение временного промежутка, а также фильтрацию по юнитам или идентификаторам процессов.

Для взаимодействия с журналами из юнита служит утилита командной строки journalctl. Этот процесс может оказаться для вас неожиданностью, если вы предполагали наличие дополнительной подкоманды из systemd, включающей вспомогательные функции для журналирования.