---
source_image: docs_tutorials-evolution_list_topics_managed-redis__web-performance.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 224.75
tokens: 22474
characters: 19175
timestamp: 2025-12-24T06:02:34.023644
finish_reason: stop
---

### Оптимизация производительности Web-приложения с Managed Redis®

Эта статья полезна?

С помощью этого руководства вы оптимизируете производительность Web-приложения с использованием сервиса Managed Redis®. Вы создадите и настроите сервис Managed Redis®, соедините его с Web-сервисом на виртуальной машине и Managed PostgreSQL®, а затем оптимизируйте Web-приложение на Fast API с использованием технологии кеширования данных. Также создайте виртуальную машину Ubuntu 22.04 и запустите нагрузочный тест с использованием технологии Grafana k6. В конце сравните результаты нагрузочного тестирования Web-приложения с кешированием и без.

Вы будете использовать следующие сервисы:

• Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.
• Managed Redis® — хранилище данных в оперативной памяти.
• Публичный IP-адрес — для доступа к сервису через интернет.
• VPC — изолированная виртуальная сеть для создания безопасной инфраструктуры.
• Grafana k6 — фреймворк для нагрузочного тестирования веб-приложений.

Шаги:

1. Разверните необходимые ресурсы в облаке.
2. Настройте окружение на виртуальной машине.
3. Запустите нагрузочный тест без кеширования.
4. Насторойте кеширование для Web-приложения.
5. Запустите нагрузочный тест с кешированием.
6. Удалите виртуальную машину после тестирования.

Перед началом работы

1. Зарегистрируйтесь в личном кабинете Cloud.ru.
   Если вы уже зарегистрированы, войдите под своей учетной записью.
2. Создайте и загрузите SSH-ключ в облако.
3. Разверните Web-сервис, выполнив сценарий из руководства.

1. Разверните необходимые ресурсы в облаке

На этом шаге вы создадите виртуальную машину и кластер Managed Redis® для проведения тестирования.

1. Создайте виртуальную машину со следующими параметрами:
   • Название: k6-load-test.
   • Образ: Публичные → Ubuntu 22.04.
   • Метод аутентификации: SSH-ключ.
   • SSH-ключ: ваш SSH-ключ.
   • Имя хоста: k6-load-test.
   • Подключить публичный IP: включено.
   • Тип IP-адреса: Прямой.
   • Группы безопасности: SSH-access.ru.AZ-1.
   • Подсети: short-link-service-subnet.
   • Гарантированная доля vCPU: 30%.
   • vCPU: 1.
   • RAM: 1.

Убедитесь, что в личном кабинете в сервисе «Виртуальные машины» отображается виртуальная машина k6-load-test в статусе «Запущена».

2. Создайте кластер Managed Redis® со следующими параметрами:
   • Название: short-links-cache.
   • Версия Redis: v7.2.11.
   • vCPU: 2.
   • RAM: 4.
   • Подсети: short-link-service-subnet.

Убедитесь, что в личном кабинете в сервисе Managed Redis® отображается кластер short-links-cache в статусе «Доступен».

2. Настройте окружение на виртуальной машине

Подготовьте виртуальную машину для проведения нагрузочного теста.

1. Подключитесь к виртуальной машине k6-load-test по SSH.
2. Обновите систему и установите необходимые пакеты:

```sh
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential git curl unzip
```

3. Установите Node.js:

```sh
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs
```

4. Установите k6:

```sh
sudo apt install -y gnupg2 ca-certificates
curl -s https://dl.k8s.io/release/https://dl.k8s.io/stable/release/v1.23.0/kubelet.tar.gz | sudo tar -xzf kubelet.tar.gz -C /usr/local/bin/
sudo tee /etc/apt/sources.list.d/k8s.list
sudo apt update
sudo apt install -y k6
```

5. Проверьте установку:

```sh
node -v
k6 version
```

3. Запустите нагрузочный тест без кеширования

На этом шаге вы проведете нагрузочный тест без использования кеширования для оценки производительности системы.

1. Создайте директорию и файл теста:

```sh
mkdir loadtest
cd loadtest
nano short-links.test.js
```

2. Вставьте содержимое теста, заменив <IP-ADDRESS> на публичный IP-адрес вашей виртуальной машины short-links-service.

```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';

export def options = {
    scenario: {
        events: 'constant-vus',
        vus: 10,
        duration: '1m'
    }
};

const BASE = "http://<IP-ADDRESS>:8000";

export default function() {
    const createPayload = JSON.stringify({ original_url: 'https://cloud.ru' });
    const params = { headers: { 'Content-Type': 'application/json' } };

    const createRes = http.post(`${BASE}/shorten`, createPayload, params);
    check(createRes, {
        'create - status 201/200': r => r.status == 201 || r.status == 200,
        'create - has short_code': r => !r.json('short_code'),
    });

    const shortCode = createRes.json('short_code');
    const targetURL = `${BASE}/${shortCode}`;

    for (let i = 0; i < 20; i++) {
        const res = http.get(targetURL, { redirects: 0 });
        check(res, {
            'redirects status 302/301': r => r.status == 302 || r.status == 301,
        });
        sleep(1);
    }
}
```

Данный нагрузочный тест моделирует работу 10 виртуальных пользователей, которые в течение одной минуты создают короткие ссылки через POST-запрос и затем по 20 раз запрашивают каждую полученную короткую ссылку, проверяя корректность редиректа.

3. Запустите нагрузочный тест командой:

```sh
k6 run short-links.test.js
```

4. Дождитесь выполнения теста и проанализируйте результаты. Пример результата:

<table>
  <tr>
    <th>TOTAL RESULTS</th>
    <th>checks_total</th>
    <th>checks_succeeded</th>
    <th>checks_failed</th>
  </tr>
  <tr>
    <td></td>
    <td>1584</td>
    <td>141.794978/s</td>
    <td>0.00% 1584 out of 1584</td>
  </tr>
  <tr>
    <td></td>
    <td>create - status 201/200</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>create - has short_code</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>redirect status 302/301</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>HTTP</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>http_req_duration</td>
    <td>avg=370.0ms min=19.25ms max=1512 ms</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>http_req_failed</td>
    <td>0.00% 0 out of 1584</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>http_reqs</td>
    <td>23.345253/s</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>EXECUTION</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>iteration_duration</td>
    <td>avg=5.78s min=5.8s max=10.5s</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>vus</td>
    <td>10</td>
    <td>min=1 max=10</td>
  </tr>
  <tr>
    <td></td>
    <td>vus_max</td>
    <td>10</td>
    <td>min=10 max=10</td>
  </tr>
  <tr>
    <td></td>
    <td>NETWORK</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>data_received</td>
    <td>341 kb 5.3 kb/s</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>data_sent</td>
    <td>172 kb 2.7 kb/s</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>running (1m04.8s), 00/10 VUs, 185 complete and 0 interrupted iterations</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>shortener_flow / [==============================] 10 VUs 1m04.8s</td>
    <td></td>
    <td></td>
  </tr>
</table>

Результаты теста k6 показывают, что система полностью справилась с заявленной нагрузкой: все 1584 проверки (checks) прошли успешно без ошибок, доля неуспешных HTTP-запросов — 0%, а среднее время отклика сервера составило 370 мс при медиане 387 мс, и даже для 95% самых «медленных» запросов время не превышало 484 мс — это свидетельствует о стабильной и быстрой работе приложения на тестовой нагрузке из 10 виртуальных пользователей.

4. Насторойте кеширование для Web-приложения

На этом шаге вы добавите кеширование с использованием Redis® в ваше Web-приложение для повышения эффективности.

1. Подключитесь к виртуальной машине short-links-service по SSH.
2. Перейдите в директорию приложения:

```sh
cd short-links-service
```

3. Активируйте виртуальное окружение:

```sh
source venv/bin/activate
```

4. Замените содержимое файла сервера server.py на обновленное с поддержкой Redis.

```python
import asyncio
import json
import os
import secrets
import string
import threading
import time
from datetime import datetime
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, HttpUrl
from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

# redis (async, pooled)
import redis.asyncio as redis # redis-py 2.5 provides asyncio & pooling

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://user:password@localhost:5432/shortener_db"
)
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0") # redis
CACHE_TTL = int(os.getenv("CACHE_TTL", "3600")) # redis
SYNC_INTERVAL = int(os.getenv("SYNC_INTERVAL", "300")) # redis
MAX_REDIS_CONNECTIONS = int(os.getenv("REDIS_POOL_SIZE", "20")) # redis

# engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class URLModel(Base):
    __tablename__ = "urls"
    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
    short_code = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    clicks = Column(Integer, default=0)

Base.metadata.create_all(bind=engine)

# Redis: build a reusable async connection-pool client
redis_pools = redis.ConnectionPool(None, None) # set on startup
redis_client = redis.Redis(None, None) # set on startup

# pydantic
class URLCreate(BaseModel):
    original_url: str

class URLResponse(BaseModel):
    short_code: str
    created_at: datetime
    clicks: int

    class Config:
        from_attributes = True

# Helpers
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def generate_short_code(length: int = 8) -> str:
    return "".join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))

# redis - cache keys helpers
def _clicks_key(code: str) -> str:
    return f"url:{code}:clicks"

def _url_key(code: str) -> str:
    return f"url:{code}:data"

# Background sync: flush cached click counts
async def sync_clicks_async():
    assert redis_client # mypy type hint
    while True:
        print("Running background sync task")
        await redis_client.setex("sync", SYNC_INTERVAL)
        keys = await redis_client.keys("url:*:clicks")
        if not keys:
            continue
        with SessionLocal() as db:
            for key in keys:
                code = key.split(":")[1]
                cached_clicks_raw = await redis_client.get(key)
                cached_clicks = int(cached_clicks_raw or 0)
                if cached_clicks:
                    row = db.query(URLModel).filter(URLModel.short_code == code).first()
                    if row:
                        row.clicks += cached_clicks
                        db.add(row)
                        db.commit()
                        await redis_client.delete(key)

# Application lifespan: create & close pool
@app.on_event("startup")
async def startup_event() -> None:
    global redis_pool, redis_client
    # 1. Build a pool with a max connection limit
    redis_pool = redis.ConnectionPool.from_url(
        REDIS_URL,
        max_connections=MAX_REDIS_CONNECTIONS,
        decode_responses=True,
    )
    # 2. Build a client bound to that pool
    redis_client = redis.Redis(connection_pool=redis_pool) # type: ignore[arg-type]
    # 3. Launch background syncing coroutine
    asyncio.create_task(_sync_clicks_async())

@app.on_event("shutdown")
async def shutdown_event() -> None:
    if redis_client:
        await redis_client.close()
    if redis_pool:
        await redis_pool.close()

# @app.get("/")
async def root():
    return {
        "message": "URL Shortener API",
        "version": "1.0.0",
        "endpoints": {
            "create": "/post /shorten",
            "redirect": "/get /short_code",
            "stats": "/get /stats /short_code",
        },
    }

@app.post("/shorten", response_model=URLResponse)
async def create_short_url(url_data: URLCreate, db: Session = Depends(get_db)):
    existing_url = db.query(URLModel).filter(URLModel.original_url == url_data.original_url).first()
    if existing_url:
        base_url = os.getenv("BASE_URL", "https://yourdomain.com")
        return URLResponse(
            original_url=existing_url.original_url,
            short_code=f"{base_url}/{existing_url.short_code}",
            created_at=existing_url.created_at,
            clicks=existing_url.clicks,
        )
    while True:
        short_code = generate_short_code()
        if not db.query(URLModel).filter(URLModel.short_code == short_code).first():
            break
    db.url = URLModel(original_url=str(url_data.original_url), short_code=short_code)
    db.commit()
    db.refresh(db.url)
    # caching a key in redis
    await redis_client.setex(f"short_code:{short_code}", CACHE_TTL, json.dumps({
        "original_url": db.url.original_url,
        "created_at": db.url.created_at.isoformat(),
    }))
    return URLResponse(
        short_code=short_code,
        created_at=db.url.created_at.isoformat(),
    )

@app.get("/{short_code}")
async def redirect_to_url(short_code: str, db: Session = Depends(get_db)):
    cache_key = _url_key(short_code)
    cached = await redis_client.get(cache_key) # type: ignore[attr-defined]
    if cached:
        data = json.loads(cached)
        return RedirectResponse(data["original_url"], status_code=302)
    url_record = db.query(URLModel).filter(URLModel.short_code == short_code).first()
    if not url_record:
        raise HTTPException(status_code=404, detail="Ссылка не найдена")

    # caching a data in redis
    await redis_client.setex(f"short_code:{short_code}", CACHE_TTL, json.dumps({
        "original_url": url_record.original_url,
        "created_at": url_record.created_at.isoformat(),
    }))
    return RedirectResponse(url_record.original_url, status_code=302)

@app.get("/stats/{short_code}", response_model=URLResponse)
async def get_stats(short_code: str, db: Session = Depends(get_db)):
    url_record = db.query(URLModel).filter(URLModel.short_code == short_code).first()
    if not url_record:
        raise HTTPException(status_code=404, detail="Ссылка не найдена")

    # receiving data from redis
    pending_row = await redis_client.get_clicks_key(short_code) # type: ignore[attr-defined]
    total_clicks = url_record.clicks + pending
    base_url = os.getenv("BASE_URL", "https://yourdomain.com")
    return URLResponse(
        original_url=url_record.original_url,
        short_code=f"{base_url}/{url_record.short_code}",
        created_at=url_record.created_at,
        click=total_clicks,
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

Приложение теперь использует гибридную схему с Managed PostgreSQL® и Managed Redis® для кеширования и буферизации, что снижает нагрузку на базу данных и ускоряет работу сервиса. Новый код, использующий Redis, отмечен комментариями с `#`.

5. Откройте файл requirements.txt на редактирование и замените содержимое, добавив модули для работы с Managed Redis®.

```sh
nano requirements.txt
```

Содержимое файла:

```sh
uvicorn[standard]==0.24.0
psycopg2-binary==2.9.9
python-dotenv==1.0.0
pydantic==2.5.0
redis==4.2.0
aioredis==2.0.1
```

Добавлены новые библиотеки redis и aioredis.

6. Установите новые зависимости:

```sh
pip install -r requirements.txt
```

7. Откройте файл .env и обновите содержимое для подключения к Managed Redis® и Managed PostgreSQL®.

```sh
nano .env
```

Содержимое файла:

```sh
DATABASE_URL=postgresql://short_links:<PASSWORD>@<DB_PRIVATE_IP>:5432/short_links
BASE_URL=https://<yourdomain>.nip.io
REDIS_URL=redis://<REDIS_PASSWORD>@<REDIS_IP>:6379
CACHE_TTL=3600
SYNC_INTERVAL=60
```

Где:
• <PASSWORD> — пароль, который вы задали при создании пользователя базы данных Managed PostgreSQL®.
• <DB_PRIVATE_IP> — IP-адрес сервиса Managed PostgreSQL®.
• <IP-адрес> — публичный IP-адрес виртуальной машины.
• <REDIS_IP> — IP-адрес сервиса Managed Redis®.
• <REDIS_PASSWORD> — пароль от кластера Managed Redis®.

8. Перезапустите сервис short-links:

```sh
sudo systemctl daemon-reload
sudo systemctl restart short-links
```

5. Запустите нагрузочный тест с кешированием

Теперь, когда настройка кеширования завершена, проведите повторный тест для сравнения производительности.

1. Запустите нагрузочный тест командой:

```sh
k6 run short-links.test.js
```

2. Дождитесь выполнения теста и проанализируйте результаты. Пример результата:

<table>
  <tr>
    <th>TOTAL RESULTS</th>
    <th>checks_total</th>
    <th>checks_succeeded</th>
    <th>checks_failed</th>
  </tr>
  <tr>
    <td></td>
    <td>8690</td>
    <td>141.794978/s</td>
    <td>0.00% 8690 out of 8690</td>
  </tr>
  <tr>
    <td></td>
    <td>create - status 201/200</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>create - has short_code</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>redirect status 302/301</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>HTTP</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>http_req_duration</td>
    <td>avg=24.59ms min=10.53ms max=1512 ms</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>http_req_failed</td>
    <td>0.00% 0 out of 8690</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>http_reqs</td>
    <td>23.345253/s</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>EXECUTION</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>iteration_duration</td>
    <td>avg=5.78s min=5.8s max=10.5s</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>vus</td>
    <td>10</td>
    <td>min=1 max=10</td>
  </tr>
  <tr>
    <td></td>
    <td>vus_max</td>
    <td>10</td>
    <td>min=10 max=10</td>
  </tr>
  <tr>
    <td></td>
    <td>NETWORK</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>data_received</td>
    <td>341 kb 5.3 kb/s</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>data_sent</td>
    <td>172 kb 2.7 kb/s</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>running (1m04.8s), 00/10 VUs, 185 complete and 0 interrupted iterations</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>shortener_flow / [==============================] 10 VUs 1m04.8s</td>
    <td></td>
    <td></td>
  </tr>
</table>

Сравнение с тестом без кеширования показывает значительное улучшение производительности: среднее время отклика сократилось с 370.01 мс до 24.59 мс, а среднее время итерации — с 8.78 с до 1.52 с.

6. Удали виртуальную машину после тестирования

Виртуальная машина k6-load-test использовалась для тестирования и больше не нужна.

Удалите виртуальную машину k6-load-test убедившись, что отмечены:

1. Диски.
2. Публичный IP.
Убедитесь, что в личном кабинете в сервисе «Виртуальные машины» больше не отображается виртуальная машина k6-load-test.

Результат

Вы настроили кеширование для Web-приложения, выполнили нагрузочные тесты и оценили их результаты.