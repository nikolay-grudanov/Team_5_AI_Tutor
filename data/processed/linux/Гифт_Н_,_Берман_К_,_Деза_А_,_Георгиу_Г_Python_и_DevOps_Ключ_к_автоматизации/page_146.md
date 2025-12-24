---
source_image: page_146.png
page_number: 146
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.45
tokens: 7330
characters: 1435
timestamp: 2025-12-24T03:04:32.825559
finish_reason: stop
---

Существует ли нужный мне модуль?

Следующий сценарий выясняет, существует ли заданный модуль, и если это так, получает путь к нему. Его удобно повторно применять для функций, использующих эту информацию для дальнейшей обработки:

try() {
    python -c "
exec('''
try:
    import ${1} as _
    print(_.__file__)
except Exception as e:
    print(e)
''')"
}

Переходим из текущего каталога по пути к модулю

При отладке библиотек и зависимостей или просто при изучении исходного кода модулей часто возникает вопрос «Где располагается этот модуль?». Способ установки и распространения модулей в Python далеко не очевиден, и в различных дистрибутивах Linux пути совершенно разные, причем применяются различные соглашения. Путь к модулю можно узнать, если импортировать его и затем воспользоваться print:

In [1]: import os

In [2]: print(os)
<module 'os' from '.virtualenvs/python-devops/lib/python3.6/os.py'>

Не слишком удобно, если вам требуется только путь, чтобы перейти по нему и посмотреть на модуль. Следующая функция пытается импортировать модуль, вывести его (напомним, что это командная оболочка, так что return ничего не делает), а затем перейти в соответствующий каталог:

cdp() {
    MODULE_DIRECTORY=`python -c "
exec('''
try:
    import os.path as _, ${module}
    print(_.dirname(_.realpath(${module}.__file__)))
except Exception as e:
    print(e)
''')`
    if [[ -d $MODULE_DIRECTORY ]]; then
        cd $MODULE_DIRECTORY