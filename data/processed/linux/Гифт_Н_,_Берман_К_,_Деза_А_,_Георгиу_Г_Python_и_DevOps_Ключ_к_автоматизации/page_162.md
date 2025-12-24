---
source_image: page_162.png
page_number: 162
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.42
tokens: 7421
characters: 1660
timestamp: 2025-12-24T03:05:02.569789
finish_reason: stop
---

Для генерации на его основе дистрибутива исходного кода выполните следующую команду:

python3 setup.py sdist

Результаты ее выполнения должны выглядеть примерно так:

$ python3 setup.py sdist
running sdist
running egg_info
writing hello_world.egg-info/PKG-INFO
writing top-level names to hello_world.egg-info/top_level.txt
writing dependency_links to hello_world.egg-info/dependency_links.txt
reading manifest file 'hello_world.egg-info/SOURCES.txt'
writing manifest file 'hello_world.egg-info/SOURCES.txt'
running check
creating hello-world-0.0.1
creating hello-world-0.0.1/hello_world
creating hello-world-0.0.1/hello_world.egg-info
copying files to hello-world-0.0.1...
copying README -> hello-world-0.0.1
copying setup.py -> hello-world-0.0.1
copying hello_world/__init__.py -> hello-world-0.0.1/hello_world
copying hello_world/main.py -> hello-world-0.0.1/hello_world
Writing hello-world-0.0.1/setup.cfg
Creating tar archive
removing 'hello-world-0.0.1' (and everything under it)

В каталоге верхнего уровня проекта появился новый каталог dist, он содержит дистрибутив исходного кода — файл hello-world-0.0.1.tar.gz. Если мы взглянем на структуру каталогов, то увидим, что она изменилась:

hello-world
│   ├── dist
│   │   └── hello-world-0.0.1.tar.gz
│   ├── hello_world
│   │   ├── __init__.py
│   │   └── main.py
│   ├── hello_world.egg-info
│   │   ├── dependency_links.txt
│   │   ├── PKG-INFO
│   │   ├── SOURCES.txt
│   │   └── top_level.txt
│   └── README
│       └── setup.py

3 directories, 9 files

Только что созданный файл tar.gz представляет собой пакет, который можно установить! Теперь его можно загрузить на PyPI, чтобы пользователи могли