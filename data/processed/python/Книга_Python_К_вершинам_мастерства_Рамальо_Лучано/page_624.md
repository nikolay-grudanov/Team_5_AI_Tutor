---
source_image: page_624.png
page_number: 624
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.76
tokens: 11660
characters: 1807
timestamp: 2025-12-24T02:03:39.267103
finish_reason: stop
---

def set_db(db):
    DbRecord.__db = db

@staticmethod
def get_db():
    return DbRecord.__db

@classmethod
def fetch(cls, ident):
    db = cls.get_db()
    try:
        return db[ident]
    except TypeError:
        if db is None:
            msg = "database not set; call '{}.set_db(my_db)'"
            raise MissingDatabaseError(msg.format(cls.__name__))
        else:
            raise

def __repr__(self):
    if hasattr(self, 'serial'):
        cls_name = self.__class__.__name__
        return '<{} serial={!r}>'.format(cls_name, self.serial)
    else:
        return super().__repr__()

1 Специальные исключения — обычно просто маркерные классы, не имеющие тела. Строка документации с объяснением порядка использования исключения лучше, чем одно лишь предложение pass.
2 Класс DbRecord расширяет Record.
3 В атрибуте класса _db хранится ссылка на открытую базу данных shelve.Shelf.
4 Метод set_db снабжен декоратором staticmethod, чтобы явно показать, что его результат не зависит от способа вызова.
5 Даже если этот метод вызывается как Event.set_db(my_db), атрибут _db будет установлен в классе DbRecord.
6 Метод get_db также снабжен декоратором staticmethod, потому что он всегда возвращает объект, на который ссылается DbRecord._db, вне зависимости от того, как вызван.
7 fetch — метод класса, чтобы его поведение было проще изменить в подклассах.
8 Здесь из базы данных выбирается запись с ключом ident.
9 Если мы получили исключение TypeError и db равно None, возбуждаем специальное исключение, означающее, что необходимо задать базу данных.
10 В противном случае повторно возбуждаем исключение, потому что не знаем, как его обрабатывать.
11 Если в записи есть атрибут serial, включаем его в строковое представление.
12 В противном случае по умолчанию используем унаследованный метод __repr__.