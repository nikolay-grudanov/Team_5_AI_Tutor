---
source_image: docs_tutorials-evolution_list_topics_managed-postgresql__pg_dump.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.56
tokens: 5270
characters: 2765
timestamp: 2025-12-24T05:57:37.911591
finish_reason: stop
---

### Резервное копирование и восстановление базы данных

С помощью этого руководства вы создадите дамп базы данных PostgreSQL® через pg_dump, а затем восстановите базу с помощью pg restore. Восстановить данные можно только в существующую базу данных. За раз вы можете восстановить одну базу данных.

Шаги:

1. Разверните необходимые ресурсы в облаке.
2. Создайте дамп базы данных.
3. Восстановите базу данных из дампа.

Перед началом работы

1. Зарегистрируйтесь в личном кабинете Cloud.ru.
   Если вы уже зарегистрированы, войдите под своей учетной записью.
2. Сгенерируйте SSH-ключ и загрузите его в облачный каталог.

1. Разверните необходимые ресурсы в облаке

1. Создайте виртуальную машину с ОС Ubuntu 24.04 в том же проекте, зоне доступности и подсети, где будет располагаться кластер Managed PostgreSQL®.
2. Назначьте виртуальной машине публичный IP-адрес.
3. Убедитесь, что вы можете подключиться к виртуальной машине по SSH.
4. Создайте кластер.
5. Подключитесь к базе данных.

2. Создайте дамп базы данных

Внимание
Перенос пользователей через дамп базы данных невозможен.
Вы можете создать пользователей через личный кабинет или API. Не используйте имена dbadmin, postgres, cnpq_pooler_pgbouncer, streaming_replica, а также имена, начинающиеся на pg, так как эти имена зарезервированы сервисом Managed PostgreSQL®.

Утилита pg_dump — встроенный инструмент для создания резервных копий в PostgreSQL®.

Используйте команду:

```sh
pg_dump \
--dbname=<database_name> \
--file=<dump_file_path> \
--format=c \
--inserts \
--disable-triggers \
--no-owner \
--if-exists \
--username=<database_user_name> \
--host=<database_host> \
--port=<database_port> \
-v
```

Где:
• <database_name> — имя базы данных.
• <dump_file_path> — путь до файла дампа.
• <database_user_name> — имя пользователя базы данных.
• <database_host> — хост базы данных.
• <database_port> — порт базы данных.

3. Восстановите базу данных из дампа

Утилита pg_restore восстанавливает данные из резервных копий, которые были созданы с помощью pg_dump.

Внимание
У пользователя dbadmin нет прав на CREATE DATABASE, поэтому восстановление можно выполнить только в существующую базу данных. Вы можете создать базу данных через личный кабинет или API.

```sh
pg_restore --dbname=<database_name> \
--username=<database_user_name> \
--host=<database_host> \
--port=<database_port> \
--disable-triggers \
--no-owner \
--if-exists \
<dump_file_path> \
-v
```

Где:
• <database_name> — имя базы данных.
• <database_user_name> — имя пользователя базы данных.
• <database_host> — хост базы данных.
• <database_port> — порт базы данных.
• <dump_file_path> — путь до файла дампа.

Результат

Вы создали дамп базы данных PostgreSQL® с помощью утилиты pg_dump, а затем восстановили базу с помощью pg_restore.