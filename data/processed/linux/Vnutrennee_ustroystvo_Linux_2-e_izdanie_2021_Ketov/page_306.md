---
source_image: page_306.png
page_number: 306
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.37
tokens: 7890
characters: 2184
timestamp: 2025-12-24T04:41:12.942537
finish_reason: stop
---

В примере из листинга 7.15 иллюстрируется использование различных X-библиотек, среди которых библиотека самого X-протокола ① W:[Xlib], библиотеки виджетов Xt и Xaw ② и библиотеки расширений X-протокола ③, например W:[XRender].

Листинг 7.15. Библиотеки Xlib и Xt и Xaw

homer@ubuntu:~$ ldd $(which xeyes) | grep -i libX
    libXext.so.6 => /lib/x86_64-linux-gnu/libXext.so.6 (0x00007f9f16776000)
    libXmu.so.6 => /lib/x86_64-linux-gnu/libXmu.so.6 (0x00007f9f1675a000)
② libXt.so.6 => /lib/x86_64-linux-gnu/libXt.so.6 (0x00007f9f164f1000)
① libX11.so.6 => /lib/x86_64-linux-gnu/libX11.so.6 (0x00007f9f163b3000)
③ libXrender.so.1 => /lib/x86_64-linux-gnu/libXrender.so.1 (0x00007f9f161a9000)
    libxcb.so.1 => /lib/x86_64-linux-gnu/libxcb.so.1 (0x00007f9f15e15000)
    libXau.so.6 => /lib/x86_64-linux-gnu/libXau.so.6 (0x00007f9f15de4000)
    libXdmcp.so.6 => /lib/x86_64-linux-gnu/libXdmcp.so.6 (0x00007f9f15dc000)

homer@ubuntu:~$ ldd $(which xcalc) | grep -i Xaw
② libXaw.so.7 => /lib/x86_64-linux-gnu/libXaw.so.7 (0x00007fb4d4f743000)

Аналогично, в листинге 7.16 показан X-клиент, использующий библиотеку виджетов Motif, а в листинге 7.17 — X-клиенты, использующие Tk, Qt и Gtk.

Листинг 7.16. Библиотека декорирования Motif

homer@ubuntu:~$ ldd $(which wm) | grep -i libXm
    libXm.so.4 => /lib/x86_64-linux-gnu/libXm.so.4 (0x00007fdd8686a000)
    libXmu.so.6 => /lib/x86_64-linux-gnu/libXmu.so.6 (0x00007fdd862a1000)

Листинг 7.17. Библиотеки декорирования Tk, Gtk и Qt

homer@ubuntu:~$ ldd $(which wish) | grep -i libTk
    libtk8.6.so => /lib/x86_64-linux-gnu/libtk8.6.so (0x00007fa8a09eb000)
homer@ubuntu:~$ ldd $(which gnome-shell) | grep -i libGtk
    libgtk-3.so.0 => /lib/x86_64-linux-gnu/libgtk-3.so.0 (0x00007f7b3e3de000)
homer@ubuntu:~$ ldd $(which kcalc) | grep -i libQt.Gui
    libQt5Gui.so.5 => /lib/x86_64-linux-gnu/libQt5Gui.so.5 (0x00007f69b75cf000)

В соответствии с идеями, заложенными в X Window System, первые тулкиты, такие как Xaw, Motif или Tk, пользовались иерархией окон для формирования своих виджетов, т. е. каждый элемент управления как минимум являлся X-окном (и мог содержать дочерние окна). Впоследствии в Qt и Gtk отказались от такого подхода,