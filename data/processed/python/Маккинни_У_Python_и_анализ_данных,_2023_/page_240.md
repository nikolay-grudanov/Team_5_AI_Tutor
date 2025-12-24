---
source_image: page_240.png
page_number: 240
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.63
tokens: 7604
characters: 1910
timestamp: 2025-12-24T02:46:35.383661
finish_reason: stop
---

Метод search возвращает специальный объект соответствия для первого встретившегося в тексте адреса. В нашем случае этот объект может сказать только о начальной и конечной позициях найденного в строке образца:

In [173]: m = regex.search(text)

In [174]: m
Out[174]: <re.Match object; span=(5, 20), match='dave@google.com'>

In [175]: text[m.start():m.end()]
Out[175]: 'dave@google.com'

Метод regex.match возвращает None, потому что находит соответствие образцу только в начале строки:

In [176]: print(regex.match(text))
None

Метод sub возвращает новую строку, в которой вхождения образца заменены указанной строкой:

In [177]: print(regex.sub("REDACTED", text))
Dave REDACTED
Steve REDACTED
Rob REDACTED
Ryan REDACTED

Предположим, что мы хотим найти почтовые адреса и в то же время разбить каждый адрес на три компонента: имя пользователя, имя домена и суффикс домена. Для этого заключим соответствующие части образца в скобки:

In [178]: pattern = r"([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})"
In [179]: regex = re.compile(pattern, flags=re.IGNORECASE)

Метод groups объекта соответствия, порожденного таким модифицированным регулярным выражением, возвращает кортеж компонентов образца:

In [180]: m = regex.match("wesm@bright.net")

In [181]: m.groups()
Out[181]: ('wesm', 'bright', 'net')

Если в образце есть группы, то метод findall возвращает список кортежей:

In [182]: regex.findall(text)
Out[182]:
[('dave', 'google', 'com'),
 ('steve', 'gmail', 'com'),
 ('rob', 'gmail', 'com'),
 ('ryan', 'yahoo', 'com')]

Метод sub тоже имеет доступ к группам в каждом найденном соответствии с помощью специальных конструкций \1, \2 и т. д.:

In [183]: print(regex.sub(r"Username: \1, Domain: \2, Suffix: \3", text))
Dave Username: dave, Domain: google, Suffix: com
Steve Username: steve, Domain: gmail, Suffix: com
Rob Username: rob, Domain: gmail, Suffix: com
Ryan Username: ryan, Domain: yahoo, Suffix: com