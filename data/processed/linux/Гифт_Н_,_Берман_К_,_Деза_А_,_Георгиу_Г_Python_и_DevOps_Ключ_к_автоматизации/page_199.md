---
source_image: page_199.png
page_number: 199
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.99
tokens: 7353
characters: 1521
timestamp: 2025-12-24T03:06:06.510441
finish_reason: stop
---

lifecycleState: ACTIVE
name: helloml
projectId: helloml-xxxxx
projectNumber: '881692383648'
```

5. Возможно, вы захотите проверить, что работаете с нужным проектом. Если нет, можете переключиться на другой с помощью следующей команды:

gcloud config set project $GOOGLE_CLOUD_PROJECT

6. Создайте приложение App Engine:

gcloud app create

При выполнении этой команды у вас будет запрошен регион. Выберите us-central [12]:

Creating App Engine application in project [helloml-xxx]
and region [us-central]....done.
Success! The app is now created.
Please use `gcloud app deploy` to deploy your first app.

7. Клонируйте репозиторий примера приложения hello world:

git clone https://github.com/GoogleCloudPlatform/python-docs-samples

8. Перейдите в каталог репозитория с помощью команды cd:

cd python-docs-samples/appengine/standard_python37/hello_world

9. Обновите образ контейнера Cloudshell (отмечу, что это необязательный шаг):

git clone https://github.com/noahgift/gcp-hello-ml.git
# Отредактируйте .cloudshellcustomimagerepo.json, указав названия проекта и образа
# Совет: включите "Boost Mode" в Cloudshell
cloudshell env build-local
cloudshell env push
cloudshell env update-default-image
# Перезапускаем виртуальную машину Cloudshell

10. Создайте виртуальную среду с помощью команды source:

virtualenv --python $(which python) venv
source venv/bin/activate

Проверьте еще раз, что все работает:

which python
/home/noah_gift/python-docs-samples/appengine/\
    standard_python37/hello_world/venv/bin/python