---
source_image: page_844.png
page_number: 844
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.87
tokens: 7501
characters: 1837
timestamp: 2025-12-24T05:08:53.152166
finish_reason: stop
---

6. Проверьте доступ к службе. Чтобы убедиться, что служба доступна из NodePort, используйте команду curl (применив IP-адрес для своего инстанса Minikube):

$ curl $(minikube ip):$NODE_PORT
Hello Kubernetes bootcamp!|Running on:kubernetes-bootcamp-765bf4c7b4-fdl96|v=1

Метки для службы
Описанный далее процесс используется для добавления метки к существующей службе.

1. Проверьте метку пода. Пока что kubernetes-bootcamp — это единственная метка, присвоенная модулю. Чтобы убедиться в этом, введите следующее:

$ kubectl describe deployment
Name:                kubernetes-bootcamp
Namespace:           default
CreationTimestamp:   Fri, 14 Feb 2020 05:43:49 +0000
Labels:             run=kubernetes-bootcamp
Annotations:        deployment.kubernetes.io/revision: 1

2. Добавьте другую метку. Чтобы у модуля появилась еще одна метка (v1), получите имя пода и добавьте ее следующим образом:

$ export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{. metadata.name }}{{"\n"}}{{end}}')
echo Name of the Pod: $POD_NAME
Name of the Pod: kubernetes-bootcamp-765bf4c7b4-fdl96

$ kubectl label pod $POD_NAME app=v1
pod/kubernetes-bootcamp-765bf4c7b4-fdl96 labeled

3. Проверьте метку и используйте ее. Убедитесь, что метка v1 назначена поду, а затем примените ее для отображения информации о нем:

$ kubectl describe pods $POD_NAME
Name:                kubernetes-bootcamp-765bf4c7b4-fdl96
Namespace:           default
Priority:            0
Node:                minikube/172.17.0.62
Start Time:          Fri, 14 Feb 2020 05:44:08 +0000
Labels:              app=v1
                     pod-template-hash=765bf4c7b4
                     run=kubernetes-bootcamp
$ kubectl get pods -l app=v1
NAME                                 READY   STATUS    RESTARTS
AGE
kubernetes-bootcamp-765bf4c7b4-fdl96   1/1     Running   0
60m