---
source_image: page_385.png
page_number: 385
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.03
tokens: 7472
characters: 1602
timestamp: 2025-12-24T03:11:00.585653
finish_reason: stop
---

prometheus-server        ClusterIP   10.0.4.74   <none>   80/TCP
    3m51s

$ kubectl get configmaps -nmonitoring
NAME                DATA   AGE
prometheus-alertmanager   1   3m58s
prometheus-server       3   3m58s

Подключаемся к UI Prometheus с помощью команды kubectl port-forward:

$ export PROMETHEUS_POD_NAME=$(kubectl get pods --namespace monitoring \
-l "app=prometheus,component=server" -o jsonpath="{.items[0].metadata.name}")

$ echo $PROMETHEUS_POD_NAME
prometheus-server-7555945646-d86gn

$ kubectl --namespace monitoring port-forward $PROMETHEUS_POD_NAME 9090
Forwarding from 127.0.0.1:9090 -> 9090
Forwarding from [::1]:9090 -> 9090
Handling connection for 9090

Переходим по адресу localhost:9090 в браузере и видим UI Prometheus.

Установим чарт Helm для Grafana (https://oreil.ly/--wEN) в пространстве имен monitoring:

$ helm install --name grafana --namespace monitoring stable/grafana
NAME:   grafana
LAST DEPLOYED: Tue Aug 27 13:10:02 2019
NAMESPACE: monitoring
STATUS: DEPLOYED

Выводим списки всех относящихся к Grafana модулей, сервисов, объектов ConfigMap и Secret в пространстве имен monitoring:

$ kubectl get pods -nmonitoring | grep grafana
grafana-84b887cf4d-wplcr   1/1   Running   0

$ kubectl get services -nmonitoring | grep grafana
grafana   ClusterIP   10.0.5.154   <none>   80/TCP

$ kubectl get configmaps -nmonitoring | grep grafana
grafana   1   99s
grafana-test   1   99s

$ kubectl get secrets -nmonitoring | grep grafana
grafana   Opaque
grafana-test-token-85x4x   kubernetes.io/service-account-token
grafana-token-jw2qg   kubernetes.io/service-account-token