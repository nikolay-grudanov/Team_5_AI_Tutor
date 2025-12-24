---
source_image: page_728.png
page_number: 728
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.75
tokens: 11576
characters: 1339
timestamp: 2025-12-24T02:08:10.654930
finish_reason: stop
---

print('*** Error for {}: {}'.format(cc, error_msg))

return counter
# END FLAGS2_DOWNLOAD_MANY_SEQUENTIAL

if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)

Глава 19: скрипты и тесты для обработки набора данных OSCON

В примере А.12 приведен тестовый скрипт для модуля schedule1.py (пример 19.9). Используется библиотека py.test и исполнитель тестов.

Пример А.12. test_schedule1.py

import shelve
import pytest

import schedule1 as schedule

@ pytest.yield_fixture
def db():
    with shelve.open(schedule.DB_NAME) as the_db:
        if schedule.CONFERENCE not in the_db:
            schedule.load_db(the_db)
        yield the_db

def test_record_class():
    rec = schedule.Record(spam=99, eggs=12)
    assert rec.spam == 99
    assert rec.eggs == 12

def test_conference_record(db):
    assert schedule.CONFERENCE in db

def test_speaker_record(db):
    speaker = db['speaker.3471']
    assert speaker.name == 'Anna Martelli Ravenscroft'

def test_event_record(db):
    event = db['event.33950']
    assert event.name == 'There *Will* Be Bugs'

def test_event_venue(db):
    event = db['event.33950']
    assert event.venue_serial == 1449

В примере А.13 приведен полный текст скрипта schedule2.py, который был разбит на четыре части в разделе «Выборка связанных записей с помощью свойств» главы 19.