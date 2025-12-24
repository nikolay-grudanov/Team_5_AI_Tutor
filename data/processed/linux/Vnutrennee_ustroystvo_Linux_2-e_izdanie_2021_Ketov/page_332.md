---
source_image: page_332.png
page_number: 332
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.60
tokens: 7493
characters: 1977
timestamp: 2025-12-24T04:41:34.663649
finish_reason: stop
---

выводит список глобальных объектов композитора, предоставляющих соответствующие интерфейсы.

Листинг 8.1. Интерфейсы Wayland-протокола

homer@ubuntu:~$ weston-info
interface: 'wl_drm', version: 2, name: 1
interface: 'wl_compositor', version: 4, name: 2
interface: 'wl_shm', version: 1, name: 3
    formats: XRGB8888 ARGB8888
    ...
interface: 'zxdg_shell_v6', version: 1, name: 10
interface: 'wl_shell', version: 1, name: 11
interface: 'gtk_shell1', version: 3, name: 12
    ...
interface: 'wl_seat', version: 5, name: 16
    name: seat0
    capabilities: pointer keyboard
    keyboard repeat rate: 33
    keyboard repeat delay: 500
    ...
interface: 'zwp_linux_dmabuf_v1', version: 3, name: 20
    ...

Интерфейс wl_compositor является основой протокола, позволяющей клиентам создавать окна (surfaces), в которые они при помощи буферов в разделяемой памяти и специального интерфейса wl_shm отправляют изображения, подлежащие компози- тингу. Интерфейсы wl_drm и/или zwp_linux_dmabuf_v1 используются при прямом OpenGL-рендеринге и обеспечивают поддержку DRI для доставки результата рендеринга от клиента к композитору при помощи DRM-буферов в памяти видеоадаптера. Кроме того, интерфейс zwp_linux_dmabuf_v1 (как и расширение X-протокола DRI3, проиллюстрированное в разд. 7.8.2) позволяет доставлять от клиента к композитору DMA-BUF-буферы, которые широко используются драйверами устройств, например видеокамер. Это позволяет с минимальными накладными расходами изображать видео, например захватываемое с веб-камеры.

Интерфейс wl_seat доставляет клиентам события указателя (мыши), нажатия клавиш и события тачскрина, если такие устройства обнаружены композитором, а shell-интерфейсы wl_shell, zxdg_shell_v6 и gtk_shell1 организуют управление местоположением и размерами окон на экране. Другими словами, реализуют функции оконного менеджера X Window System, за исключением декорирования окон, которое в Wayland возложено на самих-клиентов (см. CSD, W:[Client-Side Decoration]).