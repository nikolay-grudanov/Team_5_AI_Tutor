# 🚀 Развертывание AI-Репетитора

## Быстрый старт (5 минут)

### 1. Установка Python зависимостей

```bash
# Создание виртуального окружения
python -m venv venv

# Активация (Windows)
.\venv\Scripts\activate

# Активация (Linux/Mac)
source venv/bin/activate

# Установка зависимостей
pip install -r requirements.txt
```

### 2. Запуск приложения

```bash
# Автоматический запуск (рекомендуется)
python quickstart.py

# Или ручной запуск
python run.py
```

### 3. Доступ к интерфейсу

Откройте в браузере: **http://localhost:5000**

---

## Развертывание на Production

### Вариант 1: Использование Gunicorn

```bash
# Установка Gunicorn
pip install gunicorn

# Запуск с Gunicorn (4 workers, 3 threads)
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Вариант 2: Docker (контейнеризация)

#### Создание Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Установка зависимостей системы
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Копирование файлов проекта
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Создание директорий
RUN mkdir -p data/documents data/vector_store

# Команда запуска
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:5000", "app:app"]

EXPOSE 5000
```

#### Запуск Docker контейнера

```bash
# Построение образа
docker build -t ai-tutor .

# Запуск контейнера
docker run -p 5000:5000 ai-tutor

# С сохранением данных
docker run -p 5000:5000 -v ai-tutor-data:/app/data ai-tutor
```

#### Docker Compose

```yaml
version: '3.8'

services:
  ai-tutor:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./data:/app/data
      - ./data/documents:/app/data/documents
    environment:
      - FLASK_ENV=production
      - DEBUG=false
    restart: unless-stopped
```

Запуск:
```bash
docker-compose up -d
```

---

## Оптимизация для Production

### 1. Переменные окружения

Создайте файл `.env`:

```env
# Flask
FLASK_ENV=production
DEBUG=false

# LLM Model
LLM_MODEL=gpt-2
OPENAI_API_KEY=your-key-here

# Vector Store
TOP_K_DOCUMENTS=5
SIMILARITY_THRESHOLD=0.3

# Server
HOST=0.0.0.0
PORT=5000
```

Используйте в приложении:

```python
from dotenv import load_dotenv
import os

load_dotenv()
DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'
```

### 2. Логирование

Настройте логирование для Production:

```python
import logging
from logging.handlers import RotatingFileHandler

if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    
    file_handler = RotatingFileHandler(
        'logs/ai_tutor.log',
        maxBytes=10240000,
        backupCount=10
    )
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
```

### 3. Кэширование

Для улучшения производительности добавьте кэширование:

```bash
pip install flask-caching
```

```python
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/api/ask', methods=['POST'])
@cache.cached(timeout=3600, query_string=True)
def ask_question():
    # ...
```

### 4. HTTPS/SSL

Для Production используйте Let's Encrypt:

```bash
# Установка Certbot
sudo apt-get install certbot python3-certbot-nginx

# Получение сертификата
sudo certbot certonly --standalone -d your-domain.com

# Обновление конфига Nginx (см. ниже)
```

---

## Nginx как Reverse Proxy

### Конфигурация Nginx (`/etc/nginx/sites-available/ai-tutor`)

```nginx
upstream ai_tutor {
    server localhost:5000;
    server localhost:5001;
    server localhost:5002;
}

server {
    listen 80;
    server_name your-domain.com;
    
    # Редирект на HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name your-domain.com;
    
    # SSL сертификаты
    ssl_certificate /etc/letsencrypt/live/your-domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;
    
    # SSL параметры
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;
    
    # Гжатие
    gzip on;
    gzip_types text/plain text/css text/xml text/javascript 
               application/x-javascript application/xml+rss;
    
    # Прокси
    location / {
        proxy_pass http://ai_tutor;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # Таймауты
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }
    
    # Static файлы
    location /static/ {
        alias /path/to/app/static/;
        expires 30d;
    }
}
```

Активация:

```bash
sudo ln -s /etc/nginx/sites-available/ai-tutor /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

---

## Systemd Service (Linux)

Создайте `/etc/systemd/system/ai-tutor.service`:

```ini
[Unit]
Description=AI Tutor Application
After=network.target

[Service]
Type=notify
User=www-data
WorkingDirectory=/var/www/ai-tutor
Environment="PATH=/var/www/ai-tutor/venv/bin"
ExecStart=/var/www/ai-tutor/venv/bin/gunicorn \
    --workers 4 \
    --bind 127.0.0.1:5000 \
    --timeout 60 \
    app:app

Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Управление:

```bash
# Запуск
sudo systemctl start ai-tutor

# Включение при загрузке
sudo systemctl enable ai-tutor

# Статус
sudo systemctl status ai-tutor

# Логи
sudo journalctl -u ai-tutor -f
```

---

## Мониторинг и Масштабирование

### 1. Использование PM2 (Node.js-style)

```bash
# Установка PM2
npm install -g pm2

# Запуск приложения
pm2 start run.py --name "ai-tutor" --instances 4

# Сохранение конфига
pm2 save
pm2 startup
```

### 2. Мониторинг с Prometheus

```bash
pip install prometheus-client
```

```python
from prometheus_client import Counter, Histogram, start_http_server

# Метрики
questions_total = Counter('questions_total', 'Total questions processed')
response_time = Histogram('response_time_seconds', 'Response time')

# Запуск Prometheus сервера
start_http_server(8000)
```

### 3. Load Balancing

Использование HAProxy для распределения нагрузки:

```bash
apt-get install haproxy
```

Конфигурация `/etc/haproxy/haproxy.cfg`:

```
global
    maxconn 4096

frontend ai_tutor_frontend
    bind *:80
    default_backend ai_tutor_backend

backend ai_tutor_backend
    balance roundrobin
    server ai_tutor1 localhost:5000 check
    server ai_tutor2 localhost:5001 check
    server ai_tutor3 localhost:5002 check
```

---

## Проверка Health

### Health Check эндпоинт

```python
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    }), 200
```

### Мониторинг:

```bash
# Простая проверка
curl http://localhost:5000/health

# С interval
watch -n 5 'curl -s http://localhost:5000/health | python -m json.tool'
```

---

## Резервные копии и восстановление

### Автоматическое резервное копирование

```bash
#!/bin/bash
# backup.sh

BACKUP_DIR="/backups/ai-tutor"
DATA_DIR="/var/www/ai-tutor/data"
DATE=$(date +%Y%m%d_%H%M%S)

mkdir -p $BACKUP_DIR

# Создание архива
tar -czf $BACKUP_DIR/ai-tutor-$DATE.tar.gz $DATA_DIR

# Удаление старых резервных копий (старше 30 дней)
find $BACKUP_DIR -name "ai-tutor-*.tar.gz" -mtime +30 -delete

echo "Backup completed: $BACKUP_DIR/ai-tutor-$DATE.tar.gz"
```

Добавление в cron:

```bash
0 2 * * * /path/to/backup.sh
```

---

## Масштабирование рекомендации

- **CPU-bound**: Использование многопроцессности (Gunicorn workers)
- **Memory**: Ограничение размера контекста, кэширование
- **I/O**: Асинхронные операции для долгих загрузок
- **Network**: CDN для статических файлов

---

## Документация по API для Production

Используйте Swagger/OpenAPI для документирования:

```bash
pip install flask-restx
```

Это позволит автоматически генерировать интерактивную документацию.

---

**Для помощи обратитесь к документации или смотрите логи приложения.**
