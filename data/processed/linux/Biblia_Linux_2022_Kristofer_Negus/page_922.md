---
source_image: page_922.png
page_number: 922
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.52
tokens: 7328
characters: 1605
timestamp: 2025-12-24T05:10:48.095159
finish_reason: stop
---

6. Чтобы запустить файл my_playbook снова и установить пакет httpd, введите следующее:

$ ansible-playbook my_playbook.yaml
...
TASK [Install httpd] *******************************************************
changed: [localhost]
PLAY RECAP *******************************************************
localhost: ok=2 changed=1 unreachable=0 failed=0 skipped=0 rescued=0 ignored=0

7. Чтобы запустить службу httpd и установить ее так, чтобы она запускалась каждый раз при загрузке системы, измените файл my_playbook.yaml следующим образом:

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
    - name: start httpd
      service:
        name: httpd
        state: started

8. Чтобы выполнить команду ansible так, чтобы она проверяла, находится ли служба httpd на localhost, введите:

$ ansible localhost -m service \
    -a "name=httpd state=started" --check
localhost | SUCCESS => {
    "changed": false,
    "name": "httpd",
    "state": "started",
    "status": { ...

9. Чтобы создать в текущем каталоге файл index.html с текстом Web server is up, который запускает команду ansible для копирования этого файла в каталог /var/www/html на localhost, выполните следующие действия (замените joe нужным именем пользователя):

$ echo "Web server is up" > index.html
$ ansible localhost
  -m copy -a \
    "src=./index.html dest=/var/www/html/ \
    owner=apache group=apache mode=0644" \
    -b --user joe --become-user root --become-method sudo
host01 | CHANGED => { ...