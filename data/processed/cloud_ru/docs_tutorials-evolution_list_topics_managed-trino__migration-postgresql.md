---
source_image: docs_tutorials-evolution_list_topics_managed-trino__migration-postgresql.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 61.80
tokens: 8981
characters: 4859
timestamp: 2025-12-24T06:02:40.191944
finish_reason: stop
---

Миграция PostgreSQL с помощью Trino

Постановка задачи
1. Создать таблицу-источник и целевую таблицу.
2. Перенести данные в целевую таблицу с помощью:
   • JDBC-клиента (DBeaver);
   • Python-скрипта.

Перед началом работы
1. Зарегистрируйтесь в личном кабинете Cloud.ru.
   Если вы уже зарегистрированы, войдите под своей учетной записью.
2. Настройте DNS-сервер и подсеть.
3. Создайте кластер Data Platform, в котором будет размещен инстанс.
   Назовите кластер «dp-labs».
4. Скачайте и установите root-сертификат на устройство.
5. Установите JDBC-клиент DBeaver.

Внимание
Все сущности должны располагаться в одной VPC и подсетях одного типа.

Подготовка инфраструктуры
Подготовьте базу данных и таблицы, которые будете переносить, а также каталоги и инстанс Trino.

Создайте Managed PostgreSQL®
1. Создайте кластер Managed PostgreSQL.
2. Создайте две базы данных с названиями:
   • pg_1 — это исходная база данных, которая содержит таблицы для миграции;
   • pg_2 — это целевая база данных, куда нужно перенести таблицы из pg_1.
3. Сохраните пароль из карточки кластера в сервисе Secret Manager.

Создайте каталог Managed Trino
1. Перейдите в раздел Evolution и выберите сервис Managed Trino.
2. Откройте раздел Каталоги.
3. Нажмите Создать каталог.
4. Заполните поля следующими значениями:
   • Название:
     • pg_1 — для исходной базы данных pg_1;
     • pg_2 — для целевой базы данных pg_2.
   • Коннектор — PostgreSQL.
   • Хост — внутренний IP, указанный в карточке кластера Managed PostgreSQL®.
   • Порт — порт, указанный в карточке кластера Managed PostgreSQL®.
   • Название базы данных:
     • pg_1
     • pg_2
   • Логин — логин, указанный в карточке кластера Managed PostgreSQL®.
   • Пароль — выберите секрет с паролем кластера Managed PostgreSQL®.
5. Нажмите Создать.

Создайте инстанс Managed Trino
1. Перейдите в раздел Evolution и выберите сервис Managed Trino.
2. Откройте раздел Инстансы.
3. Нажмите Создать инстанс.
4. В блоке Общие параметры заполните поля:
   • Название — trino-instance-migration.
   • Кластер — db-labs.
   • Вычислительные ресурсы — vCPU 4, RAM 16.
   • Количество node — 3.
5. Нажмите Продолжить.
6. На шаге Каталоги выберите каталоги «pg_1» и «pg_2».
7. Нажмите Продолжить.
8. В блоке Сетевые настройки заполните поля:
   • Зона доступности — выберите зону доступности, для которой создан SNAT-шлюз.
   • Подсеть — выберите подсеть с DNS-сервером.
   • Подключить публичный хост — активируйте опцию.
   • Пользователь — задайте имя пользователя для доступа к Trino.
   • Пароль — создайте пароль в сервисе Secret Manager, нажав Создать секрет, и выберите его.
9. Нажмите Создать.

Создайте структуру данных
Выполните команды:

CREATE SCHEMA IF NOT EXISTS pg_1.lab_migration;
CREATE TABLE IF NOT EXISTS pg_1.lab_migration.users (id_user INT, email VARCHAR(255));
INSERT INTO pg_1.lab_migration.users values (1, 'one@example.com'), (2, 'two@example.com'), (3, 'three@example.com');

Миграция
Рассмотрим два способа миграции таблиц с помощью:
• JDBC-клиента DBeaver;
• Python-скрипта.

С помощью DBeaver
1. Подключите инстанс к DBeaver.
2. Чтобы подготовить данные, в DBeaver выполните SQL-запросы:

CREATE SCHEMA IF NOT EXISTS pg_1.lab_migration;
CREATE TABLE IF NOT EXISTS pg_1.lab_migration.users (id_user INT, email VARCHAR(255));
INSERT INTO pg_1.lab_migration.users values (1, 'xxx@example.com'), (2, 'yyy@example.com'), (3, 'zzz@example.com');

Можете создать дополнительные таблицы с данными в схеме «lab_migration» в базе данных «pg_1».
3. Выполните:

Миграция таблицы с данными	Миграция таблицы без данных (только структура)

CREATE TABLE pg_2.lab_migration.users AS
SELECT * FROM pg_1.lab_migration.users;

4. Автоматизируйте миграцию таблиц.
   a. Чтобы сгенерировать SQL-запросы для каждой таблицы, выполните:

SELECT
    'CREATE TABLE pg_2.lab_migration.' || table_name ||
    ' AS SELECT * FROM pg_1.lab_migration.' || table_name || ';'
FROM pg_1.information_schema.tables
WHERE table_schema = 'lab_migration';

b. Скопируйте полученные строки.
c. Выполните их по очереди.

С помощью скрипта
1. В командной строке выполните:

python3 -m venv venv
source venv/bin/activate
pip install trino

2. Скопируйте скрипт, введите необходимые значения и сохраните файл с названием trino_pg_migration.py :

Скрипт Python

3. Запустите скрипт:

python trino_pg_migration.py

Проверка результата
В DBeaver выполните следующие запросы:
• Чтобы проверить, что таблицы созданы:

SHOW TABLES IN pg_2.lab_migration;

• Чтобы проверить количество строк в каждой таблице:

SELECT COUNT(*) FROM pg_2.lab_migration.users;
SELECT COUNT(*) FROM pg_2.lab_migration.products;
SELECT COUNT(*) FROM pg_2.lab_migration.orders;

• Чтобы проверить содержимое (первые 10 строк):

SELECT * FROM pg_2.lab_migration.users LIMIT 10;
SELECT * FROM pg_2.lab_migration.products LIMIT 10;
SELECT * FROM pg_2.lab_migration.orders LIMIT 10;