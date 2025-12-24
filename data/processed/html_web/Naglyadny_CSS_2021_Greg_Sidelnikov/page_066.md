---
source_image: page_066.png
page_number: 66
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.33
tokens: 7347
characters: 1341
timestamp: 2025-12-24T09:22:23.153028
finish_reason: stop
---

Посмотрите на лигатуры с настройками font-feature-settings: "liga" 1 и font-feature-settings: "liga" on:

LIGATURES ON
Affirmative
font-family: "chaparral-pro";
font-feature-settings: "liga" 1;
font-feature-settings: "liga" on;

Affirmative
font-family: "Fira Sans";
font-feature-settings: "liga" 1;
font-feature-settings: "liga" on;

LIGATURES OFF
Affirmative
font-family: "chaparral-pro";
font-feature-settings: "liga" 0;
font-feature-settings: "liga" off;

Affirmative
font-family: "Fira Sans";
font-feature-settings: "liga" 0;
font-feature-settings: "liga" off;

Ligatures
AAÆA/MBMDME
FFFIFLHELAMP
KNTOOGOGE
EHEERTTTWTY
ThUBUDULUPUR
ae ae cky ct ee fb fh fi
fj fl fr ft fy ff ffb ffh
ffh ffj ffl ffr fft ffy gg
gi gy ggy ip it ky oe oe
py sp fs ss st tw ty tt tty

Распространенные текстовые эффекты (italic (курсив), bold (полужирный) и oblique (наклонный)) достигаются с помощью свойств font-style и font-weight:

Enter your email address.
Курсив Полужирный Полужирный курсив Обычный
italic bold bold italic regular oblique

Свойства text-align и line-height часто используются для центрирования текста на кнопках:

Sign Up
Стиль по умолчанию <span> не очень корректно работает для кнопок

Sign Up
Выравнивание по центру и line-height можно установить для точности положения текста

text-align: center;
height: 40px;
line-height: 40px;