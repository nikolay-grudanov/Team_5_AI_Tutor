---
source_image: page_387.png
page_number: 387
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.50
tokens: 7389
characters: 1665
timestamp: 2025-12-24T03:11:01.677201
finish_reason: stop
---

Шаблонизированные манифесты Kubernetes хранятся по умолчанию в подкаталогах templates каталогов чартов, так что в данном случае они будут располагаться в prometheus/templates и grafana/templates. Параметры конфигурации конкретного чарта объявляются в файле values.yaml в каталоге чарта.

В качестве примера настройки под свои нужды чарта Helm добавим в Grafana том постоянного хранения, чтобы не потерять данные при перезапуске модулей Grafana.

Отредактируйте файл grafana/values.yaml, задав значение true для подключа enabled родительского ключа persistence (по умолчанию false) в следующем разделе:

## Открываем возможности постоянного хранения данных с помощью объектов Persistent Volume Claim
## ссылка: http://kubernetes.io/docs/user-guide/persistent-volumes/
##
persistence:
  enabled: true
  # storageClassName: default
  accessModes:
    - ReadWriteOnce
  size: 10Gi
  # annotations: {}
  finalizers:
    - kubernetes.io/pvc-protection
  # subPath: ""
  # existingClaim:

Обновите текущий выпуск чарта grafana Helm с помощью команды helm upgrade. Последний аргумент этой команды — название локального каталога с чартом. Выполните в родительском каталоге каталога чарта grafana следующую команду:

$ helm upgrade grafana grafana/
Release "grafana" has been upgraded. Happy Helming!

Убеждаемся, что для Grafana был создан PVC в пространстве имен monitoring:

kubectl describe pvc grafana -nmonitoring
Name:        grafana
Namespace:   monitoring
StorageClass:standard
Status:      Bound
Volume:      pvc-31d47393-c910-11e9-87c5-42010a8a0021
Labels:      app=grafana
             chart=grafana-3.8.3
             heritage=Tiller
             release=grafana