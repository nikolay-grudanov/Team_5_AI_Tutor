---
source_image: page_336.png
page_number: 336
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.97
tokens: 7730
characters: 2180
timestamp: 2025-12-24T03:09:54.194418
finish_reason: stop
---

Не забудьте извлечь код приложения на удаленном EC2-инстансе. В данном случае код состоит из одного файла app.py.

Далее запустите контейнер Docker, основанный на опубликованном нами в Docker Hub образе. Единственное отличие — в качестве аргумента команды docker run используется образ griggheo/hello-world-docker:v1, а не просто griggheo/hello-world-docker.

Выполните команду docker login, а затем:

$ docker run --rm -d -v `pwd`:/app -p 5000:5000 griggheo/hello-world-docker:v1

Unable to find image 'griggheo/hello-world-docker:v1' locally
v1: Pulling from griggheo/hello-world-docker
921b31ab772b: Already exists
1a0c422ed526: Already exists
ec0818a7bbe4: Already exists
b53197ee35ff: Already exists
8b25717b4dbf: Already exists
d997915c3f9c: Pull complete
f1fd8d3cc5a4: Pull complete
10b64b1c3b21: Pull complete
Digest: sha256:af8b74f27a0506a0c4a30255f7ff563c9bf858735baa610fda2a2f638ccfe36d
Status: Downloaded newer image for griggheo/hello-world-docker:v1
9d67dc321ffb49e5e73a455bd80c55c5f09febc4f2d57112303d2b27c4c6da6a

Обратите внимание на то, что движок Docker на EC2-инстансе понимает, что образа Docker на локальной машине нет, и скачивает его из Docker Hub, после чего запускает контейнер, основанный на только что скачанном образе.

На этом этапе был открыт доступ к порту 5000 посредством добавления правила в соответствующую этому EC2-инстансу группу безопасности. Зайдите на URL http://54.187.189.51:5000¹ (где http://54.187.189.51 — внешний IP-адрес этого EC2-инстанса) — и вы увидите приветствие Hello, World! (from a Docker container with modified code).

При модификации кода приложения на удаленном EC2-инстансе запущенный внутри контейнера Docker сервер Flask автоматически перезагружает модифицированный код. Поменяйте приветствие на Hello, World! (from a Docker container on an EC2 Linux 2 AMI instance) — и вы увидите из журналов контейнера Docker, что сервер Flask перезагрузил приложение:

[ec2-user@ip-10-0-0-111 hello-world-docker]$ docker ps
CONTAINER ID   IMAGE                  COMMAND                  CREATED
9d67dc321ffb   griggheo/hello-world-docker:v1   "python app.py"   3 minutes ago

¹ Это просто пример URL, у вас будет другой IP-адрес.