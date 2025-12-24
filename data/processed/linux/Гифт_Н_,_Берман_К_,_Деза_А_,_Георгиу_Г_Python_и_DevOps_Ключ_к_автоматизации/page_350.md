---
source_image: page_350.png
page_number: 350
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.42
tokens: 7362
characters: 1801
timestamp: 2025-12-24T03:10:01.147684
finish_reason: stop
---

Removing flask-by-example_worker_1    ... done
Removing flask-by-example_app_1     ... done
Removing flask-by-example_migrations_1 ... done
Removing flask-by-example_redis_1   ... done
Removing postgres                   ... done
Removing network flask-by-example_default

$ source <(sops -d environment.secrets); docker-compose up -d
Creating network "flask-by-example_default" with the default driver
Creating flask-by-example_redis_1     ... done
Creating postgres                     ... done
Creating flask-by-example_migrations_1 ... done
Creating flask-by-example_worker_1    ... done
Creating flask-by-example_app_1       ... done

Обратите внимание на то, как просто теперь остановить и запустить набор контейнеров Docker с помощью docker-compose.

Даже если вам нужен всего один контейнер Docker, все равно имеет смысл включить его в файл docker-compose.yaml и запускать с помощью команды docker-compose up -d. Это облегчит задачу, если вы захотите добавить второй контейнер, а также послужит маленьким примером инфраструктуры как кода, в котором docker-compose.yaml будет отражать состояние локальной схемы организации Docker для вашего приложения.

Портирование сервисов docker-compose на новый хост-компьютер и операционную систему

А сейчас покажем, как перенести организованную нами структуру docker-compose из предыдущего раздела на сервер под управлением Ubuntu 18.04.

Запустите Amazon EC2-инстанс с Ubuntu 18.04 и установите там docker-engine и docker-compose:

$ sudo apt-get update
$ sudo apt-get remove docker docker-engine docker.io containerd runc
$ sudo apt-get install \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg-agent \
  software-properties-common
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo add-apt-repository \