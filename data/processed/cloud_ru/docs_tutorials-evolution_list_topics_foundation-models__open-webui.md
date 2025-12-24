---
source_image: docs_tutorials-evolution_list_topics_foundation-models__open-webui.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 149.39
tokens: 18357
characters: 10701
timestamp: 2025-12-24T05:39:18.315433
finish_reason: stop
---

### Интеграция веб-интерфейса Open WebUI с Foundation Models

С помощью этого руководства вы развернете веб-интерфейс Open WebUI на бесплатной виртуальной машине в облаке Cloud.ru Evolution. Создайте виртуальную машину Ubuntu 22.04, назначите ей публичный IP-адрес, установите Docker и Docker Compose, запустите Open WebUI и опубликуете сервис через Nginx с SSL-сертификатом, выпущенным в Let’s Encrypt. В результате вы сконфигурируете Open WebUI для работы с Foundation Models и получите сервис, готовый к работе.

Вы будете использовать следующие сервисы:

• Foundation Models — сервис для доступа к API популярных фундаментальных моделей машинного обучения с открытым исходным кодом.
• Виртуальная машина — сервис, в рамках которого предоставляется виртуальная машина.
• Публичный IP-адрес.
• Docker — система контейнеризации.
• Docker Compose — инструмент для запуска и управления Docker-контейнерами.
• Бесплатный сервис nip.io для получения публичного доменного имени и сертификата. Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.
• Nginx — веб-сервер для проксиирования запросов и организации защищенного HTTPS-доступа к приложению.
• Let’s Encrypt — сервис для автоматического получения бесплатного SSL-сертификата.
• Open WebUI — веб-интерфейс с открытым исходным кодом для работы с различными моделями искусственного интеллекта.

Шаги:

1. Разверните необходимые ресурсы в облаке.
2. Сгенерируйте API-ключ для доступа к Foundation Models.
3. Настройте окружение на виртуальной машине.
4. Настройте Nginx и HTTPS.
5. Разверните приложение Open WebUI.
6. Отключите доступ по SSH для виртуальной машины.

Перед началом работы

1. Зарегистрируйтесь в личном кабинете Cloud.ru.
   Если вы уже зарегистрированы, войдите под своей учетной записью.
2. Сгенерируйте SSH-ключ.
3. Загрузите публичную часть SSH-ключа в облако Cloud.ru Evolution.

1. Разверните необходимые ресурсы в облаке

На этом шаге вы создадите группу безопасности и виртуальную машину.

1. Создайте группу безопасности с названием open-web-ui и добавьте в нее правила:
   • Правило входящего трафика 1:
     • Протокол: TCP
     • Порт: 443
     • Тип источника: IP-адрес
     • Источник: 0.0.0.0/0
   • Правило входящего трафика 2:
     • Протокол: TCP
     • Порт: 80
     • Тип источника: IP-адрес
     • Источник: 0.0.0.0/0
   • Правило исходящего трафика:
     • Протокол: Любой
     • Тип адресата: IP-адрес
     • Адресат: 0.0.0.0/0

2. На странице Сети → Группы безопасности убедитесь, что отображается группа безопасности open-web-ui со статусом «Создана».

3. Создайте бесплатную виртуальную машину со следующими параметрами:
   • Название: open-web-ui
   • Образ: публичный образ Ubuntu 22.04
   • Подключить публичный IP: включено
   • Публичный IP: Арендовать новый
   • Группы безопасности: SSH-access_ru.AZ-1 , open-web-ui
   • Логин: openwebui
   • Метод аутентификации: Публичный ключ и Пароль
   • Публичный ключ: укажите ранее созданный SSH-ключ
   • Пароль: задайте надежный пароль
   • Имя хоста: open-web-ui

4. На странице Инфраструктура → Виртуальные машины убедитесь, что отображается виртуальная машина open-web-ui со статусом «Запущена».

2. Сгенерируйте API-ключ для доступа к Foundation Models

Следуйте инструкции по созданию API-ключа для Foundation Models. Сохраните API-ключ, он будет использоваться для конфигурации сервиса.

1. На верхней панели слева нажмите и перейдите в раздел Пользователи, на вкладку Сервисные аккаунты.
2. Нажмите на название сервисного аккаунта, который будете использовать для отправки запроса к модели.

![Сервисные аккаунты](https://cloud.ru/images/servicenew.png)

3. В разделе Учетные данные доступа нажмите Создать API-ключ.

![Создать API-ключ](https://cloud.ru/images/newaccount.png)

4. Введите название и описание API-ключа, которое поможет в будущем идентифицировать его среди других ключей.

5. Заполните параметры API-ключа:
   • Сервисы — Foundation Models .
   • Время действия — срок действия API-ключа и часовой пояс. Вы можете установить значение от одного дня до одного года с текущей даты. Если параметр не задан, срок действия ключа устанавливается на максимальное значение — один год. Из соображений безопасности рекомендуется выставлять средние значения, например 90 дней.
   • Интервал работы ключа — один или несколько интервалов времени, в которые можно использовать API-ключ.

6. Нажмите Создать.

7. Сохраните Key Secret. После закрытия окна получить его будет нельзя.

Созданный API-ключ появится в списке ключей в статусе «Активен». Подробнее о работе с API-ключом.

3. Настройте окружение на виртуальной машине

На этом шаге вы установите необходимые пакеты и настроите систему на виртуальной машине.

1. Подключитесь к виртуальной машине open-web-ui через серийную консоль или по SSH.

2. Обновите систему и установите необходимые зависимости:

```sh
sudo apt update && sudo apt upgrade -y &&\
sudo apt install -y curl apt-transport-https ca-certificates software-properties-common gnupg2 lsb-release
```

3. После обновления желательно перезагрузить машину:

```sh
sudo reboot
```

4. Установите Docker:

```sh
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io -y
```

5. Дайте текущему пользователю права на запуск Docker:

```sh
sudo usermod -aG docker $USER
newgrp docker
```

6. Установите Docker Compose:

```sh
sudo apt-get install docker-compose -y
```

7. Проверьте, что Docker и Docker Compose установлены корректно:

```sh
docker --version
docker compose version
```

8. Установите сервер Nginx:

```sh
sudo apt install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx
```

9. Установите Let’s Encrypt и плагин для Nginx:

```sh
sudo apt install certbot python3-certbot-nginx -y
```

4. Настройте Nginx и HTTPS

На этом шаге настройте службу Nginx и обеспечьте доступ по HTTPS.

1. Подключитесь к виртуальной машине open-web-ui через серийную консоль или по SSH.

2. Настройте файервол:

```sh
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw enable
```

3. Создайте конфигурационный файл:

```sh
sudo nano /etc/nginx/sites-available/openwebui.conf
```

4. Вставьте конфигурацию, заменив <ip-address> на IP-адрес вашей виртуальной машины:

```sh
server {
    listen 80;
    server_name webui.<ip-address>.nip.io www.webui.<ip-address>.nip.io;

    location / {
        proxy_pass http://localhost:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
}
```

5. Примените конфигурацию и перезапустите Nginx:

```sh
sudo ln -sf /etc/nginx/sites-available/openwebui.conf /etc/nginx/sites-enabled/openwebui.conf
sudo nginx -t
sudo systemctl reload nginx
```

6. Проверьте, что Nginx работает:

```sh
sudo systemctl status nginx
```

Сервис Nginx должен быть в статусе «active (running)».

7. Перейдите по адресу http://webui.<ip-address>.nip.io . Откроется страница с текстом «502 Bad Gateway».

8. Запустите команду для выпуска SSL-сертификата:

```sh
sudo certbot --nginx -d webui.<ip-address>.nip.io --redirect --agree-tos --email <email>
```

Где:
• <ip-address> — IP-адрес вашей виртуальной машины.
• <email> — email для регистрации сертификата.

9. После выпуска сертификата перейдите по адресу https://webui.<ip-address>.nip.io .

Откроется страница с текстом «502 Bad Gateway». В свойствах сайта браузер отметит соединение как безопасное.

5. Разверните приложение Open WebUI

Разверните серверное приложение Open WebUI с помощью Docker Compose.

1. Подключитесь к виртуальной машине open-web-ui через серийную консоль или по SSH.

2. Создайте структуру проекта:

```sh
mkdir -p $HOME/openwebui
cd $HOME/openwebui
```

3. Создайте файл docker-compose.yml:

```sh
nano docker-compose.yml
```

4. Вставьте содержимое в файл docker-compose.yml:

```yaml
services:
  open-web-ui:
    image: ghcr.io/open-webui/open-webui:latest
    ports:
      - '8080:8080'
    env_file:
      - ./env
    volumes:
      - open-web-ui:/app/backend/data
    restart: always
volumes:
  open-web-ui:
```

5. Создайте файл конфигурации .env:

```sh
nano .env
```

6. Вставьте содержимое в файл, заменив переменные на значения:

```sh
OPENAI_API_BASE_URL=https://foundation-models.api.cloud.ru/v1/
OPENAI_API_KEY=<api-key>
```

Где <api-key> — ключ для доступа к сервису Foundation Models, сгенерированный на шаге 2.

7. Запустите сервис:

```sh
docker-compose up -d
```

8. Проверьте, что сервис запущен:

```sh
docker compose ps
```

9. Перейдите по адресу https://webui.<ip-address>.nip.io . Откроется страница Open WebUI, при первом входе система попросит ввести регистрационные данные Администратора.

Давайте начнём с Open WebUI
Open WebUI не устанавливает никаких внешних соединений, и ваши данные надежно хранятся на вашем локальном сервере.

Имя
Введите ваше полное имя
Электронная почта
Введите вашу электронную почту
Пароль
Введите ваш пароль
Создать аккаунт Администратора

10. В интерфейсе Open WebUI выберите модель для работы.

11. Введите ваш запрос в чат и получите ответ от LLM-модели Foundation Models.

6. Отключите доступ по SSH для виртуальной машины

Для повышения безопасности закройте доступ по SSH, после того как вы развернули и настроили сервис.

1. В личном кабинете Cloud.ru на верхней панели слева нажмите и выберите Инфраструктура → Виртуальные машины.

2. В списке виртуальных машин выберите open-web-ui.

3. Перейдите на вкладку Сетевые параметры.

4. В строке подсети нажмите и выберите Изменить группы безопасности.

5. Удалите группу SSH-access ru и сохраните изменения.

6. Убедитесь, что доступа нет — попробуйте подключиться к виртуальной машине по SSH. После отключения доступа по SSH, администрирование сервиса будет доступно через серийную консоль виртуальной машины.

Результат

В данной лабораторной работе вы развернули чат-сервис для работы в облаке Cloud.ru с сетевой изоляцией и публикацией по HTTPS. Полученные навыки помогут вам создавать AI-сервисы с использованием сервисов Foundation Models.

Вы можете добавить аутентификацию по SSO или подключить внешнее S3 хранилище для хранения файлов, которые пользователи добавляют в Open WebUI при работе с моделями, например, Evolution Object Storage.