---
source_image: docs_tutorials-evolution_list_topics_bare-metal__1c_deploy.jpg
page_number: 1
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 60.61
tokens: 7159
characters: 3348
timestamp: 2025-12-24T05:28:38.876422
finish_reason: stop
---

### Развертывание 1С на сервере Bare Metal

С помощью этого руководства вы развернете и настроите программу «1C: Предприятие» на сервере Bare Metal с OC Ubuntu 22.04. Для управления базой данных используем СУБД PostgreSQL.

Шаги:

1. Разверните инфраструктуру.
2. Установите кластер 1С.
3. Настройте PostgreSQL.
4. Запустите и настройте сервер 1С.

#### 1. Разверните инфраструктуру

1. Арендуйте сервер Bare Metal с публичным IP-адресом. Для корректной работы 1С выбирайте конфигурации с:
   • количеством CPU от 4;
   • объемом оперативной памяти не менее 16 ГБ;
   • объемом дискового пространства от 150 ГБ.
2. Подключитесь к серверу по SSH или через виртуальную консоль.
3. Установите дополнительные пакеты для работы:

```sh
sudo apt update
sudo apt install -y wget curl unzip nano htop
```

4. Установите зависимости для работы с 1С:

```sh
sudo apt install -y libatdc++6 libgtk2.0-0 libxslt1.1 libcanberra-gtk-module
```

5. Установите PostgreSQL:

```sh
sudo apt install -y postgresql postgresql-contrib
```

Подробнее об установке PostgreSQL.

#### 2. Установите кластер 1С

1. Скачайте дистрибутив 1С с официального сайта.
2. Установите дистрибутив:

```sh
sudo dpkg -i 1c_Enterprise*.deb
sudo apt --fix-broken install
```

3. Проверьте установку:

```sh
rac cluster list
```

В результате должны отобразиться параметры кластера 1С.

#### 3. Настройте PostgreSQL

1. Войдите в консоль PostgreSQL:

```sh
sudo -u postgres psql
```

2. Создайте базу данных и пользователя для нее:

```sql
CREATE USER <user_name> WITH PASSWORD '<password>';
CREATE DATABASE <db_name> OWNER <user_name>;
\q
```

Где:
• <user_name> — имя пользователя БД.
• <password> — пароль пользователя БД.
• <db.name> — название БД.

3. Откройте файл с конфигурацией аутентификации пользователей:

```sh
sudo nano /etc/postgresql/<postgresql_version>/main/pg_hba.conf
```

4. Добавьте в конец файла строку:

```sh
host    all         all         0.0.0.0/0           md5
```

5. Перезагрузите PostgreSQL:

```sh
sudo systemctl restart postgresql
```

6. Проверьте работу PostgreSQL:

```sh
sudo systemctl status postgresql
```

#### 4. Запустите и настройте сервер 1С

1. Запустите службу сервера 1С и проверьте его статус:

```sh
sudo systemctl start srvlev83
sudo systemctl enable srvlev83
sudo systemctl status srvlev83
```

2. Получите информацию о кластере:

```sh
rac cluster list
```

Результат:

```sh
cluster        : <1c_cluster_UUID>
host           : baremetal-1c
port           : 1541
name           : "ваш кластер"
expiration-timeout : 60
lifetime-limit : 0
max-memory-size : 0
max-memory-time-limit : 0
security-level : 0
```

Где <1c_cluster_UUID> — идентификатор кластера 1С.

3. Создайте информационную базу:

```sh
rac infobase create --cluster=<1c_cluster_UUID> \
--create-database \
--name=dblc \
--desc="BaseForBareMetal" \
--db=PostgreSQL \
--db-server=baremetal-1c \
--db-user=usr1c \
--db-pwd="password" \
--license-distribution=allow --scheduled-jobs-deny-on
```

4. Проверьте создание информационной базы:

```sh
rac infobase --cluster=<1c_cluster_UUID> summary list
```

5. Настройте UFW для ограничения доступа к серверу:

```sh
sudo ufw allow ssh
sudo ufw allow 1540-1560/tcp
sudo ufw enable
```

6. Настройте регулярное резервное копирование баз данных:

```sh
pg_dump -U usr1c -d dblc > backup.sql
```

Сервер 1С развернут и готов к работе.