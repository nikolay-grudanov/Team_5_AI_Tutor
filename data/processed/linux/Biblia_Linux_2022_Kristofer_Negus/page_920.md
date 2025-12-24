---
source_image: page_920.png
page_number: 920
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.75
tokens: 7334
characters: 1391
timestamp: 2025-12-24T05:10:47.461727
finish_reason: stop
---

4. Создайте файл метаданных cloud-init под названием meta-data, который включает в себя следующее:

instance-id: myvm
local-hostname: myvm.example.com

5. Создайте файл данных пользователя cloud-init под названием user-data, который включает в себя следующее:

#cloud-config
password: test
chpasswd: {expire: False}

6. Выполните команду genisoimage, чтобы объединить файлы meta-data и user-data и создать файл mydata.iso:

# genisoimage -output mydata.iso -volid cidata \
    -joliet-long -rock user-data meta-data

7. Используйте команду virt-install, чтобы объединить образ виртуальной машины myvm.qcow2 с файлом mydata.iso для создания нового образа виртуальной машины с именем newvm.

# virt-install --import --name newvm \
    --ram 4096 --vcpus 2 \
    --disk path=myvm.qcow2,format=qcow2,bus=virtio \
    --disk path=mydata.iso,device=cdrom \
    --network network=default &

8. Чтобы открыть виртуальную машину newvm с помощью команды virt-viewer, введите следующее:

# virt-viewer newvm

9. Войдите в виртуальную машину newvm с помощью пользователя fedora и пароля test:

Login: fedora
Password: test

Глава 29. Автоматизация приложений и инфраструктуры с помощью системы Ansible

1. Чтобы установить пакет ansible, выполните следующие действия:
   ▪ RHEL 8:

      # subscription-manager repos \
          --enable ansible-2.9-for-rhel-8-x86_64-rpms
      # dnf install ansible -y