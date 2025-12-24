---
source_image: page_093.png
page_number: 93
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.80
tokens: 7506
characters: 1759
timestamp: 2025-12-24T02:42:20.112060
finish_reason: stop
---

f = open(path, mode="w")

try:
    write_to_file(f)
except:
    print("Ошибка")
else:
    print("Все хорошо")
finally:
    f.close()

Исключения в IPython
Если исключение возникает в процессе выполнения скрипта командой %run или при выполнении любого предложения, то IPython по умолчанию распечатывает весь стек (выполняет трассировку стека) и несколько строк вокруг каждого предложения в стеке, чтобы можно было понять контекст:

In [10]: %run examples/ipython_bug.py

AssertionError
Traceback (most recent call last)
/home/wesm/code/pydata-book/examples/ipython_bug.py in <module>()
    13 throws_an_exception()
    14
--> 15 calling_things()

/home/wesm/code/pydata-book/examples/ipython_bug.py in calling_things()
    11 def calling_things():
    12 works_fine()
--> 13 throws_an_exception()
    14
    15 calling_things()

/home/wesm/code/pydata-book/examples/ipython_bug.py in throws_an_exception()
    7 a = 5
    8 b = 6
--> 9 assert(a + b == 10)
    10
    11 def calling_things():

AssertionError:

Наличие дополнительного контекста уже является весомым преимуществом по сравнению со стандартным интерпретатором Python (который никакого контекста не выводит). Объемом контекста можно управлять с помощью магической команды %xmode, он может варьироваться от Plain (так же, как в стандартном интерпретаторе Python) до Verbose (печатаются значения аргументов функций и многое другое). Ниже в приложении В мы увидим, что можно пошагово выполнять стек (с помощью команды %debug или %pdb) после возникновения ошибки, т. е. производить интерактивную постоперационную отладку.

3.3. Файлы и операционная система
В этой книге для чтения файла с диска и загрузки данных из него в структуры Python, как правило, используются такие высокоуровневые средства, как