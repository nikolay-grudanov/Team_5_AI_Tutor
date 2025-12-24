---
source_image: docs_tutorials-evolution_list_topics_monitoring-and-logging__client-log__kubernetes.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 257.63
tokens: 17064
characters: 13426
timestamp: 2025-12-24T06:08:23.566866
finish_reason: stop
---

<h2>Передача логов с кластера Managed Kubernetes</h2>
<p>С помощью инструкции подготовим и настроим передачу логов с кластера Managed Kubernetes в сервис «Клиентское логирование».</p>

<h3>Перед началом работы</h3>
<ol>
<li><b>Создайте и настройте лог-группу.</b></li>
<li><b>Создайте сервисный аккаунт.</b> В блоке Доступы и роли выберите роли:
<ul>
<li>в блоке Проект — «Пользователь сервисов»;</li>
<li>в блоке Сервисы — «logaas.writer».</li>
</ul>
</li>
<li>Для сервисного аккаунта создайте ключи доступа.</li>
</ol>

<h3>Шаг 1. Выбор стратегии логирования</h3>
<p>В инструкции рассмотрим две стратегии настройки логирования — с DaemonSet и с Sidecar.</p>
<p>Отличия между ними:</p>
<table>
<tr>
<th>Характеристика</th>
<th>Подход с DaemonSet</th>
<th>Подход с Sidecar</th>
</tr>
<tr>
<td>Использование ресурсов</td>
<td>1 экземпляр на узел</td>
<td>1 экземпляр на под</td>
</tr>
<tr>
<td>Область сбора логов</td>
<td>Логи всех подов на узле</td>
<td>Только логи текущего пода</td>
</tr>
<tr>
<td>Конфигурация</td>
<td>Централизованная</td>
<td>Индивидуальная для пода</td>
</tr>
<tr>
<td>Оптимальный сценарий</td>
<td>Логирование всего кластера</td>
<td>Изоляция логов отдельных подов</td>
</tr>
<tr>
<td>Масштабируемость</td>
<td>Зависит от количества узлов</td>
<td>Зависит от количества подов</td>
</tr>
<tr>
<td>Задержка логирования</td>
<td>Минимальная (локальный сбор)</td>
<td>Возможна задержка из-за дополнительных шагов (сбор + передача)</td>
</tr>
<tr>
<td>Надежность</td>
<td>Высокая (отказоустойчивость на уровне узла, переживает перезапуски подов)</td>
<td>Зависит от стабильности пода</td>
</tr>
<tr>
<td>Сложность настройки</td>
<td>Проще (единная конфигурация)</td>
<td>Сложнее (индивидуальные настройки)</td>
</tr>
<tr>
<td>Влияние на сеть</td>
<td>Низкое (логи агрегируются на узле)</td>
<td>Выше (каждый sidecar передает логи)</td>
</tr>
<tr>
<td>Гибкость обработки</td>
<td>Ограничена (общие правила)</td>
<td>Высокая (возможность применять уникальные Lua-скрипты или фильтры для каждого пода)</td>
</tr>
<tr>
<td>Безопасность</td>
<td>Риск смешения логов</td>
<td>Изоляция логов в рамках пода (меньше риск несанкционированного доступа и утечки)</td>
</tr>
</table>

<p>Таким образом, вам может подойти:</p>
<ul>
<li>DaemonSet — для централизованного сбора логов всего кластера. Это подходит для мониторинга системных компонентов или всех сервисов на узлах.</li>
<li>Sidecar — для изоляции логов отдельных подов. Например, если вам нужна отдельная обработка логов для критичных микросервисов или мультитенантных сред.</li>
</ul>

<h3>Шаг 2. Определение структуры проекта</h3>
<p>В процессе настройки передачи логов с кластера Managed Kubernetes вы создадите на вашем локальном компьютере или виртуальной машине следующие файлы:</p>
<div class="code-block">
<pre>
├── app/
│   └── generator.py        # Сгенерировать логи
├── fluent-bit-logaas/
│   ├── Dockerfile          # Кастомный образ Fluent Bit с плагином logaas
│   └── Dockerfile         # Dockerfile для сборки fluent-bit-logaas
├── k8s/
│   ├── deployment.yaml     # Базовая конфигурация Kubernetes
│   ├── service.yaml        # Конфигурация сервиса
│   └── logging/
│       ├── fluent-bit/
│       │   ├── daemonset.yaml    # Daemonset для Fluent Bit
│       │   ├── configmap.yaml    # ConfigMap для Fluent Bit
│       │   ├── fluent-bit.conf   # Основной конфиг Fluent Bit
│       │   └── parsers.conf      # Дополнительные парсеры (опционально)
│       └── sidecar/            # Аппернамент поддон с sidecar
└── deployment-with-sidecar.yaml # Deployment app с sidecar-приложениям
</pre>
</div>

<h3>Шаг 3. Подготовка окружения</h3>
<p>Исходные данные для развертывания можно подготовить в любой из сред: Windows, macOS, Linux на локальном устройстве, Linux на виртуальной машине. ПО для управления развертыванием также доступно для всех сред.</p>
<p>Установка Docker</p>
<ul>
<li>Windows/macOS: <a>Docker Desktop</a> (включает Docker Engine);</li>
<li>Linux: <a>Docker Engine</a>.</li>
</ul>
<p>Создание Artifact Registry</p>
<ol>
<li><b>Создайте реестр в Artifact Registry.</b> В примере в инструкции мы назовем его <code>your-registry</code>.</li>
<li>Создайте репозитории:
<ul>
<li>simple-logging-app — для приложения-генератора логов;</li>
<li>fluent-bit-logaas — для кастомизированного Fluent Bit.</li>
</ul>
</li>
</ol>
<p>Пример URL реестра: your-registry.cr.cloud.ru . Замените его на URL вашего реестра.</p>
<p>Настройка кластера Managed Kubernetes</p>
<ol>
<li><b>Создайте кластер Managed Kubernetes.</b></li>
<li><b>Добавьте группу узлов.</b></li>
<li><b>Подключитесь к кластеру.</b></li>
</ol>

<h3>Шаг 4. Создание базового приложения для генерации логов</h3>
<p>Модуль генератора логов app/generator.py :</p>
<div class="code-block">
<pre>
import random
import json
import os
from datetime import datetime, timezone
import time

LOG_LEVELS = ['DEBUG', 'INFO', 'WARN', 'ERROR', 'FATAL']
MESSAGE_TEMPLATES = [
    "data received [ID: {id}]",
    "processing request from user {user}",
    "failed to connect to database {db}",
    "connection timeout {sec} seconds",
    "file {file} not found",
    "Authentication failed for {service}",
    "received (size) bytes from {ip}",
    "task {task} completed in {ms}ms",
    "cache miss for key {key}! [job_id]!"
]

def generate_message():
    template = random.choice(MESSAGE_TEMPLATES)
    replacements = {
        'id': lambda: random.randint(1000, 9999),
        'user': lambda: "user" + random.randint(100, 999),
        'db': lambda: random.choice(["mysql", "replias", "archive"]),
        'sec': lambda: random.randint(1, 30),
        'file': lambda: f"/var/log/random.choice('app', 'system', 'auth').log",
        'service': lambda: random.choice(["API", "SSH", "database"]),
        'size': lambda: random.randint(1, 4096),
        'ip': lambda: ".".join(str(random.randint(1, 255)) for _ in range(4)),
        'task': lambda: random.choice(["cleanup", "backup", "sync"]),
        'ms': lambda: random.randint(100, 5000),
        'key': lambda: hex(random.getrandbits(128))[2:10],
        'job_id': lambda: f"JOB-{random.randint(10000, 99999)}"
    }
    return template.format(**{k: v() for k, v in replacements.items() if k in template})

def generate_log():
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z'),
        "level": random.choice(LOG_LEVELS),
        "label": "loggger",
        "host": socket.gethostname(),
        "pid": os.getpid(),
        "random": random.randint(1, 1000)
    }

if __name__ == "__main__":
    while True:
        log_entry = generate_log()
        print(json.dumps(log_entry))
        time.sleep(random.uniform(0.1, 2.0))
</pre>
</div>
<p>Docker-образ приложения app/Dockerfile :</p>
<div class="code-block">
<pre>
FROM python:3.13-alpine
WORKDIR /app
COPY log_generator.py .
CMD ["python", "-u", "log_generator.py"]
</pre>
</div>

<h3>Шаг 5. Сборка кастомизированного образа Fluent Bit</h3>
<p>Docker-образ с плагином logaas — fluent-bit-logaas/Dockerfile :</p>
<div class="code-block">
<pre>
ARG fluentbit_ver=3.2.0
FROM debian:bullseye-slim as builder
RUN apt-get update &amp;&amp; apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    &amp;&amp; rm -rf /var/lib/apt/lists/*
WORKDIR /build
RUN wget https://github.com/fluent/fluent-bit-plugins/raw/main/logaas.so -O /logaas.so
FROM fluent/fluent-bit:$(fluentbit_ver) as fluentbit
COPY --from-builder /build/logaas.so /fluent-bit/bin/
ENTRYPOINT ["fluent-bit/bin/fluent-bit", "-f", "/fluent-bit/bin/logaas.so"]
CMD ["-d", "/fluent-bit/etc/fluent-bit.conf"]
</pre>
</div>

<h3>Шаг 6. Публикация образов в Artifact Registry</h3>
<p>Сборка и публикация образа приложения:</p>
<div class="code-block">
<pre>
docker build -t your-registry.cr.cloud.ru/simple-logging-app:latest -f app/Dockerfile.app/
docker push your-registry.cr.cloud.ru/simple-logging-app:latest
</pre>
</div>
<p>Сборка и публикация кастомного образа Fluent Bit:</p>
<div class="code-block">
<pre>
docker build -t your-registry.cr.cloud.ru/fluent-bit-logaas:latest -f fluent-bit-logaas/Dockerfile fluent-bit-logaas
docker push your-registry.cr.cloud.ru/fluent-bit-logaas:latest
</pre>
</div>
<p>Не забудьте заменить URL реестра с your-registry.cr.cloud.ru на URL вашего реестра.</p>

<h3>Шаг 7. Подготовка развертывания базового приложения в Managed Kubernetes</h3>
<p>Создайте базовые файлы:</p>
<ul>
<li>k8s/deployment.yaml :</li>
</ul>
<div class="code-block">
<pre>
apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: python-app
  template:
    metadata:
      labels:
        app: python-app
    spec:
      containers:
      - name: main-app
        image: your-registry.cr.cloud.ru/simple-logging-app:latest
        ports:
        - containerPort: 5000
</pre>
</div>
<ul>
<li>k8s/service.yaml :</li>
</ul>
<div class="code-block">
<pre>
apiVersion: v1
kind: Service
metadata:
  name: python-app-service
spec:
  selector:
    app: python-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 5000
    type: LoadBalancer
</pre>
</div>

<h3>Шаг 8. Настройка развертывания логирования через Fluent Bit</h3>
<p>Выберите, какая стратегия настройки логирования подходит вам больше. Мы рекомендуем подход с DaemonSet.</p>
<table>
<tr>
<th>Подход с DaemonSet</th>
<th>Подход с Sidecar</th>
</tr>
<tr>
<td colspan="2">В этом варианте запускается один экземпляр Fluent Bit на каждом узле.<br>Для этого подхода требуется доступ к логам узла: /var/log .<br>Заполните содержимое файлов:
<ul>
<li>k8s/logging/fluent-bit/configmap.yaml :</li>
</ul>
</td>
</tr>
<tr>
<td colspan="2">
<div class="code-block">
<pre>
apiVersion: v1
kind: ConfigMap
metadata:
  name: fluent-bit-config
  labels:
    app: fluent-bit
data:
  fluent-bit.conf: |
    [SERVICE]
      Flush           info
      Daemon          off
      Parsers_File    /fluent-bit/etc/parsers.conf
    [INPUT]
      Name              tail
      Path              /var/log/containers/*.log
      Parser            docker
      Tag               kube.*
      Refresh_Interval  3
    [FILTER]
      Name              logaas
      Match             *
      Kube_URL           https://console.cloud.ru/
      Kube_CA_File       /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
      Kube_Token_File    /var/run/secrets/kubernetes.io/serviceaccount/token
      Merge_Log          on
    [OUTPUT]
      Name              logaas
      Match             *
      address           https://auth.iam.cloud.ru/
      iam_client_id     REPLACE_TO_LOGGING_SA_KEY_ID
      iam_client_secret REPLACE_TO_LOGGING_SA_SECRET
      default_project_id REPLACE_TO_PROJECT_ID
      default_group_id  REPLACE_TO_LOG_GROUP_ID
      default_labels    {"some_label":"default_value"}
</pre>
</div>
<p>Добавьте в файл свои данные:</p>
<ul>
<li>REPLACE_TO_LOGGING_SA_KEY_ID и REPLACE_TO_LOGGING_SA_SECRET — Key ID (логин) и Key Secret (пароль) сервисного аккаунта с ролью «logaas.writer» для получения токена и отправки логов. Проверьте, что у вас есть доступ к проекту, а для вашего сервисного аккаунта выбраны проект «Пользователь сервисов» и роль «logaas.writer».</li>
<li>REPLACE_TO_PROJECT_ID и REPLACE_TO_LOG_GROUP_ID — ID проекта и ID лог-группы, в которую будут отправлены логи.</li>
<li>default_labels — необязательный раздел. В нем вы можете указать метки, которые будут добавлены ко всем логам.</li>
</ul>
</td>
</tr>
<tr>
<td colspan="2">
<div class="code-block">
<pre>
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluent-bit
  labels:
    app: fluent-bit
spec:
  selector:
    matchLabels:
      app: fluent-bit
  template:
    metadata:
      labels:
        app: fluent-bit
    spec:
      containers:
      - name: fluent-bit
        image: your-registry.cr.cloud.ru/fluent-bit-logaas:latest
        volumeMounts:
        - name: varlog
          mountPath: /var/log
        - name: config
          mountPath: /fluent-bit/etc/
      volumes:
      - name: varlog
        hostPath:
          path: /var/log
      - name: config
        configMap:
          name: fluent-bit-config
</pre>
</div>
</td>
</tr>
</table>

<h3>Шаг 9. Развертывание приложения и логирования в Managed Kubernetes</h3>
<p><span style="color:green;">Примечание</span><br>Для PROD-стенд добавьте права RBAC для Fluent Bit.</p>
<ol>
<li>Разверните основное приложение:</li>
</ol>
<div class="code-block">
<pre>
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
</pre>
</div>
<ol start="2">
<li>Разверните логирование Fluent Bit:</li>
</ol>
<table>
<tr>
<th>Подход с DaemonSet</th>
<th>Подход с Sidecar</th>
</tr>
<tr>
<td colspan="2">
<div class="code-block">
<pre>
kubectl apply -f k8s/logging/fluent-bit/configmap.yaml
kubectl apply -f k8s/logging/fluent-bit/demonset.yaml
</pre>
</div>
</td>
</tr>
</table>

<h3>Шаг 10. Просмотр логов</h3>
<p>Логи появятся в сервисе «Клиентское логирование» вскоре после успешного развертывания приложения и логирования.</p>
<p>Вы можете посмотреть логи в лог-группах. Логи можно <a>отфильтровать с помощью языка фильтрующих выражений</a> выгрузить как файл.</p>

<h3>После окончания работы</h3>
<p>Если кластер Managed Kubernetes, реестр в Artifact Registry и его логи стали неактуальными, вы можете удалить их:</p>
<ul>
<li>Удалить кластер Managed Kubernetes</li>
<li>Удалить реестр в Artifact Registry</li>
<li>Удалить лог-группу</li>
<li>Удалить проект</li>
</ul>