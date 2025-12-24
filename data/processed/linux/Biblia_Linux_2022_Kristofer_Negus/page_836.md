---
source_image: page_836.png
page_number: 836
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.74
tokens: 7175
characters: 908
timestamp: 2025-12-24T05:08:36.874243
finish_reason: stop
---

Доступ к кластеру Kubernetes

Далее я расскажу, как получить доступ к кластеру Kubernetes либо через руководство Kubernetes, либо установив и запустив Minikube.

Доступ с помощью руководства

Чтобы запустить интерактивное руководство Kubernetes, перейдите в браузере на страницу kubernetes.io/docs/tutorials/kubernetes-basics/create-cluster/cluster-interactive.
На рис. 30.1 показано начало обучения основам Kubernetes.

![Пошаговое руководство Kubernetes](../images/chapter_30_1.png)

Рис. 30.1. Пошаговое руководство Kubernetes

На этом этапе вы можете следовать инструкциям, данным в руководстве. Поскольку в руководстве запускается живой кластер, можно использовать этот интерфейс и для других команд.

Запуск Minikube

Для запуска Minikube на персональном компьютере требуется выполнить несколько действий.

• Компьютер нужно настроить как гипервизор, чтобы он мог запускать виртуальные машины Minikube.