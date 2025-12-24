---
source_image: page_410.png
page_number: 410
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.73
tokens: 7284
characters: 1303
timestamp: 2025-12-24T03:11:37.902570
finish_reason: stop
---

Следующий этап — установка платформы OpenFaaS на кластере Kubernetes k3s.

Установите утилиту faas-cli в локальной системе под управлением macOS:

$ brew install faas-cli

Создайте права доступа RBAC для Tiller — серверной части Helm:

$ kubectl -n kube-system create sa tiller \
    && kubectl create clusterrolebinding tiller \
    --clusterrole cluster-admin \
    --serviceaccount=kube-system:tiller
serviceaccount/tiller created
clusterrolebinding.rbac.authorization.k8s.io/tiller created

Установите Tiller с помощью команды helm init¹:

$ helm init --skip-refresh --upgrade --service-account tiller

Скачайте, настройте и установите чарт Helm для OpenFaaS:

$ wget \
https://raw.githubusercontent.com/openfaas/faas-netes/master/namespaces.yml

$ cat namespaces.yml
apiVersion: v1
kind: Namespace
metadata:
  name: openfaas
  labels:
    role: openfaas-system
    access: openfaas-system
    istio-injection: enabled
---
apiVersion: v1
kind: Namespace
metadata:
  name: openfaas-fn
  labels:
    istio-injection: enabled
    role: openfaas-fn

$ kubectl apply -f namespaces.yml
namespace/openfaas created
namespace/openfaas-fn created

$ helm repo add openfaas https://openfaas.github.io/faas-netes/
"openfaas" has been added to your repositories

¹ См. сноску на с. 383 в главе 12. — Примеч. пер.