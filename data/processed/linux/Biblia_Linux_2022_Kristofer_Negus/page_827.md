---
source_image: page_827.png
page_number: 827
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.35
tokens: 7426
characters: 1816
timestamp: 2025-12-24T05:08:24.160064
finish_reason: stop
---

Как и при запуске playbook, выполнение специальных ad-hoc-команд фокусируется на достижении желаемого состояния. Команда ad-hoc принимает задачу, выясняет, что запрашивается, и делает то, что нужно, чтобы достичь запрошенного состояния. Чтобы опробовать работу таких команд в Ansible, задействуйте файл inventory ws, созданный ранее.

Примеры использования команд ad-hoc

Запуская команду ad-hoc, вы выполняете действия с помощью модуля Ansible. Командный модуль применяется по умолчанию, если не указан другой модуль. Используя модуль, вы указываете, какие команды и параметры нужно запустить на группе узлов в качестве одноразового действия.
Проверьте, что файл inventory запущен и работает. В примере видно, что в файле inventory ws все хосты работают:

$ ansible ws -u joe -m ping
host03 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    },
    "changed": false,
    "ping": "pong"
}
host02 | SUCCESS => { ... }
host01 | SUCCESS => { ... }

Вы можете узнать, работает ли служба httpd на хостах в inventory, проверив состояние этой службы с помощью команды ansible следующим образом:

$ ansible ws -u joe -m service \
    -a "name=httpd state=started" --check
host02 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    },
    "changed": false,
    "name": "httpd",
    "state": "started",
    "status": { ... }
host 01 | SUCCESS => { ... }

В данный момент на веб-серверах нет содержимого. Чтобы добавить файл index.html, содержащий текст Hello from your web server!, для всех хостов в inventory, вы можете запустить следующую команду (введите пароль суперпользователя при появлении запроса):

$ echo "Hello from your web server!" > index.html
$ ansible ws -m copy -a \
    "src=./index.html dest=/var/www/html/ \