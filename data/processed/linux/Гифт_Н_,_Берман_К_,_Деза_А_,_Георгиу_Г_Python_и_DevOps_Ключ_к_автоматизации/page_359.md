---
source_image: page_359.png
page_number: 359
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.95
tokens: 7421
characters: 1819
timestamp: 2025-12-24T03:10:12.622967
finish_reason: stop
---

Выполните команду kompose convert для создания файлов манифестов Kubernetes на основе имеющегося файла docker_compose.yaml:

$ kompose convert
INFO Kubernetes file "app-service.yaml" created
INFO Kubernetes file "db-service.yaml" created
INFO Kubernetes file "redis-service.yaml" created
INFO Kubernetes file "app-deployment.yaml" created
INFO Kubernetes file "db-deployment.yaml" created
INFO Kubernetes file "dbdata-persistentvolumeclaim.yaml" created
INFO Kubernetes file "migrations-deployment.yaml" created
INFO Kubernetes file "redis-deployment.yaml" created
INFO Kubernetes file "worker-deployment.yaml" created

Теперь можно удалить файл docker-compose.yaml:

$ rm docker-compose.yaml

Развертывание манифестов Kubernetes на локальном кластере Kubernetes, основанном на minikube

Наш следующий шаг — развертывание манифестов Kubernetes на локальном кластере Kubernetes, основанном на minikube.

Для запуска minikube на macOS там должен быть предварительно установлен VirtualBox. Скачайте пакет VirtualBox для macOS со страницы загрузки (https://oreil.ly/BewRq), установите его, а затем переместите в /usr/local/bin/minikube, чтобы сделать исполняемым. Учтите, что на момент написания данной книги пакет minikube устанавливается с кластером Kubernetes версии 1.15. Чтобы следить за ходом рассмотрения данных примеров, укажите при установке minikube желаемую версию Kubernetes:

$ minikube start --kubernetes-version v1.15.0
😄 minikube v1.2.0 on darwin (amd64)
🔥 Creating virtualbox VM (CPUs=2, Memory=2048MB, Disk=20000MB) ...
🐳 Configuring environment for Kubernetes v1.15.0 on Docker 18.09.6
💾 Downloading kubeadm v1.15.0
💾 Downloading kubelet v1.15.0
🚜 Pulling images ...
🚀 Launching Kubernetes ...
⌛ Verifying: apiserver proxy etcd scheduler controller dns
🏁 Done! kubectl is now configured to use "minikube"