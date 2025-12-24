---
source_image: page_146.png
page_number: 146
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.81
tokens: 11813
characters: 2051
timestamp: 2025-12-24T01:41:22.496150
finish_reason: stop
---

norm_txt = unicodedata.normalize('NFD', txt)
shaved = ''.join(c for c in norm_txt
    if not unicodedata.combining(c))
return unicodedata.normalize('NFC', shaved)

1 Разлагаем все символы на базовые и модифицирующие.
2 Находим все модифицирующие символы.
3 Производим обратную композицию.

В примере 4.15 демонстрируются два применения функции shave_marks.

Пример 4.15. Два применения функции shave_marks из примера 4.14

>>> order = '"Herr Voß: • ½ cup of Etker™ caffè latte • bowl of açaí."'
>>> shave_marks(order)
'"Herr Voß: • ½ cup of Etker™ caffe latte • bowl of acai."'
>>> Greek = 'Ζέφυρος, Zéfiro'
>>> shave_marks(Greek)
'Ζεφυρος, Zefiro'

1 Заменены только буквы «è», «ç» и «í».
2 Заменены буквы «έ» и «é».

Функция shave_marks работает правильно, но, быть может, чрезмерно усердствует. Часто диакритические знаки удаляются только для того, чтобы перевести текст из кодировки Latin в чистый ASCII, но shave_marks изменяет также и нелатинские символы, например греческие буквы, которые — что с акцентами, что без — никогда не превратятся в ASCII. Поэтому имеет смысл проанализировать каждый базовый символ и удалять присоединенные знаки, только если он является буквой из набора символов Latin. Именно это делает функция из примера 4.16.

Пример 4.16. Функция удаления модифицирующих знаков только для символов из набора Latin (предложения импорта опущены, поскольку это часть модуля sanitize.py из примера 4.14)

def shave_marks_latin(txt):
    """Удалить все диакритические знаки для базовых символов набора Latin"""
    norm_txt = unicodedata.normalize('NFD', txt)
    latin_base = False
    keepers = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:
            continue # игнорировать диакритические знаки
            # для базовых символов набора Latin
        keepers.append(c) # если это не модифицирующий символ, значит новый базовый
        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters
    shaved = ''.join(keepers)
    return unicodedata.normalize('NFC', shaved)