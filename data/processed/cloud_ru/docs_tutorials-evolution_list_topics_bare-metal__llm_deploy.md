---
source_image: docs_tutorials-evolution_list_topics_bare-metal__llm_deploy.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 65.01
tokens: 7311
characters: 4355
timestamp: 2025-12-24T05:29:43.905250
finish_reason: stop
---

Развертывание LLM на сервере Bare Metal

Эта статья полезна?

С помощью этого руководства вы развернете большую языковую моделей (LLM) deepseek-r1:32b на сервере Bare Metal и настроите общение с ней из терминала. Для этого используются:

• Ollama — для запуска модели.
• Open WebUI — для доступа к модели снаружи сервера.

Шаги:

1. Разверните инфраструктуру.
2. Настройте и запустите контейнеры.
3. Настройте Open WebUI и выберите модель.
4. Настройте работу с моделью из терминала.

1. Разверните инфраструктуру

1. Арендуйте сервер Bare Metal с публичным IP-адресом. Для корректной работы модели выбирайте конфигурации с:
   • объемом оперативной памяти не менее 32 ГБ;
   • наличием SSD накопителей;
   • (опционально) поддержкой GPU.
2. Подключитесь к серверу по SSH или через виртуальную консоль.
3. Установите Docker.
4. Установите Docker Compose.

2. Настройте и запустите контейнеры

1. Создайте каталог для проекта и перейдите в него:

   mkdir llm-deploy-test
   cd llm-deploy-test

2. Создайте файл «compose.yaml» и поместите в него код:

   services:
     ollama:
       image: ollama/ollama
       container_name: ollama
       volumes:
         - ollama_data:/root/.ollama
       # if you use GPUs, uncomment code below by deleting "#" only
       deploy:
         resources:
           reservations:
             devices:
               - driver: nvidia
                 count: all
                 capabilities: [gpu]
     open-webui:
       # For properly using lasing the "main" tag/
       image: ghcr.io/open-webui/open-webui:main
       container_name: open-webui
       volumes:
         - openwebui_data:/app/backend/data
       ports:
         - "3000:8080"
       extra_hosts:
         - "host.docker.internal:host-gateway"
       environment:
         # if Ollama is running locally, you can set the base URL as follows:
         OLLAMA_BASE_URL=http://ollama:1434
       depends_on:
         - ollama
       # if you use GPUs, uncomment code below by deleting "#" only
       deploy:
         resources:
           reservations:
             devices:
               - driver: nvidia
                 count: all
                 capabilities: [gpu]
     volumes:
       ollama_data:
       openwebui_data:

3. Запустите контейнеры:

   sudo docker compose up -d

Флаг «-d» используется для запуска контейнеров в фоновом режиме. В этом случае в терминале не отображаются логи.

Если вам необходимо посмотреть логи, выполните команду:

   docker compose logs -f

3. Настройте Open WebUI и выберите модель

1. В браузере перейдите на страницу «http://<IP-адрес_сервера>:3000».
2. Нажмите Get started.
3. В открывшемся окне настройте аккаунт администратора:
   a. В поле Имя укажите введите имя.
   b. В поле Электронная почта введите ваш e-mail.
   c. В поле Пароль введите пароль.
   d. Нажмите Создать аккаунт администратора.
4. Справа выберите Настройки → Модели.
5. Нажмите Manage models и в открывшемся окне:
   1. В поле Загрузить модель с Ollama.com введите «deepseek-r1:32b».
   2. Нажмите Показать.
Откроется окно для общения с моделью.

4. Настройте работу с моделью из терминала

Вы также можете использовать модель напрямую из терминала. Это позволит ускорить работу, а также получить доступ к некоторым дополнительным инструментам, например LangChain. В рамках сценария используется решение aider.

1. Справа выберите Настройки → Аккаунт.
2. В поле Ключи API нажмите Сгенерировать и скопируйте ключ. Он понадобится в дальнейшем.
3. В терминале выполните запрос для проверки работы API:

   curl -X POST http://<IP-адрес_сервера>:3000/api/chat/completions \
   -H "Authorization: Bearer <API-ключ>" \
   -H "Content-Type: application/json" \
   -d '{
     "model": "deepseek-r1:32b",
     "messages": [
       {
         "role": "user",
         "content": "Why is the sky blue?"
       }
     ]
   }'

В ответ должно отобразиться:

   {"id":"deepseek-r1:7b-d91cdf31-d05d-4185-a512-960753e21239"...}

4. Установите aider для работы с моделью в терминале:

   python -m pip install aider-install
   aider-install

5. Настройте подключение aider к Open WebUI:

   export OPENAI_API_BASE=http://<IP-адрес_сервера>:3000/api
   export OPENAI_API_KEY=<API-ключ>

6. Откройте окно для общения с моделью:

   aider --model openai/deepseek-r1:32b

Теперь вы можете задавать модели вопросы и получать ответы напрямую в терминале.