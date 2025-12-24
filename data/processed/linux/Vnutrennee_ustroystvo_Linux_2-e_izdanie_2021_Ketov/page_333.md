---
source_image: page_333.png
page_number: 333
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.17
tokens: 7702
characters: 2331
timestamp: 2025-12-24T04:41:45.306143
finish_reason: stop
---

8.1. Wayland-композитор

Как уже сказано выше, основной компонентой Wayland является композитор. Однако, в отличие от оконной системы X, спецификации Wayland не накладывают вообще никаких ограничений на внутреннее устройство композитора. Вместо этого стандартизуется всего лишь протокол взаимодействия и функции, предоставляемые клиентам при помощи тех или иных интерфейсов.

Для тестирования жизнеспособности и уточнения концепции разработчики Wayland-протокола и спецификаций поддерживают клиентскую и серверную библиотеки основного (core) протокола (куда как раз входят интерфейсы wl_compositor, wl_shm и пр.) и прототип (reference) композитора под названием W:[Weston]. Кроме этого, коллегиально стандартизуются расширения протокола (наборы интерфейсов), предложенные другими заинтересованными разработчиками, которые на основе этого «конструктора» и создают законченные решения, такие как W:[Mutter (software)], являющиеся основой для gnome-shell(1)) из настольного окружения GNOME, kwin из настольного окружения KDE (листинг 8.2) и пр.

Листинг 8.2. Wayland-композиторы weston, gnome-shell и kwin

homer@ubuntu:~$ ldd $(which weston) | grep wayland
    libwayland-server.so.0 => /lib/x86_64-linux-gnu/libwayland-server.so.0 (0x00007f9d4ee4e000)

homer@ubuntu:~$ ldd $(which gnome-shell) | grep wayland
    libwayland-server.so.0 => /lib/x86_64-linux-gnu/libwayland-server.so.0 (0x00007f8c30150000)
    libwayland-cursor.so.0 => /lib/x86_64-linux-gnu/libwayland-cursor.so.0 (0x00007f8c2dfa1000)
    libwayland-egl.so.1 => /lib/x86_64-linux-gnu/libwayland-egl.so.1 (0x00007f8c2df9c000)
    libwayland-client.so.0 => /lib/x86_64-linux-gnu/libwayland-client.so.0 (0x00007f8c2df8b000)

homer@ubuntu:~$ ldd $(which kwin_wayland) | grep wayland
    libwayland-client.so.0 => /lib/x86_64-linux-gnu/libwayland-client.so.0 (0x00007f1dc6c52000)
    libwayland-server.so.0 => /lib/x86_64-linux-gnu/libwayland-server.so.0 (0x00007f1dc6c3d000)

В листинге 8.3 показано, что при запуске Wayland-композитора он действует ровно так же, как и X-сервер (для сравнения см. листинг 7.1), т. е. инициализирует устройства ввода (видеоадаптер) ①, устройства ввода (мышь и пр.) ② и открывает локальный сокет для взаимодействия с клиентами ③.

Листинг 8.3. Wayland-композитор

homer@ubuntu:~$ pgrep -l gnome-shell
5628 gnome-shell
5672 gnome-shell-cal