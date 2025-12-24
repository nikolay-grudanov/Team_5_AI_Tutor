---
source_image: page_506.png
page_number: 506
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.99
tokens: 7652
characters: 2118
timestamp: 2025-12-24T02:54:19.692732
finish_reason: stop
---

ipdb> u
> /home/wesm/code/pydata-book/examples/ipython_bug.py(13)calling_things()
    12    works_fine()
--> 13    throws_an_exception()

Команда %pdb устанавливает режим, в котором IPython автоматически вызывает отладчик после любого исключения, многие считают этот режим особенно полезным.

Отладчик также помогает разрабатывать код, особенно когда хочется рассставить точки останова либо пройти функцию или скрипт в пошаговом режиме, изучая состояние после каждого шага. Сделать это можно несколькими способами. Первый — воспользоваться функцией %run с флагом -d, которая вызывает отладчик, перед тем как начать выполнение кода в переданном скрипте. Для входа в скрипт нужно сразу же нажать s (step — пошаговый режим):

In [5]: run -d examples/ipython_bug.py
Breakpoint 1 at /home/wesm/code/pydata-book/examples/ipython_bug.py:1
NOTE: Enter 'c' at the ipdb> prompt to start your script.
> <string>(1)<module>()

ipdb> s
--Call--
> /home/wesm/code/pydata-book/examples/ipython_bug.py(1)<module>()
1----> 1 def works_fine():
    2     a = 5
    3     b = 6

После этого вы сами решаете, каким образом работать с файлом. Например, в приведенном выше примере исключения можно было бы поставить точку останова прямо перед вызовом метода works_fine и выполнить программу до этой точки, нажав c (continue — продолжить):

ipdb> b 12
ipdb> c
> /home/wesm/code/pydata-book/examples/ipython_bug.py(12)calling_things()
    11 def calling_things():
2--> 12    works_fine()
    13    throws_an_exception()

В этот момент можно войти внутрь works_fine() командой step или выполнить works_fine() без захода внутрь, т. е. перейти к следующей строке, нажав n (next — дальше):

ipdb> n
> /home/wesm/code/pydata-book/examples/ipython_bug.py(13)calling_things()
    2    12 works_fine()
--> 13 throws_an_exception()
    14

Далее мы можем войти внутрь throws_an_exception, дойти до строки, где возникает ошибка, и изучить переменные в текущей области видимости. Отметим, что у команд отладчика больший приоритет, чем у имен переменных, поэтому для просмотра переменной с таким же именем, как у команды, необходимо предпослать ей знак !.