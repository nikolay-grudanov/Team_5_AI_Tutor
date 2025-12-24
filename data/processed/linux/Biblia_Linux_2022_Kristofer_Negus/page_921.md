---
source_image: page_921.png
page_number: 921
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 13.84
tokens: 7254
characters: 1254
timestamp: 2025-12-24T05:10:47.315993
finish_reason: stop
---

Fedora:
# dnf install ansible -y

Ubuntu:
$ sudo apt update
$ sudo apt install software-properties-common
$ sudo apt-add-repository --yes --update ppa:ansible/ansible
$ sudo apt install ansible

2. Чтобы добавить привилегии sudo для пользователя, выполняющего команды Ansible, запустите команду visudo и создайте запись, аналогичную следующей (измените joe на нужное имя пользователя):
joe    ALL=(ALL)        NOPASSWD: ALL

3. Откройте файл my_playbook.yaml и добавьте к нему следующее:
---
- name: Create web server
  hosts: localhost
  tasks:
  - name: Install httpd
    yum:
      name: httpd
      state: present

4. Чтобы запустить файл my_playbook.yaml в режиме проверки, выполните следующую команду (она не будет выполнена, потому что у пользователя нет прав на установку пакета):
$ ansible-playbook -C my_playbook.yaml
...
TASK [Install httpd]
*******************************
fatal: [localhost]: FAILED! => {"changed": false, "msg": "This command has to be run under the root user.", "results": []}
...

5. Внесите в файл my_playbook.yaml следующие изменения:
---
- name: Create web server
  hosts: localhost
  become: yes
  become_method: sudo
  become_user: root
  tasks:
  - name: Install httpd
    yum:
      name: httpd
      state: present