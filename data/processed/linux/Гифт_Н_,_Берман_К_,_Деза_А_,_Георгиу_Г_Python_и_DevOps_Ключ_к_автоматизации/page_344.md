---
source_image: page_344.png
page_number: 344
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.20
tokens: 7439
characters: 1632
timestamp: 2025-12-24T03:09:46.231713
finish_reason: stop
---

Sa9lkz3Y7V4KC\nefzBiS8pivm55T0s+zPBPB/GWUVlqGaxRhv1TAU=\n=WA4+
\n----END PGP MESSAGE-----\n",
"fp": "E14104A0890994B9AC9C9F6782C1FF5E679EFF32"
}
],
"unencrypted_suffix": "_unencrypted",
"version": "3.0.5"
}
}%

Для его расшифровки выполните:

$ sops -d environment.secrets
export DBPASS=MYPASS

Существует одна небольшая проблема, связанная с взаимодействием sops с gpg на компьютерах Macintosh. Перед расшифровкой файла с помощью sops необходимо выполнить следующие команды:

$ GPG_TTY=$(tty)
$ export GPG_TTY

Наша цель — запустить сервис migrations, описанный ранее в файле docker-compose.yml. Связать метод управления секретными данными sops с docker-compose, расшифровать файл environments.secrets с помощью sops -d, отправить с помощью команды source его содержимое в виртуальную среду текущей командной оболочки, после чего вызвать docker-compose up -d migrations, и все это — в однорядочной команде, чтобы секретные данные не отображались в истории командной оболочки:

$ source <(sops -d environment.secrets); docker-compose up -d migrations
postgres is up-to-date
Recreating flask-by-example_migrations_1 ... done

Проверяем, что миграция выполнена успешно, заглянув в базу данных и убедившись, что были созданы две таблицы — alembic_version и results:

$ docker-compose exec db psql -U postgres wordcount
psql (11.4 (Debian 11.4-1.pgdg90+1))
Type "help" for help.

wordcount=# \dt
    List of relations
 Schema |      Name      | Type  |  Owner
--------+----------------+-------+----------
 public | alembic_version | table | wordcount_dbadmin
 public | results        | table | wordcount_dbadmin
(2 rows)

wordcount=# \q