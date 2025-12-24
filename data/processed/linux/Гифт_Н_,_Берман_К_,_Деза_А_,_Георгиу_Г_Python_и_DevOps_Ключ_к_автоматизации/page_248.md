---
source_image: page_248.png
page_number: 248
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.16
tokens: 7469
characters: 2030
timestamp: 2025-12-24T03:07:22.023147
finish_reason: stop
---

но фреймворк pytest может без проблем работать и с другими структурами данных, например со списками и ассоциативными массивами. Приходилось ли вам сравнивать в тестах очень длинные списки? Вот небольшой фрагмент кода с длинными списками:

    assert ['a', 'very', 'long', 'list', 'of', 'items'] == [
        'a', 'very', 'long', 'list', 'items']
E   AssertionError: assert [...'of', 'items'] == [...ist', 'items']
E     At index 4 diff: 'of' != 'items'
E     Left contains more items, first extra item: 'items'
E     Use -v to get the full diff

Проинформировав пользователя о том, что тест не пройден, фреймворк точно указывает позицию элемента (индекс 4, то есть пятый элемент) и сообщает, что в одном из списков на один элемент больше. Без такого уровня диагностики отладка занимала бы очень много времени. Еще одно достоинство такого отчета — по умолчанию очень длинные элементы опускаются при сравнении, так что выводится только имеющая отношение к делу порция информации. В конце концов, нам хочется знать не только что списки (или другие структуры данных) различаются, но и в каком именно месте.

Параметризация

Параметризация — одна из возможностей, разобраться в которой непросто, поскольку в unittest она отсутствует и имеется только в фреймворке pytest. Но все станет понятно, когда вам придется писать очень похожие тесты, исследующие одно и то же, но с небольшими различиями во входных данных. Возьмем для примера класс для тестирования функции, которая должна возвращать True, если переданное ей строковое значение описывает истину:

from my_module import string_to_bool

class TestStringToBool(object):

    def test_it_detects_lowercase_yes(self):
        assert string_to_bool('yes')

    def test_it_detects_odd_case_yes(self):
        assert string_to_bool('YeS')

    def test_it_detects_uppercase_yes(self):
        assert string_to_bool('YES')

    def test_it_detects_positive_str_integers(self):
        assert string_to_bool('1')

    def test_it_detects_true(self):
        assert string_to_bool('true')