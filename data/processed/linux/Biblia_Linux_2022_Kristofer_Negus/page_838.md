---
source_image: page_838.png
page_number: 838
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.90
tokens: 7582
characters: 1961
timestamp: 2025-12-24T05:08:50.368577
finish_reason: stop
---

Запуск руководства Kubernetes Basics

Руководство Kubernetes Basics описывает набор команд, с помощью которых начинается знакомство с Kubernetes: kubernetes.io/docs/tutorials/kubernetes-basics/create-cluster/cluster-interactive.

Далее мы познакомимся с первыми пятью модулями руководства Kubernetes Basics.

Если используете интерактивную систему непосредственно со страниц руководства Kubernetes, продолжайте там же и запустите Minikube (minikube start). Если вы задействуете Minikube с виртуальной машины, уже работающей на ноутбуке, также можете выполнить следующие шаги, так как оба варианта применяют Minikube.

Информация о кластере

Запустите следующие команды, чтобы получить основную информацию о своем кластере.

1. Версия Minikube. Чтобы узнать версию minikube, введите следующее:

$ minikube version
minikube version: v1.7.2
commit: 50d543b5fcb0e1c0d7c27b1398a9a9790df09dfb

2. Информация о кластере. Чтобы увидеть URL-адрес, с которого доступны службы Kubernetes master и DNS, введите следующее:

$ kubectl cluster-info
Kubernetes master is running at https://192.168.39.150:8443
KubeDNS is running at
https://192.168.39.150:8443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.

3. Информация об узлах. Чтобы увидеть количество запущенных узлов (в Minikube только один мастер-узел) и их состояние, введите следующее:

$ kubectl get nodes
NAME      STATUS   ROLES    AGE   VERSION
minikube  Ready    master   23m   v1.17.2

4. Версии кластера и клиента. Чтобы перечислить версии клиента kubectl и кластера Kubernetes (и убедиться, что они находятся в пределах одной версии), введите следующее:

$ kubectl version
Client Version: version.Info{Major:"1", Minor:"17",
GitVersion:"v1.17.2",
GitCommit:"59603c6e503c87169aea6106f57b9f242f64df89",
GitTreeState:"clean", BuildDate:"2020-01-18T23:30:10Z",
GoVersion:"go1.13.5", Compiler:"gc", Platform:"linux/amd64"}