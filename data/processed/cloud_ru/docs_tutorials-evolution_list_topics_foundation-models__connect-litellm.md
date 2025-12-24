---
source_image: docs_tutorials-evolution_list_topics_foundation-models__connect-litellm.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 189.87
tokens: 20546
characters: 13566
timestamp: 2025-12-24T05:36:49.060910
finish_reason: stop
---

### Подключение LLM-шлюза Litellm к Foundation Models

Эта статья полезна?

С помощью этого руководства вы развернете LLM-шлюз Litellm на бесплатной виртуальной машине в облаке Cloud.ru Evolution. Вы создадите виртуальную машину Ubuntu 22.04, назначите ей публичный IP-адрес, установите Docker и Docker Compose, запустите Litellm и опубликуйте сервис через Nginx с SSL-сертификатом, выпущенным в Let’s Encrypt. В результате вы сконфигурируете Litellm для работы с Foundation Models и получите сервис, готовый к работе.

Вы будете использовать следующие сервисы:

• Foundation Models — сервис для доступа к API популярных фундаментальных моделей машинного обучения с открытым исходным кодом.
• Виртуальная машина — сервис, в рамках которого предоставляется виртуальная машина.
• Публичный IP-адрес.
• Docker — система контейнеризации.
• Docker Compose — инструмент для запуска и управления Docker-контейнерами.
• Бесплатный сервис nip.io для получения публичного доменного имени и сертификата. Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.
• Nginx — веб-сервер для проксирования запросов и организации защищенного HTTPS-доступа к приложению.
• Let’s Encrypt — сервис для автоматического получения бесплатного SSL-сертификата.
• Litellm — комплексная платформа, предназначенная для упрощения управления несколькими большими языковыми моделями (LLM) через унифицированное API. LitellM предлагает унифицированное API, балансировку нагрузки, механизмы резервирования, отслеживание расходов и обработку ошибок.

Шаги:

1. Разверните необходимые ресурсы в облаке.
2. Сгенерируйте API-ключ для доступа к Foundation Models.
3. Настройте окружение на виртуальной машине.
4. Настройте Nginx и HTTPS.
5. Разверните приложение.
6. Добавьте модели из Foundation Models в Litellm.
7. Обратитесь к добавленным моделям.
8. Отключите доступ по SSH для виртуальной машины.

Перед началом работы

1. Зарегистрируйтесь в личном кабинете Cloud.ru.
   Если вы уже зарегистрированы, войдите под своей учетной записью.
2. Сгенерируйте SSH-ключ.
3. Загрузите публичную часть SSH-ключа в облако Cloud.ru Evolution.

1. Разверните необходимые ресурсы в облаке

На этом шаге вы создадите группу безопасности и виртуальную машину.

1. Создайте группу безопасности с названием litellm-service и добавьте в нее правила:
   • Правило входящего трафика:
     • Протокол: TCP
     • Порт: 443
     • Тип источника: IP-адрес
     • Источник: 0.0.0.0/0
   • Правило исходящего трафика:
     • Протокол: TCP
     • Порт: 80
     • Тип источника: IP-адрес
     • Источник: 0.0.0.0/0
   • Правило исходящего трафика:
     • Протокол: Любой
     • Тип адресата: IP-адрес
     • Адресат: 0.0.0.0/0

2. На странице Сети → Группы безопасности убедитесь, что отображается группа безопасности litellm-service со статусом «Создана».

3. Создайте бесплатную виртуальную машину со следующими параметрами:
   • Название: litellm-service
   • Образ: публичный образ Ubuntu 22.04
   • Подключить публичный IP: включено
   • Тип IP: прямой IP-адрес
   • Группы безопасности: SSH-access-ru.AZ-1 , litellm-service
   • Логин: litellm
   • Метод аутентификации: Публичный ключ и Пароль
   • Публичный ключ: укажите ранее созданный SSH-ключ
   • Пароль: задайте надежный пароль
   • Имя хоста: litellm-service

4. На странице Инфраструктура → Виртуальные машины убедитесь, что отображается виртуальная машина litellm-service со статусом «Запущена».

2. Сгенерируйте API-ключ для доступа к Foundation Models

Следуйте инструкции по созданию API-ключа для Foundation Models. Сохраните API-ключ, он будет использоваться для конфигурации сервиса.

1. На верхней панели слева нажмите и перейдите в раздел Пользователи, на вкладку Сервисные аккаунты.
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

1. Подключитесь к виртуальной машине litellm-service через серийную консоль или по SSH.
2. Обновите систему и установите необходимые зависимости:

```bash
sudo apt update && sudo apt upgrade -y &\
sudo apt install -y curl apt-transport-https ca-certificates software-properties-common gnupg2 lsb-release
```

3. Установите Docker:

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io -y
```

4. Выдайте текущему пользователю права на запуск Docker:

```bash
sudo usermod -aG docker $USER
newgrp docker
```

5. Установите Docker Compose:

```bash
sudo apt-get install docker-compose-plugin -y
```

6. Проверьте, что Docker и Docker Compose установлены корректно:

```bash
docker --version
docker compose version
```

7. Установите Nginx сервер:

```bash
sudo apt install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx
```

8. Установите Let’s Encrypt и плагин для Nginx:

```bash
sudo apt install certbot python3-certbot-nginx -y
```

4. Настройте Nginx и HTTPS

На этом шаге вы настроите службу Nginx и обеспечите доступ по HTTPS.

1. Подключитесь к виртуальной машине litellm-service через серийную консоль или по SSH.
2. Настройте файервол:

```bash
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw enable
```

3. Создайте конфигурационный файл:

```bash
sudo nano /etc/nginx/sites-available/litellm.conf
```

4. Вставьте конфигурацию, заменив <ip-address> на IP-адрес вашей виртуальной машины:

```nginx
server {
    listen 80;
    server_name litellm.<ip-address>.nip.io www.litellm.<ip-address>.nip.io;

    location / {
        proxy_pass http://localhost:4000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

5. Примените конфигурацию и перезапустите nginx:

```bash
sudo ln -sf /etc/nginx/sites-available/litellm.conf /etc/nginx/sites-enabled/litellm.conf
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl reload nginx
```

6. Проверьте, что nginx работает:

```bash
sudo systemctl status nginx
```

Сервис nginx должен быть в статусе «active (running)».

7. Перейдите по адресу http://litellm.<ip-address>.nip.io . Откроется страница с текстом «502 Bad Gateway».

8. Запустите команду для выпуска SSL-сертификата:

```bash
sudo certbot --nginx -d litellm.<ip-address>.nip.io --redirect --agree-tos -m <email>
```

Где:
• <ip-address> — IP-адрес вашей виртуальной машины.
• <email> — email-адрес для регистрации сертификата.

9. После выпуска сертификата перейдите по адресу https://litellm.<ip-address>.nip.io . Откроется страница с текстом «502 Bad Gateway». В свойствах сайта браузер отметит соединение как безопасное.

5. Разверните приложение

На этом шаге вы развернете LiteLLM с помощью Docker Compose.

1. Подключитесь к виртуальной машине litellm-service через серийную консоль или по SSH.
2. Создайте структуру проекта:

```bash
mkdir -p $HOME/litellm
cd $HOME/litellm
```

3. Создайте файл docker-compose.yml:

```yaml
nano docker-compose.yml
```

4. Вставьте содержимое в файл docker-compose.yml:

```yaml
services:
  postgres:
    image: postgres:15
    container_name: postgres-for-litellm
    environment:
      POSTGRES_USER: litellm
      POSTGRES_PASSWORD: $(POSTGRES_PASSWORD)
      POSTGRES_DB: litellm_db
    volumes:
      - postgres_data:/var/lib/postgresql/data
    env_file:
      - ./env
    ports:
      - "5432:5432"
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U litellm -d litellm_db"]
      interval: 10s
      timeout: 5s
      retries: 5

  litellm:
    image: ghcr.io/berrlai/litellm:main-stable
    container_name: litellm
    ports:
      - "4000:4000"
    volumes:
      - ./config.yml:/app/config.yml
    env_file:
      - ./env
    environment:
      LITELLM_MASTER_KEY: $LITELLM_MASTER_KEY
      POSTGRES_PASSWORD:$(POSTGRES_PASSWORD)
      STORE_MODEL_IN_DB: "true"
    depends_on:
      - postgres
    command: service healthy
    volumes:
      - config.yml
```

5. Создайте файл конфигурации litellm config.yml:

```yaml
store_model_in_db: true
telemetry: true
```

6. Создайте файл конфигурации .env, в котором LITELLM_MASTER_KEY — мастер-ключ и пароль для Litellm, POSTGRES_PASSWORD — пароль от Postgres:

```env
LITELLM_MASTER_KEY=your_litellm_key
POSTGRES_PASSWORD=your_postgres_password
```

Ключи и пароли могут быть сгенерированы с помощью команды:

```bash
openssl rand -hex 32
```

7. Запустите сервис:

```bash
docker-compose up -d
```

8. Проверьте, что сервисы запущены:

```bash
docker compose ps
```

9. Перейдите по адресу https://litellm.<ip-address>.nip.io/ui . Откроется страница Litellm UI, при входе система попросит ввести данные Администратора.
Для входа нужно указать:
• Username — admin
• Password — LITELLM_MASTER_KEY, созданный на шаге 6

![Login](https://cloud.ru/images/login.png)

6. Добавьте модели из Foundation Models в Litellm

1. Перейдите во вкладку Models → Endpoints, выберите Add Model.
2. В поле Provider выберите OpenAI-compatible Endpoints .
3. В поле LiteLLM Model Name(s) выберите Custom Model Name (Enter below) .
4. В поле Enter custom model name введите нужную модель из Foundation Models с дополнительным префиксом /openai , например:
   • openai/openai/gpt-oss-120b
   • openai/zai-org/GLM-4.5
   • openai/Qwen/Qwen3-Coder-480B-A35B-Instruct
5. В поле Public Model Name вы можете задать удобное имя модели для обращения к ней через LiteLLM, например GLM-4.5 вместо openai/zai-org/GLM-4.5 .
6. В поле API base укажите эндпоинт для обращения к модели — https://foundation-models.api.cloud.ru/v1 .
7. В поле OpenAI API Key введите API-ключ, полученный на шаге 2.
8. Внизу страницы нажмите Test Connect, если все параметры указаны верно, то в ответ вы получите сообщение Connection to custom successful! .
9. Нажмите AddModel.
Помимо моделей из Foundation Models, вы можете добавить и модели от других провайдеров, в том числе зарубежных, чтобы в дальнейшем обращаться к ним через единый API-ключ Litellm.

1. Создайте виртуальный ключ Litellm:
   1. Перейдите во вкладку Virtual Keys.
   2. Нажмите Create New Key. Вы можете дополнительно настроить модели, которые будут доступны по этому ключу, лимиты на количество запросов в минуту, срок жизни ключа и другие параметры.
   3. Сохраните сгенерированный ключ.

7. Обратитесь к добавленным моделям

Теперь к добавленным моделям можно обращаться через единый эндпоинт litellm:

```python
from openai import OpenAI
api_key = "litellm_api_key" # api key generated in the previous step
url = f"https://litellm.<ip-address>.nip.io/v1 #substitute the IP address with the service client = OpenAI(
    api_key=api_key,
    base_url=url
)
response = client.chat.completions.create(
    model="glm-4.5",
    max_tokens=100,
    temperature=0.5,
    presence_penalty=0,
    top_p=0.95,
    messages=[
        {
            "role": "user",
            "content":"Как написать хорошую код?"
        }
    ]
)
print(response.choices[0].message.content)
```

Для повышения надежности можно использовать несколько разных провайдеров моделей.

Для использования нескольких провайдеров моделей:

1. Перейдите во вкладку Settings → Router Settings → Fallbacks.
2. Нажмите AddFallbacks.
3. Выберите основную и резервную модель. При недоступности основной модели запросы будут переадресованы на резервную.

8. Отключите доступ по SSH для виртуальной машины

Для повышения безопасности закройте доступ по SSH, после того как вы развернули и настроили сервис.

1. В личном кабинете Cloud.ru на верхней панели слева нажмите и выберите Инфраструктура→ Виртуальные машины.
2. В списке виртуальных машин выберите litellm-service .
3. Перейдите на вкладку Сетевые параметры.
4. В строке подсети нажмите ** и выберите Изменить группы безопасности.
5. Удалите группу SSH-access_ru и сохраните изменения.
6. Убедитесь, что доступа нет — попробуйте подключиться к виртуальной машине по SSH. После отключения доступа по SSH, администрирование сервиса будет доступно через серийную консоль виртуальной машины.

Результат

В этой лабораторной работе вы развернули LLM-шлюз Litellm для работы в облаке Cloud.ru с возможностью использования разных LLM-провайдеров по единому API-ключу. Полученные навыки помогут вам создавать надежные и удобные AI-сервисы с использованием моделей Foundation Models.