---
source_image: docs_tutorials-evolution_list_topics_managed-kubernetes__secret.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 93.52
tokens: 13974
characters: 9834
timestamp: 2025-12-24T05:57:20.054218
finish_reason: stop
---

<h2>Работа с секретами при публикации приложений в Managed Kubernetes</h2>
<p>Приложения, развернутые в кластерах Kubernetes, часто требуют подключения к базам данных или внешним сервисам. Однако чувствительные данные, например логины, пароли или ключи API, не следует хранить в открытом виде в манифестах. Защищенное хранение таких данных — одна из ключевых задач обеспечения безопасности приложений.</p>
<p>С помощью этого руководства вы научитесь подключать Flask-приложение к PostgreSQL с использованием встроенных в Kubernetes секретов для хранения логина и пароля от базы данных PostgreSQL в сервисе Managed Kubernetes на платформе Cloud.ru Evolution.</p>
<p>Вы будете использовать следующие сервисы:</p>
<ul>
<li>Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.</li>
<li>Managed Kubernetes — сервис управления кластерами Kubernetes на вычислительных ресурсах облака.</li>
<li>Artifact Registry для хранения, совместного использования и управления Docker-образами и Helm-чартами.</li>
<li>sNAT-шлюзы — сервис управления сетевыми шлюзами облака.</li>
<li>kubectl — инструмент командной строки, позволяющий запускать команды для кластеров Kubernetes.</li>
<li>Docker — система контейнеризации.</li>
</ul>
<p>Шаги:</p>
<ol>
<li><b>Разверните необходимые ресурсы в облаке.</b></li>
<li><b>Создайте секрет и базу данных PostgreSQL.</b></li>
<li><b>Соберите и загрузите образ приложения в Artifact Registry Cloud.ru.</b></li>
<li><b>Разверните Flask-приложение в Managed Kubernetes.</b></li>
<li><b>Проверьте результат.</b></li>
</ol>
<h3>Перед началом работы</h3>
<ol>
<li>Зарегистрируйтесь в личном кабинете Cloud.ru.<br>Если вы уже зарегистрированы, войдите под своей учетной записью.</li>
<li>Убедитесь, что у вас достаточно прав для создания реестра и загрузки артефактов в сервисе Artifact Registry.</li>
</ol>
<h4>1. Разверните необходимые ресурсы в облаке</h4>
<ol>
<li><b>Создайте кластер Managed Kubernetes с хотя бы одной группой узлов.</b></li>
<li><b>Создайте виртуальную машину в той же зоне доступности, что и кластер.</b><br>В сетевых настройках ВМ выберите параметр Подсеть с публичным IP.<br>С виртуальной машины вы будете подключаться к кластеру Managed Kubernetes.</li>
<li>Выполните подключение к кластеру Managed Kubernetes с ВМ:
  <ol type="a">
    <li>Подключитесь к ВМ по SSH.</li>
    <li>На ВМ установите kubectl и cloudlogin.</li>
    <li>Подключитесь с ВМ к кластеру Managed Kubernetes.</li>
  </ol>
  d. Проверьте подключение:
  <pre>kubectl get nodes</pre>
  Если отобразится список узлов, подключение настроено.
</li>
<li><b>Создайте sNAT-шлюз в той же зоне доступности, что и кластер.</b><br>Он понадобится для работы с внешними образами, например postgres.</li>
</ol>
<h4>2. Создайте секрет и базу данных PostgreSQL</h4>
<p>Этот шаг выполняется на виртуальной машине, с которой выполнено подключение к созданному кластеру Managed Kubernetes.</p>
<ol>
<li>Создайте секрет, содержащий логин и пароль для PostgreSQL:</li>
</ol>
<pre>kubectl create secret generic pg-secret \
--from-literal=POSTGRES_USER=demo \
--from-literal=POSTGRES_PASSWORD=supersecret</pre>
<p>Этот секрет будет использоваться как самой базой данных, так и приложением-клиентом для подключения.</p>
<p>Результат:</p>
<pre>secret/pg-secret created</pre>
<ol start="2">
<li>Создайте файл <code>postgres-deployment.yaml</code>:</li>
</ol>
<pre>apiVersion: apps/v1
kind: Deployment
metadata:
  name: postgres
spec:
  replicas: 1
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
        - name: postgres
          image: postgres:15
          env:
            - name: POSTGRES_USER
              valueFrom:
                secretKeyRef:
                  name: pg-secret
                  key: POSTGRES_USER
            - name: POSTGRES_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: pg-secret
                  key: POSTGRES_PASSWORD
          ports:
            - containerPort: 5432
---
apiVersion: v1
kind: Service
metadata:
  name: postgres
spec:
  selector:
    app: postgres
  ports:
    - port: 5432
      targetPort: 5432
      clusterIP: ""
</pre>
<ol start="3">
<li>Примените манифест:</li>
</ol>
<pre>kubectl apply -f postgres-deployment.yaml</pre>
<p>Результат:</p>
<pre>deployment.apps/postgres created
service/postgres created</pre>
<h4>3. Соберите и загрузите образ приложения в Artifact Registry Cloud.ru</h4>
<p>На этом шаге вы создадите Docker-образ Flask-приложения, которое подключается к PostgreSQL, и загрузите его в Artifact Registry Cloud.ru. Использование собственного образа в Artifact Registry гарантирует, что приложение будет работать с нужными зависимостями и будет доступно для вашего кластера без внешних зависимостей.</p>
<p>Если вы хотите пропустить сборку, можете перейти к шагу 4 и использовать тестовый образ kollekcioner47/secretapp из Docker Hub. Однако в рамках этого практического руководства рекомендуется использовать свой образ в Artifact Registry, так как это целевой сценарий для продакшн-развертывания.</p>
<p>Если вы загрузите в реестр случайный или неполный образ без описанных ниже настроек Dockerfile, приложение не запустится, так как в нем не будут установлены необходимые библиотеки, например Flask, psycopg2-binary и другие.</p>
<ol>
<li>Подготовьте приложение. На отдельной виртуальной машине с установленным Docker создайте файл <code>app.py</code>:</li>
</ol>
<pre>import os
import psycopg2
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    conn = psycopg2.connect(
        dbname="postgres",
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host="postgres",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT version();")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return f"Connected to PostgreSQL: {result}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)</pre>
<ol start="2">
<li>Создайте Dockerfile:</li>
</ol>
<pre>FROM python:3.10-slim
WORKDIR /app
COPY app.py .
RUN apt-get update && apt-get install -y gcc libpq-dev && \
    pip install flask psycopg2-binary && \
    apt-get clean
CMD ["python", "app.py"]</pre>
<ol start="3">
<li>Подготовьте среду для сборки образа приложения и его загрузки в Artifact Registry. Для этого выполните шаги 2–6 <a href="#">инструкции</a>.</li>
<li>Соберите и загрузите образ:</li>
</ol>
<pre>docker build -t <your-registry-uri>/secretapp:latest .
docker push <your-registry-uri>/secretapp:latest</pre>
<p>Где <code>&lt;your-registry-uri&gt;</code> — URI реестра из сервиса Artifact Registry.</p>
<h4>4. Разверните Flask-приложение в Managed Kubernetes</h4>
<p>На этом шаге вы развернете приложение, которое подключается к PostgreSQL с использованием Kubernetes Secret.</p>
<p>Если вы выполнили шаг 3, используйте образ из своего Artifact Registry. Если вы пропустили шаг 3, укажите тестовый образ kollekcioner47/secretapp из Docker Hub. Работоспособность образа в этом случае не гарантируется при изменённых настройках.</p>
<ol>
<li>Создайте файл <code>app-deployment.yaml</code>:</li>
</ol>
<pre>apiVersion: apps/v1
kind: Deployment
metadata:
  name: pg-client
spec:
  replicas: 1
  selector:
    matchLabels:
      app: pg-client
  template:
    metadata:
      labels:
        app: pg-client
    spec:
      containers:
        - name: pg-client
          image: <your-registry-uri>/secretapp:latest # basic scenario
            # image: kollekcioner47/secretapp # alternative scenario
          env:
            - name: POSTGRES_USER
              valueFrom:
                secretKeyRef:
                  name: pg-secret
                  key: POSTGRES_USER
            - name: POSTGRES_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: pg-secret
                  key: POSTGRES_PASSWORD
          ports:
            - containerPort: 5000
---
apiVersion: v1
kind: Service
metadata:
  name: pg-client-service
spec:
  selector:
    app: pg-client
  ports:
    - port: 80
      targetPort: 5000
      type: LoadBalancer</pre>
<ol start="2">
<li>Примените манифест:</li>
</ol>
<pre>kubectl apply -f app-deployment.yaml</pre>
<p>Результат:</p>
<pre>deployment.apps/pg-client created
service/pg-client-service created</pre>
<h4>5. Проверьте результат</h4>
<p>Убедитесь, что приложение работает корректно.</p>
<ol>
<li>Получите внешний IP:</li>
</ol>
<pre>kubectl get svc pg-client-service</pre>
<p>2. Перейдите по адресу <code>http://&lt;external-ip&gt;</code> в браузере. Если все настроено верно, в веб-интерфейсе отобразится текст с версией PostgreSQL, например:</p>
<pre>Connected to PostgreSQL: ('PostgreSQL 15.14 (Debian 15.14-1.pgdg11+1) on x86_64-pc-linux-gnu', compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit.)</pre>
<p>Это означает, что Flask-приложение развернуто в Kubernetes и успешно подключено к базе данных: приложение выполняет SQL-запрос <code>SELECT VERSION()</code>, получает из PostgreSQL строку с номером версии и отображает ее на странице.</p>
<p>Таким образом, вы развернули контейнерное Flask-приложение в Kubernetes и использовали Secret для безопасного хранения логина и пароля к базе данных.</p>
<h3>Результат</h3>
<p>Вы научились:</p>
<ul>
<li>Использовать Kubernetes Secrets для безопасного хранения логинов и паролей.</li>
<li>Разворачивать базу данных PostgreSQL в Kubernetes.</li>
<li>Собирать и использовать готовое Flask-приложение, читающее из базы данных.</li>
<li>Подключать приложение к базе данных с помощью переменных среды из Secret.</li>
<li>Использовать Service типа LoadBalancer для доступа к приложению.</li>
</ul>
<p>Этот подход можно использовать в реальных проектах при развертывании микросервисов и работе с конфиденциальными данными.</p>