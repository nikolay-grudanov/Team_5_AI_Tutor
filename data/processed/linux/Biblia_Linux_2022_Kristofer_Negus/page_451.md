---
source_image: page_451.png
page_number: 451
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.85
tokens: 7559
characters: 2150
timestamp: 2025-12-24T04:58:11.545212
finish_reason: stop
---

abrt-vmcore.service    lldpad.service    sm-client.service
atd.service            mcelog.service    sshd-keygen.service
auditd.service         mdmonitor.service sshd.service
...
# ls -l /etc/systemd/system/multi-user.target.wants
total 0
lrwxrwxrwx. 1 root root 37 Nov 2 22:29 abrt-ccpp.service ->
    /lib/systemd/system/abrt-ccpp.service
lrwxrwxrwx. 1 root root 33 Nov 2 22:29 abrtd.service ->
    /lib/systemd/system/abrtd.service
...
lrwxrwxrwx. 1 root root 32 Apr 26 20:05 sshd.service ->
    /lib/systemd/system/sshd.service

Далее представлен процесс добавления файла символической ссылки для My_New_Service:

# ln -s /etc/systemd/system/My_New_Service.service
/etc/systemd/system/multi-user.target.wants/My_New_Service.service

Символическая ссылка создается в каталоге multi-user.target.wants. Теперь новая служба My_New_Service активизируется (запускается) при активизации юнита multi-user.target.

СОВЕТ
Если вы хотите изменить целевой юнит systemd для службы, необходимо изменить символическую ссылку так, чтобы она указывала на новое целевое местоположение каталога Wants. Примените команду ln -sf, чтобы принудительно разорвать любую текущую символическую ссылку и принудительно назначить новую.

Приведенные ранее шаги добавят новую или пользовательскую службу на сервер Linux systemd. Помните, что новая служба не запустится до перезагрузки сервера. Чтобы запустить новую службу перед перезагрузкой, задействуйте команды, рассмотренные в подразделе «Остановка и запуск служб».

Резюме
Способ запуска и остановки служб зависит от того, какой демон инициализации применяет ваш Linux-сервер: SysVinit, Upstart или Systemd. Прежде чем приступить к управлению службами, обязательно воспользуйтесь примерами из этой главы, чтобы определить демон инициализации вашего Linux-сервера.
Принципы запуска и остановки служб сочетаются с другими принципами управления службами, такими как: создание постоянных служб, запуск определенных служб во время загрузки сервера, перезагрузка службы и перезапуск службы. Понимание этого очень полезно, поскольку в следующей главе мы будем рассматривать процесс настройки сервера печати Linux и управления им.