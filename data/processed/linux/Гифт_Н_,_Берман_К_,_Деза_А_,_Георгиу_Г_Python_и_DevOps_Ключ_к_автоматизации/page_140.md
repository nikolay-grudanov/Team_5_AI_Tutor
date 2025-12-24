---
source_image: page_140.png
page_number: 140
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.59
tokens: 7437
characters: 1682
timestamp: 2025-12-24T03:04:29.502460
finish_reason: stop
---

Настойка командной оболочки Python под свои нужды

Вы можете настроить командную оболочку Python под свои нужды с помощью пакета helpers и импортировать полезные модули в файл Python, а затем экспортить его в виде переменной среды. Я храню свои файлы конфигурации в репозитории dotfiles, так что в файле конфигурации командной оболочки (в моем случае $HOME/.zshrc) я написал такой оператор экспорта:

export PYTHONSTARTUP=$HOME/dotfiles/pythonstartup.py

Чтобы поэкспериментировать с этим, создайте новый файл Python с названием pythonstartup.py (хотя название может быть любым) со следующим содержимым:

import types
import uuid

helpers = types.ModuleType('helpers')
helpers.uuid4 = uuid.uuid4()

Теперь откройте новую командную оболочку Python, указав только что созданный файл pythonstartup.py:

$ PYTHONSTARTUP=pythonstartup.py python
Python 3.7.3 (default, Apr  3 2019, 06:39:12)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> helpers
<module 'helpers'>
>>> helpers.uuid4()
UUID('966d7dbe-7835-4ac7-bbbf-06bf33db5302')

Сразу же становится доступен объект helpers. А к добавленному свойству uuid4 можно обращаться как helpers.uuid4(). Как вы, наверное, догадались, все импорты и определения становятся доступны в командной оболочке Python. Такой способ расширения поведения очень удобен при использовании командной оболочки по умолчанию.

Рекурсивные подстановки

Рекурсивная подстановка включена в ZSH по умолчанию, но Bash (версии 4 и выше) требует использования встроенной команды shopt для ее включения. Рекурсивная подстановка — удобная возможность, позволяющая обходить пути с помощью следующего синтаксиса:

$ ls **/*.py