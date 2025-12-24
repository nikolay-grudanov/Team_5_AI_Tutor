---
source_image: page_324.png
page_number: 324
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.29
tokens: 7834
characters: 2167
timestamp: 2025-12-24T04:41:37.644175
finish_reason: stop
---

Как было проиллюстрировано выше, для эффективной работы приложений с GPU и памятью аппаратных ускорителей им необходимо обеспечить прямой доступ к этим устройствам, что реализуется менеджером прямого отрисовки — W:[DRM], а для согласования взаимодействия между X-клиентами и X-сервером при доступе к DRM используется инфраструктура прямой отрисовки (рендеринга) W:[DRI].

Кроме того, необходимы компоненты, реализующие расширение X-протокола GLX, сам программный интерфейс OpenGL и драйверы, умеющие транслировать OpenGL-команды в обращения к GPU и видеопамяти, специфические для того или иного видеоускорителя. Эти роли обычно выполняют проприетарные библиотеки от производителей самих видеоускорителей или библиотеки проекта W:[Mesa], изначально задуманного только как программный рендерер OpenGL (и расширение GLX), но впоследствии интегрировавшего в себя свободные DRI-драйверы аппаратного рендеринга для видеоускорителей Intel, AMD и NVIDIA.

Листинг 7.38. Трассировка GLX-клиента

homer@ubuntu:~$ lddtree `which glxdemo`
glxdemo => /usr/bin/glxdemo (interpreter => /lib64/ld-linux-x86-64.so.2)
    libGL.so.1 => /lib/x86_64-linux-gnu/libGL.so.1
    libGLX.so.0 => /lib/x86_64-linux-gnu/libGLX.so.0
    libX11.so.6 => /lib/x86_64-linux-gnu/libX11.so.6

homer@ubuntu:~$ ltrace -n4 -x dllopen -e gl*@@MAIN++X*@@MAIN -s 256 glxdemo

1 glxdemo->XOpenDisplay(nil) = 0x55a43bc9bd40
2 glxdemo->glXChooseVisual(0x55a43bc9bd40, 0, 0x7ffea01b4700, 0 <unfinished ...>
    dllopen@libdl.so.2("libGLX_mesa.so.0", 1) = 0x55a43bca9890
3 dllopen@libdl.so.2("/usr/lib/x86_64-linux-gnu/dri/i965_dri.so", 258) = 0x55a43bcb6ec0
<... glXChooseVisual resumed> ) = 0x55a43bcb7830
4 glxdemo->XCreateWindow(0x55a43bc9bd40, 380, 0, 0) = 0xe00002
glxdemo->glXCreateContext(0x55a43bc9bd40, 0x55a43bcb7830, 0, 1) = 0x55a43bcb7d90
5 glxdemo->glXMakeCurrent(0x55a43bc9bd40, 0xe00002, 0x55a43bcb7d90, 0) = 1
6 glxdemo->XMapWindow(0x55a43bc9bd40, 0xe00002) = 1
7 glxdemo->XNextEvent(0x564f9b53cd40, ..., 0x564f9b60a58c) = 0
    Redraw event
8 glxdemo->glClear(0x4000, 0x55a43bcb4760, 0, 0x7ff3e5e88317) = 0
8 glxdemo->glColor3f(0, 0, 1, 0) = 0x55a43bdea424
8 glxdemo->glRectf(12, 4, 5460, 0) = 1