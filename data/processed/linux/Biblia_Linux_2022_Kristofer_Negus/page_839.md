---
source_image: page_839.png
page_number: 839
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.58
tokens: 7561
characters: 2083
timestamp: 2025-12-24T05:08:50.069311
finish_reason: stop
---

Server Version: version.Info{Major:"1", Minor:"17",
GitVersion:"v1.17.2",
GitCommit:"59603c6e503c87169aea6106f57b9f242f64df89",
GitTreeState:"clean", BuildDate:"2020-01-18T23:22:30Z",
GoVersion:"go1.13.5", Compiler:"gc", Platform:"linux/amd64"}

Развертывание приложения Kubernetes

Запросы на запуск контейнерных приложений (в виде подов) и управление ими в кластере Kubernetes называются развертыванием. После создания развертывания кластер Kubernetes должен убедиться, что запрошенные поды всегда работают. Делает это он так:

● готовится к созданию развертывания через сервер API;
● запрашивает у планировщика запуск необходимых контейнеров из каждого пода на доступных рабочих узлах;
● наблюдает за подами, чтобы убедиться, что они продолжают работать в соответствии с запросом;
● запускает новый экземпляр пода (на том же или другом узле) в случае сбоя модуля (например, если контейнер перестает работать).

Далее показан пример создания простого развертывания из образа контейнера. В этом примере вы просто даете ему имя и определяете образ контейнера. Остальные параметры развертывания заполняются из значений по умолчанию.

1. Создайте развертывание. Чтобы запустить развертывание, которое извлекает контейнер kubernetesbootcamp с именем развертывания kubernetes bootcamp, введите следующее:

$ kubectl create deployment kubernetes-bootcamp \
    --image=gcr.io/google-samples/kubernetes-bootcamp:v1
deployment.apps/kubernetes-bootcamp created

2. Перечислите развертывания. Чтобы убедиться, что развертывание существует (а также имеет один запрошенный инстанс и один запущенный), введите следующее:

$ kubectl get deployments
NAME                READY   UP-TO-DATE   AVAILABLE   AGE
kubernetes-bootcamp 1/1     1             1           4m38s

3. Просмотрите сведения о развертывании. Чтобы просмотреть подробные сведения о развертывании, введите следующие данные:

$ kubectl describe deployments kubernetes-bootcamp
Name:                 kubernetes-bootcamp
Namespace:            default
...
Replicas:      1 desired | 1 updated | 1 total | 1 available | 0 unavailable
...