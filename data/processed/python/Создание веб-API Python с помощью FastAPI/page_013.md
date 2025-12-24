---
source_image: page_013.png
page_number: 13
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 51.43
tokens: 8379
characters: 1354
timestamp: 2025-12-24T02:16:19.268583
finish_reason: stop
---

Загрузите файлы примеров кода
Вы можете загрузить файлы примеров кода для этой книги с GitHub по адресу https://github.com/PacktPublishing/Building-Python-Web-APIs-with-FastAPI. Если есть обновление кода, оно будет обновлено в репозитории GitHub.

У нас также есть другие пакеты кода из нашего богатого каталога книг и видео, доступных по адресу https://github.com/PacktPublishing/. Проверь их!

Загрузите цветные изображения
Мы также предоставляем PDF-файл с цветными изображениями снимков экрана и диаграмм, использованных в этой книге. Скачать его можно здесь: https://packt.link/qqhpc.

Используемые соглашения
В этой книге используется ряд текстовых соглашений.

Код в тексте: указывает кодовые слова в тексте, имена таблиц базы данных, имена папок, имена файлов, расширения файлов, пути, фиктивные URL-адреса, пользовательский ввод и дескрипторы Twitter. Вот пример: «Чтобы вернуться к исходной основной ветке, мы запускаем git checkout main». Блок кода устанавливается следующим образом:

from fastapi import FastAPI
from routes.user import user_router

import uvicorn

Когда мы хотим привлечь ваше внимание к определенной части блока кода, соответствующие строки или элементы выделяются жирным шрифтом:

from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str