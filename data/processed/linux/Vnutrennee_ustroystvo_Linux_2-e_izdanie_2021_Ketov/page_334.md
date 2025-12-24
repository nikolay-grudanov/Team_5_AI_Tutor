---
source_image: page_334.png
page_number: 334
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.22
tokens: 7652
characters: 2224
timestamp: 2025-12-24T04:41:43.467350
finish_reason: stop
---

homer@ubuntu:~$ lsof -p 5628 -a /dev

COMMAND   PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
gnome-she 5628 homer mem CHR 226,0      398 /dev/dri/card0
gnome-she 5628 homer 0r CHR 1,3     0t0    6 /dev/null
gnome-she 5628 homer 10u CHR 226,0     0t0  398 /dev/dri/card0
gnome-she 5628 homer 20u CHR 13,64     0t0  149 /dev/input/event0
gnome-she 5628 homer 26u CHR 13,68     0t0  336 /dev/input/event4

homer@ubuntu:~$ lsof -p 5628 -a -U

COMMAND   PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
gnome-she 5628 homer 29u unix 0x000000...00000000 0t0 54619 /run/user/1000/wayland-0 type=STREAM

8.2. Wayland-клиенты и Wayland-протокол

Как было сказано выше, Wayland-протокол по сравнению с X-протоколом весьма прост, т. к. большинство задач возложено на самого клиента или клиентские библиотеки виджетов, в качестве которых выступают все те же Gtk+ и Qt. В стеке тулкита Gtk (gimp toolkit) изначально присутствовала библиотека рисования W:[gdk] (gimp drawing kit), абстрагирующая саму Gtk от оконной системы. Кроме этого, современная gdk базируется на библиотеке 2D-рендеринга W:[cairo (graphics)], что вместе составляет достаточную базу для работы поверх Wayland, т. к. позволяет получать именно растровые изображения окна клиентского приложения, отправляемые Wayland-композитору.

Более того, сами приложения совсем (!) не нуждаются в адаптации для работы в графической системе Wayland. Однако таким свойством Gtk обладает, только начиная с версии 3, поэтому запустить откомпилированный ранее пример из листинга 7.33 не получится¹. А вот пересобрать тот же пример с библиотекой libgtk-3 можно так, как показано в листинге 8.4, причем получившаяся программа за счет свойств Gtk/Gdk сможет выполняться как в X, так и в Wayland.

Листинг 8.4. Wayland-клиент на основе Gtk 3

homer@ubuntu:~$ gcc hello.c -o hello $(pkg-config --cflags --libs gtk+-3.0)
hello.c: In function 'main':
hello.c:13:6: warning: 'gtk_vbox_new' is deprecated: Use 'gtk_box_new' instead [-Wdeprecated-declarations]
    vbox = gtk_vbox_new(TRUE, 0);

¹ Если быть точнее, то получится, но только в режиме совместимости, т. к. практически любой Wayland-композитор имеет в своем составе Xwayland — X-сервер, конвертирующий X-окна в Wayland-поверхности (surfaces).