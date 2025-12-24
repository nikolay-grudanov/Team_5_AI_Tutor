---
source_image: page_374.png
page_number: 374
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.10
tokens: 7467
characters: 1695
timestamp: 2025-12-24T03:10:47.773323
finish_reason: stop
---

Создаем сервис с помощью команды kubectl create:

$ kubectl create -f app-service.yaml
service/app created

$ kubectl get services
NAME           TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)         AGE
app            LoadBalancer   10.99.55.191   <pending>     5000:30097/TCP   2s
db             ClusterIP      10.110.108.96  <none>        5432/TCP        21h
kubernetes     ClusterIP      10.96.0.1      <none>        443/TCP         26h
redis          ClusterIP      10.106.44.183  <none>        6379/TCP        21h

Далее выполните команду:

$ minikube service app

В результате будет открыт используемый по умолчанию браузер с URL http://192.168.99.100:30097/ и отображает домашнюю страницу сайта Flask.

В следующем разделе выполним развертывание тех же самых файлов манифестов Kubernetes для нашего приложения в кластере Kubernetes, выделенном на Google Cloud Platform (GCP), с помощью Pulumi.

Запуск кластера GKE Kubernetes в GCP с помощью Pulumi

В этом разделе воспользуемся примером GKE Pulumi (https://oreil.ly/VGBfF), а также документацией по настройке GCP (https://oreil.ly/kRsFA), так что прочитайте соответствующие документы, перейдя по указанным ссылкам.

Начнем с создания нового каталога:

$ mkdir pulumi_gke
$ cd pulumi_gke

Настройте SDK Google Cloud в соответствии с инструкциями для macOS (https://oreil.ly/f4pPs). Инициализируйте среду GCP с помощью команды gcloud init. Создайте новую конфигурацию и новый проект pythonfordevops-gke-pulumi¹:

$ gcloud init
Welcome! This command will take you through the configuration of gcloud.

¹ Название проекта следует сделать другим, чтобы не возникло конфликта с уже существующим, созданным авторами книги. — Примеч. пер.