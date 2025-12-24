---
source_image: page_055.png
page_number: 55
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.54
tokens: 7178
characters: 788
timestamp: 2025-12-24T09:21:46.271879
finish_reason: stop
---

5.5. «Липкое» позиционирование

Это позиционирование было одним из последних дополнений в CSS. Ранее для достижения того же эффекта вам приходилось писать собственный код JavaScript или мультимедийный запрос.

«Липкое» позиционирование часто используется для создания плавающих панелей навигации:

Далее приведен простой код, чтобы навигационная панель «прилипала» к верхней (top: 0) границе экрана. Обратите внимание: добавлен код -webkit-sticky для совместимости с браузерами на движке Webkit (такими как Chrome):

001 .navbar {
002     /* Определение некоторых основных настроек */
003     padding: 0px;
004     border: 20px solid silver;
005     background-color: white;
006     /* Добавить липкость */
007     position: -webkit-sticky;
008     position: sticky;
009     top: 0;
010 }