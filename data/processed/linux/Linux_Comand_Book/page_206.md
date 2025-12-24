---
source_image: page_206.png
page_number: 206
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.91
tokens: 6111
characters: 1873
timestamp: 2025-12-24T04:08:59.866925
finish_reason: stop
---

gnuplot> plot [1:10] x**2
gnuplot> quit
Чтобы сделать то же самое и при этом сохранить результаты в Postscript-файл, выполните следующую команду.
$ echo 'set terminal postscript; plot [1:10] x**2' | gnuplot > output.ps
Посетите сайт http://www.gnuplot.info для получения более подробной информации.
xscreensaver xscreensaver
/usr/X11R6/bin stdin stdout - file -- opt --help --version

Система xscreensaver - это универсальный хранитель экрана с сотнями возможных анимационных роликов. Она работает в фоновом режиме, и вы можете управлять ей различными способами.
После периода бездействия. По умолчанию, графический пользовательский интерфейс Fedora (KDE или GNOME) запускает программу xscreensaver автоматически после пяти минут бездействия. Вы можете настроить работу этой службы в главном меню. В среде KDE запустите приложение Control Сеп1ег(Центр управления), затем выберите Appearance & Themes (Внешний вид и темы), затем Screen Saver (Хранитель экрана). Либо щелкните правой кнопкой мыши на рабочем столе, выберите пункт Configure Desktop (Настроить рабочий стол), затем Screen Saver (Хранитель экрана). В среде GNOME выберите в главном меню Preferences/Screensaver (Настройки/Хранитель экрана).

В качестве блокировщика экрана. В любой момент (в GNOME или KDE) вы можете открыть главное меню и выбрать пункт Lock Screen (Заблокировать экран). Ваш экран будет заблокирован до тех пор, пока вы не введете ваш пароль.
Из командной строки. Выполните команду xscreensaver-demo, чтобы просмотреть анимационные ролики и сделать удобные для вас настройки. Затем выполните команду xscreensaver-command, чтобы задать поведение программы.

$ xscreensaver-command -activate    Активизироваться
$ xscreensaver-command -next        Выбрать следующий ролик
$ xscreensaver-command -prev        Выбрать предыдущий ролик
$ xscreensaver-command -cycle       Выбрать произвольный ролик