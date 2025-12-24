---
source_image: page_335.png
page_number: 335
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.69
tokens: 7806
characters: 2299
timestamp: 2025-12-24T04:41:52.345236
finish_reason: stop
---

In file included from /usr/include/gtk-3.0/gtk/gtk.h:282:0,
    from hello.c:1:
/usr/include/gtk-3.0/gtk/deprecated/gtkvbox.h:61:13: note: declared here
GtkWidget * gtk_vbox_new (gboolean homogeneous,

homer@ubuntu:~$ lddtree hello
hello => ./hello (interpreter => /lib64/ld-linux-x86-64.so.2)
    libgtk-3.so.0 => /usr/lib/x86_64-linux-gnu/libgtk-3.so.0
    libgdk-3.so.0 => /usr/lib/x86_64-linux-gnu/libgdk-3.so.0
    libXrandr.so.2 => /usr/lib/x86_64-linux-gnu/libXrandr.so.2
    libXrender.so.1 => /usr/lib/x86_64-linux-gnu/libXrender.so.1
    ...
    libwayland-cursor.so.0 => /usr/lib/x86_64-linux-gnu/libwayland-cursor.so.0
    libwayland-egl.so.1 => /usr/lib/x86_64-linux-gnu/libwayland-egl.so.1
    libwayland-client.so.0 => /usr/lib/x86_64-linux-gnu/libwayland-client.so.0
    ...
    libX11.so.6 => /usr/lib/x86_64-linux-gnu/libX11.so.6

Для наблюдения за работой программы можно было бы воспользоваться трассировкой библиотечных вызовов так же, как это ранее было показано в листинге 7.34, однако libwayland-client.so.0 устроена (в угоду эффективности) так, что результат практически невозможно будет трактовать. К счастью, сама библиотека предоставляет великолепные возможности трассировки (активируемые переменной окружения WAYLAND_DEBUG), показанные в листинге 8.5.

Листинг 8.5. Трассировка программного интерфейса Wayland

homer@ubuntu:~$ WAYLAND_DEBUG=1 ltrace -n2 -l libgtk-3.so.0./hello
hello->gtk_init(0x7fffda3942ac, 0x7fffda3942a0, 0x7fffda3942a0, 0
① [1406864,197] -> wl_display@1.get_registry(new id wl_registry@2)
① [1406874,203] wl_registry@2.global(2, "wl_compositor", 4)
→ [1406874,248] -> wl_registry@2.bind(2, "wl_compositor", 3, new id [unknown]@4)
② [1406874,404] wl_registry@2.global(3, "wl_shm", 1)
→ [1406874,418] -> wl_registry@2.bind(3, "wl_shm", 1, new id [unknown]@5)
③ [1406891,543] wl_registry@2.global(15, "wl_seat", 5)
→ [1406891,556] -> wl_registry@2.bind(15, "wl_seat", 5, new id [unknown]@15)
④ [1406894,912] -> wl_display@1.sync(new id wl_callback@21)
④ [1406895,627] wl_seat@15.capabilities(3)
| [1406895,632] -> wl_seat@15.get_pointer(new id wl_pointer@8)
→ [1406895,680] -> wl_seat@15.get_keyboard(new id wl_keyboard@26)
⑤ [1406895,713] wl_callback@21.done(106554)
③ [1406895,721] -> wl_registry@2.bind(9, "xdg_wm_base", 1, new id [unknown]@21)
)=1