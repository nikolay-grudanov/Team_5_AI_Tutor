---
source_image: docs_tutorials-evolution_list_topics_monitoring-and-logging__client-log__docker-fluent-bit.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 58.31
tokens: 19087
characters: 13047
timestamp: 2025-12-24T06:04:26.417716
finish_reason: stop
---

### Передача логов с виртуальной машины с помощью Docker-контейнера плагина Fluent Bit

#### Эта статья полезна?

Передача логов в сервис «Клиентское логирование» с помощью Docker-контейнера доступна для разных операционных систем. В этой инструкции мы приводим пример настройки отправки логов на созданной виртуальной машине.

#### Перед началом работы

1. **Создайте и настройте лог-группу.**
2. **Создайте сервисный аккаунт.** В блоке Доступы и роли выберите роли:
   - в блоке Проект — «Пользователь сервисов»;
   - в блоке Сервисы — «logaaS.writer».
3. Для сервисного аккаунта создайте ключи доступа.
4. **Создайте виртуальную машину** Ubuntu 22.04.
5. Подключитесь к созданной виртуальной машине по SSH.

#### Шаг 1. Установка Docker

1. Установите необходимые зависимости:

```sh
sudo apt update
sudo apt install ca-certificates curl gnupg software-properties-common
```

2. Установите ключ GPG:

```sh
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

3. Добавьте Docker-репозиторий:

```sh
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

4. Установите Docker:

```sh
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

5. Запустите Docker как службу:

```sh
sudo systemctl enable docker # Enable auto-start on boot
sudo systemctl start docker # Start Docker immediately
```

6. Проверьте, что Docker запущен:

```sh
sudo docker run hello-world
```

При проверке появится сообщение с подтверждением успешного запуска.

#### Шаг 2. Определение структуры проекта

Для записи логов через Docker-образ создайте простой проект, который будет включать в себя:

- генератор логов,
- настройки программы логирования fluent-bit,
- файл docker-compose, который все объединит.

Корневая рабочая директория проекта — /usr/local/bin/myproject :

```
.
├── app
│   ├── Dockerfile
│   └── log_generator.py
├── docker-compose.yml
├── fluent-bit-settings
│   ├── fluent-bit.conf
│   ├── fluent-bit.conf
│   ├── parsers.conf
│   └── plugins.conf
```

#### Шаг 3. Создание приложения — тестового источника логов

1. Создайте рабочую директорию /usr/local/bin/myproject/app , в которой нужно описать структуру приложения и файлы с настройками:

```
.
├── app
│   ├── Dockerfile
│   └── log_generator.py
```

2. Создайте скрипт-генератор логов log_generator.py :

```python
import random
import json
import socket
import os
from datetime import datetime, timezone
import time

LOG_LEVELS = ['DEBUG', 'INFO', 'WARN', 'ERROR', 'FATAL']
MESSAGE_TEMPLATES = [
    "Access denied [ip: {ip}]",
    "Processing request from user {user}",
    "Failed to connect to database {db}",
    "Connection timeout after {sec} seconds",
    "File {file} not found",
    "Authentication failed for {service}",
    "Received {size} bytes from {ip}",
    "Task {task} completed in {ms}ms",
    "Cache miss for key {key}",
    "Starting backup process {job_id}"
]

def generate_message():
    template = random.choice(MESSAGE_TEMPLATES)
    replacements = {
        'id': lambda: random.randint(1000, 9999),
        'user': lambda: f"user_{random.randint(100, 999)}",
        'db': lambda: random.choice(["primary", "replica", "archive"]),
        'sec': lambda: random.randint(1, 30),
        'file': lambda: f"/var/log/manager/[app, 'system', 'auth'][].log",
        'size': lambda: random.randint(512, 4096),
        'ip': lambda: ".".join(map(str, [random.randint(1, 255) for _ in range(4)])),
        'task': lambda: random.choice(["cleanup", "backup", "sync"]),
        'ms': lambda: random.randint(100, 10000),
        'key': lambda: hex(random.getrandbits(128))[2:10],
        'job_id': lambda: f"job_{random.randint(10000, 99999)}"
    }
    return template.format(**{k: v() for k, v in replacements.items() if k in template})

def generate_log():
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", ":"),
        "level": random.choice(LOG_LEVELS),
        "labels": {
            "app": "logger",
            "host": socket.gethostname(),
            "pid": os.getpid(),
            "random": random.randint(1, 1000)
        },
        "message": generate_message()
    }

if __name__ == "__main__":
    while True:
        log_entry = generate_log()
        print(json.dumps(log_entry))
        time.sleep(random.uniform(0.1, 2.0))
```

3. Для запуска этого приложения создайте файл Dockerfile :

```sh
FROM python:3.13-alpine
WORKDIR /app
COPY log_generator.py .
CMD ["python", "./log_generator.py"]
```

4. Соберите образ:

```sh
sudo docker build -t my-app:1.0 .
```

5. Запустите контейнер на основе собранного образа:

```sh
sudo docker run -d --name my_running_appl my-app:1.0
```

Будет выдан ID запущенного контейнера — например, 41f8a276da1dc3b6f03bd98f55e13786c33937a453c40a07701c94fd10d0433b. По этому ID вы сможете посмотреть логи.

6. Запросите логи одним из способов:

- по имени контейнера:

```sh
sudo docker logs -f my_running_appl
```

- по ID контейнера:

```sh
sudo docker logs -f 41f8a276da1dc3b6f03bd98f55e13786c33937a453c40a07701c94fd10d0433b
```

Чтобы остановить запущенный контейнер:

1. Выведите список контейнеров:

```sh
sudo docker ps
```

Список запущенных контейнеров отображается в виде:

<table>
  <tr>
    <th>CONTAINER ID</th>
    <th>IMAGE</th>
    <th>COMMAND</th>
    <th>CREATED</th>
    <th>STATUS</th>
    <th>PORTS</th>
    <th>NAMES</th>
  </tr>
  <tr>
    <td>e75bb4ff0ca0</td>
    <td>my-app:1.0</td>
    <td>"python ./log_generator.py"</td>
    <td>5 seconds ago</td>
    <td>Up 5 seconds</td>
    <td></td>
    <td>my_runnin</td>
  </tr>
</table>

2. Остановите запущенный контейнер одним из способов:

- по имени контейнера:

```sh
sudo docker stop my_running_appl
```

- по ID контейнера:

```sh
sudo docker stop e75bb4ff0ca0
```

Запущенный контейнер можно удалить по его ID:

```sh
sudo docker rm e75bb4ff0ca0
```

#### Шаг 4. Настстройка Fluent Bit для передачи логов

Содержимое директории с настройками fluent-bit будет иметь следующий вид:

```
fluent-bit-settings
├── fluent-bit.conf      - файл с общими настройками
├── logaaS.so           - библиотека фильтра для записи логов в сервис "Клиентское логирование"
├── parsers.conf        - файл с настройками парсеров
├── plugins.conf        - пути к используемым плагинам
```

1. Создайте директорию /usr/local/bin/myproject/fluent-bit-settings :

```sh
sudo mkdir /usr/local/bin/myproject/fluent-bit-settings
```

2. Скачайте плагин logaaS.so , который вместе с fluent-bit будет отвечать за отправку логов в сервис «Клиентское логирование»:

```sh
sudo wget https://github.com/CLOUDdotRu/fluent-bit-plugins/raw/main/logaaS.so -O /usr/local/bin/myproject/fluent-bit-settings/logaaS.so
```

3. Создайте файлы настроек:

```sh
sudo touch /usr/local/bin/myproject/fluent-bit-settings/[fluent-bit,parsers,plugins].conf
```

4. Откройте файл с настройками плагинов plugins.conf с помощью редактора nano :

```sh
sudo nano /usr/local/bin/myproject/fluent-bit-settings/plugins.conf
```

В файл добавьте путь до плагина logaaS.so :

[PLUGINS]
Path /etc/fluent-bit/logaaS.so

5. Откройте файл fluent-bit.conf :

```sh
sudo nano /usr/local/bin/myproject/fluent-bit-settings/fluent-bit.conf
```

Добавьте в него данные в виде:

[SERVICE]
Daemon Off
Flush 1
Log_Level info
Plugins_File plugins.conf
Parsers_File parsers.conf

[INPUT]
Name tail
Path <path-to-log>/logfile.log>
Parser docker

[OUTPUT]
Name logaaS
Match *
address https://console.cloud.ru/
iam_address https://auth.iam.obercloud.ru/
iam_client_id REPLACE_TO_LOGGING_SA_SECRET
iam_client_secret REPLACE_TO_LOGGING_SA_SECRET
default_project_id REPLACE_TO_PROJECT_ID
default_group_id REPLACE_TO_LOG_GROUP_ID
default_labels {"some_label":"default_value"}

Секция [INPUT] указывает на источник логов, а [OUTPUT] — на сервис, в который отправятся логи.

В режиме tail сбор логов в fluent-bit работает по принципу отслеживания новых записей в логах. При перезапуске сервиса данные, обработанные ранее, не отправляются в систему повторно.

Измените файл, подставив в него свои данные:

- <path-to-log>/logfile.log> — путь к файлу-источнику логов: fluent-bit будет сканировать этот файл и отслеживать в нем новые строки.

- REPLACE_TO_LOGGING_SA_KEY_ID и REPLACE_TO_LOGGING_SA_SECRET — Key ID (логин) и Key Secret (пароль) сервисного аккаунта с ролью «logaaS.writer» для получения токена и отправки логов. Проверьте, что у вас есть доступ к проекту, а для вашего сервисного аккаунта выбраны проект «Пользователь сервисов» и роль «logaaS.writer».

- REPLACE_TO_PROJECT_ID и REPLACE_TO_LOG_GROUP_ID — ID проекта и ID лог-группы, в которую будут отправлены логи.

- default_labels — необязательный раздел. В нем вы можете указать метки, которые будут добавлены ко всем логам.

Пример для настройки отправки логов, собираемых из приложения — тестового источника логов:

[SERVICE]
Daemon Off
Flush 1
Log_Level info
Plugins_File plugins.conf
Parsers_File parsers.conf

[INPUT]
Name tail
Path /var/log/myapp.log
Parser docker

[OUTPUT]
Name logaaS
Match *
address https://console.cloud.ru/
iam_address https://auth.iam.obercloud.ru/
iam_client_id 30dc0000000000000000000000000000
iam_client_secret 18a4f000000000000000000000000000
default_project_id 0000000-1111-2222-3333-444444444444
default_group_id aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
default_labels {"source":"docker-image", "logger":"fluentbit"}

6. Откройте файл parsers.conf :

```sh
sudo nano /usr/local/bin/myproject/fluent-bit-settings/parsers.conf
```

Добавьте в файл данные:

[PARSER]
Name docker
Format json
Time_Key time
Time_Format %Y-%m-%dT%H:%M:%S.%3N
Time_Keep On
Time_System_Timezone true

#### Шаг 5. Создание файла Docker Compose

1. Создайте файл docker-compose.yml в корне проекта:

```
.
├── app
│   ├── Dockerfile
│   └── log_generator.py
├── docker-compose.yml
├── fluent-bit-settings
│   ├── fluent-bit.conf
│   ├── fluent-bit.conf
│   ├── parsers.conf
│   └── plugins.conf
```

Файл docker-compose.yml — это YAML-файл, в котором описываются сервисы, сети, тома и настройки для запуска многоконтейнерного приложения через Docker. Он позволяет управлять всеми компонентами приложения одной командой ( docker compose up ), автоматизируя развертывание и связывание контейнеров.

2. Добавьте в файл docker-compose.yml данные в виде:

```yaml
version: '3.8'
services:
  app:
    build:
      context: ./app
      dockerfile: Dockerfile
      volumes:
        - logs:/var/log
    entrypoint: sh -c "python log_generator.py > /var/log/myapp.log 2>&1"
  fluent-bit:
    image: fluent/fluent-bit
    volumes:
      - logs:/var/log
      - fluent-bit-settings:/etc/fluent-bit/
    command: "fluent-bit", "-c", "/etc/fluent-bit/fluent-bit.conf", "-e", "/etc/fluent-bit/lo
volumes:
  logs:
```

В docker-compose.yml мы используем готовый образ fluent/fluent-bit . По желанию вы можете использовать свой образ с настроенным fluent-bit . Установка модуля fluent-bit в систему не требуется.

3. Запустите полученный Docker Compose. Чтобы запустить его в фоновом режиме, добавьте к команде флаг -d :

```sh
sudo docker compose up -d
```

Docker загрузит недостающие образы и запустит контейнеры:

```
[+] Running 2/2
✔ Container myproject-fluent-bit-1 started
✔ Container myproject-app-1 started
```

4. Если запущенные контейнеры больше не нужны, остановите их:

```sh
sudo docker compose stop
```

5. Удалите неиспользованные контейнеры:

```sh
sudo docker compose down
```

Docker удалит неиспользованные контейнеры:

```
[+] Running 3/3
✔ Container myproject-app-1 Removed
✔ Container myproject-fluent-bit-1 Removed
✔ Network myproject_default Removed
```

6. Кроме контейнеров и сетей вы можете удалить volumes:

```sh
sudo docker compose down --v
```

#### Шаг 6. Просмотр логов

В случае успешного старта Docker-образов логи появятся в сервисе «Клиентское логирование» вскоре после старта приложения.

Вы можете посмотреть логи в лог-группах. Логи можно отфильтровать с помощью языка фильтрующих выражений и выгрузить как файл.

В режиме tail сбор логов в fluent-bit работает по принципу отслеживания новых записей в логах. При перезапуске сервиса данные, обработанные ранее, не отправляются в систему повторно. Чтобы данные непрерывно поступали в сервис, выберите подходящий сценарий:

- запустите генератор логов в бесконечном цикле, чтобы поддерживать постоянное поступление данных;
- выполняйте генерацию логов пакетами — запускайте скрипт многократно с необходимым интервалом.

Это позволяет исключить дублирование записей и поддерживать актуальность передаваемых данных.

Дополнительно рекомендуется настроить ротацию логов, чтобы избежать переполнения диска при длительной работе.

#### После окончания работы

Если виртуальная машина и ее логи стали неактуальными, вы можете удалить их:

- Удалить лог-группу
- Удалить проект
- Удалить виртуальную машину