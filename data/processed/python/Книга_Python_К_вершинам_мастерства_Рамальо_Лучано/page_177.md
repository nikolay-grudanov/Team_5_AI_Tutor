---
source_image: page_177.png
page_number: 177
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.05
tokens: 11794
characters: 1898
timestamp: 2025-12-24T01:42:53.548945
finish_reason: stop
---

Получение информации о параметрах

Однако если отправить запрос на адрес http://localhost:8080/?person=Jim, то в ответ придет строка 'Hello Jim!' (см. пример 5.14).

Пример 5.14. Передача параметра person необходима для получения ответа с кодом OK

$ curl -i http://localhost:8080/?person=Jim
HTTP/1.0 200 OK
Date: Thu, 21 Aug 2014 21:42:32 GMT
Server: WSGIServer/0.2 CPython/3.4.1
Content-Type: text/html; charset=UTF-8
Content-Length: 10
Hello Jim!

Как Bobo узнает об именах параметров, необходимых функции, и о наличии у них значений по умолчанию?

У объекта-функции есть атрибут __defaults__, в котором хранится кортеж со значениями по умолчанию позиционных и именованных параметров. Значения по умолчанию чисто именованных аргументов находятся в атрибуте __kwdefaults__.
Сами же имена параметров хранятся в атрибуте __code__, который содержит ссылку на объект code с множеством собственных атрибутов.

Для демонстрации использования этих атрибутов мы проанализируем функцию clip из модуля clip.py, код которой приведен в примере 5.15.

Пример 5.15. Функция укорачивает строку, обрезая ее по пробелу вблизи указанной длины

def clip(text, max_len=80):
    """Return text clipped at the last space before or after max_len
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
    else:
        space_after = text.rfind(' ', max_len)
        if space_after >= 0:
            end = space_after
    if end is None: # no spaces were found
        end = len(text)
    return text[:end].rstrip()

В примере 5.16 показаны значения атрибутов __defaults__, __code__, co_varnames и __code__.co_argcount функции clip.

Пример 5.16. Получение информации об аргументах функции

>>> from clip import clip
>>> clip.__defaults__
(80,)
>>> clip.__code__ # doctest: +ELLIPSIS
<code object clip at 0x...>