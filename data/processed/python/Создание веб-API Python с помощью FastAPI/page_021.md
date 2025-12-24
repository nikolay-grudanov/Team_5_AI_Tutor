---
source_image: page_021.png
page_number: 21
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.44
tokens: 8165
characters: 603
timestamp: 2025-12-24T02:16:05.870281
finish_reason: stop
---

Ваш терминал должен выглядеть примерно так:

![Вывод команды git diff](./images/git_diff.png)

Рисунок 1.2 – Вывод команды git diff

Рекомендуется включать файл .gitignore в каждую папку. The Файл .gitignore содержит имена файлов и папок, которые Git игнорирует. Таким образом, вы можете добавить и зафиксировать все файлы в вашей папке, не опасаясь зафиксировать такие файлы, как .env.

Чтобы включить файл .gitignore, выполните в терминале следующую команду:

$ touch .gitignore

Чтобы освободить файл от отслеживания Git, добавьте его в файл .gitignore следующим образом:

$ echo ".env" >> .gitignore