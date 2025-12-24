---
source_image: page_891.png
page_number: 891
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.58
tokens: 7502
characters: 2122
timestamp: 2025-12-24T05:10:09.637069
finish_reason: stop
---

б) если после выполнения предыдущего пункта положительного результата не получено, выполните следующую команду для демона SysVinit init. Здесь положительный результат, как и отрицательные результаты предыдущих тестов, означает, что служба sshd все еще использует демон SysVinit:

# service ssh status
sshd (pid 2390) is running...

3. Чтобы определить предыдущий и текущий уровни выполнения вашего сервера, введите команду runlevel. Она по-прежнему работает на всех демонах init:

$ runlevel
N 3

4. Чтобы изменить уровень выполнения по умолчанию или целевой юнит на своем сервере Linux, реализуйте одно из следующих действий (в зависимости от демона init):
а) для SysVinit отредактируйте файл /etc/inittab и замените # в строке id:#:initdefault: на 2, 3, 4 или 5;
б) для systemd измените значение default.target на необходимый уровень выполнения runlevel1#.target, где значение # равно 2, 3, 4 или 5. Далее показано, как изменить целевой юнит на runlevel3.target:

# systemctl set-default runlevel3.target
Removed /etc/systemd/system/default.target.
Created symlink /etc/systemd/system/default.target → /usr/lib/systemd/system/multi-user.target.

5. Чтобы перечислить службы, запущенные (или активные) на вашем сервере, нужно использовать различные команды в зависимости от демона инициализации:
а) для SysVinit — команду service, как показано в этом примере:

# service --status-all | grep running | sort
anacron (pid 2162) is running...
atd (pid 2172) is running...

б) для systemd — команду systemctl следующим образом:

# systemctl list-unit-files --type=service | grep -v disabled
UNIT FILE                                 STATE
abrt-ccpp.service                         enabled
abrt-oops.service                         enabled
...

6. Чтобы перечислить запущенные (или активные) службы на вашем сервере Linux, используйте соответствующую команду (команды) из ответа 5 для своего демона инициализации.

7. Для каждого демона инициализации текущее состояние конкретной службы показывают следующие команды:
а) для SysVinit — команда service service_name status;
б) для systemd — команды systemctl status service_name.