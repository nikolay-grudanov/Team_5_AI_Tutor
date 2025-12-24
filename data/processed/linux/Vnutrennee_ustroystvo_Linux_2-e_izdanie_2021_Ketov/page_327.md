---
source_image: page_327.png
page_number: 327
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.09
tokens: 7768
characters: 2317
timestamp: 2025-12-24T04:41:38.144075
finish_reason: stop
---

glxdemo->XNextEvent(0x55c68d75dc0, 0x7ffe0507cc90, 0x55c68da6c880, 0...^C <no return ...>

--- SIGINT (Interrupt) ---
+++ killed by SIGINT +++

Анализ трассы показывает, что при выборе режима изображения ① X-сервер при помощи GLX-расширения X-протокола ① сообщает идентификатор «настоящей» OpenGL/GLX-библиотеки mesa ②, а затем при помощи DRI-расширения X-протокола ③ производится подключение к DRM ④ и загружается DRI-драйвер видеоускорителя i965.

Каждый раз при получении X-клиентом события на перерисовку содержимого его окна ⑦ создаются объект pixmap ⑤ и некий примитив W:[memory fence] ⑥ для синхронизации доступа к этому pixmap.

Как и ожидалось, при выполнении операций OpenGL-рендеринга ⑧ X-протокол никак не задействован, т. е. задействован режим прямой отрисовки. По окончании рендеринга ① полученные результаты «презентуются» X-серверу (при помощи соответствующего расширения X-протокола Present) ⑦, которые в конце концов помещаются им в окно X-клиента. При этом сам X-клиент оповещается о событиях высвобождения объекта pixmap ⑧ и об окончании отображения pixmap в его окно ⑨.

Сама OpenGL-отрисовка при помощи загруженного DRI-драйвера, выделение DRM-буфера под рендеринг в памяти видеоускорителя и его связь с pixmap естественным образом остаются за рамками X-протокола, т. к. прямой рендеринг и разрабатывался для вынесения процедур OpenGL-отрисовки за его рамки (см. разд. 7.6.2). Несложно предположить, что прямое взаимодействие X-клиента и DRM можно наблюдать на интерфейсе системных вызовов (листинг 7.40).

Листинг 7.40. Трассировка DRM интерфейса

homer@ubuntu:~$ xtrace strace -e socket,connect,sendmsg,recvmsg,openat,ioctl glxdemo

000:<:0009: 12: GLX-Request(155,19): glXQueryServerString ...
000>::0009:40: Reply to glXQueryServerString: string='mesa'
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/libGLX_mesa.so.0", O_RDONLY|O_CLOEXEC) = 5...
000::<001a:12: DRI3-Request(149,1): Open drawable=0x00000137 provider=0x00000000
000>::001a:32: Reply to Open: nfd=1
recvmsg(4, {... msg_control=[{..., cmsg_type=SCM_RIGHTS, cmsg_data=[5]}], ...}, 0) = 32
ioctl(5, DRM_IOCTL_VERSION, 0x555930e37770) = 0
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/dri/i965_dri.so", O_RDONLY|O_CLOEXEC) = 6
ioctl(5, DRM_IOCTL_I915_GEM_CREATE, 0x7ffe4afc40c0) = 0
ioctl(5, DRM_IOCTL_I915_GEM_MMAP, 0x7ffe4afc40d0) = 0