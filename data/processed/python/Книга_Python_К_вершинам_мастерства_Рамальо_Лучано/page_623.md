---
source_image: page_623.png
page_number: 623
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.51
tokens: 11684
characters: 1698
timestamp: 2025-12-24T02:03:39.576768
finish_reason: stop
---

Применение динамических атрибутов для обработки данных

import inspect ①
import osconfeed

DB_NAME = 'data/schedule2_db' ②
CONFERENCE = 'conference.115'

class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __eq__(self, other): ③
        if isinstance(other, Record):
            return self.__dict__ == other.__dict__
        else:
            return NotImplemented

① Модуль inspect понадобится в функции load_db (пример 19.14).
② Поскольку мы храним объекты других классов, то создадим и будем использовать другой файл базы данных, 'schedule2_db' вместо 'schedule_db' из примера 19.9.
③ Метод __eq__ всегда полезно иметь для тестирования.

В Python 2 свойства поддерживаются только классами в «новом стиле». Чтобы написать такой класс в Python 2, необходимо прямо или косвенно унаследовать классу object. Класс Record из примера 19.11 является базовым классом иерархии, в которой применяются свойства, поэтому в Python 2 его объявление должно начинаться предложением¹²:

class Record(object):
    # и т. д.

Ниже показан класс специального исключения и класс DbRecord из скрипта schedule2.py.

Пример 19.12. schedule2.py: классы MissingDatabaseError и DbRecord

class MissingDatabaseError(RuntimeError):
    """Возбуждается, когда база данных необходима, но не была задана."""

class DbRecord(Record): ②
    __db = None ③

    @staticmethod ④

¹² Явное наследование классу object в Python 3 допустимо, но излишне, потому что теперь классов «в старом стиле» просто нет. Это лишь один из примеров того, как, порвав с прошлым, язык стал чище. Если требуется, чтобы один и тот же код работал и в Python 2, и в Python 3, то наследовать object необходимо явно.