---
source_image: page_381.png
page_number: 381
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.66
tokens: 7255
characters: 1155
timestamp: 2025-12-24T03:10:44.833557
finish_reason: stop
---

TargetPort:      5432/TCP
Endpoints:       10.56.2.5:5432
Session Affinity: None
Events:          <none>

Создаем объект Secret на основе значения пароля базы данных в кодировке base64. Значение пароля в виде открытого текста сохраняется в файле, зашифрованном с помощью sops:

$ echo MYNEWPASS | base64
MYNEWPASSBASE64

$ sops secrets.yaml.enc

apiVersion: v1
kind: Secret
metadata:
  name: fbe-secret
type: Opaque
data:
  dbpass: MYNEWPASSBASE64

$ sops -d secrets.yaml.enc | kubectl create -f -
secret/fbe-secret created

kubectl describe secret fbe-secret
Name:        fbe-secret
Namespace:   default
Labels:      <none>
Annotations: <none>

Type:  Opaque

Data
===
dbpass:  21 bytes

Создайте еще один объект Secret для учетных данных Docker Hub:

$ sops -d create_docker_credentials_secret.sh.enc | bash -
secret/myregistrykey created

Поскольку мы рассматриваем сценарий развертывания приложения в GKE для целей промышленной эксплуатации, задаем параметр replicas в файле worker-deployment.yaml равным 3, чтобы в любой момент работали три модуля процесса-исполнителя:

$ kubectl create -f worker-deployment.yaml
deployment.extensions/worker created