---
source_image: page_530.png
page_number: 530
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.12
tokens: 7601
characters: 2157
timestamp: 2025-12-24T01:23:44.478971
finish_reason: stop
---

временами достичь похожих целей удается также с помощью глобальных имен и атрибутов функций. Вскоре мы обсудим это более подробно, но сначала давайте взглянем на рабочий код.

Оператор nonlocal в действии

Все приведенные примеры выполняются в Python 3.x. Ссылки на имена из областей видимости объемлющих def работают в Python 3.x как и в Python 2.x — в следующем коде tester создает и возвращает функцию nested, подлежащую вызову в более позднее время, а ссылка на state в nested отображается на имя в локальной области видимости tester с применением обычных правил поиска в областях видимости:

C:\code> c:\python33\python
>>> def tester(start):
    state = start  # Ссылка не нелокальные переменные работает нормально
    def nested(label):
        print(label, state)  # Запоминает state из объемлющей области видимости
        return nested
>>> F = tester(0)
>>> F('spam')
spam 0
>>> F('ham')
ham 0

Тем не менее, изменение имени из области видимости объемлющего def по умолчанию не разрешено; это также нормальное поведение в Python 2.x:

>>> def tester(start):
    state = start
    def nested(label):
        print(label, state)
        state += 1  # По умолчанию изменять нельзя (в Python 2.x вообще никогда)
        return nested
>>> F = tester(0)
>>> F('spam')
UnboundLocalError: local variable 'state' referenced before assignment
Ошибка несвязанной локальной переменной: ссылка на локальную переменную state перед ее присваиванием

Использование оператора nonlocal для изменений

Если теперь в Python 3.x объявить переменную state из области видимости tester как nonlocal внутри nested, то мы сможем ее также изменять во вложенной функции. Прием работает, несмотря на то, что к моменту вызова возвращенной функции nested через имя F функция tester уже завершилась:

>>> def tester(start):
    state = start  # Каждый вызов получает собственное значение state
    def nested(label):
        nonlocal state  # Запоминает из объемлющей области видимости
        print(label, state)
        state += 1      # Нелокальную переменную разрешено изменять
        return nested
>>> F = tester(0)
>>> F('spam')  # При каждом вызове state инкрементируется