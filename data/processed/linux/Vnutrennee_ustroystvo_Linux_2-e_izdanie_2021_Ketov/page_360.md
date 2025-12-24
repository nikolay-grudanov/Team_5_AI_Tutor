---
source_image: page_360.png
page_number: 360
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.33
tokens: 7555
characters: 2129
timestamp: 2025-12-24T04:42:35.298771
finish_reason: stop
---

создаются и управляются службой Docker для ограничения контейнеров в доступных им ресурсах (в данной иерархии — для ограничения в использовании оперативной памяти). Остальные группы в тех же целях созданы службой systemd, заведующей запуском и остановом всех служб операционной системы и пользовательских сеансов (см. разд. 10.3). В группе docker создана всего одна подгруппа ①, совпадающая с UUID контейнера, создание которого иллюстрировалось в листинге 9.11, а в самой группе находится ③ всего один процесс PID = 22358, при этом группе не назначены ни мягкое, ни жесткое ограничения ④ по памяти, при этом группа потребила ⑤ порядка 31 Мб памяти.

Листинг 9.13. Использование групп управления для собственных нужд

① rick@ubuntu:~ $ ps o pid,cgroup:512,cmd p $$

PID CGROUP CMD
23746 ...,3:cpu,cpuacct:/user.slice,... -bash

② rick@ubuntu:~ $ sudo mkdir /sys/fs/cgroup/cpu,cpuacct/mygroup

③ rick@ubuntu:~ $ echo $$ | sudo tee /sys/fs/cgroup/cpu,cpuacct/mygroup/tasks
rick@ubuntu:~ $ cat /sys/fs/cgroup/cpu,cpuacct/mygroup/tasks
23746
★ 25110

rick@ubuntu:~ $ ps o pid,cgroup:512,cmd p $$

PID CGROUP CMD
23746 ...,3:cpu,cpuacct:/mygroup,... -bash
rick@ubuntu:~ $ ls /sys/fs/cgroup/cpu,cpuacct/mygroup/cpu.*
/sys/fs/cgroup/cpu,cpuacct/mygroup/cpu.cfs_period_us
/sys/fs/cgroup/cpu,cpuacct/mygroup/cpu.shares
/sys/fs/cgroup/cpu,cpuacct/mygroup/cpu.cfs_quota_us
/sys/fs/cgroup/cpu,cpuacct/mygroup/cpu.stat
rick@ubuntu:~ $ cat /sys/fs/cgroup/cpu,cpuacct/mygroup/cpu.shares
1024
④ rick@ubuntu:~ $ echo 256 | sudo tee /sys/fs/cgroup/cpu,cpuacct/mygroup/cpu.shares

В листинге 9.13 проиллюстрирована процедура создания группы, помещения в нее процесса и накладывания ограничений на использование центрального процессора. Утилита ps(1) умеет ① показывать членство процессов в группах управления, хотя и делает это не очень удобным образом. Оказывается, что по умолчанию systemd(1) (и его напарник systemd-logind(8)) размещают интерактивные пользовательские процессы в группах с названием user.slice, что, например, удобно использовать для

1 На самом деле они «как бы» назначены, но кого сможет ограничить 8 Эйб (экзабайт, \(2^{60}\))?