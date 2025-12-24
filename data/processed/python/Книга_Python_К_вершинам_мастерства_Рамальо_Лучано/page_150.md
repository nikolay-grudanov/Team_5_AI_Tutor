---
source_image: page_150.png
page_number: 150
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 58.33
tokens: 11967
characters: 2418
timestamp: 2025-12-24T01:41:55.397125
finish_reason: stop
---

перечислены в статье MSDN «Language Identifier Constants and Strings» (http://bit.ly/1IqyKAl), а идентификаторы кодовых страниц — в статье «Code Page Identifiers» (http://bit.ly/1IqyP79)10.

• Локаль должна быть правильно реализована производителем ОС. С Ubuntu 14.04 мне повезло, а с OS X (Mavericks 10.9) — нет. На двух разных компьютерах Mac обращение setlocale(LC_COLLATE, 'pt_BR.UTF-8') честно возвращало строку 'pt_BR.UTF-8'. Однако вызов sorted(fruits, key=locale.strxfrm) давал тот же неправильный результат, что и sorted(fruits). Я пробовал также локали fr_FR, es_ES и de_DE в OS X, но ни разу locale.strxfrm не отработала, как положено11.

Таким образом, содержащееся в стандартной библиотеке решение для интернационализированной сортировки работает, но лучше всего поддерживано в GNU/Linux (или в Windows, если вы специалист по этой ОС). Но даже в этом случае оно зависит от настройки локали, что может вызвать неприятности при развертывании.

По счастью, существует более простое решение: библиотека PyUCA, доступная на сайте PyPI.

Сортировка с помощью алгоритма упорядочивания Unicode

Джеймсу Тауберу (James Tauber), автору многих проектов для Django, должно быть, надоела эта путаница, и он написал модуль PyUCA (https://pypi.python.org/pypi/ruycsa/), реализацию алгоритма упорядочивания Unicode (Unicode Collation Algorithm — UCA) на чистом Python. В примере 4.20 показано, как просто его использовать.

Пример 4.20. Использование метода pyuca.Collator.sort_key

```python
>>> import pyuca
>>> coll = pyuca.Collator()
>>> fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
>>> sorted_fruits = sorted(fruits, key=coll.sort_key)
>>> sorted_fruits
['açaí', 'acerola', 'atemoia', 'cajá', 'caju']
```

Метод удобный и работает правильно. Я проверял его в системах GNU/Linux, OS X и Windows. В настоящее время поддерживаются только версии Python 3.x.

Библиотека PyUCA не обращает внимания на локаль. Если требуется изменить порядок сортировки, укажите путь к своей таблице упорядочения при

10 Спасибо Леонардо Рахаэлю, который не ограничился обязанностями технического рецензента, а нашел эти сведения, относящиеся к Windows, хотя сам работает с GNU/Linux.
11 Я не смог найти решение, но другие тоже жаловались на эту проблему. Алекс Мартелли, один из технических рецензентов, не сталкивался с ошибкой при использовании setlocale и locale.strxfrm на своем Mac с OS X 10.9. Короче говоря, как повезет.