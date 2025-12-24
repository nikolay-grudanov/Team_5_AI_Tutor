---
source_image: docs_tutorials-evolution_list_topics_vm__postgresql-keycloak.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 292.81
tokens: 15350
characters: 10951
timestamp: 2025-12-24T06:34:09.389405
finish_reason: stop
---

<h2>Развертывание Identity Provider Keycloak на виртуальной машине и Managed PostgreSQL®</h2>
<p>С помощью этого руководства вы развернете Identity Provider Keycloak в облаке для централизованной аутентификации пользователей. Вы создадите инфраструктуру, настроите подключение к управляемой базе данных Managed PostgreSQL®, опубликуете сервис через Nginx и обеспечите безопасный доступ по HTTPS. В результате вы получите готовый сервис аутентификации, полностью изолированный в собственной VPC и доступный из интернета.</p>
<p>Вы будете использовать следующие сервисы:</p>
<ul>
<li>Виртуальная машина — сервис, в рамках которого предоставляется виртуальная машина для размещения приложения.</li>
<li>Публичный IP-адрес для доступа к сервису через интернет.</li>
<li>Managed PostgreSQL — управляемая база данных PostgreSQL.</li>
<li>VPC — изолированная виртуальная сеть для создания безопасной инфраструктуры.</li>
<li>Бесплатный сервис nip.io для получения публичного доменного имени и сертификата. Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.</li>
<li>Nginx — веб-сервер для проксирования запросов и организации защищенного HTTPS-доступа к приложению.</li>
<li>Let’s Encrypt — сервис для автоматического получения бесплатного SSL-сертификата.</li>
</ul>
<p>Шаги:</p>
<ol>
<li>Разверните ресурсы в облаке.</li>
<li>Настройте окружение виртуальной машины.</li>
<li>Настройте защищенный доступ через Nginx.</li>
<li>Установите и запустите Keycloak.</li>
<li>Отключите SSH-доступ.</li>
</ol>
<h3>Перед началом работы</h3>
<ol>
<li>Зарегистрируйтесь в личном кабинете Cloud.ru.<br>Если вы уже зарегистрированы, войдите под своей учетной записью.</li>
<li>Сгенерируйте ключевую пару и загрузите публичный ключ в Cloud.ru Evolution.</li>
</ol>
<h4>1. Разверните ресурсы в облаке</h4>
<p>На этом шаге вы подготовите сеть, группу безопасности, виртуальную машину и кластер Managed PostgreSQL®. Все ресурсы будут расположены в одной VPC, что обеспечит сетевую изоляцию.</p>
<ol>
<li><b>Создайте виртуальную сеть с названием identity-provider-VPC</b>.</li>
<li><b>Создайте подсеть</b> со следующими параметрами:
<ul>
<li>Название — identity-provider-subnet .</li>
<li>VPC — identity-provider-VPC .</li>
<li>Адрес — 10.10.1.0/24 .</li>
<li>DNS-серверы — 8.8.8.8 .</li>
</ul>
</li>
<li><b>Создайте новую группу безопасности</b> со следующими параметрами:
<ul>
<li>а. Укажите Название группы безопасности, например identity-provider-sg .</li>
<li>б. Добавьте правила входящего и исходящего трафика.</li>
</ul>
<table>
<tr>
<th>Трафик</th>
<th>Протокол</th>
<th>Порт</th>
<th>Тип источника/адресата</th>
<th>Источник/Адресат</th>
</tr>
<tr>
<td>Входящий</td>
<td>TCP</td>
<td>443</td>
<td>IP-адрес</td>
<td>0.0.0.0/0</td>
</tr>
<tr>
<td>Входящий</td>
<td>TCP</td>
<td>80</td>
<td>IP-адрес</td>
<td>0.0.0.0/0</td>
</tr>
<tr>
<td>Исходящий</td>
<td>Любой</td>
<td>Оставьте пустым</td>
<td>IP-адрес</td>
<td>0.0.0.0/0</td>
</tr>
</table>
</li>
<li><b>Создайте виртуальную машину</b> со следующими параметрами:
<ul>
<li>Название — identity-provider .</li>
<li>Образ — публичный образ Ubuntu 22.04.</li>
<li>Сетевой интерфейс — выберите тип Подсеть с публичным IP .</li>
<li>VPC — identity-provider-VPC .</li>
<li>Подсеть — identity-provider-subnet .</li>
<li>Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.</li>
<li>Группы безопасности — добавьте группу identity-provider-sg .</li>
<li>Логин — keycloak .</li>
<li>Метод аутентификации — Публичный ключ и Пароль .</li>
<li>Публичный ключ — укажите ключ, созданный ранее.</li>
<li>Пароль — задайте пароль пользователя.</li>
</ul>
</li>
<li><b>Создайте кластер Managed PostgreSQL</b> со следующими параметрами:
<ul>
<li>В поле Имя кластера укажите identity-provider .</li>
<li>В поле Название базы данных укажите identity_provider_database .</li>
<li>В поле Версия PostgreSQL выберите 16.</li>
<li>Выберите Режим — Стандарт .</li>
<li>Выберите Тип — Single .</li>
<li>Выберите Подсеть — identity-provider-subnet .</li>
</ul>
</li>
</ol>
<p>Убедитесь, что ресурсы созданы и отображаются в личном кабинете:</p>
<ol>
<li>На странице Сети → VPC отображается сеть identity-provider-VPC , а в списке ее подсетей — identity-provider-subnet .</li>
<li>На странице Сети → Группы безопасности отображается группа безопасности identity-provider-sg со статусом «Создана».</li>
<li>На странице Инфраструктура → Виртуальные машины отображается виртуальная машина identity-provider со статусом «Запущена».</li>
<li>На странице Базы данных → Managed PostgreSQL® отображается кластер identity-provider со статусом «Доступен».</li>
</ol>
<h4>2. Настройте окружение виртуальной машины</h4>
<p>На этом шаге вы установите необходимые пакеты и подготовите среду для Keycloak.</p>
<ol>
<li>Подключитесь к виртуальной машине по SSH.</li>
<li>Обновите систему и установите утилиты:</li>
</ol>
<pre>sudo apt update &amp;&amp; sudo apt upgrade -y</pre>
<ol start="3">
<li>Установите и запустите Nginx:</li>
</ol>
<pre>sudo apt install nginx -y<br>sudo systemctl enable nginx<br>sudo systemctl start nginx</pre>
<ol start="4">
<li>Установите Java 17:</li>
</ol>
<pre>sudo apt install openjdk-17-jdk -y<br>export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64<br>echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64' &gt;&gt; ~/.bashrc</pre>
<ol start="5">
<li>Установите Let’s Encrypt и плагин для Nginx:</li>
</ol>
<pre>sudo apt install certbot python3-certbot-nginx -y</pre>
<h4>3. Настройте защищенный доступ через Nginx</h4>
<p>На этом шаге вы зарегистрируете доменное имя, настройте Nginx в качестве защищенного прокси, получите SSL-сертификат и ограничите доступ через межсетевой экран.</p>
<ol>
<li>Создайте конфигурационный файл Nginx:</li>
</ol>
<pre>sudo nano /etc/nginx/sites-available/identity-provider.conf</pre>
<ol start="2">
<li>Вставьте код, заменив <ip_address> на значение публичного IP-адреса виртуальной машины:</li>
</ol>
<pre>server {
    listen 80;
    server_name <ip_address>.nip.io www.<ip_address>.nip.io;
    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto https;
        proxy_set_header X-Forwarded-Host $host;
        proxy_set_header X-Forwarded-Port 443;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_buffer_size 128k;
        proxy_buffers 4 256k;
        proxy_busy_buffers_size 256k;
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }
}</pre>
<ol start="3">
<li>Сконфигурируйте межсетевой экран:</li>
</ol>
<pre>sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw enable</pre>
<ol start="4">
<li>Активируйте конфигурацию и перезапустите Nginx:</li>
</ol>
<pre>sudo ln -sf /etc/nginx/sites-available/identity-provider.conf /etc/nginx/sites-enabled/identity-provider.conf
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx
sudo systemctl reload nginx</pre>
<ol start="5">
<li>Выпустите SSL-сертификат:</li>
</ol>
<pre>sudo certbot --nginx -d <ip_address>.nip.io --redirect --agree-tos -m <email></email></pre>
<p>Где:</p>
<ul>
<li><ip_address> — публичный IP-адрес виртуальной машины.</li>
<li><email> — email для регистрации сертификата.</li>
</ul>
<ol start="6">
<li>Перейдите по адресу https://<ip_address>.nip.io и убедитесь, что браузер отмечает соединение как безопасное.</li>
</ol>
<h4>4. Установите и запустите Keycloak</h4>
<p>На этом шаге вы установите Keycloak, настройте подключение к базе данных и запустите сервис как systemd-службу.</p>
<ol>
<li>Загрузите и распакуйте Keycloak:</li>
</ol>
<pre>cd /opt
sudo wget https://github.com/keycloak/keycloak/releases/download/26.0.2/keycloak-26.0.2.tar.gz
sudo tar -xf keycloak-26.0.2.tar.gz
sudo mv keycloak-26.0.2 keycloak
sudo chown -R keycloak:keycloak /opt/keycloak
sudo chmod o+x /opt/keycloak/bin/</pre>
<ol start="2">
<li>Создайте файл конфигурации Keycloak:</li>
</ol>
<pre>sudo nano /opt/keycloak/conf/keycloak.conf</pre>
<ol start="3">
<li>Вставьте код, заменив значения параметров ниже на свои:</li>
</ol>
<pre>db=postgres
db-username=<postgres_admin_user>
db-password=<postgres_admin_password>
db-url=jdbc:postgresql://<postgres_ip>:5432/identity_provider_database

proxy-edge
hostname=https://<ip_address>.nip.io
http-enabled=true
proxy-headers=x-forwarded
hostname-strict=false
hostname-admin=https://<ip_address>.nip.io

health-enabled=true
metrics-enabled=true</pre>
<p>Где:</p>
<ul>
<li><postgres_admin_user> — имя пользователя кластера Managed PostgreSQL®.</li>
<li><postgres_admin_password> — пароль указанного пользователя.</li>
<li><postgres_ip> — приватный IP-адрес кластера.</li>
<li><ip_address> — публичный IP-адрес виртуальной машины.</li>
</ul>
<ol start="4">
<li>Соберите приложение:</li>
</ol>
<pre>sudo -u keycloak /opt/keycloak/bin/kc.sh build</pre>
<ol start="5">
<li>Создайте файл службы systemd:</li>
</ol>
<pre>sudo nano /etc/systemd/system/keycloak.service</pre>
<ol start="6">
<li>Содержимое файла:</li>
</ol>
<pre>[Unit]
Description=Keycloak Identity Provider
After=network.target
Wants=network.target

[Service]
Type=simple
User=keycloak
Group=keycloak
Environment=JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
WorkingDirectory=/opt/keycloak
ExecStart=/opt/keycloak/bin/kc.sh start
ExecReload=/bin/kill -HUP $MAINPID
KillMode=mixed
TimeoutStopSec=30
Restart=always
RestartSec=10</pre>
<ol start="7">
<li>Создайте временного администратора:</li>
</ol>
<pre>sudo -u keycloak /opt/keycloak/bin/kc.sh bootstrap-admin user</pre>
<ol start="8">
<li>Запустите сервис:</li>
</ol>
<pre>sudo systemctl daemon-reload
sudo systemctl enable keycloak
sudo systemctl start keycloak</pre>
<ol start="9">
<li>Перейдите по адресу https://<ip_address>.nip.io и войдите в администраторскую консоль Keycloak, используя созданные учетные данные.</li>
</ol>
<h4>5. Отключите SSH-доступ</h4>
<p>Когда вы развернули и настроили сервис, закройте доступ по SSH для повышения безопасности.</p>
<ol>
<li>В личном кабинете на верхней панели слева нажмите :: и выберите Инфраструктура → Виртуальные машины.</li>
<li>В списке виртуальных машин выберите identity-provider .</li>
<li>Перейдите на вкладку Сетевые параметры.</li>
<li>В блоке сетевого интерфейса нажмите *** и выберите Изменить группы безопасности.</li>
<li>Удалите группу SSH-access_ru и сохраните изменения.</li>
<li>Убедитесь, что доступа нет — попробуйте подключиться к виртуальной машине по SSH. После отключения доступа по SSH, администрирование сервиса будет доступно через серийную консоль виртуальной машины.</li>
</ol>
<h3>Результат</h3>
<p>Вы развернули Keycloak, настроили его взаимодействие с Managed PostgreSQL®, обеспечили безопасный доступ через Nginx и отключили неиспользуемый SSH-доступ.</p>