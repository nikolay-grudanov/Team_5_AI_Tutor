---
source_image: page_409.png
page_number: 409
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.48
tokens: 7287
characters: 1122
timestamp: 2025-12-24T03:11:35.069567
finish_reason: stop
---

Установите k3s с помощью команды k3sup install:

$ k3sup install --ip 35.167.68.86 --user ubuntu
ВЫВОД ОПУЩЕН
Saving file to: kubeconfig

Взглянем на содержимое файла kubeconfig:

$ cat kubeconfig
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: BASE64_FIELD
    server: https://35.167.68.86:6443
    name: default
contexts:
- context:
    cluster: default
    user: default
    name: default
current-context: default
kind: Config
preferences: {}
users:
- name: default
  user:
    password: OBFUSCATED
    username: admin

Сделайте так, чтобы переменная среды KUBECONFIG указывала на локальный файл kubeconfig, и попробуйте выполнить команды kubectl для удаленного кластера k3s:

$ export KUBECONFIG=./kubeconfig

$ kubectl cluster-info
Kubernetes master is running at https://35.167.68.86:6443
CoreDNS is running at
https://35.167.68.86:6443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.

$ kubectl get nodes
NAME           STATUS   ROLES    AGE   VERSION
ip-10-0-0-185 Ready    master   10m   v1.14.6-k3s.1