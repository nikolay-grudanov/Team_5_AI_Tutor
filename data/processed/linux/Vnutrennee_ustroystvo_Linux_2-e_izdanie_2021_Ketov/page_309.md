---
source_image: page_309.png
page_number: 309
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.80
tokens: 7292
characters: 1219
timestamp: 2025-12-24T04:40:52.722023
finish_reason: stop
---

В листинге 7.19 показано, что практически все современные X-клиенты имеют для взаимодействия с X-сервером помимо файлового сокета (см. листинг 7.7) еще и сегмент разделяемой памяти System V IPC.

Расширение W:[RANDR] (Resize AND Rotate) позволяют управлять сменой графического разрешения, ориентацией, подключением и отключением видеовыходов дисплея X-сервера и т.д. В примере из листинга 7.20 иллюстрируется утилита xrandr(1), реализующая расширение RANDR, которая может использоваться как для запроса списка видеовыходов (и поддерживаемых ими видеорежимов работы), так и для переключения заданного видеовыхода в тот или иной видеорежим и смены ориентации изображения.

Листинг 7.20. Расширения X-сервера: RANDR

homer@ubuntu:~$ xdpyinfo | grep -i randr

RANDR

1 homer@ubuntu:~$ xrandr
Screen 0: minimum 1 x 1, current 1600 x 900, maximum 8192 x 8192
LVDS1 connected 1600x900+0+0 (normal left inverted right x axis y axis) 423mm x 238mm
    1600x900      60.00*+
    1440x900      59.89
    800x600       60.32
    640x480       59.94
VGA1 disconnected (normal left inverted right x axis y axis)
HDMI1 disconnected (normal left inverted right x axis y axis)
DP1 disconnected (normal left inverted right x axis y axis)