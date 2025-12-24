---
source_image: page_433.png
page_number: 433
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.99
tokens: 7531
characters: 2172
timestamp: 2025-12-24T04:57:36.493198
finish_reason: stop
---

lrwxrwxrwx. 1 root root 17 Apr 9 04:25 /lib/systemd/system/runlevel4.target
    -> multi-user.target
lrwxrwxrwx. 1 root root 16 Apr 9 04:25 /lib/systemd/system/runlevel5.target
    -> graphical.target
lrwxrwxrwx. 1 root root 13 Apr 9 04:25 /lib/systemd/system/runlevel6.target
    -> reboot.target

Файл /etc/inittab все еще существует, но содержит только комментарии, указывающие на то, что он не используется, а лишь передает базовую информацию в systemd. Файл /etc/inittab больше не имеет истинного функционального применения. Далее приведен пример файла /etc/inittab на сервере Linux, задействующем systemd:

# cat /etc/inittab
# inittab is no longer used.
#
# ADDING CONFIGURATION HERE WILL HAVE NO EFFECT ON YOUR SYSTEM.
#
# Ctrl-Alt-Delete is handled by
# /etc/systemd/system/ctrl-alt-del.target
#
# systemd uses 'targets' instead of runlevels.
# By default, there are two main targets:
#
# multi-user.target: analogous to runlevel 3
# graphical.target: analogous to runlevel 5
#
# To view current default target, run:
# systemctl get-default
#
# To set a default target, run:
# systemctl set-default TARGET.target

В файле /etc/inittab объясняется, что, если вы хотите получить что-то похожее на классический уровень выполнения 3 или 5 в качестве уровня по умолчанию, нужно запустить команду systemctl default.target и установить нужный уровень выполнения. Чтобы проверить, с чем default.target в данный момент символически связан (или, используя устаревшие термины, проверить уровень выполнения по умолчанию), примените команду, показанную далее. Видно, что на этом сервере Linux по умолчанию запускается на уровне выполнения 3:

# ls -l /etc/systemd/system/default.target
lrwxrwxrwx. 1 root root 36 Mar 13 17:27
    /etc/systemd/system/default.target ->
        /lib/systemd/system/runlevel3.target

По-прежнему доступна возможность переключения уровней выполнения с помощью команды init или telinit. Любая из этих команд преобразуется в запрос активизации целевого юнита systemd. Поэтому, введя команду init 3 в командной строке, в действительности вы получите команду systemctl isolate multi-user.target. Кроме того, все еще можно использовать команду runlevel