---
source_image: page_185.png
page_number: 185
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.34
tokens: 7189
characters: 767
timestamp: 2025-12-24T09:24:41.579422
finish_reason: stop
---

Имя анимации должно совпадать с именем, указанным в директиве @keyframes:

001 @keyframes имяАнимации {
002    0% { }
003    100% { }
004 }

23.3. Свойство animation-duration

Обычно в первую очередь указывается продолжительность одного цикла анимации.

Можно также указать длительность в секундах или миллисекундах, если необходима большая точность. Например, 3000 мс — это 3 с, а 1500 мс — 1,5 с.

0s        1.5s        3s
0ms       1500ms      3000ms

animation-duration: 3000m то же, что и sanimation-duration: 3s

23.4. Свойство animation-delay

Если анимация должна воспроизводиться не сразу, то можно добавить задержку, например установить время задержки в миллисекундах до начала воспроизведения анимации.

animation-delay: 1200ms   animation-duration: 1800ms