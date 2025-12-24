---
source_image: page_828.png
page_number: 828
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.44
tokens: 7550
characters: 1928
timestamp: 2025-12-24T05:08:31.616111
finish_reason: stop
---

owner=apache group=apache mode=0644" \
    -b --user joe --become --ask-become-pass
BECOME password: **********
host01 | CHANGED => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    },
    "changed": true,
    "checksum": "213ae4bb07e9b1e96fbc7fe94de372945a202bee",
    "dest": "/var/www/html/index.html",
    "gid": 48,
    "group": "apache",
    "md5sum": "495feb8ad508648cfacf69681d94f97",
    "mode": "0644",
    "owner": "apache",
    "secontext": "system_u:object_r:httpd_sys_content_t:s0",
    "size": 52,
    "src": "/home/joe/.ansible/tmp/ansible-tmp-1581027374.649223-29961128730253/source",
    "state": "file",
    "uid": 48
}
host02 | CHANGED => { ... }
host03 | CHANGED => { ... }

Из примера видно, что файл index.html создается владельцем apache (UID 48) и группой apache (GID 48) в каталоге /var/www/html на host01. Затем его копия сохраняется на host02 и host03. Проверьте, что все работает, получив доступ к этому файлу с хоста ansible через веб-сервер с помощью команды curl:

$ curl host01
Hello from your web server!

Автоматизация задач с помощью Ansible Tower Automation Framework

Запуск Ansible playbook и команд отлично подходит для автоматизации и последующего изменения наборов хостов, но для создания полностью управляемой структуры можно пойти и дальше. Используя программу Ansible Tower, можно расширить систему развертывания Ansible.

Утилита Ansible Tower предоставляет веб-интерфейс для управления всей вашей ИТ-инфраструктурой с помощью Ansible playbook и других компонентов. Она позволяет сохранить все ресурсы Ansible в одном месте и получать уведомления. Утилита также дает возможность управлять различными административными ролями на предприятии. Интерфейс Ansible Tower позволяет легко и непрерывно обновлять подготовленные ресурсы. Вместо того чтобы запоминать параметры командной строки, вы можете просто нажать кнопку, чтобы настроить и запустить