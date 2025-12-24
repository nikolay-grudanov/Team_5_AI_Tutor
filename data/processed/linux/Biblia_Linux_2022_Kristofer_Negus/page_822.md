---
source_image: page_822.png
page_number: 822
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.81
tokens: 7324
characters: 1448
timestamp: 2025-12-24T05:08:12.494962
finish_reason: stop
---

Установка системы Ansible

Пакеты программного обеспечения Ansible доступны для RHEL, Fedora, Ubuntu и других дистрибутивов Linux. Поскольку файлы playbooks Ansible запускаются с управляющего узла, нет необходимости устанавливать программное обеспечение Ansible на других узлах, с которыми будет работать система.

Итак, начнем с установки пакета ansible на RHEL, Fedora, Ubuntu или другой системе Linux, которую вы хотите использовать в качестве контрольного узла. Этот узел должен иметь возможность подключаться к службе SSH, работающей на узлах хоста, на которых вы хотите осуществить развертывание.

Установите пакет ansible одним из следующих способов.

● В дистрибутиве RHEL 8:

# subscription-manager repos \
    --enable ansible-2.9-for-rhel-8-x86_64-rpms
# dnf install ansible -y

● В дистрибутиве Fedora:

# dnf install ansible -y

● В дистрибутиве Ubuntu:

$ sudo apt update
$ sudo apt install software-properties-common
$ sudo apt-add-repository --yes --update ppa:ansible/ansible
$ sudo apt install ansible

Установив Ansible, можно создавать файлы inventories, которые предоставляют целевые объекты для файлов playbooks.

Создание файлов inventories

Простой файл inventory может состоять из имени, представляющего цель для файла playbook, и хост-систем, связанных с этим именем. Для начала приведу пример inventory, который содержит три группы статических хостов:

[ws]
host01
host02
host03

[newyork]
host01

[houston]
host02
host03