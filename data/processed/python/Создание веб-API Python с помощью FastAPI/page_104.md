---
source_image: page_104.png
page_number: 104
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.29
tokens: 8391
characters: 1666
timestamp: 2025-12-24T02:18:38.562136
finish_reason: stop
---

Метод create_engine() принимает в качестве аргумента URL-адрес базы данных. URL-адрес базы данных имеет вид sqlite:///database.db или sqlite:///database.sqlite. Он также принимает необязательный аргумент echo, который, если установлено значение True распечатывает команды SQL, выполняемые при выполнении операции.

Однако одного метода create_engine() одного метода для создания файла базы данных. Чтобы создать файл базы данных, вызывается метод, SQLModel.metadata.create_all(engine), аргументом которого является экземпляр метода create_engine(), например:

```python
database_file = "database.db"
engine = create_engine(database_file, echo=True)
SQLModel.metadata.create_all(engine)
```

Метод create_all() создает базу данных, а также определенные таблицы. Важно отметить, что файл, содержащий таблицы, импортируется в файл, в котором происходит подключение к базе данных.

В нашем приложении-планировщике мы выполняем CRUD операции для событий. В папке базы данных создайте следующий модуль:

connection.py

В этом файле мы настроим необходимые данные для базы данных:

(venv)$ touch database/connection.py

Теперь, когда мы создали файл подключения к базе данных, давайте создадим функции, необходимые для подключения нашего приложения к базе данных:

1. Мы начнем с обновления класса модели событий, определенного в models/events.py, до класса модели таблицы SQLModel:

```python
from sqlmodel import JSON, SQLModel, Field, Column
from typing import Optional, List

class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
```