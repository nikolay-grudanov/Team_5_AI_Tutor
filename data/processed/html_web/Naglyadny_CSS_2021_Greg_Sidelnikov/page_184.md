---
source_image: page_184.png
page_number: 184
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.84
tokens: 7239
characters: 1093
timestamp: 2025-12-24T09:24:50.052984
finish_reason: stop
---

23.1. Свойство animation

Данное свойство является сокращенной записью восьми свойств анимации, описанных ниже:

□ animation-name — имя ключевого кадра, заданного директивой @keyframes;
□ animation-duration — продолжительность одного цикла анимации в миллисекундах;
□ animation-timing-function — описывает плавность воспроизведения анимации между каждой парой ключевых кадров;
□ animation-delay — добавляет задержку до начала воспроизведения анимации;
□ animation-iteration-count — устанавливает, сколько раз анимация должна проигрываться;
□ animation-direction — определяет воспроизведение вперед, назад или в случайной последовательности;
□ animation-fill-mode — выясняет состояние анимации, когда она не воспроизводится;
□ animation-play-state — определяет, запущена анимация или приостановлена.

В следующих разделах мы наглядно рассмотрим каждое из перечисленных свойств.

23.2. Свойство animation-name

Буквенно-цифровое имя идентификатора анимации:

001 .классАнимации {
002   animation-name: имяАнимации;
003   animation-fill-mode: normal;
004   animation: normal 3000ms ease-in;
005 }