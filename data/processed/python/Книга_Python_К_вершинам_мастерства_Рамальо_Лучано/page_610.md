---
source_image: page_610.png
page_number: 610
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 45.34
tokens: 11812
characters: 2006
timestamp: 2025-12-24T02:03:07.522487
finish_reason: stop
---

Глава 19. Динамические атрибуты и свойства

С каждым из четырех ключей ассоциирован список записей. В примере 19.1 в каждом списке всего одна запись, но в полном наборе данных каждый раздел содержит списки с десятками и даже сотнями записей — за исключением раздела "conferences", в котором запись только одна — та, что показана выше. В каждой записи имеется поле "serial", уникально идентифицирующее запись в пределах списка.

Первый написанный мной скрипт просто загружает весь набор данных OSCON, но избегает лишнего трафика, проверяя наличие локальной копии. Это разумно, потому что набор OSCON 2014 уже стал достоянием истории и больше не обновляется.

В примере 19.2 нет никакого метапрограммирования. Все сводится к выражению json.load(fp), но и этого достаточно, что начать исследование набора данных. Функция osconfeed.load используется в следующих примерах.

Пример 19.2. osconfeed.py: загрузка файла osconfeed.json (doctest-скрипты приведены в примере 19.3)

from urllib.request import urlopen
import warnings
import os
import json

URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = 'data/osconfeed.json'

def load():
    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg) ①
        with urlopen(URL) as remote, open(JSON, 'wb') as local: ②
            local.write(remote.read())

    with open(JSON) as fp:
        return json.load(fp) ③

① Напечатать предупреждение, если предстоит заново загрузить файл.
② В этом предложении with используются два контекстных менеджера (разрешено, начиная с версий Python 2.7 и 3.1), чтобы прочитать удаленный файл и сохранить его.
③ Функция json.load разбирает JSON-файл и возвращает объекты Python. В данном наборе встречаются типы dict, list, str и int.

Имея этот код, мы можем проинспектировать любое поле данных.

Пример 19.3. osconfeed.py: doctest-скрипты для кода из примера 19.2

>>> feed = load() ①
>>> sorted(feed['Schedule'].keys()) ②
['conferences', 'events', 'speakers', 'venues']