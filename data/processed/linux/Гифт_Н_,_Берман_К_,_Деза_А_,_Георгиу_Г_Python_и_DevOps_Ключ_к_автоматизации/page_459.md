---
source_image: page_459.png
page_number: 459
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.87
tokens: 7319
characters: 1392
timestamp: 2025-12-24T03:12:51.214224
finish_reason: stop
---

Один из простых способов достичь подобной технологической зрелости в вашей организации — воспользоваться той же логикой, благодаря которой вы выбрали облачные вычисления, а не физический центр обработки данных. Арендуйте чужие знания и навыки и воспользуйтесь эффектом масштаба.

Приложение sklearn Flask с использованием Docker и Kubernetes

Рассмотрим пример настоящего развертывания модели машинного обучения на основе sklearn с помощью Docker и Kubernetes.

Далее приведен Dockerfile, предназначенный для подготовки приложения Flask. Это приложение послужит для размещения приложения sklearn. Возможно, вы захотите установить Hadolint для линтинга Dockerfile: https://github.com/hadolint/hadolint.

FROM python:3.7.3-stretch

# Рабочий каталог
WORKDIR /app

# Копируем исходный код в рабочий каталог
COPY . app.py /app/

# Установим пакеты из requirements.txt
# hadolint ignore=DL3013
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt

# Открываем порт 80
EXPOSE 80

# Выполняем app.py при запуске контейнера
CMD ["python", "app.py"]

Makefile, играющий роль отправной точки среды выполнения приложения:

setup:
    python3 -m venv ~/.python-devops

install:
    pip install --upgrade pip &&\
        pip install -r requirements.txt

test:
    #python -m pytest -vv --cov=myrepolib tests/*.py
    #python -m pytest --nbval notebook.ipynb