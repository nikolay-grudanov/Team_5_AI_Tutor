---
source_image: page_211.png
page_number: 211
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.51
tokens: 7610
characters: 1875
timestamp: 2025-12-24T02:45:43.146929
finish_reason: stop
---

ве SQL (например, SQL Server, PostgreSQL и MySQL), а равно альтернативные базы данных, быстро набирающие популярность. Выбор базы данных обычно диктуется производительностью, необходимостью поддержания целостности данных и потребностями приложения в масштабируемости.

В pandas есть несколько функций для упрощения загрузки результатов SQL-запроса в DataFrame. В качестве примера я создам базу данных SQLite3, целиком размещающуюся в памяти, и драйвер sqlite3, включенный в стандартную библиотеку Python:

In [135]: import sqlite3

In [136]: query = """
......: CREATE TABLE test
......: (a VARCHAR(20), b VARCHAR(20),
......: c REAL, d INTEGER
......: );"""

In [137]: con = sqlite3.connect("mydata.sqlite")

In [138]: con.execute(query)
Out[138]: <sqlite3.Cursor at 0x7fd7d73b69c0>

In [139]: con.commit()

Затем вставлю несколько строк в таблицу:

In [140]: data = [("Atlanta", "Georgia", 1.25, 6),
......: ("Tallahassee", "Florida", 2.6, 3),
......: ("Sacramento", "California", 1.7, 5)]

In [141]: stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"

In [142]: con.executemany(stmt, data)
Out[142]: <sqlite3.Cursor at 0x7fd7d73a00c0>

In [143]: con.commit()

Большинство драйверов SQL, имеющихся в Python, при выборе данных из таблицы возвращают список кортежей:

In [144]: cursor = con.execute("SELECT * FROM test")

In [145]: rows = cursor.fetchall()

In [146]: rows
Out[146]:
[('Atlanta', 'Georgia', 1.25, 6),
 ('Tallahassee', 'Florida', 2.6, 3),
 ('Sacramento', 'California', 1.7, 5)]

Этот список кортежей можно передать конструктору DataFrame, но необходимы еще имена столбцов, содержащиеся в атрибуте курсора description. Отметим, что в случае SQLite3 атрибут description дает только имена столбцов (прочие поля, упомянутые в спецификации API доступа к базам данных из Python, равны None), но некоторые другие драйверы баз данных возвращают больше информации о столбцах: