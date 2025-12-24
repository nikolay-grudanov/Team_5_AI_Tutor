---
source_image: page_472.png
page_number: 472
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.04
tokens: 7710
characters: 2776
timestamp: 2025-12-24T01:22:09.248018
finish_reason: stop
---

Хотя в определенных компаниях есть внутренние стандарты, не существует какого-то четкого стандарта относительно того, что должно помещаться в текст строк документации. В свое время предлагались разнообразные языки разметки и шаблоны (например, HTML или XML), но они, похоже, не обрели популярность в мире Python. Откровенно говоря, убедить программистов на Python в необходимости документировать свой код, используя вручную написанную HTML-разметку, вряд ли удастся в наше время. Может быть, мы требуем слишком много, и это неприменимо к документированию кода в целом.

Для некоторых программистов документация имеет тенденцию обладать более низким приоритетом, нежели должна. Слишком часто мы считаем себя удачливыми, если обнаруживаем в файле хоть какие-нибудь комментарии (и даже больше, когда они точны и актуальны). Я настоятельно рекомендую вам свободно документировать свой код — документация действительно является важной частью хорошо написанных программ. Однако имейте в виду, что на сегодняшний день не существует стандартов, регламентирующих структуру строк документации; если вы хотите их использовать, то сейчас подходит все, что угодно. Как и в случае написания самого кода, именно от вас зависит, создавать ли документацию и поддерживать ее в актуальном состоянии, но в такой задаче вашим лучшим союзником, вероятно, будет здравый смысл.

Встроенные строки документации

Как выясняется, встроенные модули и объекты в Python применяют похожие методики для присоединения документации помимо списков атрибутов, возвращаемых функцией dir. Скажем, чтобы увидеть фактическое описание встроенного модуля, предназначенное для человека, импортируйте модуль и выведите его строку __doc__:

>>> import sys
>>> print(sys.__doc__)
This module provides access to some objects used or maintained by the interpreter and to functions that interact strongly with the interpreter.
Dynamic objects:
argv -- command line arguments; argv[0] is the script pathname if known
path -- module search path; path[0] is the script directory, else ''
modules -- dictionary of loaded modules
...остальной текст не показан...

Функции, классы и методы внутри встроенных модулей также имеют присоединенные описания в своих атрибутах __doc__:

>>> print(sys.getrefcount.__doc__)
getrefcount(object) -> integer
Return the reference count of object. The count returned is generally one higher than you might expect, because it includes the (temporary) reference as an argument to getrefcount().

Получить сведения о встроенных функциях можно также через их строки документации:

>>> print(int.__doc__)
int(x[, base]) -> integer
Convert a string or number to an integer, if possible. A floating point argument will be truncated towards zero (this does not include a
...остальной текст не показан...