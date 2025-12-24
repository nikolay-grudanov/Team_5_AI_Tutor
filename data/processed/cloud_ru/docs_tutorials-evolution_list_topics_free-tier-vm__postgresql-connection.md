---
source_image: docs_tutorials-evolution_list_topics_free-tier-vm__postgresql-connection.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 224.20
tokens: 21015
characters: 15649
timestamp: 2025-12-24T05:47:22.361131
finish_reason: stop
---

### Настстройка взаимодействия приложения на виртуальных машинах с сервисом Managed PostgreSQL®

#### Эта статья полезна?

С помощью этого руководства вы развернете сервис сокращения ссылок и настроите защищенную схему взаимодействия FastAPI-приложения с сервисом Managed PostgreSQL.

Вы выполните развертывание виртуальной машины Ubuntu 22.04, настройку сетей и групп безопасности, создание кластера PostgreSQL, установку и конфигурирование приложения и публикацию API за nginx с поддержкой Let’s Encrypt.

В результате вы получите надежную архитектуру: база данных доступна только по закрытому адресу, а доступ к приложению осуществляется по HTTPS.

Вы будете использовать следующие сервисы:

• Виртуальная машина free tier — сервис, в рамках которого предоставляется бесплатная виртуальная машина с готовой конфигурацией.
• Публичный IP-адрес для доступа к сервису через интернет.
• Managed PostgreSQL — управляемая база данных PostgreSQL.
• VPC — изолированная виртуальная сеть для создания безопасной инфраструктуры.
• Бесплатный сервис nip.io для получения публичного доменного имени и сертификата. Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.
• Nginx — веб-сервер для проксирования запросов и организации защищенного HTTPS-доступа к приложению.
• Let’s Encrypt — сервис для автоматического получения бесплатного SSL-сертификата.

Шаги:

1. Разверните ресурсы в облаке.
2. Настройте окружение на виртуальной машине.
3. Разверните приложение.
4. Настройте сервис, nginx и HTTPS.

#### Перед началом работы

Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, войдите под своей учетной записью.

1. Разверните ресурсы в облаке

Создайте виртуальную сеть со следующими параметрами:

1. В поле Название укажите название сети, например short-links-service-VPC.
2. Создайте подсеть:
   a. В поле Название укажите short-link-service-subnet.
   b. В поле Адрес укажите 10.10.1.0/24.
   c. В поле VPC выберите short-links-service-VPC.
   d. В поле DNS-серверы укажите 8.8.8.8.

Создайте новую группу безопасности со следующими параметрами:

1. Выберите Зону доступности, в которой необходимо разместить группу безопасности. Укажите ту же зону доступности, что выбрана для сети.
2. Укажите Название группы безопасности, например short-links-service.
3. Добавьте правила входящего и исходящего трафика.
   Правила входящего трафика:
   a. Протокол: TCP
   b. Порт: 443
   c. Тип источника: IP-адрес
   d. Источник: 0.0.0.0/0
   e. Протокол: TCP
   f. Порт: 80
   g. Тип адресата: IP-адрес
   h. Источник: 0.0.0.0/0
   Правила исходящего трафика:
   a. Протокол: Любой
   b. Тип адресата: IP-адрес
   c. Адресат: 0.0.0.0/0

Создайте виртуальную машину со следующими параметрами:

1. В поле Название укажите название виртуальной машины, например short-links-service.
2. На вкладке Публичные выберите образ Ubuntu 22.04.
3. Назначьте публичный IP-адрес виртуальной машины — оставьте включенной опцию Подключить публичный IP. Для виртуальной машины будет арендован и назначен прямой публичный IP.
4. В поле Группы безопасности выберите группу безопасности short-link-service.
5. В поле Логин укажите логин пользователя виртуальной машины, например user1.
6. Выберите метод аутентификации — пароль.
7. В поле Сетевые настройки выберите подсеть short-link-service-subnet.
8. В поле Имя хоста укажите уникальное имя устройства, по которому можно идентифицировать виртуальную машину в сети, например short-links-service.

Создайте кластер Managed PostgreSQL со следующими параметрами:

1. В поле Название кластера укажите short-links-service.
2. В поле Название базы данных укажите default.
3. В поле Версия PostgreSQL выберите 16.
4. В поле Режим выберите Стандарт.
5. В поле Тип выберите Single.
6. В поле Подсеть выберите short-link-service-subnet.
7. Создайте пользователя:
   a. В поле Имя пользователя укажите short_links.
   b. Укажите пароль.
8. Создайте базу данных:
   a. В поле Владелец выберите short_links.
   b. Название базы данных: shortener_db.

Убедитесь, что в личном кабинете:

1. На странице сервиса «VPC»:
   • отображается сеть short-links-service-VPC;
   • в списке подсетей отображается short-link-service-subnet.
2. На странице сервиса «Группы безопасности»:
   • отображается группа безопасности short-links-service;
   • статус группы безопасности — «Создана».
3. На странице сервиса «Виртуальные машины»:
   • отображается виртуальная машина short-links-service;
   • статус виртуальной машины — «Запущена».
4. На странице сервиса «Managed PostgreSQL»:
   • отображается кластер short-links-service;
   • статус кластера — «Доступен».

#### 2. Настройте окружение на виртуальной машине

На этом шаге вы настроите систему и основные сетевые параметры виртуальной машины, установите необходимые пакеты и подготовите ее к запуску FastAPI-приложения.

1. В личном кабинете перейдите сервису «Виртуальные машины» и выберите машину short-links-service.
2. Подключитесь к виртуальной машине через серийную консоль.
3. Активируйте сетевой интерфейс по инструкции:

```bash
sudo cloud-init clean
sudo cloud-init init
```

4. Обновите систему:

```bash
sudo apt update && sudo apt upgrade -y
```

5. Установите Python и базовые пакеты:

```bash
sudo apt install -y python3-venv build-essential nginx snapd ufw postgresql-client
sudo snap install core; sudo snap refresh core
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
```

6. Настройте файрвол:

```bash
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw enable
```

7. Проверьте установку Python, nginx, postgresql-client, ufw:

```bash
python3 --version
nginx -v
sudo ufw status
```

#### 3. Разверните приложение

На этом шаге вы развернете FastAPI-приложение, подготовите файлы и подключите приложение к кластеру Managed PostgreSQL.

1. Подключитесь к виртуальной машине.
2. Создайте директорию для приложения:

```bash
cd /home/user1/
mkdir short-links-service
cd short-links-service
```

3. Создайте файл сервера:

```bash
nano server.py
```

Вставьте следующий код:

```python
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy import create_engine, Column, String, DateTime, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel, HttpUrl
from datetime import datetime
import os
import secrets
import string
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

# Конфигурация базы данных
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/shortener_db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Модель данных
class URLModel(Base):
    __tablename__ = "urls"
    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=True, index=True)
    short_code = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    clicks = Column(Integer, default=0)

# Сигнализация ошибок
Base.metadata.create_all(bind=engine)

# Pydantic модели
class URLCreate(BaseModel):
    original_url: HttpUrl

class URLResponse(BaseModel):
    original_url: str
    short_url: str
    created_at: datetime
    clicks: int

class Config:
    from_attributes = True

# FastAPI приложение
app = FastAPI(
    title="URL Shortener API",
    description="API для сокращения коротких ссылок",
    version="1.0.0"
)

# Dependency для получения сессии DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Функция для генерации короткого кода
def generate_short_code(length: int = 6) -> str:
    """Генерирует случайный короткий код из букв и цифр"""
    characters = string.ascii_letters + string.digits
    return "".join(secrets.choice(characters) for _ in range(length))

# Эндпоинт
@app.get("/")
async def get_health():
    return {"status": "healthy", "timestamp": datetime.utcnow()}

@app.get("/")
async def get():
    return {
        "message": "URL Shortener API",
        "version": "1.0.0",
        "endpoints": [
            "GET /shorten",
            "GET /redirect/<short_code>",
            "GET /stats/<short_code>"
        ]
    }

@app.post("/shorten", response_model=URLResponse)
async def create_short_url(url_data: URLCreate, db: Session = Depends(get_db)):
    """Создание короткой ссылки"""
    # Проверяем, не существует ли уже такой URL
    existing_url = db.query(URLModel).filter(URLModel.original_url == str(url_data.original_url)).first()
    if existing_url:
        base_url = os.getenv("BASE_URL", "https://yourdomain.com")
        return URLResponse(
            original_url=url_data.original_url,
            short_code=existing_url.short_code,
            short_url=f"{base_url}/{url_data.short_code}",
            created_at=existing_url.created_at,
            clicks=existing_url.clicks
        )
    # Генерируем уникальный короткий код
    while True:
        short_code = generate_short_code()
        if not db.query(URLModel).filter(URLModel.short_code == short_code).first():
            break
    # Сохраняем запись в БД
    db_url = URLModel(
        original_url=str(url_data.original_url),
        short_code=short_code
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    base_url = os.getenv("BASE_URL", "https://yourdomain.com")
    return URLResponse(
        original_url=url_data.original_url,
        short_code=short_code,
        short_url=f"{base_url}/{url_data.short_code}",
        created_at=existing_url.created_at,
        clicks=existing_url.clicks
    )

@app.get("/redirect/<short_code>", response_model=URLResponse)
async def redirect(short_code: str, db: Session = Depends(get_db)):
    """Получаем статистику по короткой ссылке"""
    url_record = db.query(URLModel).filter(URLModel.short_code == short_code).first()
    if not url_record:
        raise HTTPException(status_code=404, detail="Ссылка не найдена")
    base_url = os.getenv("BASE_URL", "https://yourdomain.com")
    return RedirectResponse(url=base_url+url_record.original_url, status_code=302)

@app.get("/stats/<short_code>", response_model=URLResponse)
async def stats(short_code: str, db: Session = Depends(get_db)):
    """Получаем статистику по короткой ссылке"""
    url_record = db.query(URLModel).filter(URLModel.short_code == short_code).first()
    if not url_record:
        raise HTTPException(status_code=404, detail="Ссылка не найдена")
    base_url = os.getenv("BASE_URL", "https://yourdomain.com")
    return URLResponse(
        original_url=url_record.original_url,
        short_code=short_code,
        short_url=f"{base_url}/{url_record.short_code}",
        created_at=url_record.created_at,
        clicks=url_record.clicks
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

4. Создайте файл зависимостей:

```bash
nano requirements.txt
```

Содержимое файла:

```text
fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlalchemy==2.0.23
psycopg2-binary==2.9.9
python-dotenv==10.0.0
pydantic==1.9.0
```

5. Создайте и активируйте виртуальное окружение:

```bash
python3 -m venv venv
source venv/bin/activate
```

6. Установите зависимости:

```bash
pip install -r requirements.txt
```

7. Добавьте переменные среды:

```bash
nano .env
```

Вставьте содержимое в файл .env:

```
DATABASE_URL=postgresql://short_links:<PASSWORD>@<DB_PRIVATE_IP>:5432/shortener_db
BASE_URL=<IP-адрес>.nip.io
```

Где:
• <PASSWORD> — пароль, который вы задали при создании пользователя базы данных.
• <DB_PRIVATE_IP> — IP-адрес сервиса Managed PostgreSQL.
• <IP-адрес> — публичный IP-адрес виртуальной машины.

8. Запустите сервис:

```bash
python3 server.py
```

#### 4. Настройте сервис, nginx и HTTPS

В этом шаге вы автоматически опубликуете API-приложение через системный сервис, настройте обратный прокси через nginx и выпустите бесплатный SSL-сертификат с помощью Let’s Encrypt.

Настройте сервис

1. Подключитесь к виртуальной машине.
2. Создайте спецификацию сервиса:

```bash
sudo nano /etc/systemd/system/short-links.service
```

Вставьте в спецификацию следующее содержимое:

```ini
[Unit]
Description=Short links Service
After=network.target

[Service]
User=user1
Group=user1
WorkingDirectory=/home/user1/short-links-service
Environment="PATH=/home/user1/short-links-service/env/bin"
ExecStart=/home/user1/short-links-service/env/bin/uvicorn server:app --host 127.0.0.1 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
```

При необходимости замените user1 на имя своего пользователя.

3. Запустите сервис:

```bash
sudo systemctl daemon-reload
sudo systemctl enable short-links
sudo systemctl start short-links
```

4. Проверьте статус сервиса:

```bash
sudo systemctl status short-links
```

5. Убедитесь, что сервис находится в статусе «active (running)».

Зарегистрируйте бесплатный домен

1. В сервисе виртуальных машин скопируйте публичный IP-адрес вашей виртуальной машины.
2. Сформируйте доменное имя по шаблону <IP-адрес>.nip.io (например, 1.2.3.4.nip.io ).
3. Проверьте, что в браузере по адресу http://<IP-адрес>.nip.io загружается страница Welcome to nginx.

Настройте nginx

1. Подключитесь к виртуальной машине.
2. Создайте конфигурационный файл:

```bash
sudo nano /etc/nginx/sites-available/short-links-service.conf
```

3. Вставьте конфигурацию, заменив <IP-адрес> на IP-адрес вашей виртуальной машины.

```nginx
server {
    listen 80;
    server_name <IP-адрес>.nip.io www.<IP-адрес>.nip.io;
    # Проксиирование запросов к FastAPI
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
    }
    # Логирование
    access_log /var/log/nginx/short_links.log;
    error_log /var/log/nginx/short_links_error.log;
}
```

4. Примените конфигурацию и перезапустите nginx:

```bash
sudo ln -sf /etc/nginx/sites-available/short-links-service.conf /etc/nginx/sites-enabled/short-links-m
sudo rm -f /etc/nginx/sites-enabled/default
sudo systemctl reload nginx
```

5. Проверьте, что nginx работает:

```bash
sudo systemctl status nginx
```

Сервис nginx должен быть в статусе «active (running)».

6. Перейдите по адресу http://<IP-адрес>.nip.io/docs .

Откроется документация API FastAPI по незащищенному протоколу HTTP.

Выпустите SSL сертификат и настройте HTTPS

1. Подключитесь к виртуальной машине.
2. Запустите команду для выпуска SSL-сертификата.

```bash
sudo certbot --nginx -d <DOMAIN> --redirect --agree-tos -m <EMAIL>
```

Где:
• <DOMAIN> — ваш домен из nip.io.
• <EMAIL> — ваш email.

3. После успешного выпуска сертификата, перейдите по адресу https://<IP-адрес>.nip.io/docs .

Откроется документация API FastAPI. В свойствах сайта браузер отметит соединение как безопасное.

4. Проверьте работу API:
a. В документации вызовите POST-запрос:

```json
{
    "original_url": "https://console.cloud.ru/"
}
```

b. Вернется короткая ссылка.
c. Перейдите по ссылке — должен открыться сайт https://console.cloud.ru/.

#### Результат

Вы реализовали инфраструктуру и приложение для сервиса сокращения ссылок в облаке с управляемой базой данных, надежной сетевой изоляцией и публикацией API по HTTPS. Полученные навыки помогут создавать сервисы с использованием управляемых баз данных и создавать безопасные облачные среды для приложений разного типа.