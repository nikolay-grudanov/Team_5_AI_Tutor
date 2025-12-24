---
source_image: page_338.png
page_number: 338
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.96
tokens: 7678
characters: 2049
timestamp: 2025-12-24T04:42:01.159430
finish_reason: stop
---

Листинг 8.6. Трассировка библиотек Wayland

homer@ubuntu:~$ ./hello &
[1] 28237
homer@ubuntu:~$ pgrep -l gnome-shell
5628 gnome-shell

homer@ubuntu:~$ lsof -p 28237 | grep memfd
hello   28237 homer DEL   REG   0,5   387481 /memfd:gdk-wayland

homer@ubuntu:~$ pmap 28237 | grep memfd
00007f3068202000  268K rw-s- memfd:gdk-wayland (deleted)

homer@ubuntu:~$ lsof -p 5628 | grep 387481
gnome-she 5628 homer DEL   REG   0,5   387481 /memfd:gdk-wayland

homer@ubuntu:~$ pmap 5628 | grep 268K
00007f2974fde000  268K rw-s- memfd:gdk-wayland (deleted)

Практически идентичным образом работают и «продвинутые» Wayland-клиенты, задействующие OpenGL-рендеринг, для которого, однако, в Wayland в принципе нет специального протокольного расширения, подобного GLX. Вместо этого есть интерфейсы, позволяющие доставлять композитору DRM-буферы (в виде файловых дескрипторов DMA-BUF примерно так же, как ему доставляются «обычные» буферы в виде файловых дескрипторов разделяемой памяти). Такой подход позволяет в принципе охватить целый класс приложений, работающих с растровыми изображениями, получаемыми аппаратным образом, будь то результат рендеринга 3D-сцены GPU видеоускорителя, аппаратно декодированный кадр W:[H.264]/W:[H.265] видео или видеокадр, полученный видеокамерой. В листинге 8.7 показана работа демонстрационного Wayland-клиента weston-simple-egl, который использует программный интерфейс W:[EGL(API)] (аналог GLX) для OpenGL-рендеринга и zwp_linux_dmabuf_v1 интерфейс Wayland для отправки результата отрисовки композитору.

Листинг 8.7. OpenGL-рендеринг при помощи программного интерфейса EGL в Wayland

homer@ubuntu:~$ WAYLAND_DEBUG=1 strace -fe ioctl /usr/lib/weston/weston-simple-egl

(1) [2890473.319] -> wl_display@1.get_registry(new id wl_registry@3)
(1) [2890474.242] wl_registry@3.global(1, "wl_drm", 2)
(1) [2890474.417] -> wl_registry@3.bind(1, "wl_drm", 2, new id [unknown]@10)
(2) [2890479.041] wl_registry@3.global(20, "zwp_linux_dmabuf_v1", 3)
(2) [2890479.284] -> wl_registry@3.bind(20, "zwp_linux_dmabuf_v1", 3, new id [unknown]@11)