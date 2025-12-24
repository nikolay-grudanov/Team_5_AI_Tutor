---
source_image: page_619.png
page_number: 619
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 50.20
tokens: 11766
characters: 1936
timestamp: 2025-12-24T02:03:43.464199
finish_reason: stop
---

Применение динамических атрибутов для обработки данных

>>> speaker = db['speaker.3471'] ①
>>> type(speaker) ②
<class 'schedule1.Record'>
>>> speaker.name, speaker.twitter ③
('Anna Martelli Ravenscroft', 'annaraven')
>>> db.close() ④

1 shelve.open открывает файл базы данных, предварительно создав его, если он еще не существует.
2 Чтобы быстро определить, заполнилась ли база данных, ищем известный ключ, в данном случае conference.115 — ключ единственной записи типа conference.7
3 Если база данных пуста, загружаем ее, вызывая load_db(db).
4 Получаем запись о докладчике speaker.
5 Это экземпляр класса Record, определенного в примере 19.9.
6 В каждом объекте Record имеется набор атрибутов, соответствующих полям хранящейся в нем JSON-записи.
7 Не забываем закрывать shelve.Shelf. По возможности следует использовать блок with, гарантирующий закрытие shelf.8

Код скрипта schedule1.py приведен в примере 19.9.

Пример 19.9. schedule1.py: исследование данных о расписании мероприятий OSCON, сохраненных в объекте shelve.Shelf

import warnings

import osconfeed ①

DB_NAME = 'data/schedule1_db'
CONFERENCE = 'conference.115'

class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs) ②

def load_db(db):
    raw_data = osconfeed.load() ③
    warnings.warn('loading ' + DB_NAME)
    for collection, rec_list in raw_data['Schedule'].items(): ④
        record_type = collection[:-1] ⑤
        for record in rec_list:
            key = '{}.{}'.format(record_type, record['serial']) ⑥
            record['serial'] = key ⑦
            db[key] = Record(**record) ⑧

7 Можно было бы также вывести значение len(db), но в случае большой базы данных оно вычислялось бы долго.
8 У системы doctest есть принципиальный недостаток — отсутствие механизма инициализации и гарантированной очистки ресурсов. Большинство тестов для скрипта schedule1.py я написал с использованием системы py.test, они приведены в примере A.12.