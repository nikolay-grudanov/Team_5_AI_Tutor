---
source_image: page_841.png
page_number: 841
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.06
tokens: 7622
characters: 2232
timestamp: 2025-12-24T05:09:00.269013
finish_reason: stop
---

$ kubectl get pods
NAME                                 READY   STATUS    RESTARTS   AGE
kubernetes-bootcamp-69fbc6f4cf-njc4b   1/1     Running   0          12m

$ kubectl describe pod kubernetes-bootcamp-69fbc6f4cf-njc4b
Name:           kubernetes-bootcamp-69fbc6f4cf-njc4b
Namespace:      default
Priority:       0
Node:           minikube/192.168.39.150
...
Containers:
  kubernetes-bootcamp:
    Container ID:
    docker://dd24fd43ff19d6cf12f5c759036cee74adcf2d0e2c55a42e...
    Image:         gcr.io/google-samples/kubernetes-bootcamp:v1
    Image ID:      docker-pullable://gcr.io/google-samples...
...
Events:
  Type    Reason     Age   From                   Message
  ----    ------     ----  ----                   --------
  Normal  Scheduled  14m   default-scheduler       Successfully assigned default/kubernetes-bootcamp-69fbc6f4cf-njc4b to minikube
  Normal  Pulled     14m   kubelet, minikube       Container image "gcr.io/google-samples/kubernetes-bootcamp:v1" already present on machine
  Normal  Created    14m   kubelet, minikube       Created container kubernetes-bootcamp
  Normal  Started    14m   kubelet, minikube       Started container kubernetes-bootcamp

В выходных данных в примере видны имя пода, пространство имен, в котором он находится (default), и узел, на котором работает (minikube/192.168.39.150). В разделе Containers содержатся имя запущенного контейнера (docker://dd24fd43ff1...), образ, из которого он получен (...kubernetes-bootcamp:v1), и идентификатор образа для него. В разделе Events, начиная снизу, вы можете увидеть kubelet на узле minikube, который запускает и создает контейнер. Он проверяет образ и обнаруживает, что тот уже находится на узле. Затем он назначает модуль для запуска на этом узле.

4. Подключитесь к поду. Используйте команду curl, чтобы связаться с модулем и заставить его ответить на ваш запрос:

$ export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{. metadata.name }}{{"\n"}}{{end}}') ; \
echo Name of the Pod: $POD_NAME
Name of the Pod: kubernetes-bootcamp-69fbc6f4cf-njc4b

$ curl \
http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME/proxy/
Hello Kubernetes bootcamp!|Running on:kubernetes-bootcamp-5b48cfdcbd-1f9t2|v=1