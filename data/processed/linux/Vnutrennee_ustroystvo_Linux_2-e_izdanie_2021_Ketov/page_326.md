---
source_image: page_326.png
page_number: 326
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 199.21
tokens: 8477
characters: 2812
timestamp: 2025-12-24T04:44:21.075763
finish_reason: stop
---

326

(3) 000:<000d: 12: Request(98): QueryExtension name='DRI3'
    000>::000d:32: Reply to QueryExtension: present=true(0x01) ...
    000:<000e: 16: Request(98): QueryExtension name='Present'
    000>::000e:32: Reply to QueryExtension: present=true(0x01) ...

(4) 000:<001a: 12: DRI3-Request(149,1): Open drawable=0x00000137 provider=0x00000000
    000>::001a:32: Reply to Open: nfd=1

(5) dlopen@libdl.so.2("/usr/lib/x86_64-linux-gnu/dri/i965_dri.so", 258) = 0x55c68d77b480
<... glXChooseVisual resumed> ) = 0x55c68d774dd0

(6) glxdemo->XCreateWindow(0x55c68d75dc0d0, 311, 0, ...) = 0x3600002
    000:<001d: 48: Request(1): CreateWindow depth=0x18 window=0x03600002 parent=0x00000137 ...
glxdemo->glXCreateContext(0x55c68d75dc0d0, 0x55c68d774dd0, 0, ...)
    000:<001e: 24: GLX-Request(155,3): glXCreateContext context=0x03600003 ...
    000:<001f: 8: GLX-Request(155,6): glXIsDirect context=0x03600003
    000>::001f:32: Reply to glXIsDirect: is_direct=1
) = 0x55c68d775330

(7) glxdemo->glXMakeCurrent(0x55c68d75dc0d0, 0x3600002, 0x55c68d775330,
    ... ... ... ...
(5) 000:<0026: 24: DRI3-Request(149,2): PixmapFromBuffer pixmap=0x03600006 drawable=0x03600002 ...
(6) 000:<0027: 16: DRI3-Request(149,4): FenceFromFD drawable=0x03600006 fence=0x03600007 ...
) = 1
    ... ... ...

(8) glxdemo->XMapWindow(0x55c68d75dc0d0, 0x3600002
    0000::<0028: 8: Request(8): MapWindow window=0x03600002
    000>::0028: Event MapNotify(19) event=0x03600002 window=0x03600002 ...
) = 1
    ... ... ... ...

(9) glxdemo->XNextEvent(0x55b3b9d62cd0, 0x7fffa3e90a00, 0x7fffa3e908f0, 0x55b3ba01919c) = 0

(10) glxdemo->glClear(0x4000, 0x6520776172646552, 0x7fee08ec18c0, 0x746e657665207761
    (5) 000::<008f: 24: DRI3-Request(149,2): PixmapFromBuffer pixmap=0x03600006 drawable=0x03600002 ...
    (6) 000::<0090: 16: DRI3-Request(149,4): FenceFromFD drawable=0x03600006 fence=0x03600009 ...
    000::<0098: 28: Request(62): CopyArea src-drawable=0x03600006 dst-drawable=0x03600008 ...
    000::<0099: 8: SYNC-Request(134,15): TriggerFence fid=0x03600009
    000::<009a: 8: Request(54): FreePixmap drawable=0x03600006
    000::<009b: 8: SYNC-Request(134,17): DestroyFence fid=0x03600007
) = 0

(11) glxdemo->glColor3f(0x7fee04f53c5b, 2, 0x7fee04f6bed8, 0) = 0x55c68da5ad04

(12) glxdemo->glRectf(0, 0, 5126, 2) = 1

(13) glxdemo->glXSwapBuffers(0x55c68d75dc0d0, 0x3600002, 519, 4
    ... ... ... ...
(7) 000::<002a: 72: Present-Request(148,1): Pixmap window=0x03600002 pixmap=0x03600008 idle_fence=0x03600009 ...
) = 1
    ... ... ... ...

(14) 0000::<008e: Event Generic(35) Present(148) IdleNotify(2) event=0x03600005 window=0x03600002 serial=19 pixmap=0x03600008 idle_fence=0x03600009
(15) 000::<009c: Event Generic(35) Present(148) CompleteNotify(1) kind=Pixmap(0x00) mode=Copy(0x00) event=0x03600005 window=0x03600002 ...