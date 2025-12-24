---
source_image: page_261.png
page_number: 261
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.55
tokens: 11770
characters: 1862
timestamp: 2025-12-24T01:46:45.140437
finish_reason: stop
---

Слабые ссылки

более 40 сортов сыра, в том числе чеддер и моцареллу, но ни одного не оказывается в продаже3.

В примере 8.18 реализован тривиальный класс, представляющий один сорт сыра.

Пример 8.18. В классе Cheese есть атрибут kind и стандартное представление

class Cheese:

    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind

В примере 8.19 каждый сорт сыра загружается из объекта catalog в объект stock, реализованный в виде WeakValueDictionary. Однако все сыры, кроме одного, исчезают из stock, как только объект catalog удаляется. Сможете ли вы объяснить, почему сыр пармезан задержался дольше остальных4? Ответ приведен в замечании после кода.

Пример 8.19. Покупатель: «Да хоть какой-нибудь сыр у вас есть?»

>>> import weakref
>>> stock = weakref.WeakValueDictionary() ①
>>> catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
...             Cheese('Brie'), Cheese('Parmesan')]
...
>>> for cheese in catalog:
...     stock[cheese.kind] = cheese ②
...
>>> sorted(stock.keys())
['Brie', 'Parmesan', 'Red Leicester', 'Tilsit'] ③
>>> del catalog
>>> sorted(stock.keys())
['Parmesan'] ④
>>> del cheese
>>> sorted(stock.keys())
[]

① stock — объект типа weakref.WeakValueDictionary.
② stock отображает название сыра на слабую ссылку на экземпляр этого сыра в каталоге catalog.
③ Склад stock полон.

3 cheeseshop.python.org — это еще и псевдоним PyPI — репозитория пакетов Python Package Index — который начал жизнь совсем пустым. На момент написания этой книги в сырной лавке Python находилось 41 426 пакетов. Неплохо, но все равно далеко от 131 000 с лишним модулей в CPAN — архиве кода на Perl — предмете зависти сообществ всех динамических языков.
4 Сыр пармезан выдерживается на фабрике как минимум год, поэтому он хранится дольше свежих сыров, но это не тот ответ, который мы ищем.