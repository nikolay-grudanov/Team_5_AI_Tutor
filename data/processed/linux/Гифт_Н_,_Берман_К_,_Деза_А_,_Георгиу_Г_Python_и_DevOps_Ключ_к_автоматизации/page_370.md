---
source_image: page_370.png
page_number: 370
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.70
tokens: 7387
characters: 1394
timestamp: 2025-12-24T03:10:40.468979
finish_reason: stop
---

Расшифровываем зашифрованный файл с помощью sops и пропускаем его через bash:

$ sops -d create_docker_credentials_secret.sh.enc | bash - secret/myregistrykey created

Просматриваем объект Secret:

$ kubectl get secrets myregistrykey -oyaml
apiVersion: v1
data:
  .dockerconfigjson: eyJhdXRocyI6eyJkb2NrZXIuaW8iO
kind: Secret
metadata:
  creationTimestamp: "2019-07-17T22:11:56Z"
  name: myregistrykey
  namespace: default
  resourceVersion: "16062"
  selfLink: /api/v1/namespaces/default/secrets/myregistrykey
  uid: 47d29ffc-69e4-41df-a237-1138cd9e8971
type: kubernetes.io/dockerconfigjson

Единственное изменение, которое необходимо внести в манифест развертывания процесса-исполнителя, — следующие строки:

    imagePullSecrets:
    - name: myregistrykey

Вставить их надо сразу вслед за строкой:

    restartPolicy: Always

Удалите развертывание процесса-исполнителя и создайте его заново:

$ kubectl delete -f worker-deployment.yaml
deployment.extensions "worker" deleted

$ kubectl create -f worker-deployment.yaml
deployment.extensions/worker created

Теперь модуль процесса-исполнителя находится в состоянии Running без каких-либо ошибок:

$ kubectl get pods
NAME                   READY   STATUS    RESTARTS   AGE
db-67659d85bf-vrnw7    1/1     Running   1          22h
redis-c6476fbff-8kpqz  1/1     Running   1          21h
worker-7dbf5ff56c-hga37 1/1     Running   0          4m53s