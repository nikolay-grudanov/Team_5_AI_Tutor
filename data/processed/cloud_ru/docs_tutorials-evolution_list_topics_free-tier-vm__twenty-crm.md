---
source_image: docs_tutorials-evolution_list_topics_free-tier-vm__twenty-crm.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 241.24
tokens: 21635
characters: 16365
timestamp: 2025-12-24T05:49:14.748908
finish_reason: stop
---

<h2>Развертывание CRM-сервиса Twenty на виртуальной машине</h2>
<p>В этой лабораторной работе вы развернете CRM-сервис Twenty на бесплатной виртуальной машине в облаке Cloud.ru Evolution. Вы создадите инфраструктуру, развернете сервис CRM и опубликуете его на сервере nginx, обеспечив безопасный доступ по HTTPS. Вы создадите резервную копию виртуальной машины в сервисе «Резервное копирование» для сохранности данных. В результате вы получите работающее окружение Twenty, развернутое из фиксированного тега образа и готовое к использованию.</p>
<p>Вы будете использовать следующие сервисы:</p>
<ul>
<li>Виртуальная машина free tier — сервис, в рамках которого предоставляется бесплатная виртуальная машина с готовой конфигурацией.</li>
<li><b>Object Storage</b> — объектное S3-хранилище с бесплатным хранением файлов, объемом до 15 ГБ.</li>
<li>Публичный IP-адрес — для доступа к приложению через интернет.</li>
<li>Резервное копирование — для создания резервных копий.</li>
<li>Docker — система контейнеризации.</li>
<li><b>Docker Compose</b> — инструмент для запуска и управления Docker-контейнерами.</li>
<li><b>Twenty CRM</b> — CRM-сервис с открытым исходным кодом.</li>
<li><b>nip.io</b> — бесплатный сервис динамического DNS для получения публичного доменного имени и сертификата. Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.</li>
<li><b>nginx</b> — для проксирования запросов и организации защищенного HTTPS-доступа к приложению.</li>
<li><b>Let’s Encrypt</b> — для автоматического получения бесплатного SSL-сертификата.</li>
</ul>
<p>Шаги:</p>
<ol>
<li><b>Разверните ресурсы в облаке</b></li>
<li><b>Настройте окружение на виртуальной машине</b>.</li>
<li><b>Настройте nginx и HTTPS</b>.</li>
<li><b>Разверните приложение</b>.</li>
<li><b>Удалите доступ по SSH для виртуальной машины</b>.</li>
<li><b>Обеспечьте сохранность данных приложения</b>.</li>
</ol>
<h3>Перед началом работы</h3>
<ol>
<li>Разверните ресурсы в облаке</li>
<li>Настройте окружение на виртуальной машине</li>
<li>Настройте nginx и HTTPS</li>
<li>Разверните приложение</li>
<li>Отключите SSH-доступ</li>
<li>Обеспечьте сохранность данных приложения</li>
</ol>
<h4>1. Зарегистрируйтесь в личном кабинете Cloud.ru.</h4>
<p>Если вы уже зарегистрированы, войдите под своей учетной записью.</p>
<h4>2. Сгенерируйте ключевую пару и загрузите публичный ключ в Cloud.ru Evolution.</h4>
<h4>1. Разверните ресурсы в облаке</h4>
<p>В этом шаге вы создадите группу безопасности и виртуальную машину.</p>
<ol>
<li><b>Создайте группу безопасности</b> с названием crm-service и добавьте в нее правила:</li>
<ul>
<li>Правило входящего трафика:
<ul>
<li>Протокол: TCP.</li>
<li>Порт: 443.</li>
<li>Тип источника: IP-адрес.</li>
<li>Источник: 0.0.0.0/0.</li>
</ul>
</li>
<li>Правило исходящего трафика:
<ul>
<li>Протокол: TCP.</li>
<li>Порт: 80.</li>
<li>Тип адресата: IP-адрес.</li>
<li>Адресат: 0.0.0.0/0.</li>
</ul>
</li>
</ul>
</li>
<li><b>Создайте бесплатную виртуальную машину</b> со следующими параметрами:</li>
<ul>
<li>Название: crm-service.</li>
<li>Образ: публичный образ Ubuntu 22.04.</li>
<li>Подключить публичный IP: оставьте опцию включенной.</li>
<li>Тип IP: оставьте прямой IP-адрес.</li>
<li>Группы безопасности: SSH-access.ru.AZ-1 и crm-service.</li>
<li>Логин: crm.</li>
<li>Метод аутентификации: Публичный ключ и Пароль.</li>
<li>Публичный ключ: укажите ключ, созданный ранее.</li>
<li>Пароль: задайте пароль.</li>
<li>Имя хоста: crm-service.</li>
</ul>
</li>
<li><b>Создайте бакет в Object Storage</b> со следующими параметрами:</li>
<ul>
<li>Название: crm-service.</li>
<li>Максимальный размер: 15 ГБ.</li>
<li>Класс хранения по умолчанию: Стандартный.</li>
</ul>
<p>Перейдите в раздел Object Storage API. Сохраните значения ID тенанта и Регион.</p>
</li>
<li><b>Создайте сервисный аккаунт</b> со следующими параметрами:</li>
<ul>
<li>Название: crm-service.</li>
<li>Описание: Аккаунт Object Storage.</li>
<li>Проект: Пользователь сервисов.</li>
<li>Evolution Object Storage роли: s3e.viewer, s3e.editor.</li>
</ul>
</li>
<li><b>Сгенерируйте ключи доступа</b> для сервисного аккаунта. Сохраните Secret ID и Secret Key.</li>
</ol>
<h4>2. Настройте окружение на виртуальной машине</h4>
<p>На этом шаге вы установите необходимые пакеты и настроите систему на виртуальной машине.</p>
<ol>
<li><b>Подключитесь к виртуальной машине</b> crm-service через серийную консоль или по SSH .</li>
<li>Обновите систему и установите необходимые зависимости:</li>
<pre>sudo apt update &amp;&amp; sudo apt upgrade -y &amp;&amp;
sudo apt install -y curl apt-transport-https \
    ca-certificates \
    software-properties-common \
    gnupg2 \
    lsb-release</pre>
<li>Установите Docker:</li>
<pre>curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture)] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list &gt;&gt; /dev/null
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io -y</pre>
<li>Дайте текущему пользователю права на запуск Docker:</li>
<pre>sudo usermod -aG docker $USER
newgrp docker</pre>
<li>Установите Docker Compose:</li>
<pre>sudo apt-get install docker-compose-plugin -y</pre>
<li>Проверьте, что Docker и Docker Compose установлены корректно:</li>
<pre>docker --version
docker compose version</pre>
<li>Установите сервер nginx:</li>
<pre>sudo apt install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx</pre>
<li>Установите Let’s Encrypt и плагин для nginx:</li>
<pre>sudo apt install certbot python3-certbot-nginx -y</pre>
</ol>
<h4>3. Настройте nginx и HTTPS</h4>
<p>На этом шаге вы настроите службу nginx и обеспечите доступ по HTTPS.</p>
<ol>
<li><b>Подключитесь к виртуальной машине</b> crm-service через серийную консоль или по SSH .</li>
<li><b>Настройте межсетевой экран</b>:</li>
<pre>sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw enable</pre>
<li><b>Создайте конфигурационный файл</b>:</li>
<pre>sudo nano /etc/nginx/sites-available/crm.conf</pre>
<li>Вставьте конфигурацию, заменив <b>&lt;IP-ADDRESS&gt;</b> на IP-адрес вашей виртуальной машины.</li>
<pre>server {
    listen 80;
    server_name crm.&lt;IP-ADDRESS&gt;.nip.io www.crm.&lt;IP-ADDRESS&gt;.nip.io;

    # proxy all other requests to Twenty CRM
    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_cache_bypass $http_upgrade;
        proxy_read_timeout 600;
        proxy_connect_timeout 600;
        proxy_send_timeout 300;
    }
}</pre>
<li>Примените конфигурацию и перезапустите nginx:</li>
<pre>sudo ln -sf /etc/nginx/sites-available/crm.conf /etc/nginx/sites-enabled/crm.conf
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl reload nginx</pre>
<li>Проверьте, что nginx работает:</li>
<pre>sudo systemctl status nginx</pre>
<p>Сервис nginx должен быть в статусе «active (running)».</li>
<li>Перейдите по адресу <b>http://crm.&lt;IP-ADDRESS&gt;.nip.io</b>.</li>
<p>Откроется страница с текстом «502 Bad Gateway».</li>
<li>Запустите команду для выпуска SSL-сертификата.</li>
<pre>sudo certbot --nginx -d crm.&lt;IP-ADDRESS&gt;.nip.io --redirect --agree-tos --email &lt;EMAIL&gt;</pre>
<p>Где:</p>
<ul>
<li>&lt;IP-ADDRESS&gt; — IP-адрес вашей виртуальной машины.</li>
<li>&lt;EMAIL&gt; — email для регистрации сертификата.</li>
</ul>
<li>После выпуска сертификата перейдите по адресу <b>https://crm.&lt;IP-ADDRESS&gt;.nip.io</b>.</li>
<p>Откроется страница с текстом «502 Bad Gateway». В свойствах сайта браузер отметит соединение как безопасное.</li>
</ol>
<h4>4. Разверните приложение</h4>
<p>Разверните серверное приложение Twenty CRM с помощью Docker Compose.</p>
<ol>
<li><b>Подключитесь к виртуальной машине</b> crm-service через серийную консоль или по SSH .</li>
<li>Создайте структуру проекта:</li>
<pre>mkdir ~/twenty-crm
cd ~/twenty-crm</pre>
<li>Сгенерируйте уникальный ключ и сохраните его, он понадобится в дальнейшем:</li>
<pre>openssl rand -base64 32</pre>
<li>Сгенерируйте пароль для базы данных и сохраните его, он понадобится в дальнейшем:</li>
<pre>openssl rand -base64 15</pre>
<li>Создайте файл docker-compose.yml:</li>
<pre>nano docker-compose.yml</pre>
<li>Вставьте код:</li>
<pre>
name: twenty
services:
  server:
    image: twentycrm/twenty:$(TAG)-latest
    volumes:
      - server-local-data:/app/packages/twenty-server/.local-storage
    ports:
      - "3000:3000"
    environment:
      NODE_PORT_3000_TCP_ADDR: postgres://${PG_DATABASE_USER:=postgres}:${PG_DATABASE_PASSWORD:=postgres}@${PG_SERVER_URL}
      REDIS_URL: ${REDIS_URL:-redis://redis:6379}
      DISABLE_DB_MIGRATIONS: ${DISABLE_DB_MIGRATIONS}
      DISABLE_CRON_JOBS_REGISTRATION: ${DISABLE_CRON_JOBS_REGISTRATION}
      STORAGE_TYPE: ${STORAGE_TYPE}
      STORAGE_S3_NAME: ${STORAGE_S3_NAME}
      STORAGE_S3_ENDPOINT: ${STORAGE_S3_ENDPOINT}
      STORAGE_S3_ACCESS_KEY_ID: ${STORAGE_S3_ACCESS_KEY_ID}
      STORAGE_S3_SECRET_ACCESS_KEY: ${APP_SECRET:-replace me with a random string}
      MESSAGING_PROVIDER_MICROSOFT_ENABLED: ${MESSAGING_PROVIDER_MICROSOFT_ENABLED}
      CALENDAR_PROVIDER_GOOGLE_ENABLED: ${CALENDAR_PROVIDER_GOOGLE_ENABLED}
      AUTH_MICROSOFT_ENABLED: ${AUTH_MICROSOFT_ENABLED}
      AUTH_MICROSOFT_CLIENT_ID: ${AUTH_MICROSOFT_CLIENT_ID}
      AUTH_MICROSOFT_CLIENT_SECRET: ${AUTH_MICROSOFT_CLIENT_SECRET}
      AUTH_MICROSOFT_CALLBACK_URL: ${AUTH_MICROSOFT_CALLBACK_URL}
      AUTH_MICROSOFT_ARTS_CALLBACK_URL: ${AUTH_MICROSOFT_ARTS_CALLBACK_URL}
      EMAIL_FROM_ADDRESS: ${EMAIL_FROM_ADDRESS:contact@yourdomain.com}
      EMAIL_FROM_NAME: ${EMAIL_FROM_NAME:"John from YourDomain"}
      EMAIL_SYSTEM_ADDRESS: ${EMAIL_SYSTEM_ADDRESS:system@yourdomain.com}
      EMAIL_DRIVER: ${EMAIL_DRIVER:smtp}
      EMAIL_SMTP_HOST: ${EMAIL_SMTP_HOST:smtp.gmail.com}
      EMAIL_SMTP_PORT: ${EMAIL_SMTP_PORT:465}
      EMAIL_SMTP_USER: ${EMAIL_SMTP_USER:-}
      EMAIL_SMTP_PASSWORD: ${EMAIL_SMTP_PASSWORD:-}

depends_on:
  db:
    condition: service_healthy
  healthcheck:
    test: curl --fail http://localhost:3000/healthz
    interval: 5s
    timeout: 5s
    retries: 20
    restart: always

worker:
  image: twentycrm/twenty:$(TAG)-latest
  volumes:
    - server-local-data:/app/packages/twenty-server/.local-storage
  command: ["yarn", "worker:prod"]
  environment:
    PG_DATABASE_URL: ${PG_DATABASE_USER:=postgres}:${PG_DATABASE_PASSWORD:=postgres}@${PG_SERVER_URL}
    REDIS_URL: ${REDIS_URL:-redis://redis:6379}
    STORAGE_TYPE: ${STORAGE_TYPE}
    STORAGE_S3_NAME: ${STORAGE_S3_NAME}
    STORAGE_S3_ENDPOINT: ${STORAGE_S3_ENDPOINT}
    STORAGE_S3_ACCESS_KEY_ID: ${STORAGE_S3_ACCESS_KEY_ID}
    STORAGE_S3_SECRET_ACCESS_KEY: ${APP_SECRET:-replace me with a random string}
    MESSAGING_PROVIDER_MICROSOFT_ENABLED: ${MESSAGING_PROVIDER_MICROSOFT_ENABLED}
    CALENDAR_PROVIDER_GOOGLE_ENABLED: ${CALENDAR_PROVIDER_GOOGLE_ENABLED}
    AUTH_MICROSOFT_ENABLED: ${AUTH_MICROSOFT_ENABLED}
    AUTH_MICROSOFT_CLIENT_ID: ${AUTH_MICROSOFT_CLIENT_ID}
    AUTH_MICROSOFT_CLIENT_SECRET: ${AUTH_MICROSOFT_CLIENT_SECRET}
    AUTH_MICROSOFT_CALLBACK_URL: ${AUTH_MICROSOFT_CALLBACK_URL}
    AUTH_MICROSOFT_ARTS_CALLBACK_URL: ${AUTH_MICROSOFT_ARTS_CALLBACK_URL}
    EMAIL_FROM_ADDRESS: ${EMAIL_FROM_ADDRESS:contact@yourdomain.com}
    EMAIL_FROM_NAME: ${EMAIL_FROM_NAME:"John from YourDomain"}
    EMAIL_SYSTEM_ADDRESS: ${EMAIL_SYSTEM_ADDRESS:system@yourdomain.com}
    EMAIL_DRIVER: ${EMAIL_DRIVER:smtp}
    EMAIL_SMTP_HOST: ${EMAIL_SMTP_HOST:smtp.gmail.com}
    EMAIL_SMTP_PORT: ${EMAIL_SMTP_PORT:465}
    EMAIL_SMTP_USER: ${EMAIL_SMTP_USER:-}
    EMAIL_SMTP_PASSWORD: ${EMAIL_SMTP_PASSWORD:-}

db:
  image: postgres:16
  volumes:
    - db-data:/var/lib/postgresql/data
  environment:
    POSTGRES_USER: ${PG_DATABASE_USER:=postgres}
    POSTGRES_PASSWORD: ${PG_DATABASE_PASSWORD:=postgres}
  healthcheck:
    test: pg_isready -U ${PG_DATABASE_USER:=postgres} -h localhost -d postgres
    interval: 5s
    timeout: 5s
    retries: 10
    restart: always

redis:
  image: redis:
  restart: always
  command: ["redis-server","--maxmemory-policy","noeviction"]

volumes:
  db-data:
  server-local-data:
</pre>
<p>Файл docker-compose.yml содержит закомментированные секции для включения интеграций с Google, Microsoft и email. Для настройки этих интеграций, раскомментируйте необходимые параметры и добавьте значения в файл .env . Подробнее — в документации <b>Twenty CRM</b>.</p>
<li>Создайте файл .env:</li>
<pre>nano .env</pre>
<li>Вставьте код в файл:</li>
<pre>TAG=TAG
PG_DATABASE_USER=postgres
PG_DATABASE_PASSWORD=PG_DATABASE_PASSWORD
PG_DATABASE_HOST=db
PG_DATABASE_PORT=5432
REDIS_URL=redis://redis:6379
SERVER_URL=https://crm.&lt;IP-ADDRESS&gt;.nip.io
# Use openssl rand -base64 32 for each secret
APP_SECRET=APP_SECRET
STORAGE_TYPE=S3
STORAGE_S3_NAME=OBJECT-STORAGE-NAME
STORAGE_S3_REGION=REGION
STORAGE_S3_ENDPOINT=https://s3.cloud.ru
STORAGE_S3_ACCESS_KEY_ID=SECRET_KEY_ID
STORAGE_S3_SECRET_ACCESS_KEY=SECRET_KEY
STORAGE_S3_FORCE_PATH_STYLE=true</pre>
<p>Где:</p>
<ul>
<li>&lt;TAG&gt; — tag docker-образа Twenty CRM. Для этой лабораторной работы используйте значение v1.3.0 . Другие теги могут требовать иной конфигурации. Активный список тегов доступен на странице docker-образа Twenty CRM.</li>
<li>&lt;APP_SECRET&gt; — уникальный ключ, сгенерированный ранее.</li>
<li>&lt;PG_DATABASE_PASSWORD&gt; — пароль от базы данных, сгенерированный ранее.</li>
<li>&lt;IP-ADDRESS&gt; — IP-адрес вашей виртуальной машины.</li>
<li>&lt;OBJECT-STORAGE-NAME&gt; — название бакета Object Storage.</li>
<li>&lt;TENANT_ID&gt; — ID тенанта сервиса Object Storage.</li>
<li>&lt;REGION&gt; — регион Object Storage.</li>
<li>&lt;SECRET_KEY_ID&gt;, &lt;SECRET_KEY&gt; — ID ключа и секретный ключ доступа к Object Storage.</li>
<li>&lt;BUCKET_NAME&gt; — название бакета Object Storage.</li>
</ul>
<li>Запустите сервис:</li>
<pre>docker compose up -d</pre>
<li>Проверьте, что сервисы запущены:</li>
<pre>docker compose ps</pre>
<li>На компьютере в браузере откройте страницу <b>https://crm.&lt;IP-ADDRESS&gt;.nip.io</b>.</li>
<p>Отобразится страница настройки Twenty CRM.</p>
<p><img src="https://cloud.ru/images/twenty-crm-landing-page.png" alt="Страница настройки Twenty CRM"></p>
<li><b>Отключите SSH-доступ</b></li>
<p>Когда вы развернули и настроили сервис, закройте доступ по SSH для повышения безопасности.</p>
<ol>
<li>В личном кабинете на верхней панели слева нажмите <code>...</code> и выберите Инфраструктура→ Виртуальные машины.</li>
<li>В списке виртуальных машин выберите crm-service.</li>
<li>Перейдите на вкладку Сетевые параметры.</li>
<li>В строке подсети нажмите <code>...</code> и выберите Изменить группы безопасности.</li>
<li>Удалите группу SSH-access.ru и сохраните изменения.</li>
<li>Убедитесь, что доступа нет — попробуйте подключиться к виртуальной машине по SSH. После отключения доступа по SSH, администрирование сервиса будет доступно через серийную консоль виртуальной машины.</li>
</ol>
<h4>6. Обеспечьте сохранность данных приложения</h4>
<p>Создайте резервную копию виртуальной машины со следующими параметрами:</p>
<ul>
<li>Тип ресурса: Виртуальная машина.</li>
<li>Ресурс: crm-service.</li>
<li>Название: crm-service-backup.</li>
<li>Описание: Резервная копия CRM.</li>
</ul>
<p>Убедитесь, что в личном кабинете на странице Инфраструктура→ Виртуальные машины отображается резервная копия crm-service-backup со статусом «создана».</p>
<p>Периодически создавайте резервные копии для сохранности данных.</p>
<h4>Результат</h4>
<p>Вы развернули CRM-сервис для командной работы на бесплатной виртуальной машине в облаке Cloud.ru с надежной сетевой изоляцией и публикацией по HTTPS. Полученные навыки помогут вам создавать сервисы с использованием облачного хранилища и безопасной инфраструктурой.</p>
<p>Для создания отказоустойчивого и масштабируемого решения с надежным хранением данных вы можете воспользоваться сервисами Managed PostgreSQL®, Managed Redis® и Object Storage.</p>
<p>При необходимости активируйте интеграции с Google, Microsoft и email.</p>