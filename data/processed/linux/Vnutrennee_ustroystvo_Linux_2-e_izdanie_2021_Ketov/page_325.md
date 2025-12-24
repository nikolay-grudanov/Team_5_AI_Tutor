---
source_image: page_325.png
page_number: 325
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.76
tokens: 7620
characters: 2117
timestamp: 2025-12-24T04:41:29.586137
finish_reason: stop
---

В листинге 7.38 показана работа простейшего X-клиента glxdemo(1), использующего библиотеки libGL, libGLX и libX11. Как и любой другой X-клиент, он для начала подключается к X-серверу, затем при выборе режима изображения «оберточной» библиотекой libGLX загружается «настоящая» OpenGL/GLX-библиотека libGLX_mesa.so.0, которая, в свою очередь, загружает DRI-драйверы (выполненные как разделяемые библиотеки), в данном случае — для видеоускорителя на чипе Intel i965. После инициализации создается обычное окно, которое затем прикрепляется к контексту вывода и изображается на экране. При получении события на перерисовку содержимого окна начинается собственно OpenGL-рендеринг, который завершается отправкой результата рендлинга в окно. В glxdemo(1), как и большинстве OpenGL-приложений, используется контекст вывода с двойной буферизацией, т. е. рендеринг происходит во внеэкранный буфер (back buffer), изображается всегда экранный (front buffer), а по завершении рендлинга они быстро меняются местами (swap buffers), что позволяет изображать только полностью отрисованные сцены.

Тем не менее из результата трассировки в листинге 7.38 не очевидно, что был использован GLX-режим прямой отрисовки (direct rendering), что можно явно увидеть при совместной трассировке библиотечных вызовов и команд X-протокола (листинг 7.39).

Листинг 7.39. Трассировка GLX- и DRI3-расширений X-протокола

homer@ubuntu:~$ xtrace -n ltrace -n4 -x dlopen -e gl*@MAIN+X*@MAIN -s 256 glxdemo

glxdemo->XOpenDisplay(nil)
    000::< an lsb-first want 11:0 authorising with '' of length 0
    000:: Success, version is 11:0 vendor='The X.Org Foundation' ... roots={root=0x00000137 ...};

glxdemo->glXChooseVisual(0x55c68d75dcd0, 0, 0x7ffe0507cc90, <unfinished ...>
    000::0007: 12: Request(98): QueryExtension name='GLX'
    000::0007:32: Reply to QueryExtension: present=true(0x01) ...
    000::0009: 12: GLX-Request(155,19): glXQueryServerString ...
    000::0009:40: Reply to glXQueryServerString: string='mesa'

dlopen@libdl.so.2("libGLX_mesa.so.0", 1) = 0x55c68d76ac30

1 В этом месте могла бы загружаться проприетарная библиотека GL/GLX.