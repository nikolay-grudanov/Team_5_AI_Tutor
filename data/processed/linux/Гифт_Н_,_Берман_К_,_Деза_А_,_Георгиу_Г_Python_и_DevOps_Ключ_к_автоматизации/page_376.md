---
source_image: page_376.png
page_number: 376
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.68
tokens: 7464
characters: 1587
timestamp: 2025-12-24T03:10:47.874020
finish_reason: stop
---

gcp:project: The Google Cloud project to deploy into: pythonfordevops-gke-pulumi
Saved config

Your new project is ready to go!

To perform an initial deployment, run the following commands:

1. virtualenv -p python3 venv
2. source venv/bin/activate
3. pip3 install -r requirements.txt

Then, run 'pulumi up'.

Команда pulumi new создала следующие файлы:

$ ls -la
ls -la
total 40
drwxr-xr-x 7 ggheo staff 224 Jul 16 15:08 .
drwxr-xr-x 6 ggheo staff 192 Jul 16 15:06 ..
-rw------- 1 ggheo staff 12 Jul 16 15:07 .gitignore
-rw-r--r-- 1 ggheo staff 50 Jul 16 15:08 Pulumi.dev.yaml
-rw------- 1 ggheo staff 107 Jul 16 15:07 Pulumi.yaml
-rw------- 1 ggheo staff 203 Jul 16 15:07 __main__.py
-rw------- 1 ggheo staff 34 Jul 16 15:07 requirements.txt

Далее мы воспользуемся примером gcp-ru-gke из репозитория GitHub примеров Pulumi (https://oreil.ly/SIT-v).

Скопируйте файлы *.py и requirements.txt из examples/gcp-ru-gke в текущий каталог:

$ cp ~/pulumi-examples/gcp-ru-gke/*.py .
$ cp ~/pulumi-examples/gcp-ru-gke/requirements.txt .

Настройте все относящиеся к GCP переменные, необходимые для работы Pulumi в GCP:

$ pulumi config set gcp:project pythonfordevops-gke-pulumi
$ pulumi config set gcp:zone us-west1-a
$ pulumi config set password --secret PASS_FOR_KUBE_CLUSTER

Создайте и начните использовать виртуальную среду Python, установите объявленные в файле requirements.txt зависимости, после чего загрузите кластер GKE, описанный в файле main.py, с помощью команды pulumi up:

$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
$ pulumi up