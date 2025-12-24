---
source_image: page_705.png
page_number: 705
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 87.79
tokens: 12259
characters: 3274
timestamp: 2025-12-24T02:07:53.158189
finish_reason: stop
---

Дополнительная литература

Брэндон Родес (Brandon Rhodes) — блестящий преподаватель Python, а его доклад «A Python Aesthetic: Beauty and Why I Python» (https://www.youtube.com/watch?v=x-kB2o8sd5c) великолепен, начиная уже с использования символа Unicode U+00C6 (LATIN CAPITAL LETTER AE) в названии. Другой замечательный преподаватель, Раймонд Хэттингер, говорил о красоте в Python на конференции PyCon US в своем выступлении «Transforming Code into Beautiful, Idiomatic Python» (https://www.youtube.com/watch?v=OSGv2VnC0go).

Стоит почитать обсуждение «The Evolution of Style Guides» (http://bit.ly/1e8pV4h), начатое Яном Ли (Ian Lee) в списке рассылки Python-ideas. Ли отвечает за сопровождение пакета pep8 (https://pypi.python.org/pypi/pep8/), который проверяет исходный Python-код на совместимость с документом PEP 8. Для проверки кода в этой книге я пользовался программами flake8 (https://pypi.python.org/pypi/flake8), которая обертывает pep8, pyflakes (https://pypi.python.org/pypi/pyflakes) и подключаемым модулем McCabe для оценки сложности, написанным Нэдом Бэтчелдером (Ned Batchelder) (https://pypi.python.org/pypi/mccabe).

Помимо PEP 8, есть и другие авторитетные стилистические руководства: Google Python Style Guide (https://google-styleguide.googlecode.com/svn/trunk/pyguide.html) и Pocoo Style Guide (http://www.pocoo.org/internal/styleguide/), предложенное командой, подарившей нам Flake, Sphinx, Jinja 2 и другие не менее замечательные библиотеки на Python.

Руководство автостопщика по Python (Hitchhiker's Guide to Python!) (http://docs.python-guide.org/en/latest/) — коллективный труд, посвященный написанию кода в духе Python. Наибольший вклад в него внес Кеннет Рейц (Kenneth Reitz), легендарный герой сообщества, прославившийся своим образцово «питоническим» пакетом requests. Дэвид Гуджер (David Goodger) представил на конференции PyCon US 2008 пособие под названием «Code Like a Pythonista: Idiomatic Python» (http://bit.ly/1e8r8sj). В печатном виде оно занимает 30 страниц. Разумеется, доступен исходный код в формате reStructuredText, который можно вывести в виде HTML или слайдов S5 (http://meyerweb.com/eric/tools/s5/) с помощью программы docutils. Ведь именно Гуджер и создал как reStructuredText, так и docutils, положенные в основу Sphinx, великолепной системы документирования для Python (кстати говоря, в ней подготовлена и официальная документация по MongoDB (http://bit.ly/1e8r4ss) и многим другим проектам).

Мартин Фаассен (Martijn Faassen) поднимает вопрос «Что такое дух Python?» в своем блоге (http://blog.startifact.com/posts/older/what-is-pythonic.html) В списке рассылки python-list есть обсуждение с таким же заголовком (http://bit.ly/1e8raAA). Статья Мартина относится к 2005 году, а это обсуждение — к 2003, но «питонический» идеал изменился не сильно — как, впрочем, и сам язык. Из обсуждений, в заголовке которых встречается слово «Pythonic», хотелось бы выделить «Pythonic way to sum n-th list element?» (http://bit.ly/1e8reQP), которое я обильно цитировал во врезке «Поговорим» на стр. 335.

В документе «PEP 3099 – Things that will Not Change in Python 3000» (https://www.python.org/dev/peps/pep-3099/) объясняется, почему многие вещи реализованы так, а не иначе, даже после масштабной переработки Python при выходе вер-