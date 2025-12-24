---
source_image: docs_tutorials-evolution_list_topics_foundation-models__connect-librechat.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 162.52
tokens: 19829
characters: 11270
timestamp: 2025-12-24T05:36:11.761643
finish_reason: stop
---

### Подключение корпоративной AI чат-платформы LibreChat к Foundation Models

С помощью этого руководства вы развернете чат-платформу LibreChat на бесплатной виртуальной машине в облаке Cloud.ru Evolution.

Вы создадите виртуальную машину Ubuntu 22.04, назначите ей публичный IP-адрес, установите Docker и Docker Compose, запустите LibreChat и опубликуете сервис через Nginx с SSL-сертификатом, выпущенным в Let’s Encrypt.

В результате вы сконфигурируете LibreChat для работы с Foundation Models и получите сервис, готовый к работе.

Вы будете использовать следующие сервисы:

• Foundation Models — сервис для доступа к API популярных фундаментальных моделей машинного обучения с открытым исходным кодом.
• Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.
• Публичный IP-адрес.
• Docker — система контейнеризации.
• Docker Compose — инструмент для запуска и управления Docker-контейнерами.
• Бесплатный сервис nip.io для получения публичного доменного имени и сертификата. Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.
• Nginx — веб-сервер для проксирования запросов и организации защищенного HTTPS-доступа к приложению.
• Let’s Encrypt — сервис для автоматического получения бесплатного SSL-сертификата.
• LibreChat — бесплатная open-source-платформа, объединяющая в одном веб-интерфейсе различные языковые модели.

Шаги:

1. Разверните необходимые ресурсы в облаке.
2. Сгенерируйте API-ключ для доступа к Foundation Models.
3. Настройте окружение на виртуальной машине.
4. Насторойте Nginx и HTTPS.
5. Разверните приложение LibreChat.
6. Отключите доступ по SSH для виртуальной машины.

Перед началом работы

1. Зарегистрируйтесь в личном кабинете Cloud.ru.
   Если вы уже зарегистрированы, войдите под своей учетной записью.
2. Сгенерируйте SSH-ключ.
3. Загрузите публичную часть SSH-ключа в облако Cloud.ru Evolution.

1. Разверните необходимые ресурсы в облаке

На этом шаге вы создадите группу безопасности и виртуальную машину.

1. Создайте группу безопасности с названием ai-chat-service и добавьте в нее правила:
   • Правило входящего трафика 1:
     • Протокол: TCP
     • Порт: 443
     • Типисточника: IP-адрес
     • Источник: 0.0.0.0/0
   • Правило входящего трафика 2:
     • Протокол: TCP
     • Порт: 80
     • Типисточника: IP-адрес
     • Источник: 0.0.0.0/0
   • Правило исходящего трафика:
     • Протокол: Любой
     • Тип адресата: IP-адрес
     • Адресат: 0.0.0.0/0

На странице Сети → Группы безопасности убедитесь, что отображается группа безопасности ai-chat-service со статусом «Создана».

2. Создайте бесплатную виртуальную машину со следующими параметрами:
   • Название: ai-chat-service
   • Образ: публичный образ Ubuntu 22.04
   • Подключить публичный IP: включено
   • Тип IP: прямой IP-адрес
   • Группы безопасности: SSH-access_ru.AZ-1 , ai-chat-service
   • Логин: aichat
   • Метод аутентификации: Публичный ключ и Пароль
   • Публичный ключ: укажите ранее созданный ключ
   • Пароль: задайте надежный пароль
   • Имя хоста: ai-chat-service

3. На странице Инфраструктура → Виртуальные машины убедитесь, что отображается виртуальная машина ai-chat-service со статусом «Запущена».

2. Сгенерируйте API-ключ для доступа к Foundation Models

Следуйте инструкции по созданию API-ключа для Foundation Models. Сохраните API-ключ, он будет использоваться для конфигурации сервиса.

1. На верхней панели слева нажмите ::: и перейдите в раздел Пользователи, на вкладку Сервисные аккаунты.
2. Нажмите на название сервисного аккаунта, который будете использовать для отправки запроса к модели.

3. В разделе Учетные данные доступа нажмите Создать API-ключ.

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

1. Подключитесь к виртуальной машине ai-chat-service через серийную консоль или по SSH.
2. Обновите систему и установите необходимые зависимости:

```sh
sudo apt update && sudo apt upgrade -y && \
sudo apt install -y curl apt-transport-https ca-certificates software-properties-common gnupg2 lsb-release
```

3. Установите Docker:

```sh
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io -y
```

4. Дайте текущему пользователю права на запуск Docker:

```sh
sudo usermod -aG docker $USER
newgrp docker
```

5. Установите Docker Compose:

```sh
sudo apt-get install docker-compose-plugin -y
```

6. Проверьте, что Docker и Docker Compose установлены корректно:

```sh
docker --version
docker compose version
```

7. Установите Nginx сервер:

```sh
sudo apt install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx
```

8. Установите Let’s Encrypt и плагин для Nginx:

```sh
sudo apt install certbot python3-certbot-nginx -y
```

4. Насторойте Nginx и HTTPS

На этом шаге вы настроите службу Nginx и обеспечите доступ по HTTPS.

1. Подключитесь к виртуальной машине ai-chat-service через серийную консоль или по SSH.
2. Настройте файервол:

```sh
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw enable
```

3. Создайте конфигурационный файл:

```sh
sudo nano /etc/nginx/sites-available/librechat.conf
```

4. Вставьте конфигурацию, заменив <ip-address> на IP-адрес вашей виртуальной машины.

```sh
server {
    listen 80;
    server_name chat.<ip-address>.nip.io www.chat.<ip-address>.nip.io;
    location / {
        proxy_pass http://localhost:3080;
        proxy_set_header Host $host;
        proxy_set_header X-real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

5. Примените конфигурацию и перезапустите Nginx:

```sh
sudo ln -s /etc/nginx/sites-available/librechat /etc/nginx/sites-enabled/librechat.conf
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl reload nginx
```

6. Проверьте, что Nginx работает:

```sh
sudo systemctl status nginx
```

Сервис Nginx должен быть в статусе «active (running)».

7. Перейдите по адресу http://chat.<ip-address>.nip.io . Откроется страница с текстом «502 Bad Gateway».

8. Запустите команду для выпуска SSL-сертификата.

```sh
sudo certbot --nginx -d chat.<ip-address>.nip.io --redirect --agree-tos -m <email>
```

Где:
• <ip-address> — IP-адрес вашей виртуальной машины.
• <email> — email для регистрации сертификата.

9. После выпуска сертификата перейдите по адресу https://chat.<ip-address>.nip.io .

Откроется страница с текстом «502 Bad Gateway». В свойствах сайта браузер отметит соединение как безопасное.

5. Разверните приложение LibreChat

Разверните серверное приложение LibreChat с помощью Docker Compose.

1. Подключитесь к виртуальной машине ai-chat-service через серийную консоль или по SSH.
2. Создайте структуру проекта:

```sh
mkdir -p $HOME/librechat
cd $HOME/librechat
```

3. Сгенерируйте уникальные ключи и сохраните их, они понадобятся в дальнейшем:

```sh
openssl rand -hex 32 # save as JWT_SECRET
openssl rand -hex 32 # save as JWT_REFRESH_SECRET
```

4. Создайте файл docker-compose.yml:

```sh
nano docker-compose.yml
```

5. Вставьте содержимое в файл docker-compose.yml:

```sh
services:
  mongo:
    image: mongo:6.0
    restart: always
    volumes:
      - mongo-data:/data/db
    ports:
      - '27017:27017'

  librechat:
    image: librechat/librechat:latest
    depends_on:
      - mongo
    ports:
      - '3080:3080'
    env_file:
      - ./env
    volumes:
      - /data/app/data
    restart: always
volumes:
  mongo-data:
```

6. Создайте файл конфигурации .env:

```sh
nano docker.env
```

7. Вставьте содержимое в файл, заменив переменные на значения:

```sh
NODE_ENV=production
MONGO_URI=mongodb://mongo:27017/librechat
JWT_SECRET=<jwt_secret>
JWT_REFRESH_SECRET=<jwt-refresh-secret>
DOMAIN_CLIENT=https://chat.<ip-address>.nip.io
DOMAIN_SERVER=https://chat.<ip-address>.nip.io
OPENAI_API_REVERSE_PROXY=https://foundation-models.api.cloud.ru/v1/
OPENAI_API_KEY=<api-key>
```

Где:
• <jwt-secret>, <jwt-refresh-secret> — секреты, сгенерированные ранее.
• <ip-address> — публичный IP-адрес виртуальной машины.
• <api-key> — ключ для доступа к сервису Foundation Models, сгенерированный на шаге 2.

8. Запустите сервис:

```sh
docker-compose up -d
```

9. Проверьте, что сервис запущен:

```sh
docker compose ps
```

10. Сгенерируйте пользователя с правами администратора:

```sh
sudo docker exec -it librechat_librechat_1 \
  npm run create-user <email> --username --email-verified=true
```

Где <email> — email-адрес пользователя. Во время выполнения команды задайте логин и пароль для нового пользователя.

11. Перейдите по адресу https://chat.<ip-address>.nip.io . Откроется страница LibreChat.

12. Авторизуйтесь в LibreChat, используя пароль пользователя с правами администратора.

13. В интерфейсе чата выберите Агенты -> OpenAI и выберите модель для работы в чате.

![Screenshot of the LibreChat interface showing available models and code examples](https://i.imgur.com/3Q5z5QG.png)

14. Введите ваш запрос в чат и получите ответ от LLM-модели Foundation Models.

![Screenshot of the LibreChat interface with code example and response](https://i.imgur.com/3Q5z5QG.png)

6. Отключите доступ по SSH для виртуальной машины

Для повышения безопасности закройте доступ по SSH, после того как вы развернули и настроили сервис.

1. В личном кабинете Cloud.ru на верхней панели слева нажмите ::: и выберите Инфраструктура → Виртуальные машины.
2. В списке виртуальных машин выберите ai-chat-service .
3. Перейдите на вкладку Сетевые параметры.
4. В строке подсети нажмите ::: и выберите Изменить группы безопасности.
5. Удалите группу SSH-access_ru и сохраните изменения.
6. Убедитесь, что доступ нет — попробуйте подключиться к виртуальной машине по SSH. После отключения доступа по SSH, администрирование сервиса будет доступно через серийную консоль виртуальной машины.

Результат

В этой лабораторной работе вы развернули чат-сервис для работы в облаке Cloud.ru с сетевой изоляцией и публикацией по HTTPS. Полученные навыки помогут вам создавать AI-сервисы с использованием сервисов Foundation Models.

Для командной работы с конфигурируйте требуемый провайдер авторизации.