---
source_image: docs_tutorials-evolution_list_topics_managed-trino__trino-iceberg.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.36
tokens: 12261
characters: 7041
timestamp: 2025-12-24T06:03:01.264843
finish_reason: stop
---

### Подключение Trino к Iceberg

#### Постановка задачи
1. Создать и заполнить таблицу с данными сотрудников.
2. Прочитать данные таблицы в определенной точке времени, используя формат данных Iceberg.

#### Перед началом работы
1. Зарегистрируйтесь в личном кабинете Cloud.ru.
   Если вы уже зарегистрированы, войдите под своей учетной записью.
2. Создайте публичный SNAT-шлюз, чтобы обеспечить инстансу доступ в интернет и связь с внешними источниками.
3. Создайте бакет Object Storage, в котором будут храниться таблицы и схемы.
4. Создайте секреты в сервисе Secret Management для доступа к Object Storage. Понадобится сохранить идентификатор ключа доступа (access key) и секретный ключ доступа (key secret).
5. Настройте DNS-сервер и подсеть.
6. Создайте кластер Data Platform, в котором будет размещен инстанс.
   Назовите кластер «dp-labs».
7. Скачайте и установите root-сертификат на устройство.
8. Установите JDBC-клиент DBeaver.

**Внимание**
Все сущности должны располагаться в одной VPC и подсетях одного типа.

#### Создайте инстанс Managed Metastore
1. Перейдите в раздел Evolution и выберите сервис Managed Metastore.
2. Нажмите Создать инстанс.
3. В блоке Общие параметры заполните поля следующими значениями:
   • Название — iceberg-metastore-lab.
   • Кластер — dp-labs.
   • Лог-группа — группа, в которой будут храниться логи инстанса.
   • Файловая система — S3 и выберите Object Storage.
   • Бакет — созданный бакет Object Storage.
4. Нажмите Продолжить.
5. В блоке Сетевые настройки выберите:
   • Зона доступности — зону доступности, для которой создан SNAT-шлюз.
   • Подсеть — подсеть с DNS-сервером.
6. Нажмите Создать.
7. Дождитесь, когда статус инстанса изменится на «Готов».
8. Откройте карточку инстанса. Информация об инстансе понадобится при создании каталога Trino.

#### Создайте каталог
1. Перейдите в раздел Evolution и выберите сервис Managed Trino.
2. Откройте раздел Каталог.
3. Нажмите Создать каталог.
4. Заполните поля следующими значениями:
   • Название — metastore_iceberg_lab.
   • Коннектор — Iceberg.
   • Каталог — Metastore.
   • Thrift URL — Thrift URL, скопированный с карточки Metastore.
   • Эндпоинт — https://s3.cloud.ru .
   • Идентификатор ключа доступа — access key, выбирается из Secret Management.
   • Секретный ключ доступа — secret key, выбирается из Secret Management.
   • Регион S3 — ru-central-1 .
5. Нажмите Создать.

На странице Managed Trino в разделе Каталог появится запись с названием «metastore_iceberg_lab».

#### Создайте инстанс Trino
1. Перейдите в раздел Evolution и выберите сервис Managed Trino.
2. Откройте раздел Инстансы.
3. Нажмите Создать инстанс.
4. В блоке Общие параметры заполните поля следующими значениями:
   • Название — trino-iceberg-lab.
   • Кластер — dp-labs.
   • Вычислительные ресурсы — vCPU 4, RAM 16.
   • Количество node — 3.
5. Нажмите Продолжить.
6. В блоке Каталог выберите каталог Metastore с названием «metastore_iceberg_lab».
7. Нажмите Продолжить.
8. В блоке Сетевые настройки выберите:
   • Зона доступности — зону доступности, для которой создан SNAT-шлюз.
   • Подсеть — подсеть, в которой расположен инстанс Managed Metastore.
   • Подключить публичный хост — активируйте опцию.
   • Пользователь — имя пользователя.
   • Пароль — секретный ключ.
9. Нажмите Создать.
10. Дождитесь, когда статус инстанса изменится на «Готов».
11. Откройте карточку инстанса Trino. Информация из нее понадобится при подключении к DBeaver.

#### Подключите Trino к DBeaver
Добавьте сертификат в Java KeyStore
1. Запустите терминал и перейдите в директорию, где хотите сохранить JKS-файл.
2. Введите команду:

```bash
keytool -importcert
    -alias cloudru-root
    -file <PATH>/dp-cert.crt
    -keystore <PATH>/cloudru-truststore.jks
    -storetype JKS
    -storepass <YOUR-PASSWORD>
    -noprompt
```

• В строке -file вместо <PATH> укажите путь до скачанного ранее root-сертификата.
• В строке -keystore вместо <PATH> укажите путь до места, где будет храниться JKS-файл.
   Сохраните путь. Он понадобится при добавлении JKS-файла в DBeaver.
• В строке -storepass вместо <YOUR-PASSWORD> задайте пароль для сертификата.
   Сохраните пароль. Он понадобится при добавлении JKS-файла в DBeaver.

Подключите DBeaver
1. Откройте приложение DBeaver.
2. В панели сверху нажмите База данных → Новое соединение.
3. В списке соединений выберите Trino.
4. Нажмите Далее и на вкладке Главное заполните поля информацией из карточки инстанса:
   • Хост
   • Порт
   • Пользователь
   • Пароль

![Скриншот окна подключения DBeaver](https://i.imgur.com/1234567.png)

5. На вкладке Свойства драйвера измените значение свойства SSL на true .

![Скриншот вкладки свойств драйвера](https://i.imgur.com/7654321.png)

6. Нажмите Тест соединения.
7. Нажмите Готово.

Слева в списке объектов появится база данных Metastore с названием «iceberg-metastore-lab».

#### Отправьте SQL-запросы
1. Запустите DBeaver.
2. Создайте новый редактор SQL и введите команду:

```sql
SHOW CATALOGS;
```

В списке должен появиться коннектор «metastore_iceberg_lab».
3. Создайте схему:

```sql
CREATE SCHEMA IF NOT EXISTS metastore_iceberg_lab.my_company_iceberg;
```

4. Создайте таблицу в каталоге Iceberg:

```sql
CREATE TABLE IF NOT EXISTS metastore_iceberg_lab.my_company_iceberg.employees
(
    id_employee INT,
    email VARCHAR(255)
)
WITH (
    format = 'PARQUET'
);
```

5. Вставьте данные в таблицу:

```sql
INSERT INTO metastore_iceberg_lab.my_company_iceberg.employees
values (1, 'xxx@example.com'), (2, 'yyy@example.com'), (3, 'zzz@example.com');
```

6. Прочитайте данные из таблицы, чтобы убедиться, что данные записаны:

```sql
SELECT *
FROM metastore_iceberg_lab.my_company_iceberg.employees;
```

7. Вставьте данные в таблицу:

```sql
INSERT INTO metastore_iceberg_lab.my_company_iceberg.employees
values (4, 'ttt@example.com'), (5, 'qqq@example.com'), (6, 'iii@example.com');
```

8. Прочитайте данные из таблицы, чтобы убедиться, что данные записаны:

```sql
SELECT *
FROM metastore_iceberg_lab.my_company_iceberg.employees;
```

9. Прочитайте историю таблицы:

```sql
SELECT *
FROM metastore_iceberg_lab.my_company_iceberg."employees$history"
ORDER BY made_current_at;
```

В результате выполнения запроса будет выведена история изменений таблицы, содержащая записи о создании таблицы и добавлении в нее новых строк.

10. Добавьте данные в таблицу:

```sql
INSERT INTO metastore_iceberg_lab.my_company_iceberg.employees
values (7, 'qqq@example.com'), (8, 'www@example.com'), (9, 'eee@example.com');
```

11. Прочитайте данные из таблицы, чтобы проверить, что появилась еще одна запись:

```sql
SELECT *
FROM metastore_iceberg_lab.my_company_iceberg."employees$history"
ORDER BY made_current_at;
```

12. Чтобы понаблюдать, как таблица менялась со временем, прочитайте данные из таблицы, подставляя в запрос различные значения из столбца made_current_at .

```sql
SELECT *
FROM metastore_iceberg_lab.my_company_iceberg.employees
FOR TIMESTAMP AS OF TIMESTAMP 'YYYY-MM-DD HH:MM:SS.000+0300';
```

Где 'YYYY-MM-DD HH:MM:SS.000' — скопированное время создания таблицы.