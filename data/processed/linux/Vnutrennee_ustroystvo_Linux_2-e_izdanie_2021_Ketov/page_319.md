---
source_image: page_319.png
page_number: 319
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.33
tokens: 8227
characters: 2701
timestamp: 2025-12-24T04:41:36.226372
finish_reason: stop
---

XOpenDisplay@libX11.so.6(nil) = 0x558cb64e8a70
XCreateWindow@libX11.so.6(0x558cb64e8a70, 380, 0, 0) = 0xe0000a
XCreateWindow@libX11.so.6(0x558cb64e8a70, 0xe0000a, 0, 0) = 0xe0000b
XFillRectangle@libX11.so.6(0x558cb64e8a70, 0xe0000c, 0x558cb65087a0, 0) = 1
XRenderCompositeDoublePoly@libXrender.so.1(0x558cb64e8a70, 3, 0xe00008, 0xe0000e) = 0
XQueryPointer@libX11.so.6(0x558cb64e8a70, 0xe0000b, 0x7ffffd96f4fb0, 0x7ffffd96f4fb8) = 1
XFillRectangle@libX11.so.6(0x558cb64e8a70, 0xe0000b, 0x558cb6505ee0, 45) = 1
XRenderCompositeDoublePoly@libXrender.so.1(0x558cb64e8a70, 3, 0xe00009, 0xe0000e) = 0
XFillRectangle@libX11.so.6(0x558cb64e8a70, 0xe0000b, 0x558cb6505ee0, 124) = 1
XRenderCompositeDoublePoly@libXrender.so.1(0x558cb64e8a70, 3, 0xe00009, 0xe0000e) = 0
XQueryPointer@libX11.so.6(0x558cb64e8a70, 0xe0000b, 0x7ffffd96f4fb0, 0x7ffffd96f4fb8) = 1
XFillRectangle@libX11.so.6(0x558cb64e8a70, 0xe0000b, 0x558cb6505ee0, 43) = 1
XRenderCompositeDoublePoly@libXrender.so.1(0x558cb64e8a70, 3, 0xe00009, 0xe0000e) = 0
XFillRectangle@libX11.so.6(0x558cb64e8a70, 0xe0000b, 0x558cb6505ee0, 122) = 1
XRenderCompositeDoublePoly@libXrender.so.1(0x558cb64e8a70, 3, 0xe00009, 0xe0000e) = 0

Зная назначение библиотечных вызовов XQueryPointer(3), XFillRectangle(3) и XRenderCompositeDoublePoly(3), можно составить модель функционирования X-клиента, в котором легко увидеть создание окна 0, цикл 1 опроса положения курсора при помощи XQueryPointer(3) и цикл 2 перерисовки глаз стиранием их старого изображения при помощи XFillRectangle(3) и отрисовки нового положения посредством XRenderCompositeDoublePoly(3). Можно даже предположить, что две пары XFill/XRender используются на каждой итерации, потому что перерисовываются два глаза.

Еще одним инструментом, разрешающим трассировать сообщения самого X-протокола, является xtrace(1), позволяющая увидеть обмен между X-клиентом и X-сервером (листинг 7.32).

Листинг 7.32. Трассировка X-протокола

homer@ubuntu:~$ xtrace -n xeyes | grep -E 'QueryPointer|FillRectangle|RENDER'
000:<:003c: 8: Request(38): QueryPointer window=0x02e0000b
000:>:003c:32: Reply to QueryPointer: same-screen=true(0x01) root=0x0000017c child=None(0x00000000) root-x=913 root-y=1 win-x=813 win-y=-638 mask=0
000:<:0053: 20: Request(70): PolyFillRectangle drawable=0x02e0000b gc=0x02e00006 rectangles={x=42 y=28 w=13 h=18};
000:<:0054:304: RENDER-Request(140,10): Trapezoids op=Over(0x03) src=0x02e00009 xSrc=0 ySrc=0 dst=0x02e0000e maskFormat=0x00000024 trapezoids={...};};

Кроме xtrace(1), для анализа сообщений X-протокола при передаче по сети можно использовать анализатор сетевых пакетов wireshark(1) ровно таким же образом, как и для анализа сетевых сообщений любых других сетевых служб.