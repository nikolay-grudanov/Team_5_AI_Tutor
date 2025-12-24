---
source_image: page_823.png
page_number: 823
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.29
tokens: 7359
characters: 1462
timestamp: 2025-12-24T05:08:14.166913
finish_reason: stop
---

Добывьте эти строки в файл /etc/ansible/hosts, чтобы сделать их доступными при выполнении команд и файлов playbooks в Ansible.
Хотя процедура просто развертывается на множестве хостов в группе ws, две другие группы показывают, как вы можете настроить playbooks для отдельных задач в зависимости от расположения узлов (newyork и houston).

Аутентификация на хостах
Чтобы убедиться, что вы можете получить доступ к каждому хосту из системы Ansible, настройте службу ssh для каждого хоста. Пароль вводить не нужно:

$ ssh joe@host01
Last login: Wed Feb 5 19:28:39 2020 from 192.168.122.208
$ exit

Повторите команду для каждого хоста.

Создание файла playbook
Файл playbook устанавливает и запускает программное обеспечение веб-сервера на хостах, определенных ранее в группе ws. Аналогично, playbook удостоверяется, что программное обеспечение брандмауэра установлено и работает и что порт 80 (http-порт) открыт в брандмауэре, обеспечивая доступ к веб-серверу. Я добавил в файл simple_web.yaml следующее содержимое:

---
- name: Create web server
  hosts: ws
  remote_user: joe
  become_method: sudo
  become: yes
  tasks:
    - name: Install httpd
      yum:
        name: httpd
        state: present
    - name: Check that httpd has started
      service:
        name: httpd
        state: started
    - name: Install firewalld
      yum:
        name: firewalld
        state: present
    - name: Firewall access to https
      firewalld:
        service: http