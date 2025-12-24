---
source_image: docs_tutorials-evolution_list_topics_monitoring-and-logging__monitoring__archived-metrics.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 126.66
tokens: 8038
characters: 4935
timestamp: 2025-12-24T06:06:33.094018
finish_reason: stop
---

### Просмотр архивированных метрик в Grafana

С помощью этого руководства вы настроите импорт метрик, архивированных в бакете Object Storage, в VictoriaMetrics, а затем выведете их на дашборд в Grafana.

Вы будете использовать следующие сервисы:

- Docker — система контейнеризации.
- Docker Compose — инструмент для запуска и управления Docker-контейнерами.
- VictoriaMetrics — база данных для хранения и обработки данных в виде временного ряда.
- Grafana — платформа для визуализации, мониторинга и анализа данных.

Шаги:

1. Установите Docker.
2. Создайте файлы Docker Compose и Datasource.
3. Импортируйте метрики в VictoriaMetrics.
4. Создайте дашборд в Grafana.
5. Укажите запрос для отображения метрик.

Перед началом работы

1. Зарегистрируйтесь в личном кабинете Cloud.ru.
   Если вы уже зарегистрированы, войдите под своей учетной записью.
2. Скачайте архивы с метриками из бакета.

1. Установите Docker

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
sudo systemctl start docker   # Start Docker immediately
```

6. Проверьте, что Docker запущен:

```sh
sudo docker run hello-world
```

При проверке появится сообщение с подтверждением успешного запуска.

2. Создайте файлы Docker Compose и Datasource

На этом шаге вы создадите файлы:

- docker-compose.yml — для запуска двух контейнеров: Grafana и VictoriaMetrics.
- datasource.yml — для автоматической настройки подключения Grafana к VictoriaMetrics.

1. Создайте папку со структурой:

```
├── docker-compose.yml
├── grafana/
│   └── provisioning/
│       └── datasources/
│           └── datasource.yml
└── data/
    └── grafana/
        └── victoria-metrics/
```

2. В файл docker-compose.yml добавьте данные в виде:

```yaml
version: '3.8'
services:
  victoriametrics:
    image: victoriametrics/victoria-metrics:latest
    ports:
      - "8428:8428"
    volumes:
      - ./data/victoria-metrics:/victoria-metrics-data
    command:
      - "--storageDataPath=/victoria-metrics-data"
      - "--retentionPeriod=100y" # VictoriaMetrics does not support indefinite retention, but you can
grafana:
  image: grafana/grafana:latest
  container_name: grafana
  ports:
    - "3000:3000"
  volumes:
    - ./data/grafana:/var/lib/grafana
    - ./grafana/provisioning/datasources:/etc/grafana/provisioning/datasources
  restart: unless-stopped
```

3. В файл datasource.yml добавьте данные в виде:

```yaml
apiVersion: 1
datasources:
  - name: Prometheus
    type: prometheus
    url: http://victoriametrics:8428/prometheus
    access: proxy
    isDefault: true
    editable: true
```

3. Импортируйте метрики в VictoriaMetrics

На этом шаге вы импортируете метрики, которые скачали из бакета Object Storage, в VictoriaMetrics. Импортировать можно метрики в форматах .gz или .jsonl.

Запрос для импорта метрик:

Метрики в формате .gz
Метрики в формате .jsonl

```sh
curl -X POST -H 'Content-Encoding: gzip' http://localhost:8428/api/v1/import -T <filename>.gz
```

Где filename — имя файла с метриками.

После этого метрики импортируются в VictoriaMetrics, и вы сможете добавить их на дашборд в Grafana.

4. Создайте дашборд в Grafana

На этом этапе вы создадите дашборд для визуализации метрик в Grafana.

1. Перейдите в Grafana: в адресной строке браузера введите http://localhost:3000/. Логин и пароль по умолчанию: admin / admin .
2. Создайте новый дашборд в Grafana. В разделе Select data source выберите Prometheus — этот источник мы указывали в файле datasource.yml .

Подробнее о создании дашборда в документации Grafana.

5. Укажите запрос для отображения метрик

На этом этапе с помощью запроса вы укажете, какие метрики нужно вывести на созданный дашборд.

1. На вкладке Queries выберите источник данных Prometheus.
2. Укажите запрос — данные, которые нужно вывести на дашборд. Например:

```sh
rate(container_cpu_usage_seconds_total[60s])
```

Подробнее о запросах в документации Grafana.

3. Нажмите Back to dashboard, чтобы вернуться к просмотру дашборда. На нем будут отображаться указанные в запросе метрики. Используйте фильтрацию по временному интервалу, чтобы посмотреть данные за нужный период.

Результат

Вы настроили визуализацию метрик, архивированных в бакете Object Storage, в Grafana.