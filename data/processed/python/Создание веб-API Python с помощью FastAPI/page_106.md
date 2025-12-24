---
source_image: page_106.png
page_number: 106
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.86
tokens: 8227
characters: 1022
timestamp: 2025-12-24T02:18:35.595397
finish_reason: stop
---

3. Далее давайте определим конфигурацию, необходимую для создания нашей базы данных и таблицы в connection.py:

from sqlmodel import SQLModel, Session, create_engine
from models.events import Event

database_file = "planner.db"
database_connection_string = f"sqlite:///{{database_file}}"
connect_args = {"check_same_thread": False}
engine_url = create_engine(database_connection_string, echo=True, connect_args=connect_args)

def conn():
    SQLModel.metadata.create_all(engine_url)

def get_session():
    with Session(engine_url) as session:
        yield session

В этом блоке кода мы начинаем с определения зависимостей, а также импортируем класс модели таблицы. Затем мы создаем переменную, содержащую расположение файла базы данных (который будет создан, если он не существует), строку подключения и экземпляр созданной базы данных SQL. В функции conn() мы инструктируем SQLModel создать базу данных, а также таблицу, представленную в файле, Events, , и сохранить сеанс в нашем приложении, определено, get_session().