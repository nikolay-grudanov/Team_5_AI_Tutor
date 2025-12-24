---
source_image: page_191.png
page_number: 191
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.40
tokens: 7175
characters: 846
timestamp: 2025-12-24T03:05:47.299431
finish_reason: stop
---

Преобразование с WordPress на Hugo

![Схема преобразования с WordPress на Hugo](https://i.imgur.com/3Q5z5QG.png)

Рис. 6.1. Непрерывное развертывание с помощью Hugo

Настройка Hugo

Начать работать с Hugo очень просто (см. руководство по началу работы с Hugo (https://oreil.ly/r_Rcg)). Во-первых, необходимо его установить. На моей машине под управлением OS X я воспользовался командой

brew install hugo

Если вы уже установили Hugo, возможно, необходимо его обновить:

Error: hugo 0.40.3 is already installed
To upgrade to 0.57.2, run brew upgrade hugo.

Если вы работаете на другой платформе, можете использовать инструкции, приведенные тут: https://oreil.ly/FfWdo. Чтобы проверить, что все работает, выполните команду hugo version:

(.python-devops) → ~ hugo version
Hugo Static Site Generator v0.57.2/extended darwin/amd64 BuildDate: unknown