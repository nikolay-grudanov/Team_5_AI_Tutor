---
source_image: page_915.png
page_number: 915
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.18
tokens: 7428
characters: 1634
timestamp: 2025-12-24T05:10:46.147722
finish_reason: stop
---

7. Чтобы сохранить, очистить и восстановить текущие правила брандмауэра системы Linux, выполните следующее:
а) чтобы сохранить текущие правила, введите:
    # iptables-save >/tmp/myiptables
б) чтобы очистить текущие правила, введите:
    # iptables -F
в) чтобы восстановить текущие правила, введите:
    # iptables-restore < /tmp/myiptables

8. Чтобы настроить таблицу фильтров брандмауэра системы Linux для цепочки ввода на политику DROP, введите iptables -P INPUT DROP в командной строке.

9. Чтобы изменить политику таблицы фильтров брандмауэра системы Linux обратно на accept для цепочки ввода, введите следующее:
# iptables -P INPUT ACCEPT

Чтобы добавить правило DROP для всех сетевых пакетов с IP-адреса 10.140.67.23, введите следующее:
# iptables -A INPUT -s 10.140.67.23 -j DROP

10. Чтобы удалить только что добавленное правило, не сбрасывая и не восстанавливая правила брандмауэра системы Linux, введите iptables -D INPUT 1 в командной строке. Предполагается, что правило, которое вы добавили ранее, является правилом 1. Если это не так, измените значение на соответствующий номер правила в команде iptables.

Глава 26. Работа с облаками и контейнерами

1. Чтобы установить и запустить контейнер, используйте либо команду podman (для любой системы RHEL или Fedora), либо команду docker (RHEL 7):
# yum install podman -y
ИЛИ
# yum install docker -y
# systemctl start docker
# systemctl enable docker

2. Используйте команду либо podman, либо docker, чтобы вытащить образ вашего хоста registry.access.redhat.com/ubi7/ubi:
# podman pull registry.access.redhat.com/ubi7/ubi
ИЛИ
# docker pull registry.access.redhat.com/ubi7/ubi