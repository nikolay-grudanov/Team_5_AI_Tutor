---
source_image: page_249.png
page_number: 249
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.21
tokens: 7531
characters: 2322
timestamp: 2025-12-24T03:07:26.408793
finish_reason: stop
---

def test_it_detects_true_with_trailing_spaces(self):
    assert string_to_bool('true ')

def test_it_detects_true_with_leading_spaces(self):
    assert string_to_bool(' true')

Видите, как все эти тесты вычисляют один и тот же результат на основе схожих входных данных? Именно в подобных случаях для группировки всех этих значений и передачи их в тест и пригодится параметризация — она позволяет свести все эти тесты к одному:

import pytest
from my_module import string_to_bool

true_values = ['yes', '1', 'Yes', 'TRUE', 'TruE', 'True', 'true']

class TestStrToBool(object):

    @pytest.mark.parametrize('value', true_values)
    def test_it_detects_truish_strings(self, value)
        assert string_to_bool(value)

Здесь происходит несколько вещей. Вначале, чтобы использовать модуль pytest.mark.parametrize, импортируется pytest (фреймворк), далее описываются true_values в виде переменной (списка) со всеми значениями, которые должны давать один результат, и, наконец, все тестовые методы заменяются одним, в котором применяется декоратор parametrize, объявляющий два аргумента. Первый представляет собой строку value, а второй — название ранее объявленного списка. Выглядит это немного странно, но, по существу, просто указывает фреймворку, что в качестве аргумента в тестовом методе необходимо использовать название value. Именно отсюда и берется аргумент value!

И хотя при запуске выводится довольно много информации, но в ней четко показано, какие значения передаются. Выглядит все практически как один тест,клонированный для каждого из переданных значений:

test_long_lines.py::TestLongLines::test_detects_truish_strings[yes] PASSED
test_long_lines.py::TestLongLines::test_detects_truish_strings[1] PASSED
test_long_lines.py::TestLongLines::test_detects_truish_strings[Yes] PASSED
test_long_lines.py::TestLongLines::test_detects_truish_strings[TRUE] PASSED
test_long_lines.py::TestLongLines::test_detects_truish_strings[TruE] PASSED
test_long_lines.py::TestLongLines::test_detects_truish_strings[True] PASSED
test_long_lines.py::TestLongLines::test_detects_truish_strings[true] PASSED

При этом в квадратных скобках выводятся значения, используемые на каждой из итераций одного и того же теста. Благодаря parametrize довольно обширный класс теста сокращается до одного тестового метода. Когда в следующий раз вы