---
source_image: page_842.png
page_number: 842
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.12
tokens: 7749
characters: 2126
timestamp: 2025-12-24T05:09:07.710996
finish_reason: stop
---

5. Просмотрите журналы. Чтобы просмотреть журналы любого контейнера, работающего внутри выбранного модуля, выполните следующую команду:

$ kubectl logs $POD_NAME
Kubernetes Bootcamp App Started At: 2020-02-13T21:29:21.836Z
| Running On: kubernetes-bootcamp-5b48cfdcbd-lf9t2

Running On: kubernetes-bootcamp-5b48cfdcbd-lf9t2 | Total Requests: 1 | App Uptime: 34.086 seconds | Log Time: 2020-02-13T21:29:55.923Z

6. Выполните команды в поде. Используйте команду kubectl exec для запуска команд внутри модуля. Первая команда запускает env для просмотра переменных среды оболочки изнутри модуля, а вторая открывает оболочку внутри модуля, чтобы вы могли выполнить следующие команды:

$ kubectl exec $POD_NAME env
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=kubernetes-bootcamp-5b48cfdcbd-lf9t2
KUBERNETES_SERVICE_HOST=10.96.0.1
KUBERNETES_SERVICE_PORT=443
...
$ kubectl exec -ti $POD_NAME bash
root@kubernetes-bootcamp-5b48cfdcbd-lf9t2:# date
Thu Feb 13 21:57:18 UTC 2020

kubernetes-bootcamp-5b48cfdcbd-lf9t2:# ps -ef
UID     PID  PPID  C STIME TTY      TIME CMD
root     1    0   0 21:29 ?        00:00:00 /bin/sh -c node server.js
root     6    1   0 21:29 ?        00:00:00 node server.js
root    115   0   0 21:55 pts/0    00:00:00 bash
root    123  115   0 22:01 pts/0   00:00:00 ps -ef

root@kubernetes-bootcamp-5b48cfdcbd-lf9t2:# curl localhost:8080
Hello Kubernetes bootcamp!|Running on:kubernetes-bootcamp-5b48cfdcbd-lf9t2|v=1

root@kubernetes-bootcamp-5b48cfdcbd-lf9t2:# exit

После запуска оболочки появляются выходные данные команд date и ps. Из вывода команды ps видно, что первый процесс, запущенный в контейнере (PID 1), — это скрипт server.js. После этого команда curl может успешно взаимодействовать с контейнером на локальном порте 0808.

Доступ к приложениям с помощью служб
Чтобы предоставить доступ к модулю kubernetes-bootcamp, описанному в примерах, с внешнего IP-адреса рабочего узла, можно создать объект NodePort. Вот один из способов сделать это.

1. Проверьте, работает ли под. Введите команду, приведенную далее, чтобы проверить, что модуль kubernetes bootcamp запущен: