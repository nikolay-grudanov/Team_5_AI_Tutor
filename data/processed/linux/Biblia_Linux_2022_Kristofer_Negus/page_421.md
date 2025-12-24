---
source_image: page_421.png
page_number: 421
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.05
tokens: 7516
characters: 1676
timestamp: 2025-12-24T04:57:11.452745
finish_reason: stop
---

Классические демоны init SysVinit и BSD работают схожим образом. Изначально они сильно отличались друг от друга, но со временем существенных различий осталось очень мало. К примеру, более старый демон BSD init раньше получал информацию о конфигурации из файла /etc/ttytab. Теперь, как и SysVinit, демон BSD init берет информацию о конфигурации во время загрузки из файла /etc/inittab. Далее приведен пример классического файла SysVinit /etc/inittab:

# cat /etc/inittab
# inittab This file describes how the INIT process should set up
# Default runlevel. The runlevels used by RHS are:
#   0 - halt (Do NOT set initdefault to this)
#   1 - Single user mode
#   2 - Multiuser, no NFS (Same as 3, if you do not have networking)
#   3 - Full multiuser mode
#   4 - unused
#   5 - X11
#   6 - reboot (Do NOT set initdefault to this)
#
id:5:initdefault:

# System initialization.
si::sysinit:/etc/rc.d/rc.sysinit

l0:0:wait:/etc/rc.d/rc 0
l1:1:wait:/etc/rc.d/rc 1
l2:2:wait:/etc/rc.d/rc 2
l3:3:wait:/etc/rc.d/rc 3
l4:4:wait:/etc/rc.d/rc 4
l5:5:wait:/etc/rc.d/rc 5
l6:6:wait:/etc/rc.d/rc 6

# Trap CTRL-ALT-DELETE
ca::ctrlaltdel:/sbin/shutdown -t3 -r now
pf::powerfail:/sbin/shutdown -f -h +2
"Power Failure; System Shutting Down"

# If power was restored before the shutdown kicked in, cancel it.
pr:12345:powerokwait:/sbin/shutdown -c
"Power Restored; Shutdown Cancelled"

# Run gettys in standard runlevels
1:2345:respawn:/sbin/mingetty tty1
2:2345:respawn:/sbin/mingetty tty2
3:2345:respawn:/sbin/mingetty tty3
4:2345:respawn:/sbin/mingetty tty4
5:2345:respawn:/sbin/mingetty tty5
6:2345:respawn:/sbin/mingetty tty6

# Run xdm in runlevel 5
x:5:respawn:/etc/X11/prefdm -nodaemon