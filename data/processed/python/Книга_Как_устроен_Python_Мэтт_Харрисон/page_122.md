---
source_image: page_122.png
page_number: 122
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 7.42
tokens: 7074
characters: 605
timestamp: 2025-12-24T02:36:47.990011
finish_reason: stop
---

Субклассы

Код                Что делает компьютер

CorrectChair

class StallChair(CorrectChair):
    def __init__(self, id, is_stalled):
        super().__init__(id)
        self.is_stalled = is_stalled
        self.stalls = 0

    def load(self, number):
        if self.is_stalled(number, self):
            self.stalls += 1
        super().load(number)

StallChair

Рис. 22.3. Код создания субкласса с измененными методами. Обратите внимание на использование super() для вызова метода родительского класса. Диаграмма показывает, какие объекты создаются при создании класса, который является субклассом