---
source_image: page_923.png
page_number: 923
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.36
tokens: 7338
characters: 1524
timestamp: 2025-12-24T05:10:48.235052
finish_reason: stop
---

10. Чтобы использовать команду curl для просмотра содержимого файла, который вы только что скопировали на веб-сервер, выполните следующую команду:

$ curl localhost
Web server is up

Глава 30. Развертывание приложений в контейнеры с помощью кластера Kubernetes

1. Чтобы получить доступ к инструменту Minikube, выполните один из вариантов:
   а) установите Minikube, как описано на странице kubernetes.io/docs/tasks/ tools/ install-minikube;
   б) получите доступ к удаленному инструменту Minikube, например, через руководство Kubernetes.io на странице kubernetes.io/docs/tutorials/.
2. Чтобы просмотреть версии инструмента Minikube, клиента kubectl и службы Kubernetes, введите следующее:

$ minikube version
$ kubectl version

3. Чтобы развернуть модуль под управлением образа контейнера hello-node, введите следующее:

$ kubectl create deployment hello-node \
    --image=gcr.io/hello-minikube-zero-install/hello-node

4. Чтобы просмотреть развертывание hello-node и подробно описать его, введите следующее:

$ kubectl get deployment
$ kubectl describe deployment hello-node

5. Чтобы просмотреть текущий набор реплик, связанный с развертыванием hello-node, введите следующее:

$ kubectl get rs

6. Чтобы увеличить развертывание hello-node до трех копий, введите следующую команду:

$ kubectl scale deployments/hello-node --replicas=3

7. Чтобы открыть развертывание hello-node за пределами кластера Kubernetes с помощью LoadBalancer, введите:

$ kubectl expose deployment hello-node \
    --type=LoadBalancer --port=8080