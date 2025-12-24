---
source_image: docs_tutorials-evolution_list_topics_managed-kafka__kafka-ui.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 123.45
tokens: 16401
characters: 12079
timestamp: 2025-12-24T05:52:30.367267
finish_reason: stop
---

<h2>Kafbat UI для менеджмента и мониторинга кластера Managed Kafka®</h2>
<p>С помощью этого руководства вы развернете сервис Kafbat UI на виртуальной машине Ubuntu 22.04, создадите Managed Kafka® и свяжете Kafka с Kafbat UI. Вы будете использовать виртуальную сеть VPC и подсети для связи виртуальной машины и сервиса Managed Kafka®.</p>
<p>Kafbat UI — это бесплатный и легковесный веб-интерфейс с открытым исходным кодом для мониторинга и управления кластерами Kafka, поддерживающий просмотр брокеров, топиков, групп потребителей, браузинг сообщений и работу со схемами Avro/JSON Schema/Protobuf через Schema Registry. Инструмент упрощает наблюдаемость потоков данных и ускоряет устранение неполадок, предоставляя мультикластерное управление, создание и конфигурацию топиков, а также дополнительные функции вроде RBAC и маскирования данных.</p>
<p>Вы будете использовать следующие сервисы:</p>
<ul>
<li>Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.</li>
<li>Managed Kafka® — сервис для развертывания и управления кластерами Kafka®.</li>
<li>Публичный IP-адрес — для доступа к сервису через интернет.</li>
<li>VPC — изолированная виртуальная сеть для создания безопасной инфраструктуры.</li>
<li>Docker — система контейнеризации.</li>
<li>Docker Compose — инструмент для запуска и управления Docker-контейнерами.</li>
<li>Бесплатный сервис nip.io для получения публичного доменного имени и сертификата. Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.</li>
<li>Nginx — веб-сервер для проксирирования запросов и организации защищенного HTTPS-доступа к приложению.</li>
<li>Let’s Encrypt — сервис для автоматического получения бесплатного SSL-сертификата.</li>
<li>Kafbat UI — веб-интерфейс с открытым исходным кодом для мониторинга и управления кластерами Kafka.</li>
</ul>
<p>Шаги:</p>
<ol>
<li>Разверните необходимые ресурсы в облаке.</li>
<li>Настройте окружение на виртуальной машине.</li>
<li>Настройте nginx и HTTPS.</li>
<li>Разверните и настройте сервис Kafbat UI.</li>
<li>Удалите доступ по SSH для виртуальной машины.</li>
</ol>
<h3>Перед началом работы</h3>
<ol>
<li>Зарегистрируйтесь в личном кабинете Cloud.ru.<br>Если вы уже зарегистрированы, войдите под своей учетной записью.</li>
<li>Создайте и загрузите SSH-ключ в облако.</li>
</ol>
<h3>1. Разверните необходимые ресурсы в облаке</h3>
<ol>
<li>Создайте виртуальную сеть с названием kafka-ui-VPC.</li>
<li>Создайте подсети:
<ul>
<li>Название: kafka-ui-subnet.</li>
<li>Адрес: 10.10.1.0/24.</li>
<li>VPC: kafka-ui-VPC.</li>
<li>DNS-серверы: 8.8.8.8</li>
</ul>
Убедитесь, что в личном кабинете на странице сервиса VPC:
<ul>
<li>отображается сеть kafka-ui-VPC;</li>
<li>количество подсетей — 1;</li>
<li>подсеть kafka-ui-subnet доступна.</li>
</ul>
</li>
<li>Создайте новую группу безопасности со следующими параметрами:
<ul>
<li>а. Укажите Название группы безопасности, например kafka-ui.</li>
<li>б. Добавьте правила входящего и исходящего трафика.
<ul>
<li>Правило входящего трафика:
<ul>
<li>Протокол: TCP;</li>
<li>Порт: 443;</li>
<li>Тип источника: IP-адрес;</li>
<li>Источник: 0.0.0.0/0.</li>
</ul>
</li>
<li>Правило исходящего трафика:
<ul>
<li>Протокол: Любой;</li>
<li>Тип адресата: IP-адрес;</li>
<li>Адресат: 0.0.0.0/0.</li>
</ul>
</li>
</ul>
</li>
</ul>
Убедитесь, что на странице Сети → Группы безопасности отображается группа безопасности kafka-ui со статусом «Создана».
</li>
<li>Создайте виртуальную машину со следующими параметрами:
<ul>
<li>Название: kafka-ui.</li>
<li>Образ: Публичные → Ubuntu 22.04.</li>
<li>Метод аутентификации: SSH-ключ и пароль.</li>
<li>SSH-ключ: ваш SSH-ключ.</li>
<li>Пароль: ваш пароль.</li>
<li>Имя хоста: kafka-ui.</li>
<li>Подключить публичный IP: включено.</li>
<li>Тип IP-адреса: Прямой.</li>
<li>Группы безопасности: SSH-access_ru.AZ-1, kafka-ui.</li>
<li>Подсеть: kafka-ui-subnet.</li>
<li>Гарантированная доля vCPU: 10%.</li>
<li>vCPU: 1.</li>
<li>RAM: 1.</li>
</ul>
Убедитесь, что в личном кабинете на странице сервиса «Виртуальные машины» отображается виртуальная машина kafka-ui в статусе «Запущена».
</li>
<li>Создайте кластер Managed Kafka® со следующими параметрами:
<ul>
<li>Название: kafka-ui.</li>
<li>Версия Kafka: 3.9.0.</li>
<li>Брокеры: 1.</li>
<li>vCPU: 4.</li>
<li>RAM: 16.</li>
<li>Подсеть: kafka-ui-subnet.</li>
</ul>
Убедитесь, что в личном кабинете на странице сервиса «Managed Kafka®» отображается кластер kafka-ui в статусе «Доступен».
</li>
</ol>
<h3>2. Настройте окружение на виртуальной машине</h3>
<p>Настройте систему и установите необходимые пакеты на виртуальной машине.</p>
<ol>
<li>Подключитесь к виртуальной машине через серийную консоль или по SSH.</li>
<li>Обновите систему и установите необходимые зависимости:</li>
</ol>
<pre><code>sudo apt update &amp;&amp; sudo apt upgrade -y
sudo apt install unzip gnupg software-properties-common apt-transport-https ca-certificates nginx snapd
sudo snap install core; sudo snap refresh core
sudo snap install certbot --classic
sudo ln -s /snap/bin/certbot /usr/bin/certbot
</code></pre>
<ol start="3">
<li>Установите Docker и Docker Compose:</li>
</ol>
<pre><code># Add Docker's GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Add Docker repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list &gt;&gt; /dev/null

# Install Docker
sudo apt update &amp;&amp; sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin docker

# Add user to docker group
sudo usermod -aG docker $USER
newgrp docker
</code></pre>
<ol start="4">
<li>Проверьте, что Docker установлен корректно:</li>
</ol>
<pre><code>docker --version
docker compose version
</code></pre>
<h3>3. Настройте nginx и HTTPS</h3>
<p>Настройте службу nginx и обеспечьте доступ по HTTPS.</p>
<ol>
<li>Подключитесь к виртуальной машине через серийную консоль или по SSH.</li>
<li>Сконфигурируйте межсетевой экран:</li>
</ol>
<pre><code>sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw enable
</code></pre>
<ol start="3">
<li>Создайте конфигурационный файл:</li>
</ol>
<pre><code>sudo nano /etc/nginx/sites-available/kafkau.conf
</code></pre>
<ol start="4">
<li>Вставьте конфигурацию, заменив <i>&lt;IP-адрес&gt;</i> на IP-адрес вашей виртуальной машины.</li>
</ol>
<pre><code>server {
    listen 80;
    server_name kafkaui.&lt;IP-адрес&gt;.nip.io www.kafkaui.&lt;IP-адрес&gt;.nip.io;

    location / {
        proxy_pass http://localhost:8080;
        proxy_http_version 1.1;
        # Websocket headers
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        # Preserve original host / IP
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        # Timeouts suitable for long-lived Kafbat UI streams
        proxy_read_timeout 600s;
        proxy_send_timeout 600s;
    }
}
</code></pre>
<ol start="5">
<li>Примените конфигурацию и перезапустите nginx:</li>
</ol>
<pre><code>sudo ln -sf /etc/nginx/sites-available/kafkau.conf /etc/nginx/sites-enabled/kafkau.conf
sudo ln -sf /etc/nginx/sites-enabled/default
sudo nginx
sudo systemctl reload nginx
</code></pre>
<ol start="6">
<li>Проверьте, что nginx работает:</li>
</ol>
<pre><code>sudo systemctl status nginx
</code></pre>
<p>Сервис nginx должен быть в статусе «active (running)».</p>
<ol start="7">
<li>Перейдите по адресу <a href="http://kafkaui.&lt;IP-адрес&gt;.nip.io">http://kafkaui.&lt;IP-адрес&gt;.nip.io</a>.</li>
</ol>
<p>Откроется страница с текстом 502 Bad Gateway.</p>
<ol start="8">
<li>Запустите команду для выпуска SSL-сертификата.</li>
</ol>
<pre><code>sudo certbot --nginx -d kafkaui.&lt;IP-адрес&gt;.nip.io --redirect --agree-tos --email &lt;EMAIL&gt;
</code></pre>
<p>Где:</p>
<ul>
<li>&lt;IP-адрес&gt; — IP-адрес вашей виртуальной машины.</li>
<li>&lt;EMAIL&gt; — ваш email.</li>
</ul>
<ol start="9">
<li>После успешного выпуска сертификата перейдите по адресу <a href="https://kafkaui.&lt;IP-адрес&gt;.nip.io">https://kafkaui.&lt;IP-адрес&gt;.nip.io</a>.</li>
</ol>
<p>Откроется страница с текстом 502 Bad Gateway. В свойствах сайта браузер отметит соединение как безопасное.</p>
<h3>4. Разверните и настройте сервис Kafbat UI</h3>
<ol>
<li>Создайте директорию для приложения и перейдите в нее:</li>
</ol>
<pre><code>mkdir kafkau
cd kafkau
</code></pre>
<ol start="2">
<li>Создайте файл docker-compose.yml:</li>
</ol>
<pre><code>nano docker-compose.yml
</code></pre>
<ol start="3">
<li>Вставьте содержимое файла:</li>
</ol>
<pre><code>services:
    kafbat-ui:
        image: kafbat/kafka-ui:4783bd
        container_name: kafbat-ui
        ports:
            - "8080:8080"
        restart: always
        # Load credentials from .env
        env_file:
            - .env

        environment:
            # Use Cluster basic
            KAFKA_BROKERS=${KAFKA_BROKERS}
            KAFKA_USERNAME=${KAFKA_USERNAME}
            KAFKA_PASSWORD=${KAFKA_PASSWORD}
            KAFKA_UI_USER=${KAFKA_UI_USER}
            KAFKA_UI_PASSWORD=${KAFKA_UI_PASSWORD}

            DYNAMIC_CONFIG_ENABLED="true"

            AUTH_TYPE: LOGIN_FORM
            SPRING_SECURITY_USER_NAME="${KAFKA_UI_USER}"
            SPRING_SECURITY_USER_PASSWORD="${KAFKA_UI_PASSWORD}"

            healthcheck:
                test: ["CMD", "wget", "--no-verbose", "--tries=1", "--spider", "http://localhost:8080/actuator"]
                interval: 30s
                timeout: 10s
                retries: 3
                start_period: 40s
</code></pre>
<ol start="4">
<li>Создайте файл .env:</li>
</ol>
<pre><code>nano .env
</code></pre>
<ol start="5">
<li>Вставьте содержимое файла:</li>
</ol>
<pre><code>KAFKA_BROKERS=&lt;KAFKA_BROKER_IP&gt;:9094
KAFKA_USERNAME=&lt;KAFKA_USERNAME&gt;
KAFKA_PASSWORD=&lt;KAFKA_PASSWORD&gt;
KAFKA_UI_USER=&lt;KAFKA_UI_USER&gt;
KAFKA_UI_PASSWORD=&lt;KAFKA_UI_PASSWORD&gt;
</code></pre>
<p>Где:</p>
<ul>
<li>&lt;KAFKA_BROKER_IP&gt; — IP-адрес сервиса Managed Kafka®.</li>
<li>&lt;KAFKA_USERNAME&gt; — логин от кластера Managed Kafka® с ролью Admin.</li>
<li>&lt;KAFKA_PASSWORD&gt; — пароль от кластера Managed Kafka® с ролью Admin.</li>
<li>&lt;KAFKA_UI_USER&gt; — логин для доступа к сервису Kafbat UI.</li>
<li>&lt;KAFKA_UI_PASSWORD&gt; — пароль для доступа к сервису Kafbat UI.</li>
</ul>
<p>IP-адрес, логины и пароли можно найти на странице информации о кластере в блоке Данные для подключения.</p>
<ol start="6">
<li>Запустите сервис:</li>
</ol>
<pre><code>docker compose up -d
</code></pre>
<ol start="7">
<li>Перейдите по адресу <a href="https://kafkaui.&lt;IP-адрес&gt;.nip.io">https://kafkaui.&lt;IP-адрес&gt;.nip.io</a> в браузере. Откроется страница Kafbat UI, и вы будете перенаправлены на страницу авторизации.</li>
<li>Зайдите в приложение с логином и паролем, заданными в .env (KAFKA_UI_USER/KAFKA_UI_PASSWORD).</li>
</ol>
<h3>5. Удалите доступ по SSH для виртуальной машины</h3>
<p>Так как для настроенного сервиса больше не требуется доступ по SSH, удалите доступ для повышения безопасности.</p>
<ol>
<li>В личном кабинете перейдите в сервис «Виртуальные машины» и выберите машину kafka-ui, созданную на первом шаге.</li>
<li>Перейдите в раздел Сетевые параметры.</li>
<li>Нажмите на Изменить группы безопасности для публичного IP-адреса.</li>
<li>Удалите группу «SSH-access_ru».</li>
<li>Нажмите Сохранить.</li>
<li>Попробуйте подключиться к виртуальной машине по SSH по инструкции и убедитесь, что доступ отсутствует.</li>
</ol>
<h3>Результат</h3>
<p>Вы развернули Kafbat UI на виртуальной машине Ubuntu 22.04, связали его с сервисом Managed Kafka® через виртуальную сеть VPC и подсети. Вы получили опыт управления и мониторинга Kafka-кластера через удобный веб-интерфейс, включая просмотр топиков, групп потребителей и сообщений.</p>