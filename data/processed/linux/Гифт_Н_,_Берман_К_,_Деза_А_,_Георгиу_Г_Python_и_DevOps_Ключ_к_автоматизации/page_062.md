---
source_image: page_062.png
page_number: 62
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.34
tokens: 7464
characters: 1676
timestamp: 2025-12-24T03:02:37.161446
finish_reason: stop
---

>>> print(f'''name: {matched.group("name")}
... Secondary Level Domain: {matched.group("SLD")}
... Top Level Domain: {matched.group("TLD")}''')
name: ekoenig
Secondary Level Domain: vpwk
Top Level Domain: com

Найти все

До сих пор мы демонстрировали, как вернуть первое найденное вхождение. Но можно воспользоваться методом findall, чтобы вернуть все найденные совпадения в виде списка строковых значений:

>>> matched = re.findall(r'\w+@\w+\.\w+', cc_list)
>>> matched
['ekoenig@vpwk.com', 'rostam@vpwk.com', 'ctomson@vpwk.com', 'cbaio@vpwk.com']
>>> matched = re.findall(r'(\w+)@(\w+)\.(\w+)', cc_list)
>>> matched
[('ekoenig', 'vpwk', 'com'), ('rostam', 'vpwk', 'com'),
('ctomson', 'vpwk', 'com'), ('cbaio', 'vpwk', 'com')]
>>> names = [x[0] for x in matched]
>>> names
['ekoenig', 'rostam', 'ctomson', 'cbaio']

Поисковый итератор

При работе с большими текстами, например журналами, удобно обрабатывать текст по частям. С помощью метода finditer можно сгенерировать объект-итератор, который обрабатывает текст до момента обнаружения первого совпадения, а затем прекращает работу. Передав его функции next, можно получить текущее совпадение и продолжить обработку до момента обнаружения следующего совпадения. Таким образом можно обрабатывать каждое вхождение по отдельности и не выделять ресурсы на обработку входного текста целиком:

>>> matched = re.finditer(r'\w+@\w+\.\w+', cc_list)
>>> matched
<callable_iterator object at 0x108e68748>
>>> next(matched)
<re.Match object; span=(13, 29), match='ekoenig@vpwk.com'>
>>> next(matched)
<re.Match object; span=(51, 66), match='rostam@vpwk.com'>
>>> next(matched)
<re.Match object; span=(83, 99), match='ctomson@vpwk.com'>