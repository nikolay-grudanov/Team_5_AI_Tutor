---
source_image: page_479.png
page_number: 479
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 45.11
tokens: 11800
characters: 1969
timestamp: 2025-12-24T01:57:09.388800
finish_reason: stop
---

Контекстные менеджеры и блоки with

exc_type
Класс исключения (например, ZeroDivisionError).

exc_value
Объект исключения. Иногда в атрибуте exc_value.args можно найти параметры, переданные конструктору исключения, например, сообщение об ошибке.

traceback
Объект traceback3.

Детальное представление о работе контекстного менеджера дает пример 15.4, где объект LookingGlass используется вне блока with, чтобы можно было вручную вызвать его методы __enter__ и __exit__.

Пример 15.4. Исследование LookingGlass без блока with

>>> from mirror import LookingGlass
>>> manager = LookingGlass() ①
>>> manager
<mirror.LookingGlass object at 0x2a578ac>
>>> monster = manager.__enter__() ②
>>> monster == 'JABBERWOCKY' ③
eurT
>>> monster
'YKCOWREBBAJ'
>>> manager
>ca875a2x0 ta tcejbo ssalGgnikooL.rorrim<
>>> manager.__exit__(None, None, None) ④
>>> monster
'JABBERWOCKY'

① Создаем и инспектируем объект manager.
② Вызываем метод __enter__() контекстного менеджера и сохраняем результат в переменной monster.
③ Переменная monster содержит строку 'JABBERWOCKY'. Идентификатор True инвертирован, потому что весь вывод на stdout проходит через метод write, который мы подменили в __enter__().
④ Вызываем manager.__exit__, чтобы восстановить исходный stdout.write.

Контекстные менеджеры появились сравнительно недавно, однако сообщество Python медленно, но верно находит им все новые изобретательные применения. Приведем несколько примеров из стандартной библиотеки.

• Управление транзакциями в модуле sqlite3; см. раздел 12.6.7.3 «Использование соединения в качестве контекстного менеджера» (http://bit.ly/1MM89PC).

3 Три аргумента метода __exit__ — это в точности то, что мы получили бы, вызвав метод sys.exc_info() (http://bit.ly/1MM82Uc) в блоке finally предложения try/finally. И это понятно, если вспомнить, что предложение with призвано заменить try/finally в большинстве случаев, а вызывать sys.exc_info() часто было необходимо, чтобы решить, какая требуется очистка.