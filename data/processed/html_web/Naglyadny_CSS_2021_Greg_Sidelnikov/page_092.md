---
source_image: page_092.png
page_number: 92
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.25
tokens: 7355
characters: 1137
timestamp: 2025-12-24T09:22:54.771477
finish_reason: stop
---

Вы можете выбрать любой цвет, используя значения от 0 до 300:

0   50   100   150   200   250   300

Мы уже рассмотрели примеры значений свойств, связанных с каждым градиентом. Поэкспериментируем со значениями и посмотрим, какие эффекты они оказывают на ваши элементы пользовательского интерфейса:

001 background: linear-gradient (yellow, red);
002 background: linear-gradient (black, white);
003 background: linear-gradient (to right, black, white);
004 background: linear-gradient (to left, black, white);
005 background: linear-gradient (to bottom right, black, white);
006 background: linear-gradient (90deg, black, white);
007 background: linear-gradient (
008 hsl (0, 100%, 50%),
009 hsl (50, 100%, 50%),
010 hsl (100, 100%, 50%),
011 hsl (150, 100%, 50%),
012 hsl (200, 100%, 50%),
013 hsl (250, 100%, 50%),
014 hsl (300, 100%, 50%));
015 background: radial-gradient (black, white);
016 background: radial-gradient (at bottom right, black, white);
017 background:
018 repeating-linear-gradient
019 (white 100px, black 200px, white 300px);
020 background:
021 repeating-radial-gradient
022 (white 100px, black 200px, white 300px);