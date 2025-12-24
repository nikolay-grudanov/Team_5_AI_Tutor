---
source_image: page_825.png
page_number: 825
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.69
tokens: 7537
characters: 2329
timestamp: 2025-12-24T05:08:28.679090
finish_reason: stop
---

Имейте в виду: если вы запускаете playbook с параметром -C, нельзя полностью протестировать файл, чтобы убедиться в его корректности. Причина в следующем: более позднее действие может потребовать, чтобы более раннее действие завершилось, прежде чем он может быть выполнен. В этом примере пакет httpd должен быть установлен до запуска службы httpd.

Вот пример запуска Ansible playbook с подробным выводом:

$ ansible-playbook -v simple_web.yaml
Using /etc/ansible/ansible.cfg as config file

PLAY [Create web server] *******************************************************

TASK [Gathering Facts] *******************************************************
ok: [host03]
ok: [host02]
ok: [host01]

TASK [Install httpd] *******************************************************
changed: [host01] => {"changed": true, "msg": "", "rc": 0,
    "results": ["Installed: httpd", ...]
changed: [host02] => {"changed": true, "msg": "", "rc": 0,
    "results": ["Installed: httpd", ...]
changed: [host03] => {"changed": true, "msg": "", "rc": 0,
    "results": ["Installed: httpd", ...

TASK [Check that httpd has started] ******************************************
changed: [host03] => {"changed": true, "name": "httpd",
    "state": "started", "status":
changed: [host02] => {"changed": true, "name": "httpd",
    "state": "started", "status": ...
changed: [host01] => {"changed": true, "name": "httpd",
    "state": "started", "status": ...
...
TASK [Install firewalld]*******************************************************
changed: [host03] => {"changed": true, "msg": "", "rc": 0, "results":
    ["Installed: firewalld", "Installed: python3-decorator...
changed: [host02] => {"changed": true, "msg": "", "rc": 0, "results":
    ["Installed: firewalld", "Installed: python3-decorator...
changed: [host01] => {"changed": true, "msg": "", "rc": 0, "results":
    ["Installed: firewalld"...

TASK [Firewall access to https]**********************************************
ok: [host03] => {"changed": false, "msg": "Permanent operation,
    (offline operation: only on-disk configs were altered)"}
ok: [host02] => {"changed": false, "msg": "Permanent operation,
    (offline operation: only on-disk configs were altered)"}
ok: [host01] => {"changed": false, "msg": "Permanent operation,
    (offline operation: only on-disk configs were altered)"}