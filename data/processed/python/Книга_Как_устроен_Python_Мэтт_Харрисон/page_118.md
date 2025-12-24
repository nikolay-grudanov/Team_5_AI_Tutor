---
source_image: page_118.png
page_number: 118
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.07
tokens: 7170
characters: 749
timestamp: 2025-12-24T02:36:50.981768
finish_reason: stop
---

Субклассы

Код	Что делает компьютер

class Chair6(CorrectChair):
    max_occupants = 6

CorrectChair —> [Id:1aea]
    max_occupants
    __init__
    ...
    __class__:type
        6 Int
        4 Int
[Id:1ca8]
    __class__:function
[Id:1cb2]
    (,)
    __class__:tuple
Chair6 —> [Id:1ce4]
    max_occupants
    __bases__
    __class__:type

Рис. 22.1. Атрибут __bases__ в субклассе. Связь между субклассом и его родительскими классами позволяет искать атрибуты в четко определенном порядке. Если атрибут определен в экземпляре субкласса, то используется этот атрибут. Если нет, то после экземпляра поиск продолжается в классе (__class__) экземпляра. Если и эта попытка оказывается неудачной, поиск осуществляется в родительских классах (__bases__)