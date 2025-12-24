---
source_image: page_335.png
page_number: 335
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.99
tokens: 7515
characters: 1990
timestamp: 2025-12-24T03:09:41.170139
finish_reason: stop
---

Теперь вы увидите оба тега для образа hello-world-docker:

$ docker images hello-world-docker
REPOSITORY           TAG      IMAGE ID            CREATED             SIZE
hello-world-docker   latest   dbd84c229002        2 minutes ago       97.7MB
hello-world-docker   v1       89bd38cb198f        42 seconds ago      97.7MB

Прежде чем опубликовать образ hello-world-docker в Docker Hub, необходимо также маркировать его названием репозитория Docker Hub, содержащего ваше имя пользователя или название вашей организации. В нашем случае репозиторий называется griggheo/hello-world-docker:

$ docker tag hello-world-docker:latest griggheo/hello-world-docker:latest
$ docker tag hello-world-docker:v1 griggheo/hello-world-docker:v1

Теперь опубликуйте оба тега образа в Docker Hub с помощью команды docker push:

$ docker push griggheo/hello-world-docker:latest
$ docker push griggheo/hello-world-docker:v1

Если вы следили за ходом примера и выполняли все команды, то увидите свой образ Docker опубликованным с обоими тегами в созданном под вашей учетной записью репозитории Docker Hub.

Запуск контейнера Docker из одного образа на другом хост-компьютере

Теперь, когда образ Docker опубликован в Docker Hub, мы готовы похвастаться переносимостью образов Docker, запустив основанный на опубликованном образе контейнер на другом хосте. Для этого мы рассмотрим гипотетический сценарий, в котором нам нужно работать с сотрудником, у которого нет macOS и он разрабатывает программы на ноутбуке под управлением Fedora. Этот сценарий включает извлечение из хранилища кода приложения и его модификацию.

Запускаем в AWS EC2-инстанс, в котором задействуется Linux 2 AMI, основанный на RedHat/CentOS/Fedora, после чего устанавливаем движок Docker. Добавьте пользователя по умолчанию в Linux 2 AMI (ec2-user), в группу docker, чтобы он мог выполнять команды клиента docker:

$ sudo yum update -y
$ sudo amazon-linux-extras install docker
$ sudo service docker start
$ sudo usermod -a -G docker ec2-user