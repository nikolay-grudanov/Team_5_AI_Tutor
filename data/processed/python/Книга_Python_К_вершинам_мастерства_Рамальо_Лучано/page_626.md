---
source_image: page_626.png
page_number: 626
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 52.74
tokens: 11834
characters: 2254
timestamp: 2025-12-24T02:04:03.394676
finish_reason: stop
---

При создании имен атрибутов экземпляра из данных всегда существует риск ошибок вследствие маскирования атрибутов класса (например, методов) или потери данных из-за случайного перезаписывания уже существующих атрибутов экземпляра. Эта опасность является, пожалуй, основной причиной, по которой словари в Python по умолчанию не похожи на объекты JavaScript.

Если бы класс Record больше походил бы на отображение, т. е. реализовывал динамический метод __getitem__, а не __getattr__, то можно было бы не опасаться ошибок, вызванных маскированием или перезаписью. Специальное отображение, наверное, является наиболее отвечающим духу Python способом реализации Record. Но если бы я пошел по этому пути, то у нас не было бы шанса поразмышлять о ловушках, подстерегающих нас при программировании динамических атрибутов.
И последняя часть примера — переделанная функция load_db.

Пример 19.14. schedule2.py: функция load_db

def load_db(db):
    raw_data = osconfeed.load()
    warnings.warn('loading ' + DB_NAME)
    for collection, rec_list in raw_data['Schedule'].items():
        record_type = collection[:-1] ①
        cls_name = record_type.capitalize() ②
        cls = globals().get(cls_name, DbRecord) ③
        if inspect.isclass(cls) and issubclass(cls, DbRecord): ④
            factory = cls ⑤
        else:
            factory = DbRecord ⑥
        for record in rec_list: ⑦
            key = '{{}.{}'.format(record_type, record['serial'])
            record['serial'] = key
            db[key] = factory(**record) ⑧

① До сих пор нет отличий от функции load_db из файла schedule1.py (при мер 19.9).
② Преобразуем первую букву record_type в верхний регистр, чтобы получить потенциальное имя класса (например, 'event' превращается в 'Event').
③ Получаем объект с таким именем из глобальной области видимости модуля; если такого объекта нет, получаем DbRecord.
④ Если только что полученный объект — класс, который является подклассом DbRecord...
⑤ ... связываем с ним имя factory. Это означает, что factory может быть произвольным подклассом DbRecord, определяемым переменной record_type.
⑥ В противном случае связываем имя factory с DbRecord.
⑦ Цикл for, в котором создаются ключи и сохраняются записи, такой же, как и раньше, с тем исключением, что...