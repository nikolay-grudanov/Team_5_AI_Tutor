---
source_image: page_384.png
page_number: 384
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.16
tokens: 7507
characters: 1861
timestamp: 2025-12-24T03:11:04.339211
finish_reason: stop
---

--serviceaccount=kube-system:tiller

$ kubectl patch deploy --namespace kube-system \
tiller-deploy -p '{"spec":{"template":{"spec":{"serviceAccount":"tiller"}}}}'

Скачайте соответствующий вашей операционной системе исполняемый файл Helm с официальной страницы Helm (https://oreil.ly/sPwDO) и установите его, после чего установите Tiller с помощью команды helm init:

$ helm init

Создайте пространство имен monitoring:

$ kubectl create namespace monitoring
namespace/monitoring created

Установите чарт Helm Prometheus (https://oreil.ly/CSaSo) в пространстве имен monitoring:

$ helm install --name prometheus --namespace monitoring stable/prometheus
NAME:    prometheus
LAST DEPLOYED: Tue Aug 27 12:59:40 2019
NAMESPACE: monitoring
STATUS: DEPLOYED

Выводим списки всех модулей, сервисов и объектов ConfigMap в пространстве имен monitoring:

$ kubectl get pods -nmonitoring
NAME                                 READY   STATUS    RESTARTS   AGE
prometheus-alertmanager-df57f6df6-4b8lv   2/2     Running   0          3m
prometheus-kube-state-metrics-564564f799-t6qdm   1/1     Running   0          3m
prometheus-node-exporter-b4sb9           1/1     Running   0          3m
prometheus-node-exporter-n4z2g           1/1     Running   0          3m
prometheus-node-exporter-w7hn7           1/1     Running   0          3m
prometheus-pushgateway-56b65bcf5f-whx5t   1/1     Running   0          3m
prometheus-server-7555945646-d86gn       2/2     Running   0          3m

$ kubectl get services -nmonitoring
NAME                TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)
AGE
prometheus-alertmanager   ClusterIP   10.0.6.98   <none>       80/TCP
prometheus-kube-state-metrics   ClusterIP   None      <none>       80/TCP
prometheus-node-exporter   ClusterIP   None      <none>       9100/TCP
prometheus-pushgateway   ClusterIP   10.0.13.216 <none>      9091/TCP