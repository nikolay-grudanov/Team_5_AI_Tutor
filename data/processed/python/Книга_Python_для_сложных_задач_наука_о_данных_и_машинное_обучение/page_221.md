---
source_image: page_221.png
page_number: 221
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.75
tokens: 7435
characters: 1773
timestamp: 2025-12-24T00:57:05.936474
finish_reason: stop
---

Out[5]:    0      Peter
           1      Paul
           2     None
           3     Mary
           4    Guido
      dtype: object

С помощью Tab-автодополнения для этого атрибута str можно получить список всех векторизованных строковых методов, доступных в библиотеке Pandas.

Таблицы методов работы со строками библиотеки Pandas

Если вы хорошо разбираетесь в манипуляции строковыми данными в языке Python, львиная доля синтаксиса работы со строками библиотеки Pandas будет вам интуитивно понятна настолько, что достаточно, наверное, просто привести таблицу имеющихся методов. С этого и начнем, прежде чем углубимся в некоторые нюансы. Примеры в этом разделе используют следующий ряд имен:

In[6]: monte = pd.Series(['Graham Chapman', 'John Cleese', 'Terry Gilliam',
                         'Eric Idle', 'Terry Jones', 'Michael Palin'])

Методы, аналогичные строковым методам языка Python

Практически для всех встроенных строковых методов Python есть соответствующий векторизованный строковый метод библиотеки Pandas. Вот список методов атрибута str библиотеки Pandas, дублирующий строковые методы языка Python:

len()      lower()      translate()      islower()
ljust()    upper()      startswith()     isupper()
rjust()    find()       endswith()       isnumeric()
center()   rfind()      isalnum()         isdecimal()
zfill()    index()      isalpha()        split()
strip()    rindex()     isdigit()        rsplit()
rstrip()   capitalize() isspace()        partition()
lstrip()   swapcase()   istitle()        rpartition()

Обратите внимание, что возвращаемые значения у них отличаются. Некоторые, например lower(), возвращают Series строк:

In[7]: monte.str.lower()

Out[7]:    0      graham chapman
           1      john cleese
           2      terry gilliam