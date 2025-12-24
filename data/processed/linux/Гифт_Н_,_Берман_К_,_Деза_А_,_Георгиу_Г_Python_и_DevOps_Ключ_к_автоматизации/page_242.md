---
source_image: page_242.png
page_number: 242
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.25
tokens: 7328
characters: 1560
timestamp: 2025-12-24T03:07:11.674790
finish_reason: stop
---

Тестирование с помощью pytest

Убедитесь, что pytest установлен и доступен для вызова в командной строке:

$ python3 -m venv testing
$ source testing/bin/activate

Создайте файл test_basic.py, он должен выглядеть следующим образом:

def test_simple():
    assert True

def test_fails():
    assert False

При запуске pytest без аргументов должно быть выведено сообщение о пройденном и непройденном тестах:

$ (testing) pytest
============================= test session starts ==============================
platform linux -- Python 3.6.8, pytest-4.4.1, py-1.8.0, pluggy-0.9.0
rootdir: /home/alfredo/python/testing
collected 2 items
test_basic.py .F [100%]
============================= FAILURES ================================
_________________________ test_fails _________________________________
    def test_fails():
>         assert False
E         assert False
test_basic.py:6: AssertionError
======================== 1 failed, 1 passed in 0.02 seconds =================

Выводимая информация немедленно начинает приносить пользу, показывая, сколько тестов было собрано, сколько пройдено успешно и какой тест не пройден, включая его номер строки.

Выводимая pytest по умолчанию информация полезна, но, возможно, слишком многословна. Управлять количеством выводимой информации можно с помощью настроек, чтобы сократить ее, воспользуйтесь флагом -q.

Создавать класс, включающий тесты, не обязательно — все функции были найдены и выполнены должным образом. В набор тестов могут входить тесты обоих видов, и фреймворк прекрасно работает в подобных условиях.