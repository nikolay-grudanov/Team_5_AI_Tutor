---
source_image: page_366.png
page_number: 366
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.21
tokens: 7356
characters: 1449
timestamp: 2025-12-24T03:10:27.814244
finish_reason: stop
---

Прежде всего преобразуем строку пароля в кодировку base64:

$ echo MYPASS | base64
MYPASSBASE64

Далее создаем файл манифеста, в котором описывается объект Secret Kubernetes, который мы хотим создать. Поскольку кодировка base64 нашего пароля не обеспечивает безопасность, воспользуемся sops для редактирования и сохранения зашифрованного файла манифеста secrets.yaml.enc:

$ sops --pgp E14104A0890994B9AC9C9F6782C1FF5E679EFF32 secrets.yaml.enc

Добавьте в редакторе следующие строки:

apiVersion: v1
kind: Secret
metadata:
  name: fbe-secret
type: Opaque
data:
  dbpass: MYPASSBASE64

Теперь можно вносить файл secrets.yaml.enc в систему контроля версий, поскольку в нем содержится зашифрованная версия значения пароля в кодировке base64.

Для расшифровки зашифрованного файла можно использовать команду sops -d:

$ sops -d secrets.yaml.enc
apiVersion: v1
kind: Secret
metadata:
  name: fbe-secret
type: Opaque
data:
  dbpass: MYPASSBASE64

Направляем с помощью | вывод команды sops -d в команду kubectl create -f для создания объекта Secret Kubernetes:

$ sops -d secrets.yaml.enc | kubectl create -f -
secret/fbe-secret created

Просматриваем объекты Secret Kubernetes и получаем описание созданного объекта Secret:

$ kubectl get secrets
NAME                TYPE                                  DATA   AGE
default-token-k7652  kubernetes.io/service-account-token  3      3h19m
fbe-secret          Opaque                                1      45s