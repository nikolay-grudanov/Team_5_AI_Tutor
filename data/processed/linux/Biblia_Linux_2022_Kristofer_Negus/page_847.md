---
source_image: page_847.png
page_number: 847
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.14
tokens: 7517
characters: 1836
timestamp: 2025-12-24T05:09:02.802875
finish_reason: stop
---

1. Перечислите сведения о службе. Чтобы получить подробную информацию о службе kubernetes-bootcamp, введите следующую команду:

$ kubectl describe services/kubernetes-bootcamp
Name:           kubernetes-bootcamp
Namespace:      default
Labels:         run=kubernetes-bootcamp
Annotations:    <none>
Selector:       run=kubernetes-bootcamp
Type:           NodePort
IP:             10.99.183.8
Port:           <unset> 8080/TCP
TargetPort:     8080/TCP
NodePort:       <unset> 31915/TCP
Endpoints:      172.18.0.4:8080,172.18.0.6:8080,172.18.0.7:8080 + 1 more...

Обратите внимание на IP-адрес и порт (172.18.0.4:8080, 172.18.0.4:8080 и т. д.), присвоенные каждому поду.

2. Подключите NodePort. Введите приведенную далее команду, чтобы установить $NODE_PORT в значение номера порта, назначенного службе:

$ export NODE_PORT=$(kubectl get services/kubernetes-bootcamp \
-o go-template='{{(index .spec.ports 0).nodePort}}')

$ echo NODE_PORT=$NODE_PORT
NODE_PORT=31915

3. Запустите команду curl. Выполните команду curl несколько раз, чтобы запросить службу. Если вы запустите ее несколько раз, то увидите, что она обращается к разным подам. Именно так можно понять, что балансировщик нагрузки работает:

$ curl $(minikube ip):$NODE_PORT
Hello Kubernetes bootcamp!|Running on:kubernetes-bootcamp-5b48cfdbd-9j4xp|v=1

Уменьшение масштаба приложения

Чтобы масштабировать количество наборов реплик ReplicaSets, определенных в развертывании, просто уменьшите количество реплик.

1. Уменьшите количество реплик. Введите приведенную далее команду, чтобы изменить количество реплик для развертывания на 2:

$ kubectl scale deployments/kubernetes-bootcamp --replicas=2
deployment.extensions/kubernetes-bootcamp scaled

2. Проверьте развертывание. Чтобы убедиться, что развертывание установлено на 2 и запущены только два модуля, введите следующее: