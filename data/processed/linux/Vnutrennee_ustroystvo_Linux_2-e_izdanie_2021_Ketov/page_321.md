---
source_image: page_321.png
page_number: 321
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.91
tokens: 7984
characters: 2167
timestamp: 2025-12-24T04:41:37.765341
finish_reason: stop
---

Интерфейс программы выстраивается из виджетов окна (window) и вертикального контейнера (vbox), который добавляется в это окно. В контейнер последовательно добавляются виджеты текстовой метки (label) и кнопки (button), сигнал нажатия на которую связывается с обработчиком — функцией terminate.

По запросу отображения окна библиотека прорисовывает виджеты при помощи X-протокола, после чего запускается главный цикл обработки поступающих событий X-протокола (щелчки кнопкой мыши, нажатия клавиш и т. д.), который прекращается при срабатывании обработчика сигнала нажатия на виджет кнопки.

Листинг 7.34. Трассировка библиотеки Gtk

homer@ubuntu:~$ gcc hello.c -o hello $(pkg-config --cflags --libs gtk+-2.0)
homer@ubuntu:~$ lddtree hello | grep libgtk
libgtk-x11-2.0.so.0 => /lib/x86_64-linux-gnu/libgtk-x11-2.0.so.0
homer@ubuntu:~$ ltrace -n2 -l libgtk-x11-2.0.so.0 ./hello

1 gtk_init(0xbfc98440, 0xbfc98444, 0x8049ff4, 0x80488b1, -1) = 1
2 gtk_window_new(0, 0xbfc98444, 0x8049ff4, 0x80488b1, -1) = 0x8302000
3 gtk_vbox_new(1, 0, 0x8049ff4, 0x80488b1, -1) = 0x82ab858
3 gtk_container_get_type(1, 0, 0x8049ff4, 0x80488b1, -1) = 0x82e29b0
3 gtk_container_add(0x8302000, 0x82ab858, 0x8049ff4, 0x80488b1, -1) = 0
4 gtk_label_new(0x8048960, 0x82ab858, 0x8049ff4, 0x80488b1, -1) = 0xb5b06608
4 gtk_container_get_type(0x8048960, 0x82ab858, 0x8049ff4, 0x80488b1, -1) = 0x82e29b0
4 gtk_container_add(0x82ab858, 0xb5b06608, 0x8049ff4, 0x80488b1, -1) = 0
5 gtk_button_new_with_label(0x804896e, 0xb5b06608, 0x8049ff4, 0x80488b1, -1) = 0x830a010
5 gtk_container_get_type(0x804896e, 0xb5b06608, 0x8049ff4, 0x80488b1, -1) = 0x82e29b0
5 gtk_container_add(0x82ab858, 0x830a010, 0x8049ff4, 0x80488b1, -1) = 0
7 gtk_widget_show_all(0x8302000, 0x8048973, 0x8048764, 0, 0) = 2
8 gtk_main(0x8302000, 0x8048973, 0x8048764, 0, 0 <unfinished ...>
9 gtk_main_quit(0x82ab858, 0xb73d0f30, 0xb72e5160, 0xb72e5243, 0x830a010) = 0
<... gtk_main resumed> )
+++ exited (status 0) +++

Аналогичным образом выглядят и работают программы, использующие Gtk и на других языках программирования, например на Python¹, что проиллюстрировано в листинге 7.35.

¹ При наличии установленного пакета python-gtk2.