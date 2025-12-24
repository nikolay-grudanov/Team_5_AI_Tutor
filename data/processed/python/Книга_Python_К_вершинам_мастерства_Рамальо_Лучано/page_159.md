---
source_image: page_159.png
page_number: 159
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 57.39
tokens: 12126
characters: 3046
timestamp: 2025-12-24T01:42:19.923060
finish_reason: stop
---

Дополнительная литература

мую. Далее в рецепте 6.11 «Чтение и запись двоичных массивов структур» показано применение модуля struct.

В блоге Ника Кофлина (Nick Coghlan) «Python Notes» есть две статьи, имеющие непосредственное отношение к этой главе: «Python 3 and ASCII Compatible Binary Protocols» (http://bit.ly/1dYuNJa) и «Processing Text Files in Python 3» (http://bit.ly/1dYuRbS). Настоятельно рекомендую.

Говоря о двоичных последовательностях, мы имеем в виду, в частности, новые конструкторы и методы в версии Python 3.5, где, кстати, один из ныне существующих конструкторов будет объявлен нерекомендуемым (см. документ «PEP 467 – Minor API improvements for binary sequences» по адресу https://www.python.org/dev/peps/pep-0467/). В Python 3.5, скорее всего, будет реализовано и предложение, описанное в документе «PEP 461 – Adding % formatting to bytes and bytearray» по адресу https://www.python.org/dev/peps/pep-0461/.

Список кодировок, поддерживаемых Python, приведен в разделе «Стандартные кодировки» (https://docs.python.org/3/library/codecs.html#standard-encodings) документации по модулю codecs. О том, как получить доступ к этому списку из программы, см. скрипт /Tools/unicode/listcodecs.py (http://bit.ly/1IqKrqD), входящий в состав дистрибутива CPython.

В статьях Мартина Фаассена (Martijn Faassen) «Changing the Python Default Encoding Considered Harmful» (http://bit.ly/1IqKu5I) и Тарека Зиада (Tarek Ziade) «sys.setdefaultencoding Is Evil» (http://blog.ziade.org/2008/01/08/syssetdefaultencoding-is-evil/) объясняется, почему никогда не следует изменять кодировку по умолчанию, полученную от функции sys.getdefaultencoding(), даже если вы разузнали, как это сделать.

Книги Jukka K. Korpela «Unicode Explained» (O'Reilly) и Richard Gillam «Unicode Demystified» (http://bit.ly/1dYveDl) (Addison-Wesley) не связаны с Python, но очень помогли мне в изучении концепций Unicode. Книга Виктора Стиннера (Victor Stinner) «Programming with Unicode» (http://unicodebook.readthedocs.org/index.html) — бесплатное произведение, опубликованное самим автором (распространяется по лицензии Creative Commons BY-SA); в ней рассматривается как сам стандарт Unicode, так и инструментальные средства и API для основных операционных систем и нескольких языков программирования, включая Python.

На страницах сайта W3C «Case Folding: An Introduction» (http://www.w3.org/International/wiki/Case_folding) и «Character Model for the World Wide Web: String Matching and Searching» (http://www.w3.org/TR/charmod-norm/) рассматривается концепция нормализации; первый документ написан в форме введения для начинающих, а второй — рабочий проект, изложенный сухим языком стандарта — в том же стиле, что «Unicode Standard Annex #15 — Unicode Normalization Forms» (http://unicode.org/reports/tr15/). Документ «Frequently Asked Questions / Normalization» (http://www.unicode.org/faq/normalization.html) на сайте Unicode.org (http://www.unicode.org/) проще для восприятия, равно как и NFC FAQ (http://www.macchiato.com/unicode/nfc-faq) Марка Дэвиса — автора