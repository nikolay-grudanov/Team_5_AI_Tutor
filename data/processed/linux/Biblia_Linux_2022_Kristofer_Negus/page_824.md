---
source_image: page_824.png
page_number: 824
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.66
tokens: 7486
characters: 1999
timestamp: 2025-12-24T05:08:24.576026
finish_reason: stop
---

permanent: yes
state: enabled
- name: Restart the firewalld service to load in the firewall changes
  service:
    name: firewalld
    state: restarted

Три дефиса в начале файла playbook — simple_web.yaml — указывают на начало содержимого YAML в нем. Рассмотрим остальные части файла.

● name. Скрипт play называется Create web server.
● hosts. Применяет этот файл inventory к хостам в группе ws.
● remote_user. Аккаунт обычного пользователя, который используется для аутентификации во всех удаленных системах. Это делается для того, чтобы обезопасить систему и не позволить корневой вход в удаленную систему.
● become. Включение этой функции (yes) дает команду Ansible стать другим пользователем, не remote_user, для запуска модулей в задаче.
● become_method. Выбирает функцию, которую нужно применить, чтобы расширить привилегии (sudo).
● become_user. Устанавливает, какой пользователь должен пройти аутентификацию (root).
● tasks. Запускает раздел, содержащий задачи.
● name. Название, данное задаче. В первом случае это Install httpd, затем Check that httpd has started и т. д. Следующая строка начинается с имени модуля (yum service firewalld и т. д.).

Модуль yum говорит системе, что нужно проверить, есть ли пакет httpd (present), а если нет, то установить его.
service проверяет, работает ли демон httpd (started). Если служба httpd не запущена, Ansible запускает ее.
Модуль yum говорит системе, что нужно проверить, есть ли пакет firewalld (present), а если нет, то установить его.
firewalld делает порт для службы http (TCP 80) доступным (enabled) и постоянным (permanent: yes) через брандмауэр.
Модуль service перезапускает службу firewalld (restarted), чтобы включить доступ к новому порту брандмауэра службы http.

Запуск файла playbook

Используйте команду ansible-playbook для запуска playbook. Чтобы протестировать playbook перед запуском в реальном времени, примените параметр -c. Чтобы увидеть больше деталей в выводе (по крайней мере пока тестируете файл), добавьте параметр -v.