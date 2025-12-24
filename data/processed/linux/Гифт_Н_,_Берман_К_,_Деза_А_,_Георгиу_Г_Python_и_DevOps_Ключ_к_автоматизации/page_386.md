---
source_image: page_386.png
page_number: 386
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.24
tokens: 7632
characters: 1933
timestamp: 2025-12-24T03:11:14.125843
finish_reason: stop
---

Получаем пароль для пользователя admin веб-интерфейса Grafana:

$ kubectl get secret --namespace monitoring grafana \
-o jsonpath="{.data.admin-password}" | base64 --decode ; echo

КАКОЙТОСЕКРЕТНЫЙТЕКСТ

Подключаемся к UI Grafana с помощью команды kubectl port-forward:

$ export GRAFANA_POD_NAME=$(kubectl get pods --namespace monitoring \
-l "app=grafana,release=grafana" -o jsonpath="{.items[0].metadata.name}")

$ kubectl --namespace monitoring port-forward $GRAFANA_POD_NAME 3000
Forwarding from 127.0.0.1:3000 -> 3000
Forwarding from [::1]:3000 -> 3000

Переходим по адресу localhost:3000 в браузере и видим UI Grafana. Входим как пользователь admin с помощью полученного ранее пароля.

С помощью команды helm list выводим список установленных чартов. Текущая установка чарта называется релизом Helm (Helm release):

$ helm list
NAME      REVISION  UPDATED         STATUS    CHART
APP VERSION  NAME SPACE
grafana   1        Tue Aug 27 13:10:02 2019  DEPLOYED  grafana-3.8.3
          6.2.5     monitoring
prometheus. 1      Tue Aug 27 12:59:40 2019  DEPLOYED  prometheus-9.1.0
          2.11.1    monitoring

В большинстве случаев чарты Helm придется настраивать под свои нужды. Легче всего это сделать, если скачать чарт и установить его из локальной файловой системы с помощью helm.

Самые свежие стабильные релизы чартов Helm Prometheus и Grafana можно получить с помощью команды helm fetch, скачивающей архивы чартов в формате TGZ:

$ mkdir charts
$ cd charts
$ helm fetch stable/prometheus
$ helm fetch stable/grafana
$ ls -la
total 80
drwxr-xr-x  4 ggheo staff  128 Aug 27 13:59 .
drwxr-xr-x 15 ggheo staff  480 Aug 27 13:55 ..
-rw-r--r--  1 ggheo staff 16195 Aug 27 13:55 grafana-3.8.3.tgz
-rw-r--r--  1 ggheo staff 23481 Aug 27 13:54 prometheus-9.1.0.tgz

Разархивируем содержимое TGZ-файлов, а затем удаляем их:

$ tar xzf prometheus-9.1.0.tgz; rm prometheus-9.1.0.tgz
$ tar xzf grafana-3.8.3.tgz; rm grafana-3.8.3.tgz