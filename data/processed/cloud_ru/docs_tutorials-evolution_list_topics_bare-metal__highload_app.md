---
source_image: docs_tutorials-evolution_list_topics_bare-metal__highload_app.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 80.73
tokens: 10428
characters: 6012
timestamp: 2025-12-24T05:29:39.534305
finish_reason: stop
---

### Разработка высоконагруженного приложения на сервере Bare Metal

Эта статья полезна?

С помощью этого руководства вы развернете среду для разработки высоконагруженных приложений. В отличие от виртуальных сред или локальных машин, Bare Metal обеспечивает:

• Предельную производительность — прямой доступ к CPU, RAM, дискам сервера без расходов на гипервизор, что критично для задач с интенсивными вычислениями, например при обработке 100 000+ RPS.

• Детерминированное поведение — идентичность версий приложения для разработки, тестирования и реализации. Это исключает «эффект соседа» в облачной среде и гарантирует воспроизводимость результатов.

• Экономическую эффективность — централизация ресурсов сервера позволяет заменить все локальные машины разработчиков одним мощным сервером.

• Ускорение CI/CD — сборки и тесты выполняются быстрее благодаря отсутствию ограничений виртуализации. Актуально для компиляции приложений на C++ или запуска ML-моделей.

В сценарии разберем разработку приложения командой из 10 разработчиков на сервере, у которого:
• настроена среда разработки VSCode Server;
• установлены программы для проектирования инженерных систем Ansys и HFSS;
• установлена утилита X2Go для запуска Ansys и HFSS;
• в качестве графической среды используется XFCE.

Примечание
Все действия в сценарии выполняются для создания пользователя dev1. Чтобы добавить пользователей для остальных разработчиков, повторите действия.

Шаги:
1. Разверните инфраструктуру.
2. Настройте VSCode Server и системные лимиты.
3. Подключите локальный VSCode к VSCode Server.
4. Настройте UFW для доступа к сервисам только по SSH.
5. Настройте X2Go Server для удаленного рабочего стола на Linux.
6. Настройте X2Go на устройстве разработчика.

1. Разверните инфраструктуру
1. Арендуйте сервер Bare Metal с публичным IP-адресом.
2. Подключитесь к серверу по SSH или через виртуальную консоль.
3. Установите Docker.

2. Настройте VSCode Server и системные лимиты
1. Создайте изолированное окружение для каждого разработчика:

```sh
sudo useradd -m -s /bin/bash dev1   # Создание пользователя
sudo passwd dev1                    # Установка пароля
sudo usermod -aG docker dev1        # Добавление в группу docker
```

2. Настройте системные лимиты:
a. Откройте конфигурационный файл на запись:

```sh
sudo nano /etc/security/limits.conf
```

b. Добавьте в конец файла код:

```sh
dev1 soft nproc 50000
dev1 hard nproc 50000
dev1 soft nofile 50000
dev1 hard nofile 50000
* soft core unlimited
```

Дополнительная настройка для GUI-приложений

c. Нажмите сочетание клавиш Ctrl + O .

3. Подключите локальный VSCode к VSCode Server
Чтобы обеспечить безопасность работы с приложением,
1. На устройстве разработчика создайте пару SSH-ключей:

```sh
ssh-keygen -t ed25519
```

2. Скопируйте публичный ключ на сервер:

```sh
ssh-copy-id dev1@<server_ip_address>
```

3. Установите расширение «Remote SSH» для VSCode.
4. Добавьте сервер в файл .ssh/config :

```sh
Host dev-server-dev1
    HostName <server_ip_address>
    User dev1
    IdentityFile ~/.ssh/id_ed25519
```

5. Подключитесь к серверу из VSCode:
a. Нажмите сочетание клавиш Ctrl + Shift + P .
b. В строке поиска введите Remote-SSH: Connect to Host .
c. В списке выберите dev-server-dev1.

4. Настройте UFW для доступа к сервисам только по SSH
При разработке сервисов важно обеспечить их недоступность извне. Для этого необходимо закрыть все сервисные порты с помощью UFW. В этом случае приложения будут доступны только по SSH.

1. Создайте новые правила UFW:

```sh
# Откройте всех-премиум
sudo ufw --force reset
# Запретите все исходящие соединения по умолчанию
sudo ufw default deny incoming
# Разрешите все входящие
sudo ufw default allow outgoing
# Разрешите SSH (порт 22)
sudo ufw allow 22/tcp
# Включите UFW
sudo ufw enable
```

2. Проверьте статус UFW:

```sh
sudo ufw status verbose
```

Результат

Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), disabled (routed)
New profiles: skip
To Action From
-- ---- ----
22/tcp ALLOW IN Anywhere

5. Настройте X2Go Server для удаленного рабочего стола на Linux
Для работы с графическими приложениями (CAD/CAM/CAE) терминала недостаточно. X2Go позволяет:
• запускать графические приложения через SSH;
• работать с 3D-рендерингом и тяжелыми GUI;
• использовать несколько параллельных сессий на одном сервере;
• экономить трафик.

1. Установите X2Go Server и XFCE на сервер:

```sh
sudo apt update
sudo apt install -y x2goserver x2goserver-xsession
sudo apt install -y xfce4 xfce4-goodies
```

2. Настройте пользователей:

```sh
sudo useradd -m -s /bin/bash engineer1
sudo passwd engineer1
```

3. Создайте конфигурационный файл x2goagent.options в каталоге /etc/x2go/ и добавьте в него код:

```sh
# Разрешите аппаратное ускорение
USE_XVFB = no
ENABLE_3D = yes
# Разрешите запуск CAD-приложений
NX_COMPRESSION = 0
NX_IMAGE_CACHE = 50
NX_SHM_DISABLE = no
```

4. Настройте лимиты для ресурсоемких задач:
a. Откройте конфигурационный файл на запись:

```sh
sudo nano /etc/security/limits.conf
```

b. Добавьте в конец файла код:

```sh
engineer1 hard memlock unlimited
engineer1 soft memlock unlimited
engineer1 hard nofile 1000000
engineer1 soft nofile 50000
engineer1 hard rtprio 99 # Для реального времени
```

5. Установите графические драйверы:

```sh
sudo apt install -y nvidia-driver-535-server nvidia-utils-535-server nvidia-fabricmanager-535
sudo apt install linux-headers-5.15.0-94-generic
sudo reboot
sudo systemctl enable nvidia-fabricmanager
sudo systemctl start nvidia-fabricmanager
nvidia-smi
nvidia-smi nvlink -m
```

6. Настройте X2Go на устройстве разработчика
1. Установите клиент:
Windows   Linux   MacOS
Скачайте клиент с официального сайта.
2. Создайте подключение:
• Host — публичный IP-адрес сервера.
• Login — engineer1.
• Session Type — XFCE.
• Port — 22 (SSH).
3. Укажите дополнительные настройки:

[Connection]
# Аппаратное ускорение
use_gfx=yes
glx_glx=yes # Для OpenGL
[Media]
# Для 3D-приложений
enable3d=true
printing=no

Сервер готов к работе над приложением.