---
source_image: page_164.png
page_number: 164
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.47
tokens: 7472
characters: 1995
timestamp: 2025-12-24T03:05:08.918207
finish_reason: stop
---

В начале этого раздела мы установили утилиту twine в нашей виртуальной среде. После этого ее можно применять для загрузки пакетов в тестовый экземпляр PyPI. Следующая команда загружает файл tar.gz и запрашивает имя пользователя и пароль:

$ twine upload --repository-url https://test.pypi.org/legacy/ \
    dist/hello-world-0.0.1.tar.gz
Uploading distributions to https://test.pypi.org/legacy/
Enter your username:
Enter your password:

Чтобы проверить, все ли прошло успешно, можем попробовать установить наш пакет с помощью pip:

$ python3 -m pip install --index-url https://test.pypi.org/simple/ hello-world

Может показаться, что в этой команде лишний пробел в URL PyPI, но URL каталога оканчивается на /simple/, а hello-world — еще один аргумент, который указывает название устанавливаемого пакета Python.

Для настоящей промышленной версии необходимо создать учетную запись на основном экземпляре PyPI (https://pypi.org/account/register). Загрузка пакета на настоящий PyPI ничем не отличается от загрузки на тестовый экземпляр, включая проверку.

Более старые руководства по созданию пакетов могут включать следующие команды:

$ python setup.py register
$ python setup.py upload

Эти команды входят в набор утилит setuptools и, возможно, по-прежнему сработают для загрузки проектов в каталог пакетов. Однако в число возможностей утилиты twine входят безопасная аутентификация через HTTPS, а также подпись пакетов с помощью gpg. twine работает даже тогда, когда не работает команда python setup.py upload, и, наконец, позволяет тестировать пакет перед загрузкой в каталог.

Осталось отметить, что иногда удобно создать Makefile и вставить в него команду make для автоматического развертывания проекта и сборки документации. Вот пример того, как это может работать:

deploy-pypi:
    pandoc --from=markdown --to=rst README.md -o README.rst
    python setup.py check --restructuredtext --strict --metadata
    rm -rf dist
    python setup.py sdist
    twine upload dist/*
    rm -f README.rst