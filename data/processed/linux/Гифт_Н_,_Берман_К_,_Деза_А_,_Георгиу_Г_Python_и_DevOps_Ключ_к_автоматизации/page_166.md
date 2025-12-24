---
source_image: page_166.png
page_number: 166
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.03
tokens: 7667
characters: 2200
timestamp: 2025-12-24T03:05:23.048173
finish_reason: stop
---

экспериментов, причем даже с включенной по умолчанию автоматической индексацией! Перейдите в каталог pypi, в котором находится пакет hello-world, и запустите встроенный веб-сервер:

$ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...

В новом окне терминала создайте временную виртуальную среду для установки пакета hello-world из локального экземпляра PyPI. Активируйте ее и, наконец, попробуйте установить пакет, указав в команде pip свой локальный URL:

$ python3 -m venv /tmp/local-pypi
$ source /tmp/local-pypi/bin/activate
(local-pypi) $ pip install -i http://localhost:8000/ hello-world
Looking in indexes: http://localhost:8000/
Collecting hello-world
  Downloading http://localhost:8000/hello-world/hello-world-0.0.1.tar.gz
Building wheels for collected packages: hello-world
  Building wheel for hello-world (setup.py) ... done
Successfully built hello-world
Installing collected packages: hello-world
Successfully installed hello-world-0.0.1

В сеансе, где запущен модуль http.server, при этом должны появиться записи журнала, отображающие все выполненные программой установки для извлечения пакета hello-world, и запросы:

Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
127.0.0.1 [09:58:37] "GET / HTTP/1.1" 200 -
127.0.0.1 [09:59:39] "GET /hello-world/ HTTP/1.1" 200 -
127.0.0.1 [09:59:39] "GET /hello-world/hello-world-0.0.1.tar.gz HTTP/1.1" 200

Для находящейся в промышленной эксплуатации среды понадобится более мощный веб-сервер. Для простоты в этом примере мы воспользовались модулем http.server, но он не умеет обрабатывать одновременно несколько запросов и плохо масштабируется.

При создании локального каталога пакетов без утилит наподобие devpi имеет смысл задействовать подробную спецификацию, включающую описания стандартных названий для структуры каталогов. Ее вы можете найти в PEP 503 (https://oreil.ly/sRcAe).

Создание пакетов для Debian

Если вы рассчитываете устанавливать свой проект в операционной системе Debian (или основанных на Debian дистрибутивах, например Ubuntu), понадобятся дополнительные файлы. Понимание того, какие файлы нужны и как они используются инструментами создания пакетов для Debian, значительно