---
source_image: page_617.png
page_number: 617
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.35
tokens: 11790
characters: 2178
timestamp: 2025-12-24T02:03:32.013832
finish_reason: stop
---

Применение динамических атрибутов для обработки данных

if isinstance(arg, abc.Mapping):
    return super().__new__(cls) ②
elif isinstance(arg, abc.MutableSequence):
    return [cls(item) for item in arg]
else:
    return arg

def __init__(self, mapping):
    self.__data = {}
    for key, value in mapping.items():
        if iskeyword(key):
            key += '_'
        self.__data[key] = value

def __getattr__(self, name):
    if hasattr(self.__data, name):
        return getattr(self.__data, name)
    else:
        return FrozenJSON(self.__data[name]) ④

1 Будучи методом класса, __new__ получает в качестве первого аргумента сам класс, а остальные аргументы — те же, что получает __init__, за исключением self.
2 По умолчанию работа делегируется методу __new__ суперкласса. В данном случае мы вызываем метод __new__ из базового класса object, передавая ему FrozenJSON в качестве единственного аргумента.
3 Оставшаяся часть __new__ ничем не отличается от прежнего метода build.
4 Здесь раньше вызывался метод FrozenJSON.build, а теперь мы просто вызываем конструктор FrozenJSON.

Метод __new__ получает в качестве первого аргумента класс, потому что обычно создается экземпляр именно этого класса. Таким образом, при вызове super().__new__(cls) из FrozenJSON.__new__ в действительности вызывается object.__new__(FrozenJSON), а объект, создаваемый классом object, является экземпляром класса FrozenJSON, т. е. атрибут __class__ нового экземпляра содержит ссылку на FrozenJSON, хотя собственно конструирование производилось методом object.__new__, реализованным на С в недрах интерпретатора.

В структуре набора данных OSCON имеется очевидный недостаток: для мероприятия с индексом 40, озаглавленного 'There *Will* Be Bugs', зарегистрировано два докладчика, 3471 и 5199, но найти их нелегко, потому что это порядковые номера, а не индексы в списке Schedule.speakers. В поле venue, присутствующем в каждой записи event, также хранится порядковый номер, но для нахождения соответствующей записи о месте проведения придется выполнить линейный поиск по списку Schedule.venues. Наша следующая задача — изменить структуру данных и автоматизировать извлечение связанных записей.