---
source_image: page_383.png
page_number: 383
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.45
tokens: 7510
characters: 2090
timestamp: 2025-12-24T03:11:00.313405
finish_reason: stop
---

TargetPort: 5000/TCP
NodePort: 5000 31305/TCP
Endpoints: 10.56.1.6:5000,10.56.2.12:5000
Session Affinity: None
External Traffic Policy: Cluster
Events:
Type    Reason        Age   From                Message
----    ------        ----  ------              --------
Normal  EnsuringLoadBalancer 72s  service-controller  Ensuring load balancer
Normal  EnsuredLoadBalancer 33s  service-controller  Ensured load balancer

Проверяем работу приложения, обращаясь к URL конечной точки, в основе которого лежит соответствующий LoadBalancer Ingress IP-адрес http://34.83.242.171:5000.

Мы продемонстрировали создание таких объектов Kubernetes, как Deployment, Service и Secret, из исходных файлов манифестов Kubernetes. По мере усложнения приложения начнут проявляться ограничения этого подхода, поскольку будет все сложнее настраивать эти файлы для каждой среды (например, предэксплуатационного тестирования, интеграции или промышленной эксплуатации). У каждой среды будет свой набор значений среды и секретных данных, которые придется отслеживать. В целом отслеживать, когда какие манифесты были установлены, станет все сложнее. В экосистеме Kubernetes можно найти немало решений этой проблемы, одно из наиболее распространенных — система управления пакетами Helm (https://oreil.ly/duKVw). Ее можно считать эквивалентом систем управления пакетами yum и apt для Kubernetes.

В следующем разделе мы покажем, как в кластере GKE с помощью Helm установить и настроить под свои нужды Prometheus и Grafana.

Установка чартов Helm для Prometheus и Grafana

Серверной части Tiller в текущей версии Helm¹ (v2 на момент написания книги) необходимо предоставить определенные права доступа внутри кластера Kubernetes.

Создаем новую учетную запись сервиса Kubernetes для Tiller и предоставляем ей нужные права:

$ kubectl -n kube-system create sa tiller

$ kubectl create clusterrolebinding tiller \
    --clusterrole cluster-admin \
_____________________
¹ Начиная с версии 3, для использования Helm в кластере больше не требуется устанавливать Tiller и команды helm init в этой версии уже нет. — Примеч. пер.