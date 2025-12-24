---
source_image: page_071.png
page_number: 71
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.18
tokens: 7259
characters: 1258
timestamp: 2025-12-24T02:29:00.010703
finish_reason: stop
---

def speak(text):
    def whisper(t):
        return t.lower() + '...'
    return whisper(text)

>>> speak('Привет, Мир')
'привет, мир...'

Итак, что же тут происходит? Всякий раз, когда вы вызываете функцию speak, она определяет новую внутреннюю функцию whisper и затем после этого немедленно ее вызывает. В этом месте мой мозг начинает испытывать легкий зуд, но в целом пока материал относительно последовательный.

Правда, вот вам неожиданный поворот — функция whisper не существует за пределами функции speak:

>>> whisper('Йоу')
NameError:
"name 'whisper' is not defined"

>>> speak.whisper
    :
"'function' object has no attribute 'whisper'"

Но что, если вы действительно хотите получить доступ к этой вложенной функции whisper за пределами функции speak? Не забывайте, функции являются объектами — и вы можете вернуть внутреннюю функцию источнику вызова родительской функции.

Например, ниже приведена функция, определяющая две внутренние функции. В зависимости от аргумента, передаваемого в функцию верхнего уровня, она выбирает и возвращает источнику вызова одну из внутренних функций:

def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'
    def yell(text):
        return text.upper() + '!'
    if volume > 0.5: