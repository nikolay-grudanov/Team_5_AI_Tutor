---
source_image: page_329.png
page_number: 329
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.06
tokens: 7775
characters: 2028
timestamp: 2025-12-24T04:41:41.678043
finish_reason: stop
---

напрямую работают с изображением в общей памяти видеоускорителя, накладные расходы сведены к нулю, а производительность OpenGL отрисовки максимальна.

Рисующие вызовы OpenGL-библиотеки (например, glRectf(3) и glColor3f(3)) превращаются DRI-драйвером в набор команд, понятных GPU видеоадаптера, и упаковываются в буфер команд, который потом отправляется на исполнение 8.

Для полноты картины в листинге 7.41 показаны ресурсы, используемые демонстрационным X-клиентом glxgears(1) при прямом рендеринге, а именно: локальный сокет 1 для взаимодействия с X-сервером, файловый дескриптор 2 для доступа к DRM-менеджеру, а также отображения DRM-буферов 3 в память процесса.

Листинг 7.41. DRM-буфера прямого рендеринга

homer@ubuntu:~$ glxgears &
[1] 31456
homer@ubuntu:~$ pmap 31456
COMMAND   PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
glxgears 31456 homer cwd DIR 8,4 53248 786434 /home/homer
glxgears 31456 homer rtd DIR 8,4 4096 2 /
glxgears 31456 homer txt REG 8,4 22616 8259843 /usr/bin/glxgears
glxgears 31456 homer DEL REG 0,45 453 /i915 1
glxgears 31456 homer DEL REG 0,45 522 /i915 1
glxgears 31456 homer DEL REG 0,45 253 /i915 1
glxgears 31456 homer DEL REG 0,45 386 /i915 1
glxgears 31456 homer DEL REG 0,45 370 /i915 1
glxgears 31456 homer DEL REG 0,45 247 /i915 1
glxgears 31456 homer 0u CHR 136,2 0t0 5 /dev/pts/2
glxgears 31456 homer 1u CHR 136,2 0t0 5 /dev/pts/2
glxgears 31456 homer 2u CHR 136,2 0t0 5 /dev/pts/2
glxgears 31456 homer 3u unix 0x0000000000000000 0t0 1444944 type=STREAM 1
glxgears 31456 homer 4u CHR 226,0 0t0 442 /dev/dri/card0 2

7.9. В заключение

Резюмируя современное состояние оконной системы X, нужно признать, что со временем, в силу возникших новых условий или требований, она претерпела значительные изменения и на текущий момент очень далека от исходной архитектуры.

Современные тулкиты практически не пользуются иерархией окон и их дочерне-родительскими отношениями (см. листинг 7.18). Для отрисовки «по-современному» выглядящих виджетов с тенями и градиентами широко используются растровые