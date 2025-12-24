---
source_image: page_258.png
page_number: 258
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.79
tokens: 7243
characters: 1147
timestamp: 2025-12-24T03:07:27.518338
finish_reason: stop
---

Создайте новую виртуальную среду и установите pytest:

$ python3 -m venv validation
$ source testing/bin/activate
(validation) $ pip install pytest

Установите testinfra версии 2.1.0:

(validation) $ pip install "testinfra==2.1.0"

Фикстуры pytest предоставляют всю тестовую функциональность проекта Testinfra. Чтобы извлечь пользу из этого раздела, вам необходимо знать, как они работают.

Подключение к удаленным узлам

Поскольку существуют различные типы соединений прикладных частей, то, если соединение не указано непосредственно, Testinfra использует определенные типы по умолчанию. Лучше указывать тип соединения явным образом в командной строке.

Вот список поддерживаемых Testinfra соединений:

• локальное;
• Paramiko (SSH-реализация на Python);
• Docker;
• SSH;
• Salt;
• Ansible;
• Kubernetes (через утилиту командной строки kubectl);
• WinRM;
• LXC.

В меню справки pytest можно найти раздел testinfra с пояснениями по поводу имеющихся флагов. Это очень удобная возможность, которая обязана своим возникновением фреймворку pytest и его интеграции с Testinfra. Справку по обоим проектам можно получить с помощью одной и той же команды: