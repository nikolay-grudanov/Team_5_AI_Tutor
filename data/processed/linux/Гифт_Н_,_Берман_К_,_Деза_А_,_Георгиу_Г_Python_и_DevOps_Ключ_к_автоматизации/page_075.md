---
source_image: page_075.png
page_number: 75
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.82
tokens: 7411
characters: 1646
timestamp: 2025-12-24T03:02:50.022989
finish_reason: stop
---

Одна из утилит, предназначенных для автоматизации настройки программного обеспечения, его развертывания и управления им, — Ansible. Для описания автоматизируемых действий в Ansible применяют так называемые сборники сценариев (playbooks) в формате YAML:

---
- hosts: webservers
  vars:
    http_port: 80
    max_clients: 200
  remote_user: root
  tasks:
  - name: ensure apache is at the latest version
    yum:
      name: httpd
      state: latest
...

Для синтаксического разбора YAML в Python чаще всего используется библиотека PyYAML. Она не входит в стандартную библиотеку Python, но ее можно установить с помощью pip:

$ pip install PyYAML

После установки можно импортировать и экспорттировать данные в формате YAML с помощью PyYAML аналогично тому, как мы делали с JSON:

In [18]: import yaml

In [19]: with open('verify-apache.yml', 'r') as opened_file:
    ...:     verify_apache = yaml.safe_load(opened_file)
    ...:

Данные при этом загружаются в уже привычные для нас структуры данных Python (список, содержащий ассоциативный массив):

In [20]: pprint(verify_apache)
[{'handlers': [{'name': 'restart apache',
    'service': {'name': 'httpd', 'state': 'restarted'}]},
  'hosts': 'webservers',
  'remote_user': 'root',
  'tasks': [{'name': 'ensure apache is at the latest version',
    'yum': {'name': 'httpd', 'state': 'latest'}},
    {'name': 'write the apache config file',
      'notify': ['restart apache'],
      'template': {'dest': '/etc/httpd.conf', 'src': '/srv/httpd.j2'}},
    {'name': 'ensure apache is running',
      'service': {'name': 'httpd', 'state': 'started'}}],
  'vars': {'http_port': 80, 'max_clients': 200}}]