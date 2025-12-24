---
source_image: page_135.png
page_number: 135
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.54
tokens: 7288
characters: 1480
timestamp: 2025-12-24T04:35:40.547630
finish_reason: stop
---

В примере из листинга 4.18 показано дерево процессов, построенное при помощи специальной команды pstree(1), а в листинге 4.19 — «классическое» представление дерева процессов при помощи команды ps(1).

Листинг 4.18. Дерево процессов

fitz@ubuntu:~$ pstree -cnAhT
systemd--+-systemd-journal
    |---systemd-udevd
    |---systemd-resolve
    |---rsyslogd
        |---gdm3---gdm-session-wor---gdm-session-wor
        |         |---gdm-x-session---Xorg
        |         |         `---gnome-session-b
        |---systemd---(sd-pam)
        |         |---gnome-terminal---bash---man---pager
        |         |         `---bash
        |---postgres---postgres
        |         |---postgres
        |         |---postgres
        |         |---postgres
        |         |---postgres
        |         `---postgres
    |---apache2---apache2
        |---apache2
    |---sshd---sshd---sshd---bash
        |---sshd---sshd---bash
    |---agetty
    |---login---bash---pstree

Процессы операционной системы принято классифицировать на системные (ядерные), демоны и прикладные, исходя из их назначения и свойств (см. листинг 4.19).

Прикладные процессы 3 выполняют обычные пользовательские программы (например, утилиту man), для чего им выделяют индивидуальную память, объем которой указан в столбце VSZ вывода команды ps(1). Такие процессы обычно интерактивно взаимодействуют с пользователем посредством управляющего терминала (за исключением графических программ), указанного в столбце TTY.