---
source_image: docs_tutorials-evolution_list_topics_managed-trino__trino-s3.jpg
page_number: 3
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.90
tokens: 15185
characters: 8385
timestamp: 2025-12-24T06:03:18.125532
finish_reason: stop
---

### Подключение Trino к S3

В этом руководстве мы рассмотрим:

- сценарий взаимодействия между Managed Trino, Managed Metastore и Object Storage;
- отправку запросов через DBeaver;
- работу с управляемыми таблицами;
- работу с внешними таблицами.

**Внимание**
Все сущности должны располагаться в одной VPC и подсетях одного типа.

### Перед началом работы

1. Зарегистрируйтесь в личном кабинете Cloud.ru.
   Если вы уже зарегистрированы, войдите под своей учетной записью.
2. Ознакомьтесь с разделом Управляемые и внешние таблицы. В следующих блоках вам будут встречаться термины «управляемые таблицы» и «внешние таблицы».
3. (Опционально) Создайте публичный SNAT-шлюз, если необходим доступ в интернет.
4. Создайте бакет Object Storage, в котором будут храниться таблицы и схемы.
5. Создайте секреты в сервисе Secret Management для доступа к Object Storage. Понадобится сохранить идентификатор ключа доступа (access key) и секретный ключ доступа (key secret).
6. Настройте DNS-сервер и подсеть.
7. Создайте кластер Data Platform, в котором будет размещен инстанс.
   Назовите кластер «dp-labs».
8. Скачайте и установите root-сертификат на устройство.
9. Установите JDBC-клиент DBeaver.

### Создайте инстанс Managed Metastore

1. Перейдите в раздел Evolution и выберите сервис Managed Metastore.
2. Откройте раздел Инстансы.
3. Нажмите Создать инстанс.
4. В блоке Общие параметры заполните поля следующими значениями:
   - Название — metastore_lab.
   - Кластер — dp-labs.
   - Лог-группа — группа логов.
   - Файловая система — S3.
   - Источник — Object Storage.
   - Бакет — созданный бакет Object Storage.
5. Нажмите Продолжить.
6. В блоке Сетевые настройки выберите:
   - Зона доступности — зону доступности, для которой создан SNAT-шлюз.
   - Подсеть — подсеть с DNS-сервером.
7. Нажмите Создать.
8. Дождитесь, когда статус инстанса изменится на «Готов».
9. Нажмите Скопировать Thrift URL.

### Создайте каталог Metastore

1. Перейдите в раздел Evolution и выберите сервис Managed Metastore.
2. Откройте раздел Каталоги.
3. Нажмите Создать каталог.
4. Заполните поля следующими значениями:
   - Название — metastore_lab;
   - Коннектор — Metastore;
   - Thrift URL — Thrift URL, скопированный с карточки Metastore;
   - Эндпоинт — https://s3.cloud.ru ;
   - Идентификатор ключа доступа — access key, выбирается из Secret Management;
   - Секретный ключ доступа — secret key, выбирается из Secret Management;
   - Регион S3 — ru-central-1 .
5. Нажмите Создать.

На странице Managed Trino на вкладке Каталоги появится запись с названием «metastore_lab».

### Создайте инстанс Trino

1. Перейдите в раздел Evolution и выберите сервис Managed Trino.
2. Откройте раздел Инстансы.
3. Нажмите Создать инстанс.
4. В блоке Общие параметры заполните поля следующими значениями:
   - Название — trino-lab-2.
   - Вычислительные ресурсы — vCPU 4, RAM 16.
   - Количество node — 3.
   - Каталоги — выберите из списка каталог Metastore с названием «metastore_lab».
5. Нажмите Продолжить.
6. В блоке Сетевые настройки выберите:
   - Зона доступности — зону доступности, для которой создан SNAT-шлюз.
   - Подсеть — подсеть с DNS-сервером, в которой расположен инстанс Managed Metastore.
   - Группа безопасности — группу безопасности.
   - Пользователь — введите имя пользователя.
   - Пароль — секретный ключ.
   - Подключить публичный хост — активируйте переключатель.
7. Нажмите Создать.
8. Дождитесь, когда статус инстанса изменится на «Готов».
9. Откройте карточку инстанса Trino. Информация из него понадобится на следующих этапах.

### Подключите Trino к DBeaver

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
4. Нажмите Далее заполните поля на вкладке Главное:
   • Хост — публичный хост, указанный в карточке инстанса.
   • Порт — порт, указанный в карточке инстанса.
   • Пользователь — пользователь, указанный в карточке инстанса.
   • Пароль — пароль, указанный в карточке инстанса.
5. На вкладке Свойства драйвера измените значение свойства SSL на true .

6. Нажмите Тест соединения.
7. Нажмите Готово.

Слева в списке объектов появится база данных Metastore с названием «metastore_lab».

![Скриншот окна DBeaver с подключением к Trino](https://i.imgur.com/3Q5z5QG.png)

### Работа с управляемыми таблицами

SQL-запросы в следующих шагах мы будем отправлять через DBeaver.

**Примечание**
Ознакомьтесь с разделом Управляемые и внешние таблицы перед началом.

Управляемая таблица в формате .orc

1. Создайте схему.

```sql
CREATE SCHEMA IF NOT EXISTS metastore_lab.my_company
```

В S3 автоматически создастся каталог warehouse и каталог со схемой my_company.db.

2. Создайте таблицу.

```sql
CREATE TABLE IF NOT EXISTS metastore_lab.my_company.employees (id_employee INT, email VARCHAR(255))
```

В S3 создастся каталог employees .

3. Заполните таблицу.

```sql
INSERT INTO metastore_lab.my_company.employees values (1, 'xxx@example.com'), (2, 'yyy@example.com'),
```

4. Проверьте результат.

```sql
SELECT * FROM metastore_lab.my_company.employees
```

В S3 появится файл в формате .orc .

5. Удалите таблицу.

```sql
DROP TABLE metastore_lab.my_company.employees
```

В результате таблица удалена из Metastore, в S3 все данные вместе с каталогом employees также удалены.

Управляемая таблица в текстовом формате

1. Создайте схему.

```sql
CREATE SCHEMA IF NOT EXISTS metastore_lab.my_company
```

В S3 автоматически создастся каталог warehouse и каталог со схемой my_company.db.

2. Сохраните данные в текстовом формате.

```sql
CREATE TABLE IF NOT EXISTS metastore_lab.my_company.employees_csv (id_employee INT, email VARCHAR(255));
WITH (
    format = 'TEXTFILE'
)
```

3. Заполните таблицу.

```sql
INSERT INTO metastore_lab.my_company.employees_csv values (1, 'xxx@example.com'), (2, 'yyy@example.com')
```

4. Проверьте результат.

```sql
SELECT * FROM metastore_lab.my_company.employees_csv
```

В S3 появится файл в формате .gz .

5. Удалите таблицу.

```sql
DROP TABLE metastore_lab.my_company.employees_csv
```

В результате таблица удалена из Metastore, в S3 все данные вместе с каталогом employees_csv также удалены.

### Работа с внешними таблицами

1. Откройте бакет S3.
2. Создайте каталог с названием data .
3. Подготовьте файл с данными в формате .csv :
   • колонки: id, email
   • значения в колонке id: 1, 2, 3
   • значения в колонке email: xxx@example.com , yyy@example.com , zzz@example.com
4. Добавьте файл в каталог «data» на S3.
5. Запустите DBeaver.
6. Через DBeaver создайте схему.

```sql
CREATE SCHEMA IF NOT EXISTS metastore_lab.my_company
```

7. Создайте таблицу.

```sql
CREATE TABLE IF NOT EXISTS metastore_lab.my_company.csv_external (id VARCHAR, email VARCHAR)
WITH (
    external_location = 's3a://bucket-4b8dce/data',
    format = 'CSV',
    csv_separator = ';',
    skip_header_line_count = 1
)
```

8. Проверьте результат.

```sql
SELECT * FROM metastore_lab.my_company.csv_external
```

9. Подготовьте новый файл с данными в формате .csv :
   • колонки: id, email
   • значения в колонке id: 4, 5, 6
   • значения в колонке email: aaa@example.com , bbb@example.com , ccc@example.com
10. Добавьте файл в каталог «data» на S3. В этом сценарии мы имитируем поступление новых данных из другой системы.
11. Проверьте результат.

```sql
SELECT * FROM metastore_lab.my_company.csv_external
```

Система считывает данные из двух разных файлов с одинаковой структурой и с одинаковым разрешением, как если бы это был один файл.
12. Удалите таблицу.

```sql
DROP TABLE metastore_lab.my_company.csv_external
```

В результате таблица удалена из Metastore. В отличие от управляемых таблиц файлы в S3 остаются доступными.