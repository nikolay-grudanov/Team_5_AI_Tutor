---
source_image: page_021.png
page_number: 21
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 8.54
tokens: 7364
characters: 1527
timestamp: 2025-12-23T23:02:24.095882
finish_reason: stop
---

1. Щелкните на поисковой строке Windows 10.
2. Введите поисковый запрос Control Panel (Панель управления) и откройте одноименную панель.
3. Щелкните на строке Programs and Features (Программы и компоненты).
4. В левой части открывшегося окна щелкните на строке Turn Windows features on or off (Включение и выключение компонентов Windows).
5. Установите флажок Windows Subsystem for Linux (Подсистема Windows для Linux).
6. Перезагрузите систему.
7. После перезагрузки откройте Windows Store (Хранилище Windows) и введите поисковый запрос Linux. Вы увидите список доступных к установке приложений.
8. Найдите и установите Ubuntu.
9. После установки Ubuntu откройте командную строку Windows, введите ubuntu и нажмите клавишу Enter.

Заметьте, что при подобном использовании дистрибутива WSL Linux вы можете выполнять сценарии bash и подключать файловую систему Windows, но не можете, как в Git Bash и Cygwin, выполнять вызовы системных функций к командам самой Windows.

Установив WSL и зайдя в Windows Store, помимо Ubuntu, вы можете выбрать и другие версии Linux, например Kali.

Командная строка и инструмент создания скриптов Windows

Установив подсистему Windows для Linux, с помощью команды bash -c вы можете выполнять команды Linux и сценарии bash напрямую из командной строки и с использованием инструмента создания скриптов Windows.

Например, можно выполнить Linux-команду pwd из командной строки Windows по отношению к открытому в данный момент каталогу:

C:\Users\Paul\Desktop>bash -c "pwd"

/mnt/c/Users/Paul/Desktop