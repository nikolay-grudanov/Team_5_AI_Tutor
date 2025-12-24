---
source_image: docs_tutorials-evolution_list_topics_monitoring-and-logging__monitoring__vmagent-vm.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 592.79
tokens: 19292
characters: 11313
timestamp: 2025-12-24T06:16:25.917480
finish_reason: stop
---

Мониторинг виртуальной машины с помощью vmagent

С помощью этого руководства вы настроите мониторинг виртуальной машины в сервисе «Мониторинг» с помощью плагина vmagent. Плагин представляет собой легковесный агент для сбора метрик, который поддерживает протокол remote_write для отправки данных в систему мониторинга.

Вы будете использовать следующие сервисы:

• Мониторинг — сервис сбора и хранения метрик облачных ресурсов.
• Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина, для которой будет настроен мониторинг.
• vmagent — агент, автоматизирующий сбор метрик приложений, развернутых на виртуальной машине.
• Node Exporter — агент, собирающий метрики ОС на базе ядра Linux и передающий их в систему мониторинга Prometheus.

Шаги:

1. Подготовьте виртуальную машину.
2. Установите vmagent.
3. Установите Node Exporter.
4. Настройте конфигурацию vmagent.
5. Запустите vmagent и настройте отправку метрик.
6. Создайте дашборд в сервисе «Мониторинг».
7. Настройте алерты.
8. Проверьте доступность метрик в сервисе.
9. Проверьте уведомления об алертах.
10. Оптимизируйте сбор метрик.
11. Настройте дополнительные экспортеры.

Перед началом работы

1. Зарегистрируйтесь в личном кабинете Cloud.ru.
   Если вы уже зарегистрированы, войдите под своей учетной записью.
2. Создайте сервисный аккаунт. При создании в поле Сервисы выберите роль «monaas.write».
3. Для сервисного аккаунта создайте ключи доступа.
4. Получите авторизационный токен.
5. Создайте виртуальную машину Ubuntu.
6. Убедитесь, что в сервисе «Виртуальные машины» у вас есть права администратора для установки программного обеспечения.

1. Подготовьте виртуальную машину
1. После создания виртуальной машины подключитесь к ней по SSH:
   ssh username@your-vm-ip-address
2. Обновите системные пакеты.
   sudo apt update && sudo apt upgrade -y

2. Установите vmagent
1. Создайте директорию для vmagent:
   sudo mkdir -p /opt/vmagent
   cd /opt/vmagent
2. Загрузите последний релиз vmagent. Пример для amd64:
   sudo wget https://github.com/VictoriaMetrics/VictoriaMetrics/releases/download/v1.126.0/vmutils-linux-amd64-v1.126.0.tar.gz
3. Распакуйте архив:
   sudo tar -xvzf vmutils-linux-amd64-v1.126.0.tar.gz

3. Установите Node Exporter
1. Создайте директорию для Node Exporter:
   sudo mkdir -p /opt/node_exporter
   cd /opt/node_exporter
2. Скачайте дистрибутив Node Exporter:
   sudo wget https://github.com/prometheus/node_exporter/releases/download/v1.9.1/node_exporter-1.9.1.linux-amd64.tar.gz
3. Распакуйте архив:
   sudo tar -xvzf node_exporter-1.9.1.linux-amd64.tar.gz
4. Скопируйте бинарный файл в директорию /opt/node_exporter :
   sudo cp node_exporter-1.9.1.linux-amd64/node_exporter .
5. Создайте службу systemd для Node Exporter с помощью текстового редактора, например vi :
   sudo vi /etc/systemd/system/node_exporter.service
6. В файл добавьте данные в виде:
   [Unit]
   Description=Node Exporter
   After=network.target
   [Service]
   ExecStart=/opt/node_exporter/node_exporter
   Type=simple
   Restart=always
   [Install]
   WantedBy=multi-user.target
7. Создайте пользователя для Node Exporter:
   sudo useradd -rs /bin/false node_exporter
8. Запустите службу и проверьте ее состояние:
   sudo systemctl daemon-reload
   sudo systemctl enable --now node_exporter
   sudo systemctl status node_exporter

4. Настройте конфигурацию vmagent
1. Создайте файл конфигурации для vmagent:
   sudo vi /opt/vmagent/vmagent-config.yml
2. В файл добавьте данные в виде:
   global:
     scrape_interval: 15s
     external_labels:
       monitor: 'vm-agent'
   scrape_configs:
     - job_name: 'node-exporter'
       static_configs:
         - targets: ['localhost:9100']
           metric_path: /metrics
     - job_name: 'vmagent'
       static_configs:
         - targets: ['localhost:8429']
           metric_path: /metrics

5. Запустите vmagent и настройте отправку метрик
На этом этапе вы создадите службу vmagent с конфигурацией для отправки метрик в сервис «Мониторинг».
1. Создайте файл службы vmagent:
   sudo vi /etc/systemd/system/vmagent.service
2. В файл добавьте данные в виде:
   [Unit]
   Description=vmagent
   After=network.target
   [Service]
   Type=simple
   User=vmagent
   Group=vmagent
   ExecStart=/opt/vmagent/vmagent-prod --promscrape_config=/opt/vmagent/vmagent-config.yml --remoteWrite.url=https://<monaas-write-endpoint>/api/v1/write
   Restart=always
   [Install]
   WantedBy=multi-user.target
Где:
• {projectID} — идентификатор проекта, куда будут отправляться метрики. Вы можете скопировать его из URL личного кабинета.
• {clientID} — Key ID (логин) сервисного аккаунта с ролью «monaas.write».
• {clientSecret} — Key Secret (пароль) сервисного аккаунта.
3. Создайте пользователя для vmagent:
   sudo useradd -rs /bin/false vmagent
4. Назначьте права на директорию:
   sudo chown -R vmagent:vmagent /opt/vmagent
5. Запустите службу vmagent и проверьте ее состояние:
   sudo systemctl daemon-reload
   sudo systemctl enable --now vmagent
   sudo systemctl status vmagent

6. Создайте дашборд в сервисе «Мониторинг»
1. В сервисе «Мониторинг» перейдите в раздел Мониторинг → Дашборды → Пользовательские.
2. Нажмите Создать дашборд. Укажите его название: «Мониторинг VM».
3. Перейдите на страницу дашборда и добавьте виджеты:
   а. Виджет для отслеживания использования CPU:
      1. Тип виджета: Временной ряд.
      2. Название: «Использование CPU».
      3. Описание: «Средняя загрузка CPU в процентах за 5 минут (100% минус время idle)».
      4. Запрос:
         100 - (avg by(instance)(rate(node_cpu_seconds_total{mode="idle", monitor="vm-agent"}[5m])) * 100
   5. Настройка левой оси: категория Проценты (0-100).
   б. Виджет для отслеживания объема доступной оперативной памяти:
      1. Тип виджета: Временной ряд.
      2. Название: «Использование памяти».
      3. Описание: «Объем доступной оперативной памяти».
      4. Запрос:
         node_memory_MemAvailable_bytes{monitor="vm-agent"}
   5. Настройка левой оси: категория Объем данных.
   с. Виджет для отслеживания свободного места на корневом разделе диска:
      1. Тип виджета: Временной ряд.
      2. Название: «Дисковое пространство».
      3. Описание: «Свободное место на корневом разделе диска (в байтах)».
      4. Запрос:
         node_filesystem_avail_bytes{monitor="vm-agent"}
   5. Настройка левой оси: категория Объем данных.
   d. Виджет для отслеживания сетевого трафика:
      1. Тип виджета: Временной ряд.
      2. Название: «Сетевая активность».
      3. Описание: «Входящий и исходящий сетевой трафик (в байтах)».
      4. Запрос для входящего трафика:
         rate(node_network_receive_bytes_total{device!="lo|veth.*"}[5m])
      Легенда:
         Сетевой трафик (входящий) (б/с)
      5. Запрос для исходящего трафика:
         rate(node_network_transmit_bytes_total{device!="lo|veth.*"}[5m])
      Легенда:
         Сетевой трафик (исходящий) (б/с)
   6. Настройка левой оси: категория Передача данных.

7. Настройте алерты
1. В сервисе «Мониторинг» перейдите в раздел Мониторинг → Алерты мониторинга → Правила алертов.
2. Создайте правила алертов для ключевых метрик:
   а. Правило, срабатывающее при загрузке CPU выше 90% в течение 5 минут:
      1. Название: «Высокая загрузка CPU на VM»,
      2. Описание: «Утилизация CPU на VM более 90% за 5 минут».
      3. Запрос:
         100 - (avg by(instance)(rate(node_cpu_seconds_total{mode="idle", monitor="vm-agent"}[5m])) * 100
      4. Важность: Высокая.
      5. Объект: выберите, для какой виртуальной машины создается правило алерта, указав любой из ее параметров:
         • название;
         • ID;
         • название метрики, в котором содержится название виртуальной машины, в формате {{label}}.
      6. Ресурс: «CPU».
   b. Правило, срабатывающее при использование памяти более чем на 90%:
      1. Название: «Высокая утилизация RAM на VM».
      2. Описание: «Утилизация RAM на VM более 90% за 5 минут».
      3. Запрос:
         (node_memory_MemTotal_bytes{monitor="vm-agent"}-node_memory_MemAvailable_bytes{monitor="vm-agent"})
      4. Частота проверки: 5 минут.
      5. Важность: Высокая.
      6. Объект: выберите, для какой виртуальной машины создается правило алерта, указав любой из ее параметров:
         • название;
         • ID;
         • название метрики, в котором содержится название виртуальной машины, в формате {{label}}.
      7. Ресурс: «RAM».
   c. Правило, срабатывающее при заполненности дискового пространства более чем на 85%:
      1. Название: «Диск заполнен более чем на 85%».
      2. Описание: «Дисковое пространство заполнено более чем на 85%».
      3. Запрос:
         (node_filesystem_size_bytes{monitor="vm-agent"}-node_filesystem_avail_bytes{monitor="vm-agent"})
      4. Частота проверки: 5 минут.
      5. Важность: Высокая.
      6. Объект: выберите, для какой виртуальной машины создается правило алерта, указав любой из ее параметров:
         • название;
         • ID;
         • название метрики, в котором содержится название виртуальной машины, в формате {{label}}.
      7. Ресурс: «DISK».

8. Проверьте доступность метрик в сервисе
1. Проверьте состояние службы на виртуальной машине:
   sudo systemctl status node_exporter
   sudo systemctl status vmagent
2. Проверьте логи vmagent на наличие ошибок:
   sudo journalctl -u vmagent.service -f
3. Убедитесь, что метрики поступают в сервис «Мониторинг».
4. Проверьте, что на виджетах дашборда «Мониторинг VM» отображаются показатели.

9. Проверьте уведомления об алертах
1. Чтобы провести нагрузочное тестирование и проверить, что алерты работают, установите утилиту stress-ng на виртуальную машину:
   sudo apt-get install stress-ng
2. Создайте нагрузку на CPU для тестирования оповещений:
   stress-ng --cpu 4 --timeout 300s
3. Проверьте, что на созданном дашборде отображается высокая утилизация CPU.
4. Проверьте, что срабатывает алерт о высокой загрузке CPU.

10. Оптимизируйте сбор метрик
Для оптимизации производительности vmagent:
1. Настройте фильтрацию метрик: используйте relabel_configs , чтобы отфильтровать ненужные метрики.
2. Настройте частоту сбора метрик: задайте подходящее значение scrape_interval .
3. Оптимизируйте параметры буферизации для нестабильных сетей. Пример оптимизированной конфигурации vmagent, расположенной в файле /opt/vmagent/vmagent-config.yml :
   global:
     scrape_interval: 30s
     scrape_timeout: 25s
   scrape_configs:
     - job_name: 'node-exporter'
       static_configs:
         - targets: ['localhost:9100']
           metric_path: /metrics
           relabel_configs:
             - source_labels: [_name_]
               regex: 'node_cpu_seconds_total|node_memory_MemAvailable_bytes|node_memory_MemTotal_bytes|node_filesystem_size_bytes|node_filesystem_avail_bytes'
               target_label: keep
   В сервис «Мониторинг» будут отправляться только метрики, указанные в тегах .

11. Настройте дополнительные экспортеры
Для расширенного мониторинга установите дополнительные экспортеры:
• для мониторинга Docker — cadvisor;
• для мониторинга веб-сервера — nginx-exporter или apache-exporter;
• для мониторинга баз данных — mysqld-exporter.

Результат
Вы запустили vmagent для мониторинга виртуальной машины на базе Ubuntu, настроили сбор и отправку метрик в сервис «Мониторинг», создали дашборд для отслеживания показателей и настроили оповещения по основным метрикам.