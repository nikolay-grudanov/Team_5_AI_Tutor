---
source_image: page_128.png
page_number: 128
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.21
tokens: 7267
characters: 1219
timestamp: 2025-12-24T02:37:15.255906
finish_reason: stop
---

Что лучше использовать при написании кода — модуль или пакет? Я обычно начинаю с более простого варианта и использую модуль. А если мне нужно выделять отдельные части в собственные модули, я преобразую модули в пакет.

Пример структуры каталога из популярного проекта SQLAlchemy¹ (средство объектно-реляционного отображения для баз данных):

sqlalchemy/
    __init__.py
    engine/
        __init__.py
        base.py
        schema.py

Согласно PEP 8, имена каталогов пакетов должны быть короткими и записываться в нижнем регистре. Символы подчеркивания в них недопустимы.

25.3. Импортирование пакетов

Чтобы импортировать пакет, используйте команду import с именем пакета (именем каталога):

>>> import sqlalchemy

Эта команда импортирует файл sqlalchemy/__init__.py в текущее пространство имен, если пакет будет найден в PYTHONPATH или sys.path.

Если вы захотите использовать классы Column и ForeignKey из модуля schema.py, подойдет любой из следующих фрагментов. Первый включает sqlalchemy.schema в ваше пространство имен, а второй помещает в пространство имен только schema:

>>> import sqlalchemy.schema
>>> col = sqlalchemy.schema.Column()
>>> fk = sqlalchemy.schema.ForeignKey()

¹ https://www.sqlalchemy.org/