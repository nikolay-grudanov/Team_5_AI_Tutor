---
source_image: page_198.png
page_number: 198
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.63
tokens: 7315
characters: 1166
timestamp: 2025-12-24T03:06:04.163638
finish_reason: stop
---

в репозиторий GitHub. Называется он cloudbuild.yaml. Весь исходный код данного проекта вы можете посмотреть в этом репозитории Git (https://oreil.ly/vxsnc):

steps:
- name: python:3.7
  id: INSTALL
  entrypoint: python3
  args:
    - '-m'
    - 'pip'
    - 'install'
    - '-t'
    - '.'
    - '-r'
    - 'requirements.txt'
- name: python:3.7
  entrypoint: ./pylint_runner
  id: LINT
  waitFor:
    - INSTALL
- name: "gcr.io/cloud-builders/gcloud"
  args: ["app", "deploy"]
timeout: "1600s"
images: ['gcr.io/$PROJECT_ID/pylint']

Отмечу, что файл cloudbuild.yaml устанавливает пакеты, указанные в файле requirements.txt, а также выполняет команду gcloud app deploy, развертывающую приложение App Engine при внесении в GitHub:

Flask==1.0.2
gunicorn==19.9.0
pylint==2.3.1

Вот пошаговое описание настройки этого проекта.

1. Создайте проект.
2. Активируйте облачную командную оболочку.
3. Загляните в начальное руководство из документации Python 3 App Engine (https://oreil.ly/zgf5J).
4. Выполните команду describe:

verify project is working
```bash
gcloud projects describe $GOOGLE_CLOUD_PROJECT
```
output of command:
```bash
createTime: '2019-05-29T21:21:10.187Z'