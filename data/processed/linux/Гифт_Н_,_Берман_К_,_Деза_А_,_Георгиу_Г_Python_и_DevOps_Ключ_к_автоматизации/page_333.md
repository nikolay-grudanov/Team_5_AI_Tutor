---
source_image: page_333.png
page_number: 333
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 45.68
tokens: 7843
characters: 2237
timestamp: 2025-12-24T03:09:54.266460
finish_reason: stop
---

Выполните запрос к URL конечной точки, чтобы проверить работу приложения. Поскольку порт 5000 запущенного внутри контейнера Docker приложения привязан к порту 5000 на локальной машине с помощью флага командной строки -p, можно использовать в качестве конечной точки приложения локальный IP-адрес 127.0.0.1 и порт 5000:

$ curl http://127.0.0.1:5000
Hello, World! (from a Docker container)%

Теперь поменяйте код в app.py, воспользовавшись своим любимым редактором. Поменяйте текст приветствия на Hello, World! (from a Docker container with modified code). Сохраните файл app.py и обратите внимание на примерно такие строки в журнале контейнера Docker:

* Detected change in '/app/app.py', reloading
* Restarting with stat
* Debugger is active!
* Debugger PIN: 647-161-014

Это демонстрирует, что запущенный в контейнере сервер для разработки Flask обнаружил изменение файла app.py и перезагрузил приложение.

Теперь при запросе к конечной точке приложения с помощью утилиты curl будет отображено измененное приветствие:

$ curl http://127.0.0.1:5000
Hello, World! (from a Docker container with modified code)%

Завершить выполнение контейнера можно с помощью команд docker stop или docker kill, указав в качестве аргумента идентификатор контейнера:

$ docker stop c879295baa26
c879295baa26

Удалить образ Docker с локального диска можно с помощью команды docker rmi:

$ docker rmi hello-world-docker
Untagged: hello-world-docker:latest
Deleted: sha256:dbd84c229002950550334224b4b42aba948ce450320a4d8388fa253348126402
Deleted: sha256:6a8f3db7658520a1654cc6abee8eafb463a72ddc3aa25f35ac0c5b1eccdf75cd
Deleted: sha256:aee7c3304ef6ff620956850e0b6e6b1a5a5828b58334c1b82b1a1c21afa8651f
Deleted: sha256:dca8a433d31fa06ab72af63ae23952ff27b702186de8cbea51cdea579f9221e8
Deleted: sha256:cb9d58c66b63059f39d2e70f05916fe466e5c99af919b425aa602091c943d424
Deleted: sha256:f0534bdca48bfed3c772c67489f139d1cab72d44a19c5972ed2cd09151564c1

Эта выведенная информация демонстрирует различные слои файловой системы, из которых состоит образ Docker. При удалении образа удаляются и эти слои. Больше подробностей об использовании Docker слоев файловой системы для сборки образов можно найти в документации по драйверам хранения Docker (https://oreil.ly/wqNve).