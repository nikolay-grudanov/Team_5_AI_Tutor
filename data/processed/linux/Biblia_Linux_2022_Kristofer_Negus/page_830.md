---
source_image: page_830.png
page_number: 830
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.06
tokens: 7315
characters: 1397
timestamp: 2025-12-24T05:08:31.373373
finish_reason: stop
---

воспользуйтесь ответами, приведенными в приложении Б (хотя Linux позволяет решать задачи разными способами).

1. Установите Ansible в систему Fedora или RHEL.
2. Добавьте привилегию команды sudo для того аккаунта, который будете использовать для выполнения этих упражнений.
3. Создайте файл Ansible playbook (назовите его my_playbook.yaml), который включает в себя следующее:

---
- name: Create web server
  hosts: localhost
  tasks:
    - name: Install httpd
      yum:
        name: httpd
        state: present

4. Запустите команду ansible-playbook в файле my_playbook.yaml в режиме проверки, чтобы выяснить, нет ли проблем с заполнением playbook (подсказка: есть).
5. Измените файл my_playbook.yaml и повысьте привилегии, чтобы задачи запускались от имени суперпользователя.
6. Запускайте ansible-playbook до тех пор, пока пакет httpd не будет успешно установлен в системе.
7. Измените файл my_playbook.yaml снова, чтобы запустить службу httpd и установить ее так, чтобы она запускалась каждый раз при загрузке системы.
8. Запустите команду ansible, которая проверяет, работает ли служба httpd на хосте localhost.
9. Создайте файл index.html, содержащий текст @Web server is up@, и примените команду ansible, чтобы скопировать этот файл в каталог /var/www/html на хосте localhost.
10. Используйте команду curl для просмотра содержимого файла, который вы только что скопировали на веб-сервер.