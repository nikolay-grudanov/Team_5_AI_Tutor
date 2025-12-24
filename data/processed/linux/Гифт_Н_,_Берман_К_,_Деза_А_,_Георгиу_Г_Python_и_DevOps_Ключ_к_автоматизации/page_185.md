---
source_image: page_185.png
page_number: 185
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.41
tokens: 7431
characters: 1828
timestamp: 2025-12-24T03:05:46.887436
finish_reason: stop
---

Установка юнита

Указанный файл конфигурации необходимо поместить в определенное место, чтобы systemd смогла его найти и загрузить. Поддерживается несколько возможных местоположений, но для созданных или управляемых администратором юнитов предназначен каталог /etc/systemd/system.

Имеет смысл проверить, что инструкция ExecStart работает с этими путями. Использование абсолютных путей повышает риск случайной опечатки. Для проверки выполните всю строку в терминале и посмотрите, будет ли результат выполнения примерно таким:

$ /opt/http/bin/pecan serve /opt/http/api/config.py
Starting server in PID 20621
serving on 0.0.0.0:8080, view at http://127.0.0.1:8080

После проверки работы команды скопируйте unit-файл в этот каталог, дав ему название hello-world.service:

$ cp hello-world.service /etc/systemd/system/

После этого необходимо перезагрузить systemd, чтобы дать ей знать о новом юните:

$ systemctl daemon-reload

Теперь сервис находится в полностью рабочем состоянии, его можно запускать и останавливать. Для проверки состояния процесса можно воспользоваться подкомандой status. Вкратце рассмотрим различные команды, с помощью которых можно взаимодействовать с нашим сервисом. Вначале посмотрим, распознает ли его systemd. Вот как он должен вести себя и как должен выглядеть результат работы:

$ systemctl status hello-world
● hello-world.service - hello world pecan service
  Loaded: loaded (/etc/systemd/system/hello-world.service; disabled; )
  Active: inactive (dead)

Поскольку наш сервис не запущен, неудивительно, что он отмечен как dead. Запустите сервис и снова проверьте состояние (утилита curl должна сообщать, что на порте 8080 ничего не запущено):

$ curl localhost:8080
curl: (7) Failed to connect to localhost port 8080: Connection refused
$ systemctl start hello-world
$ systemctl status hello-world