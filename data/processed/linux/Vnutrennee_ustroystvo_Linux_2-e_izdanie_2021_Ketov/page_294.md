---
source_image: page_294.png
page_number: 294
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.90
tokens: 7590
characters: 2104
timestamp: 2025-12-24T04:40:37.816595
finish_reason: stop
---

**Листинг 7.3. Дерево окон X-сервера и их атрибуты**

homer@ubuntu:~$ xwininfo -tree -root | grep gnome-terminal

0x2a0000a "homer@ubuntu: ~": ("gnome-terminal-server" "Gnome-terminal") 786x527+74+134 +74+134
0x2a00001 "Терминал": ("gnome-terminal-server" "Gnome-terminal-server") 10x10+10+10 +10+10

homer@ubuntu:~$ xwininfo -id 0x2a00001 | grep Map
Map State: IsUnMapped ①

homer@ubuntu:~$ xwininfo -id 0x2a0000a | egrep 'Map|Width|Height'
Width: 786
Height: 527
Map State: IsViewable ②

Кроме системных атрибутов, каждое окно наделяется свойствами (properties), широко используемыми для взаимодействия между X-клиентами (см. W:[ICCCM]), особенно между «обычными» клиентами и оконным менеджером (window manager), см. разд. 7.3. Оконный менеджер является «особенным» X-клиентом, обрабатывающим события создания окон «обычных» X-клиентов. Именно он добавляет к «чужим» создаваемым окнам «свои» декорирующие элементы: заголовок (title) окна — для его перемещения, бордюр (border) — для изменения его размеров и т. д. Делает он это одним незамысловатым способом — создает собственное окно с декором, и делает его родительским для декорируемого окна.

В листинге 7.4 показаны некоторые свойства окна, установленные программой-владельцем окна для оконного менеджера. Например, свойство WM_NAME используется оконным менеджером для текста заголовка (отображаемых) окон, свойство WM_LOCALE_NAME указывает на язык и кодировку текста, содержащегося в WM_NAME, свойство WM_CLIENT_MACHINE содержит имя сетевого узла X-клиента, а свойство WM_COMMAND — команду, при помощи которой был запущен клиент.

**Листинг 7.4. Свойства окон X-сервера**

homer@ubuntu:~$ xprop -id 0x2a00001 | grep ^WM_
WM_CLASS(STRING) = "gnome-terminal-server", "Gnome-terminal-server"
WM_COMMAND(STRING) = { "gnome-terminal-server" }
WM_CLIENT_LEADER(WINDOW): window id # 0x2800001
WM_LOCALE_NAME(STRING) = "ru_RU.UTF-8"
WM_CLIENT_MACHINE(STRING) = "ubuntu"
WM_NORMAL_HINTS(WM_SIZE_HINTS):
WM_PROTOCOLS(ATOM): protocols WM_DELETE_WINDOW, WM_TAKE_FOCUS, _NET_WM_PING
WM_ICON_NAME(COMPOUND_TEXT) = "Терминал"
WM_NAME(COMPOUND_TEXT) = "Терминал"