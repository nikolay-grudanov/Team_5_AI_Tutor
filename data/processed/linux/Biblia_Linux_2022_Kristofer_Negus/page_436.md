---
source_image: page_436.png
page_number: 436
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.42
tokens: 7450
characters: 1990
timestamp: 2025-12-24T04:57:36.675026
finish_reason: stop
---

alsa-restore.service        static
alsa-store.service         static
anaconda-shell@.service    static
arp-ethers.service         enabled
atd.service                enabled
auditd.service             enabled
avahi-daemon.service       enabled
bluetooth.service          enabled
console-kit-log-system-restart.service   static
console-kit-log-system-start.service     static
console-kit-log-system-stop.service      static
crond.service                 enabled
cups.service                  enabled
...
sshd-keygen.service           enabled
sshd.service enabled
system-setup-keyboard.service enabled
...
134 unit files listed.

Помните, что для службы systemd доступно три варианта состояния: enabled (включен), disabled (отключен) и static (статически включен). Нет необходимости включать состояние disabled, чтобы увидеть, какие службы будут активны. Для этого можно использовать команду grep с параметром -v, как показано в предыдущем примере. Состояние static по умолчанию активно и, значит, должно быть включено в вывод.

Чтобы узнать, запущена ли конкретная служба, задействуйте следующую команду:

# systemctl status cups.service
cups.service – CUPS Scheduler
Loaded: loaded (/lib/systemd/system/cups.service; enabled)
Active: active (running) since Wed 2019-09-18 17:32:27 EDT; 3 days ago
Docs: man:cupsd(8)
Main PID: 874 (cupsd)
Status: "Scheduler is running..."
Tasks: 1 (limit: 12232)
Memory: 3.1M
CGroup: /system.slice/cups.service
└─874 /usr/sbin/cupsd -l

Команда systemctl может использоваться для отображения состояния одной или нескольких служб. В предыдущем примере была выбрана служба печати. Обратите внимание на то, что имя службы — это cups.service. В примере приводится много полезной информации о службе, например, что она включена и активна, а также время ее запуска и идентификатор процесса (PID).

Теперь, когда вы можете проверить состояние служб и узнать что-то о них, необходимо научиться выполнять запуск, остановку и перезагрузку служб на вашем сервере Linux.