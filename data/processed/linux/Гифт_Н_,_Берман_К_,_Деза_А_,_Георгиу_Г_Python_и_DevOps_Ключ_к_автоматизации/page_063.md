---
source_image: page_063.png
page_number: 63
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.30
tokens: 7478
characters: 1614
timestamp: 2025-12-24T03:02:37.534319
finish_reason: stop
---

Объект-итератор matched можно использовать и в цикле for:

```python
>>> matched = re.finditer("(?P<name>\w+)@(?P<SLD>\w+)\.(?P<TLD>\w+)", cc_list)
>>> for m in matched:
...     print(m.groupdict())
...
{'name': 'ekoenig', 'SLD': 'vpwk', 'TLD': 'com'}
{'name': 'rostam', 'SLD': 'vpwk', 'TLD': 'com'}
{'name': 'ctomson', 'SLD': 'vpwk', 'TLD': 'com'}
{'name': 'cbaio', 'SLD': 'vpwk', 'TLD': 'com'}
```

Подстановка

Помимо поиска и сопоставления с шаблоном, регулярные выражения можно использовать для замены части или всего строкового значения:

```python
>>> re.sub("\d", "#", "The passcode you entered was 09876")
'The passcode you entered was ######'
>>> users = re.sub("(?P<name>\w+)@(?P<SLD>\w+)\.(?P<TLD>\w+)",
    "\g<TLD>.\g<SLD>.\g<name>", cc_list)
>>> print(users)
Ezra Koenig <com.vpwk.ekoenig>,
Rostam Batmanglij <com.vpwk.rostam>,
Chris Tomson <com.vpwk.ctomson,
Chris Baio <com.vpwk.cbaio
```

Компиляция

Во всех приведенных до сих пор примерах непосредственно вызывались методы модуля re. Во многих случаях это допустимо, но при необходимости многократного сопоставления с одним и тем же шаблоном можно значительно повысить производительность за счет компиляции регулярного выражения в объект, который затем можно использовать для сопоставления с шаблоном без перекомпиляции:

```python
>>> regex = re.compile(r'\w+@\w+\.\w+')
>>> regex.search(cc_list)
<re.Match object; span=(13, 29), match='ekoenig@vpwk.com'>
```

Возможности регулярных выражений намного превышают продемонстрированное ранее. Их использованию посвящено множество книг, но к большинству простых сценариев применения вы уже готовы.