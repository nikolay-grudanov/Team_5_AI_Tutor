---
source_image: page_189.png
page_number: 189
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.51
tokens: 7117
characters: 571
timestamp: 2025-12-24T09:24:39.027551
finish_reason: stop
---

animation-timing-function: ease-out cubic-bezier(0, 0, 0.58, 1);
Поначалу быстро и замедляется ближе к концу

animation-timing-function: ease-in-out cubic-bezier(0.42, 0, 0.58, 1);
Определяет эффект перехода с медленным началом и концом

Вы можете создавать собственные кубические кривые Безье:

cubic-bezier(P1.x, P1.y, P2.x, P2.y);
Определение пользовательского значения в функции кубической кривой Безье

Как же это работает? Две контрольные точки \( P_1 \) и \( P_2 \) передаются функции cubic-bezier в качестве аргументов. Диапазон значений составляет от 0.0 до 1.0.