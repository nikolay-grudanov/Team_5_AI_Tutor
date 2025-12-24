---
source_image: docs_tutorials-evolution_list_topics_free-tier-vm__outline.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 136.23
tokens: 21647
characters: 16490
timestamp: 2025-12-24T05:44:25.057453
finish_reason: stop
---

<h2>Развертывание Wiki-сервиса Outline на виртуальной машине</h2>
<p>С помощью этого руководства вы развернете Wiki-сервис для командной работы на бесплатной виртуальной машине.</p>
<p>Вы создадите виртуальную машину Ubuntu 22.04, настроите для нее публичный IP-адрес, создадите бакет в Object Storage и настроите CORS для него.</p>
<p>На виртуальной машине настройте Docker и Docker Compose, разверните сервис Outline, подключите его к Object Storage и GitLab и опубликуйте на сервере nginx, выпустите SSL-сертификат в сервисе Let's Encrypt.</p>
<p>В итоге получится надежная схема, где файлы хранятся в Object Storage, а клиентский трафик шифруется HTTPS.</p>
<p>Вы будете использовать следующие сервисы:</p>
<ul>
<li>Виртуальная машина free tier — сервис, в рамках которого предоставляется бесплатная виртуальная машина с готовой конфигурацией.</li>
<li>Публичный IP-адрес для доступа к сервису через интернет.</li>
<li>Object Storage — объективное S3-хранилище с бесплатным хранением файлов, объемом до 15 ГБ.</li>
<li>Docker — система контейнеризации.</li>
<li>Docker Compose — инструмент для запуска и управления Docker-контейнерами.</li>
<li>Outline — open-source система вики.</li>
<li>Бесплатный сервис nip.io для получения публичного доменного имени и сертификата. Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.</li>
<li>Nginx — веб-сервер для проксирования запросов и организации защищенного HTTPS-доступа к приложению.</li>
<li>Let's Encrypt — сервис для автоматического получения бесплатного SSL-сертификата.</li>
<li>GitLab — как провайдер для авторизации. Список других доступных провайдеров можно найти в документе по аутентификации Outline.</li>
</ul>
<p>Шаги:</p>
<ol>
<li>Разверните необходимые ресурсы в облаке.</li>
<li>Настройте окружение на виртуальной машине.</li>
<li>Настройте nginx и HTTPS.</li>
<li>Настройте приложение в GitLab.</li>
<li>Разверните приложение.</li>
<li>Настройте CORS в Object Storage.</li>
<li>Удалите доступ по SSH для виртуальной машины.</li>
</ol>
<h3>Перед началом работы</h3>
<ol>
<li>Зарегистрируйтесь в личном кабинете Cloud.ru.<br>Если вы уже зарегистрированы, войдите под своей учетной записью.</li>
<li>Сгенерируйте SSH-ключ по инструкции.</li>
<li>Загрузите публичную часть SSH-ключа в облако Cloud.ru Evolution по инструкции.</li>
</ol>
<h3>1. Разверните ресурсы в облаке</h3>
<p>В этом шаге вы создадите группу безопасности, виртуальную машину и бакет в Object Storage.</p>
<p>Создайте новую группу безопасности со следующими параметрами:</p>
<ol>
<li>Укажите Название группы безопасности, например outline-wiki.</li>
<li>Добавьте правила входящего и исходящего трафика.
Правила входящего трафика:
<ul>
<li>Протокол: TCP</li>
<li>Порт: 443</li>
<li>Тип источника: IP-адрес</li>
<li>Источник: 0.0.0.0/0</li>
</ul>
Правила исходящего трафика:
<ul>
<li>Протокол: Любой</li>
<li>Тип адресата: IP-адрес</li>
<li>Адресат: 0.0.0.0/0</li>
</ul>
</li>
</ol>
<p>Убедитесь, что в личном кабинете на странице сервиса «Группы безопасности»:</p>
<ul>
<li>отображается группа безопасности outline-wiki;</li>
<li>статус группы безопасности — «Создана».</li>
</ul>
<p>Создайте бесплатную виртуальную машину со следующими параметрами:</p>
<ol>
<li>В поле Название укажите название виртуальной машины, например outline-wiki.</li>
<li>На вкладке Публичные выберите образ Ubuntu 22.04.</li>
<li>В поле Логин укажите логин пользователя виртуальной машины, например outline.</li>
<li>В разделе Метод аутентификации выберите публичный ключ и пароль.</li>
<li>Укажите публичный ключ и ваш пароль для создаваемого пользователя.</li>
<li>В поле Имя хоста укажите уникальное имя устройства, по которому можно идентифицировать виртуальную машину в сети, например outline-wiki.</li>
<li>В поле Название загрузочного диска укажите outline-wiki-disk.</li>
<li>Включите опцию Подключить публичный IP.</li>
<li>В группе Тип IP-адреса выберите Прямой.</li>
<li>Выберите группы безопасности SSH-access_ru.AZ-1, outline-wiki.</li>
</ol>
<p>Убедитесь, что в личном кабинете на странице сервиса «Виртуальные машины»:</p>
<ul>
<li>отображается виртуальная машина outline-wiki;</li>
<li>статус виртуальной машины — «Запущена».</li>
</ul>
<p>Создайте бакет в Object Storage со следующими параметрами:</p>
<ol>
<li>В поле Доменное имя укажите outline-wiki (должно быть уникальным, замените на своё уникальное значение).</li>
<li>В поле Название укажите outline-wiki (совпадает с доменным именем).</li>
<li>В поле Глобальное название укажите outline-wiki (совпадает с доменным именем).</li>
<li>В поле Класс хранения по умолчанию выберите стандартный.</li>
<li>В поле Максимальный размер укажите 10 ГБ.</li>
</ol>
<p>Перейдите в раздел Object Storage API. Сохраните значения ID тенанта и Регион.</p>
<p>Убедитесь, что в личном кабинете на странице сервиса «Object Storage» отображается бакет outline-wiki.</p>
<p>Создайте сервисный аккаунт пользователя со следующими параметрами:</p>
<ol>
<li>В поле Название укажите outline-object-storage.</li>
<li>В поле Описание укажите «Аккаунт пользователя Object Storage».</li>
<li>В поле Проект выберите Пользователь сервисов.</li>
<li>Оставьте список Сервисы пустым.</li>
<li>В поле Evolution Object Storage Роли выберите s3e.viewer, s3e.editor.</li>
</ol>
<p>Сгенерируйте ключ доступа для аккаунта, сохраните Key ID (логин) и Key Secret (пароль).</p>
<h3>2. Настройте окружение на виртуальной машине</h3>
<p>Настройте систему и установите необходимые пакеты на виртуальной машине.</p>
<ol>
<li>Подключитесь к виртуальной машине outline-wiki через серийную консоль или по SSH.</li>
<li>Обновите систему и установите необходимые зависимости:</li>
</ol>
<div class="code-block">
<pre><code>sudo apt update &amp;&amp; sudo apt upgrade -y
sudo apt install unzip gpg software-properties-common apt-transport-https ca-certificates python3-pip
sudo snap install core; sudo snap refresh core
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
</code></pre>
</div>
<ol start="3">
<li>Установите Docker и Docker Compose:</li>
</ol>
<div class="code-block">
<pre><code># Add docker's GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Add docker repository
echo "[deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg]]" | tee /etc/apt/sources.list.d/docker.list &gt;&gt; /etc/apt/sources.list.d/docker.list

# Install Docker
sudo apt update &amp;&amp; sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin docker

# Add user to docker group
sudo usermod -aG docker $USER
newgrp docker
</code></pre>
</div>
<ol start="4">
<li>Проверьте, что Docker установлен корректно:</li>
</ol>
<div class="code-block">
<pre><code>docker --version
docker compose version
</code></pre>
</div>
<h3>3. Настройте nginx и HTTPS</h3>
<p>Настройте службу nginx и обеспечьте доступ по HTTPS.</p>
<ol>
<li>Подключитесь к виртуальной машине outline-wiki через серийную консоль или по SSH.</li>
<li>Сконфигурируйте файервол:</li>
</ol>
<div class="code-block">
<pre><code>sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw enable
</code></pre>
</div>
<ol start="3">
<li>Создайте конфигурационный файл:</li>
</ol>
<div class="code-block">
<pre><code>sudo nano /etc/nginx/sites-available/outline.conf
</code></pre>
</div>
<ol start="4">
<li>Вставьте конфигурацию, заменив &lt;IP-адрес&gt; на IP-адрес вашей виртуальной машины.</li>
</ol>
<div class="code-block">
<pre><code>server {
    listen 80;
    server_name wiki.&lt;IP-адрес&gt;.nip.io www.wiki.&lt;IP-адрес&gt;.nip.io;

    location / {
        proxy_pass http://localhost:3000/;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Scheme $scheme;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
    }
}
</code></pre>
</div>
<ol start="5">
<li>Примените конфигурацию и перезапустите nginx:</li>
</ol>
<div class="code-block">
<pre><code>sudo ln -sf /etc/nginx/sites-available/outline.conf /etc/nginx/sites-enabled/outline.conf
sudo rm /etc/nginx/sites-enabled/default
sudo nginx
sudo systemctl reload nginx
</code></pre>
</div>
<ol start="6">
<li>Проверьте, что nginx работает:</li>
</ol>
<div class="code-block">
<pre><code>sudo systemctl status nginx
</code></pre>
</div>
<p>Сервис nginx должен быть в статусе «active (running)».</p>
<ol start="7">
<li>Перейдите по адресу http://wiki.&lt;IP-адрес&gt;.nip.io .<br>Откроется страница с текстом 502 Bad Gateway.</li>
<li>Запустите команду для выпуска SSL-сертификата.</li>
</ol>
<div class="code-block">
<pre><code>sudo certbot --nginx -d wiki.&lt;IP-адрес&gt;.nip.io --redirect --agree-tos --email &lt;EMAIL&gt;
</code></pre>
</div>
<p>Где:</p>
<ul>
<li>&lt;IP-адрес&gt; — IP-адрес вашей виртуальной машины.</li>
<li>&lt;EMAIL&gt; — ваш email.</li>
</ul>
<ol start="9">
<li>После успешного выпуска сертификата, перейдите по адресу https://wiki.&lt;IP-адрес&gt;.nip.io .<br>Откроется страница с текстом 502 Bad Gateway. В свойствах сайта браузер отметит соединение как безопасное.</li>
</ol>
<h3>4. Настройте приложение в GitLab</h3>
<p>Создайте приложение в вашем GitLab-инстансе для интеграции с Outline.</p>
<ol>
<li>Перейдите в Настройки → Приложения в собственном или облачном GitLab-инстансе.</li>
<li>Создайте новое приложение со следующими настройками:
<ul>
<li>Имя: Outline</li>
<li>Redirect URI: https://wiki.&lt;IP-адрес&gt;.nip.io/auth/oidc/callback (замените значения IP-адрес)</li>
<li>Scopes: Выберите openid, profile и email</li>
</ul>
</li>
<li>Сохраните приложение.</li>
<li>Сохраните значения Application ID и Secret, они понадобятся в дальнейшем.</li>
</ol>
<h3>5. Разверните приложение</h3>
<p>Разверните серверное приложение Outline с помощью Docker Compose.</p>
<ol>
<li>Подключитесь к виртуальной машине outline-wiki через серийную консоль или по SSH .</li>
<li>Создайте структуру проекта:</li>
</ol>
<div class="code-block">
<pre><code>mkdir -p SHOMK/outline
cd SHOMK/outline
</code></pre>
</div>
<ol start="3">
<li>Сгенерируйте уникальные ключи и сохраните их, они понадобятся в дальнейшем:</li>
</ol>
<div class="code-block">
<pre><code># Generate two random secrets for Outline
openssl rand -hex 32 # Save this as SECRET_KEY
openssl rand -hex 32 # Save this as UTILS_SECRET

# Generate database password
openssl rand -base64 15 # Save this as POSTGRES_PASSWORD
</code></pre>
</div>
<ol start="4">
<li>Создайте файл docker-compose.yml:</li>
</ol>
<div class="code-block">
<pre><code>nano docker-compose.yml
</code></pre>
</div>
<ol start="5">
<li>Вставьте содержимое в файл docker-compose.yml, заменив переменные на значения:</li>
</ol>
<div class="code-block">
<pre><code>services:
  outline:
    image: flameshikari/outline-ru:0.86.0
    env_file: ./docker.env
    ports:
      - "8000:8000"
    volumes:
      - storage-data:/var/lib/outline/data
    depends_on:
      - postgres
    environment:
      POSTGRES_MODE: disable

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 3s

  postgres:
    image: postgres:15
    env_file: ./docker.env
    ports:
      - "5432:5432"
    volumes:
      - database-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD", "pg_isready", "-d", "outline", "-u", "user"]
      interval: 20s
      timeout: 3s
    environment:
      POSTGRES_USER: 'user'
      POSTGRES_PASSWORD: &lt;POSTGRES_PASSWORD&gt;
      POSTGRES_DB: 'outline'

volumes:
  storage-data:
  database-data:
</code></pre>
</div>
<p>Где &lt;POSTGRES_PASSWORD&gt; — пароль от базы данных, сгенерированный ранее.</p>
<ol start="6">
<li>Создайте конфигурацию Redis:</li>
</ol>
<div class="code-block">
<pre><code>nano redis.conf
</code></pre>
</div>
<ol start="7">
<li>Вставьте содержимое в файл:</li>
</ol>
<div class="code-block">
<pre><code>bind 127.0.0.1
port 6379
save 300 1
save 60 1000
dbfilename dump.rdb
dir /
</code></pre>
</div>
<ol start="8">
<li>Создайте файл docker.env:</li>
</ol>
<div class="code-block">
<pre><code>nano docker.env
</code></pre>
</div>
<ol start="9">
<li>Вставьте содержимое в файл, заменив переменные на значения:</li>
</ol>
<div class="code-block">
<pre><code>MODE_ENV=production
# Application URL
URL=https://wiki.&lt;IP-адрес&gt;.nip.io
PORT=3000

# Secrets (use the generated values from step 5)
SECRET_KEY=&lt;UTILS_SECRET&gt;
UTILS_SECRET=&lt;UTILS_SECRET&gt;
DATABASE_URL=postgres://user:&lt;POSTGRES_PASSWORD&gt;@postgres:5432/outline
POSTGRES_MODE=disable

# Redis configuration
REDIS_URL=redis:6379

# File storage (using AWS S3)
AWS_ENDPOINT_URL=https://s3.cloud.ru
AWS_REGION=ru
AWS_USER_GLOBAL_ENDPOINT=false
AWS_S3_ADMINSIGNING_STYLE=path
AWS_ACCESS_KEY_ID=&lt;TENANT_ID&gt;-&lt;SECRET_KEY_ID&gt;
AWS_SECRET_ACCESS_KEY=&lt;SECRET_KEY&gt;
AWS_S3_BUCKET_NAME=&lt;BUCKET_NAME&gt;.s3.cloud.ru
AWS_S3_UPLOAD_BUCKET_URL=https://&lt;BUCKET_NAME&gt;.s3.cloud.ru
AWS_S3_UPLOAD_BUCKET_NAME=&lt;BUCKET_NAME&gt;
AWS_S3_PRIVATE_STYLE=false
AWS_S3_MAX_FILE_SIZE=26214400
AWS_S3_SIGNATURE_VERSION=v4

# GitLab OAuth authorization
GITLAB_CLIENT_ID=&lt;GITLAB_APP_ID&gt;
GITLAB_CLIENT_SECRET=&lt;GITLAB_CLIENT_SECRET&gt;
GITLAB_AUTH_URI=https://&lt;GITLAB_DOMAIN&gt;/oauth/authorize
GITLAB_TOKEN_URI=https://&lt;GITLAB_DOMAIN&gt;/oauth/token
GITLAB_USERINFO_URI=https://&lt;GITLAB_DOMAIN&gt;/oauth/userinfo
OAUTH2_USERINFO_NAME=gitlab
OAUTH2_DISPLAY_NAME=gitlab
OAUTH2_SCOPE=openid email profile

# SSL Configuration
FORCE_HTTPS=true

# Rate limiting
RATE_LIMITER_ENABLE=true
RATE_LIMITER_REQUESTS=1000
RATE_LIMITER_DURATION_WINDOW=60

# Updates
ENABLE_UPDATES=true

# Logging
DEBUG=true
LOG_LEVEL=info
</code></pre>
</div>
<p>Где:</p>
<ul>
<li>&lt;SECRET_KEY&gt;, &lt;UTILS_SECRET&gt; — секреты, сгенерированные на шаге 5.</li>
<li>&lt;POSTGRES_PASSWORD&gt; — пароль от базы данных, сгенерированный ранее.</li>
<li>&lt;TENANT_ID&gt; — ID тенанта сервиса Object Storage.</li>
<li>&lt;REGION&gt; — регион Object Storage.</li>
<li>&lt;SECRET_KEY_ID&gt;, &lt;SECRET_KEY&gt; — ID ключа и секретный ключ доступа к Object Storage.</li>
<li>&lt;BUCKET_NAME&gt; — название бакета Object Storage.</li>
<li>&lt;GITLAB_APP_ID&gt;, &lt;GITLAB_CLIENT_SECRET&gt; — ID и секретный ключ доступа к приложению GitLab.</li>
<li>&lt;GITLAB_DOMAIN&gt; — адрес сервиса GitLab. Может быть собственный или https://gitlab.com/.</li>
</ul>
<ol start="10">
<li>Запустите сервис:</li>
</ol>
<div class="code-block">
<pre><code>docker compose up -d
</code></pre>
</div>
<ol start="11">
<li>Проверьте, что сервисы запущены:</li>
</ol>
<div class="code-block">
<pre><code>docker compose ps
</code></pre>
</div>
<ol start="12">
<li>Перейдите по адресу https://wiki.&lt;IP-адрес&gt;.nip.io . Откроется страница Outline, и вы будете перенаправлены в GitLab для авторизации.</li>
<li>Авторизуйтесь в GitLab, и вы будете автоматически перенаправлены на страницу Outline.</li>
</ol>
<p><img src="https://cloud.ru/assets/images/outline.png" alt="Страница Outline"></p>
<h3>6. Настройте CORS в Object Storage</h3>
<p>Настройте CORS для бакета в Object Storage, чтобы разрешить безопасное взаимодействие с вашим приложением.</p>
<ol>
<li>В личном кабинете перейдите в сервис Хранение данных → Object Storage.</li>
<li>Откройте бакет outline-wiki .</li>
<li>Перейдите на вкладку Правила CORS.</li>
<li>Нажмите Добавить правило.</li>
<li>В поле Источники укажите https://wiki.&lt;IP-адрес&gt;.nip.io, где &lt;IP-адрес&gt; — это публичный IP-адрес виртуальной машины.</li>
<li>В поле HTTP-методы выберите GET, PUT, POST, DELETE .</li>
</ol>
<h3>7. Удалите доступ по SSH для виртуальной машины</h3>
<p>Обеспечьте безопасность, удалив доступ по SSH для вашей виртуальной машины, поскольку он больше не требуется.</p>
<ol>
<li>Перейдите в раздел Сетевые параметры.</li>
<li>Нажмите изменить группы безопасности для публичного IP-адреса.</li>
<li>Удалите группу SSH-access_ru.</li>
<li>Нажмите Сохранить.</li>
<li>Убедитесь, что доступа нет — попробуйте подключиться к виртуальной машине по SSH.</li>
</ol>
<h3>Результат</h3>
<p>Включите развернули Wiki-сервис для командной работы в облаке Cloud.ru с надежной сетевой изоляцией и публикацией по HTTPS.</p>
<p>Полученные навыки помогут вам создавать сервисы с использованием облачного хранилища и безопасной инфраструктурой.</p>