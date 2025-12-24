---
source_image: page_307.png
page_number: 307
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.95
tokens: 7527
characters: 1653
timestamp: 2025-12-24T04:40:57.545991
finish_reason: stop
---

Потому что он приводил к «фликерингу» при отрисовке в силу независимости окон и неодновременности их обработки.

В современных тулкитах (листинг 7.18) в большинстве случаев приложение имеет всего лишь одно серверное X-окно, а элементы управления отрисовываются целиком в его пределах только тулkitом X-клиента, без участия X-сервера.

Листинг 7.18. Окна X-клиентов

homer@ubuntu:~$ xcalc & gnome-calculator &
[1] 1668
[2] 1669
homer@ubuntu:~$ xwininfo -tree -root
0x400005b "Calculator": ("xcalc" "XCalc") 226x308+10+38 +50+107
    1 child:
    0x400005c (has no name): () 226x308+0+0 +50+107
        41 children:
        0x40000d9 (has no name): () 214x48+4+4 +54+111
            1 child:
            0x40000da (has no name): () 204x38+4+4 +59+116
                7 children:
                0x40000e1 (has no name): () 10x15+4+2 +64+119
                    ...
                    ...
                    ...
                    0x40000db (has no name): () 18x15+127+21 +187+138
                    0x40000d6 (has no name): () 40x26+4+66 +54+173
                    0x40000d3 (has no name): () 40x26+48+66 +98+173
                ...
                ...
                ...
                0x4000061 (has no name): () 40x26+180+276 +230+383
            ...
            ...
            ...
        0x4200007 "Калькулятор": ("gnome-calculator" "Gnome-calculator") 448x467+70+62 +70+62
            1 child:
            0x4200008 (has no name): () 1x1+-1+-1 +69+61
                ...
                ...
                ...
            0x4200001 "gnome-calculator": ("gnome-calculator" "Gnome-calculator") 10x10+10+10 +10+10

1 См. http://tiny.cc/dgb5hz.