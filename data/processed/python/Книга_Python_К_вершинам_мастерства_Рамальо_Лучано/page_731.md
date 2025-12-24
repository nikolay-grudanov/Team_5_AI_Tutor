---
source_image: page_731.png
page_number: 731
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.34
tokens: 11589
characters: 1529
timestamp: 2025-12-24T02:08:28.136226
finish_reason: stop
---

Глава 19: скрипты и тесты для обработки набора данных OSCON

if hasattr(self, 'name'):
    cls_name = self.__class__.__name__
    return '<{} {!r}>'.format(cls_name, self.name)
else:
    return super().__repr__()
# END SCHEDULE2_EVENT

# BEGIN SCHEDULE2_LOAD
def load_db(db):
    raw_data = osconfeed.load()
    warnings.warn('loading ' + DB_NAME)
    for collection, rec_list in raw_data['Schedule'].items():
        record_type = collection[:-1]
        cls_name = record_type.capitalize()
        cls = globals().get(cls_name, DbRecord)
        if inspect.isclass(cls) and issubclass(cls, DbRecord):
            factory = cls
        else:
            factory = DbRecord
        for record in rec_list:
            key = '{}.{}'.format(record_type, record['serial'])
            record['serial'] = key
            db[key] = factory(**record)
# END SCHEDULE2_LOAD

Код из примера А.14 использовался для тестирования примера А.13 с применением библиотеки py.test.

Пример А.14. test_schedule2.py

import shelve
import pytest

import schedule2 as schedule

@pytest.yield_fixture
def db():
    with shelve.open(schedule.DB_NAME) as the_db:
        if schedule.CONFERENCE not in the_db:
            schedule.load_db(the_db)
        yield the_db

def test_record_attr_access():
    rec = schedule.Record(spam=99, eggs=12)
    assert rec.spam == 99
    assert rec.eggs == 12

def test_record_repr():
    rec = schedule.DbRecord(spam=99, eggs=12)
    assert 'DbRecord object at 0x' in repr(rec)
    rec2 = schedule.DbRecord(serial=13)