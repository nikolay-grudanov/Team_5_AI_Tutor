---
source_image: page_445.png
page_number: 445
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.02
tokens: 7461
characters: 1976
timestamp: 2025-12-24T04:57:59.568873
finish_reason: stop
---

Для демона systemd целевые юниты относятся к группам служб, которые должны быть запущены. Далее показаны различные целевые юниты, которые можно сделать постоянными, а также их обратно совместимые целевые юниты, подходящие для уровня выполнения:

● multi-user.target =;
   ▪ runlevel2.target;
   ▪ runlevel3.target;
   ▪ runlevel4.target;
● graphical.target = runlevel5.target.

Постоянный целевой юнит устанавливается с помощью символической ссылки на файл default.target unit. Рассмотрим следующий пример:

# ls -l /etc/systemd/system/default.target
lrwxrwxrwx. 1 root root 36 Mar 13 17:27
    /etc/systemd/system/default.target -> /lib/systemd/system/runlevel5.target
# ls -l /lib/systemd/system/runlevel5.target
lrwxrwxrwx. 1 root root 16 Mar 27 15:39
    /lib/systemd/system/runlevel5.target -> graphical.target

Здесь видно, что текущим постоянным целевым юнитом на этом сервере является runlevel5.target, поскольку default.targe — это символическая ссылка на файл юнита runlevel5.target. Но обратите внимание на то, что runlevel5.target также является символической ссылкой и указывает на graphical.target. Таким образом, текущий постоянный целевой юнит этого сервера — graphical.target.

Чтобы сделать другой целевой юнит постоянным, нужно просто изменить символическую ссылку на default.target.

Последовательно придерживайтесь целевых юнитов уровня выполнения, если они используются на вашем сервере. В следующем примере команда systemctl изменяет постоянный целевой юнит сервера с graphical.target на multi-user.target:

# systemctl get-default
graphical.target
#
    systemctl set-default runlevel3.target
    Removed /etc/systemd/system/default.target.
    Created symlink /etc/systemd/system/default.target → /usr/lib/systemd/system/multi-user.target.
# systemctl get-default
    multi-user.target

Когда сервер перезагружается, multi-user.target становится постоянным целевым юнитом. В это время все службы в юните multi-user.target запускаются (активизируются).