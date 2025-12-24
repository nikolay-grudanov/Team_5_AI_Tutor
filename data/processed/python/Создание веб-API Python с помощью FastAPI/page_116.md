---
source_image: page_116.png
page_number: 116
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.00
tokens: 8470
characters: 1850
timestamp: 2025-12-24T02:19:06.768074
finish_reason: stop
---

Теперь, когда мы знаем, как создать документ, давайте рассмотрим методы, используемые для выполнения CRUD операций:

• .insert() и .create(): Методы .insert() и .create() вызываются экземпляром документа для создания новой записи в базе данных. Вы также можете использовать метод .insert_one() для добавления отдельной записи в базу данных.

Чтобы вставить много записей в базу данных, вызывается метод .insert_many(), который принимает список экземпляров документа, например:

event = Event(name="Packt office launch",
location="Hybrid")
await event.create()
await Event.insert_one(event)

• .find() и .get(): Метод .find() используется для поиска списка документов, соответствующих критериям поиска, переданным в качестве аргумента метода. Метод .get() используется для получения одного документа, соответствующего предоставленному идентификатору. Отдельный документ, соответствующий критерию поиска, можно найти с помощью метода .find_one(), например следующего:

event = await Event.get("74478287284ff")
event = await Event.find(Event.location == "Hybrid").to_list() # Returns a list of matching items
event = await.find_one(Event.location == "Hybrid") # Returns a single event

• .save(), .update(), и .upsert(): Для обновления документа можно использовать любой из этих методов. Метод .update() принимает запрос на обновление, а метод .upsert() используется, когда документ не соответствует критериям поиска. В этой главе мы будем использовать метод .update(). Запрос на обновление — это инструкция, за которой следует база данных MongoDB, например, следующая:

event = await Event.get("74478287284ff")
update_query = {"$set": {"location": "virtual"}}
await event.update(update_query)

В этом блоке кода мы сначала извлекаем событие, а затем создаем запрос на обновление, чтобы установить для поля location в коллекции событий значение virtual.