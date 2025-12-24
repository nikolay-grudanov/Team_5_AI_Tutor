---
source_image: page_377.png
page_number: 377
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.46
tokens: 7522
characters: 1686
timestamp: 2025-12-24T03:10:51.024328
finish_reason: stop
---

Не забудьте активировать API Kubernetes Engine, связав его с учетной записью биллинга Google в веб-консоли GCP.

Теперь кластер GKE виден в консоли GCP (https://oreil.ly/Su5FZ).

Для взаимодействия с только что выделенным кластером GKE сгенерируйте подходящую конфигурацию kubectl и начните ее использовать. Удобно, что программа Pulumi может экспортить конфигурацию kubectl в виде выходного ресурса:

$ pulumi stack output kubeconfig > kubeconfig.yaml
$ export KUBECONFIG=./kubeconfig.yaml

Выводим список узлов, из которых состоит наш кластер GKE:

$ kubectl get nodes
NAME                                 STATUS   ROLES    AGE
VERSION
gke-gke-cluster-ea17e87-default-pool-fd130152-30p3   Ready   <none>   4m29s
    v1.13.7-gke.8
gke-gke-cluster-ea17e87-default-pool-fd130152-kf9k   Ready   <none>   4m29s
    v1.13.7-gke.8
gke-gke-cluster-ea17e87-default-pool-fd130152-x9dx   Ready   <none>   4m27s
    v1.13.7-gke.8

Развертывание примера приложения Flask в GKE

Воспользуемся теми же самыми манифестами Kubernetes, что и в примере minikube, и развернем их в кластере Kubernetes в GKE с помощью команды kubectl. Начнем с создания развертывания и сервиса redis:

$ kubectl create -f redis-deployment.yaml
deployment.extensions/redis created

$ kubectl get pods
NAME                                 READY   STATUS    RESTARTS   AGE
canary-aqw8jtfo-f54b9749-q5wqj      1/1     Running   0          5m57s
redis-9946db5cc-8g6zz              1/1     Running   0          20s

$ kubectl create -f redis-service.yaml
service/redis created

$ kubectl get service redis
NAME    TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
redis   ClusterIP   10.59.245.221 <none>       6379/TCP   18s