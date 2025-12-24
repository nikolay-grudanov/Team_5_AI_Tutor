---
source_image: page_843.png
page_number: 843
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.19
tokens: 7584
characters: 2121
timestamp: 2025-12-24T05:08:59.828916
finish_reason: stop
---

$ kubectl get pods
NAME                                 READY   STATUS    RESTARTS   AGE
kubernetes-bootcamp-765bf4c7b4-fdl96   1/1     Running   0          26m

2. Проверьте службы. Введите приведенные далее команды, чтобы увидеть службы, работающие в пространстве имен default. Обратите внимание на то, что доступна только служба kubernetes и нет никакой службы, предоставляющей доступ к модулю kubernetes-bootcamp за пределами кластера:

$ kubectl get services
NAME      TYPE           CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   31m

3. Создайте службу. Создайте службу, которая использует NodePort, чтобы сделать под доступным с IP-адреса на хосте по определенному номеру порта (8080). Например, введите команду

$ kubectl expose deployment/kubernetes-bootcamp \
    --type="NodePort" --port 8080
service/kubernetes-bootcamp exposed

4. Просмотрите новую службу. Введите приведенную далее команду, чтобы увидеть IP-адрес (10.96.66.230) и номер порта (8080), с которого служба становится доступной на хосте:

$ kubectl get services
NAME      TYPE           CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   33m
kubernetes-bootcamp   NodePort   10.96.66.230   <none>   8080:32374/
TCP 5s
$ kubectl describe services/kubernetes-bootcamp
Name:                 kubernetes-bootcamp
Namespace:            default
Labels:               app=kubernetes-bootcamp
Annotations:          <none>
Selector:             app=kubernetes-bootcamp
Type:                 NodePort
IP:                   10.96.66.230
Port:                 <unset>  8080/TCP
TargetPort:           8080/TCP
NodePort:             <unset>  30000/TCP
Endpoints:            172.17.0.6:8080
Session Affinity:     None
External Traffic Policy: Cluster

5. Назначьте порт для узла. Чтобы получить порт, назначенный службе, и установить переменную $NODE_PORT в это значение, введите следующее:

$ export NODE_PORT=$(kubectl get services/kubernetes-bootcamp \
-o go-template='{{(index .spec.ports 0).nodePort}}')
$ echo NODE_PORT=$NODE_PORT
NODE_PORT=30000