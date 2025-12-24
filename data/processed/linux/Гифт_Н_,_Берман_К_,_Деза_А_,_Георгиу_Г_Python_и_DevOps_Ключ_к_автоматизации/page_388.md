---
source_image: page_388.png
page_number: 388
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.29
tokens: 7589
characters: 2415
timestamp: 2025-12-24T03:11:20.704128
finish_reason: stop
---

Annotations: pv.kubernetes.io/bind-completed: yes
    pv.kubernetes.io/bound-by-controller: yes
    volume.beta.kubernetes.io/storage-provisioner:kubernetes.io/gce-pd
Finalizers: [kubernetes.io/pvc-protection]
Capacity: 10Gi
Access Modes:RWO
Mounted By: grafana-84f79d5c45-zlqz8
Events:
Type    Reason                Age    From                        Message
----    ------                ----   ----                        --------
Normal  ProvisioningSucceeded  88s    persistentvolume-controller  Successfully provisioned volume pvc-31d47393-c910-11e9-87c5-42010a8a0021 using kubernetes.io/gce-pd

Еще один пример настройки чартов Helm под свои нужды, на этот раз для чарта Prometheus, — изменение используемого по умолчанию срока хранения информации в Prometheus, равного 15 дням.

Измените значение параметра retention в файле prometheus/values.yaml на 30 дней:

## Срок хранения информации в Prometheus (по умолчанию 15 дней,
## если не указано иное значение)
##
retention: "30d"

Обновите текущий выпуск чарта Prometheus, запустив команду helm upgrade. Выполнить эту команду необходимо в родительском каталоге каталога чарта prometheus:

$ helm upgrade prometheus prometheus
Release "prometheus" has been upgraded. Happy Helming!

Проверим, изменился ли срок хранения информации на 30-дневный. Выполните команду kubectl describe для запущенного в настоящий момент модуля Prometheus в пространстве имен monitoring и обратите внимание на раздел Args вывода:

$ kubectl get pods -nmonitoring
NAME                                                                 READY   STATUS    RESTARTS   AGE
grafana-84f79d5c45-zlqz8                                         1/1      Running   0           9m
prometheus-alertmanager-df57f6df6-4b8lv                             2/2      Running   0           87m
prometheus-kube-state-metrics-564564f799-t6qdm                     1/1      Running   0           87m
prometheus-node-exporter-b4sb9                                      1/1      Running   0           87m
prometheus-node-exporter-n4z2g                                      1/1      Running   0           87m
prometheus-node-exporter-w7hn7                                      1/1      Running   0           87m
prometheus-pushgateway-56b65bcf5f-whx5t                             1/1      Running   0           87m
prometheus-server-779ffd445f-4llqr                                 2/2      Running   0           3m