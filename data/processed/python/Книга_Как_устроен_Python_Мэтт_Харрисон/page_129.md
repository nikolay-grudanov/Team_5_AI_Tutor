---
source_image: page_129.png
page_number: 129
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.11
tokens: 7263
characters: 1339
timestamp: 2025-12-24T02:37:15.140492
finish_reason: stop
---

или

```python
>>> from sqlalchemy import schema
>>> col = schema.Column()
>>> fk = schema.ForeignKey()
```

А если вам нужен только класс Column, импортируйте этот класс одним из двух способов:

```python
>>> import sqlalchemy.schema.Column
>>> col = sqlalchemy.schema.Column()

или

>>> from sqlalchemy.schema import Column
>>> col = Column()
```

25.4. PYTHONPATH

Переменная среды PYTHONPATH содержит список нестандартных каталогов, в которых Python ищет модули или пакеты. Обычно эта переменная пуста. Изменять PYTHONPATH обычно не обязательно, если только вы в процессе разработки не хотите использовать библиотеки, которые еще не были установлены.

СОВЕТ

Оставьте переменную PYTHONPATH пустой, если только у вас нет веских причин для ее изменения. В этом разделе показано, что может произойти при ее изменении. Последствия могут сбить с толку других разработчиков, пытающихся отладить ваш код, если они забудут о том, что переменная PYTHONPATH была изменена.

Если вы включили код в файл /home/test/a/plot.py, но работали из каталога /home/test/b/, использование PYTHONPATH предоставит доступ к этому коду. В противном случае, если файл plot.py не был установлен системными средствами или средствами Python, попытка его импортирования приведет к ошибке ImportError:

```python
>>> import plot
Traceback (most recent call last):
```