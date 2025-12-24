---
source_image: page_190.png
page_number: 190
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.75
tokens: 7211
characters: 756
timestamp: 2025-12-24T09:24:50.438624
finish_reason: stop
---

Поскольку динамика устанавливается уравнением, вы можете предоставить собственные аргументы, чтобы создать уникальные кривые для достижения конкретного типа скорости, недоступного по предопределённым значениям.

Как показано на рисунках ниже, можно воссоздать стандартный набор значений с помощью функции cubic-bezier:

001 .linear {
002   animation-timing-function: cubic-bezier(0, 0, 1, 1);
003 }
004
005 .ease {
006   animation-timing-function: cubic-bezier(0.25, 0.1, 0.25, 1);
007 }
008
009 .ease-in {
010   animation-timing-function: cubic-bezier(0.42, 0, 1, 1);
011 }
012
013 .ease-out {
014   animation-timing-function: cubic-bezier(0, 0, 0.58, 1);
015 }
016
017 .ease-in-out {
018   animation-timing-function: cubic-bezier(0.42, 0, 0.58, 1);
019 }