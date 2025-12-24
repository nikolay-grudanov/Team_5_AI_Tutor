---
source_image: page_057.png
page_number: 57
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.28
tokens: 7151
characters: 886
timestamp: 2025-12-24T02:35:27.736160
finish_reason: stop
---

Изменяемый список

Команда        Что делает компьютер
names = []     Переменные   Объекты
                names →
                Id:4f3b
                []
                Type:List

Этап 1: Python создает пустой список

names.append("Fred") Переменные   Объекты
                names →
                Id:4f3b
                []
                Type:List
                Id:4f3f
                "Fred"
                Type:String

Этап 2: Python создает объект со строкой

names.append("Fred") Переменные   Объекты
                names →
                Id:4f3b
                [ ]
                Type:List
                Id:4f3f
                "Fred"
                Type:String

Этап 3: Python вставляет строку в существующий список

Рис. 7.3. При присоединении объекта к списку изменяется значение списка. При добавлении и удалении элементов идентификатор списка не изменяется