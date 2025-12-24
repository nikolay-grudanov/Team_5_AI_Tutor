---
source_image: page_283.png
page_number: 283
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.93
tokens: 7350
characters: 1670
timestamp: 2025-12-24T04:52:59.278313
finish_reason: stop
---

Обновление групп пакетов

Чтобы упростить управление несколькими пакетами сразу, YUM позволяет использовать группы пакетов. Например, можно установить целиком GNOME Desktop Environment (весь рабочий стол) или Virtualization (все пакеты, необходимые для настройки компьютера в качестве хоста виртуализации). Начните с запуска подкоманды grouplist, чтобы увидеть список имен групп:

# yum grouplist | less
Available Environment Groups:
    Fedora Custom Operating System
    Minimal Install
    Fedora Server Edition
...
Installed Groups:
    LibreOffice
    GNOME Desktop Environment
    Fonts
...
Available Groups:
    Authoring and Publishing
    Books and Guides
    C Development Tools and Libraries
...

Допустим, вы решили попробовать другую среду рабочего стола и хотите узнать, что находится в группе LXDE. Для этого используйте подкоманду groupinfo:

# yum groupinfo LXDE
Group: LXDE
Description: LXDE is a lightweight X11 desktop environment...
Mandatory Packages:
...
    lxde-common
    lxdm
    lxinput
    lxlauncher
    lxmenu-data
...

В дополнение к описанию группы groupinfo показывает пакеты Mandatory Packages (обязательные, которые всегда устанавливаются вместе с группой), Default Packages (те, что установлены по умолчанию, но могут быть исключены) и Optional Packages (необязательные, которые являются частью группы, но не установлены по умолчанию). С помощью инструментов с графическим интерфейсом для установки групп пакетов можно отключить установку пакетов по умолчанию (Default Packages) или изменить установку дополнительных (Optional Packages).

Чтобы установить группу пакетов, используйте подкоманду groupinstall:

# yum groupinstall LXDE