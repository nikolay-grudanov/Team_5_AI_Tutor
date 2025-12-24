---
source_image: page_691.png
page_number: 691
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.89
tokens: 11669
characters: 1444
timestamp: 2025-12-24T02:06:42.388745
finish_reason: stop
---

Основы метаклассов

И снова возьмите бумагу и ручку и выпишите пронумерованные маркеры <[N]> в порядке их вывода.

Упражнение 3
Модуль evaltime_meta.py интерактивно импортируется в оболочке Python.

Упражнение 4
Модуль evaltime_meta.py выполняется из командной строки.

Решения и анализ приведены ниже.

Решение упражнения 3
В примере 21.11 показан результат импорта evaltime_meta.py в оболочке Python.

Пример 21.11. Упражнение 3: импорт evaltime_meta в оболочке Python

>>> import evaltime_meta
<[100]> evalsupport module start
<[400]> MetaAleph body
<[700]> evalsupport module end
<[1]> evaltime_meta module start
<[2]> ClassThree body
<[200]> deco_alpha
<[4]> ClassFour body
<[6]> ClassFive body
<[500]> MetaAleph.__init__ ①
<[9]> ClassSix body
<[500]> MetaAleph.__init__ ②
<[15]> evaltime_meta module end

① Основное отличие от упражнения 1 состоит в том, что метод MetaAleph.__init__ вызывается для инициализации только что созданного класса ClassFive.
② И тот же метод MetaAleph.__init__ инициализирует класс ClassSix, являющийся подклассом ClassFive.

Интерпретатор Python обрабатывает тело ClassFive, но затем для построения самого тела класса вызывает не type, а MetaAleph. Взглянув на определение класса MetaAleph в примере 21.12, мы увидим, что метод __init__ получает четыре аргумента:

self
Это инициализируемый объект класса (например, ClassFive).
name, bases, dic
Те же аргументы, что передаются type для конструирования класса.