---
source_image: page_124.png
page_number: 124
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.56
tokens: 7282
characters: 1216
timestamp: 2025-12-24T02:37:08.283510
finish_reason: stop
---

24.4. Вложенные библиотеки

У некоторых пакетов Python есть вложенное пространство имен. Например, библиотека XML, входящая в поставку Python, включает поддержку minidom и etree. Обе библиотеки размещаются внутри родительского пакета xml:

```python
>>> from xml.dom.minidom import \
...     parseString
>>> dom = parseString(
...     '<xml><foo/></xml>')

>>> from xml.etree.ElementTree import \
...     XML
>>> elem = XML('<xml><foo/></xml>')
```

Конструкция from позволяет импортировать только нужные функции и классы. Конструкция import (без from) увеличивает объем кода (но также открывает доступ ко всему содержимому пакета):

```python
>>> import xml.dom.minidom
>>> dom = xml.dom.minidom.parseString(
...     '<xml><foo/></xml>')

>>> import xml.etree.ElementTree
>>> elem = xml.etree.ElementTree.XML(
...     '<xml><foo/></xml>')
```

24.5. Организация импортирования

Согласно PEP 8, команды импортирования должны располагаться в начале файла за строкой документации модуля. В каждой строке должна находиться одна команда import, причем команды import должны быть объединены в группы:

○ Импортирование из стандартной библиотеки.
○ Импортирование из стороннего кода.
○ Импортирование из локальных пакетов.