---
source_image: page_320.png
page_number: 320
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.42
tokens: 7273
characters: 1435
timestamp: 2025-12-24T04:41:11.190501
finish_reason: stop
---

Большинство современных X-клиентов не прибегают напрямую к помощи низкоуровневых библиотек, таких как Xlib и Xrender, а используют высокоуровневые библиотеки виджетов, отрисовывающие их при помощи сообщений X-протокола. В примере из листинга 7.33 показана простейшая программа на языке программирования C, использующая библиотеку виджетов Gtk, а в листинге 7.34 приведены ее компиляция¹ и трассировка ее библиотечных вызовов к libgtk-x11-2.0.so.0.

Листинг 7.33. Язык C и библиотека виджетов Gtk

homer@ubuntu:~$ cat hello.c
#include <gtk/gtk.h>

static void terminate(GtkWidget *widget, gpointer data) {
    gtk_main_quit();
}

int main(int argc, char *argv[]) {
    GtkWidget *window, *button, *label, *vbox;
    gtk_init (&argc, &argv);
    window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    vbox = gtk_vbox_new(TRUE, 0);
    gtk_container_add(GTK_CONTAINER (window), vbox);
    label = gtk_label_new("Hello, world!");
    gtk_container_add(GTK_CONTAINER (vbox), label);
    button = gtk_button_new_with_label("Quit");
    gtk_container_add(GTK_CONTAINER (vbox), button);
    g_signal_connect(button, "clicked", G_CALLBACK (terminate), NULL);
    gtk_widget_show_all (window);
    gtk_main ();
    return 0;
}

При работе программы сначала инициализируется библиотека виджетов ①, которая инициирует соединение с X-сервером и аутентифицирует клиента при помощи «волшебной печеньки».

¹ При наличии установленного пакета libgtk2.0-dev.