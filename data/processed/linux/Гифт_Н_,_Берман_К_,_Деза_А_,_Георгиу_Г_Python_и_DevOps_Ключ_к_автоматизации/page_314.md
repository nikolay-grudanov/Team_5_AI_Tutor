---
source_image: page_314.png
page_number: 314
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.41
tokens: 7363
characters: 1695
timestamp: 2025-12-24T03:09:04.084756
finish_reason: stop
---

котором описывается желаемое итоговое состояние, с возможностями настоящего языка программирования.

При задействовании же библиотек автоматизации AWS наподобие Boto в создаваемом коде как описываются, так и выделяются отдельные ресурсы AWS. Никакого общего эскиза/состояния нет, а значит, необходимо самостоятельно отслеживать все выделяемые ресурсы и координировать их создание и удаление. Такой подход к утилитам автоматизации является императивным (процедурным). Но при нем все равно сохраняется преимущество в виде возможности написания кода Python.

Для использования Pulumi необходимо создать бесплатную учетную запись на веб-сайте pulumi.io. После этого можно установить утилиту командной строки на своей локальной машине. На компьютерах Macintosh для установки Pulumi можно применить Homebrew.

Первая команда, которую необходимо выполнить локально, — pulumi login:

$ pulumi login
Logged into pulumi.com as griggheo (https://app.pulumi.com/griggheo)

Создание нового проекта Pulumi на Python для AWS

Создаем каталог proj1, выполняем в нем команду pulumi new и выбираем шаблон aws-python. В процессе создания проекта pulumi запрашивает название стека. Назовем его staging:

$ mkdir proj1
$ cd proj1
$ pulumi new
Please choose a template: aws-python      A minimal AWS Python Pulumi program
This command will walk you through creating a new Pulumi project.

Enter a value or leave blank to accept the (default), and press <ENTER>.
Press ^C at any time to quit.

project name: (proj1)
project description: (A minimal AWS Python Pulumi program)
Created project 'proj1'

stack name: (dev) staging
Created stack 'staging'

aws:region: The AWS region to deploy into: (us-east-1)
Saved config