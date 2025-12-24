---
source_image: page_481.png
page_number: 481
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.18
tokens: 11723
characters: 1988
timestamp: 2025-12-24T01:57:16.325556
finish_reason: stop
---

Использование @contextmanager

Из всех этих утилит чаще всего, безусловно, используется декоратор @contextmanager, поэтому уделим ему особое внимание. Этот декоратор интересен еще и тем, что предложение yield применяется в нем для целей, не связанных с итерированием. И тем самым мы пролагаем путь к концепции сопрограммы — теме следующей главы.

Использование @contextmanager

Декоратор @contextmanager уменьшает объем стереотипного кода создания контекстного менеджера: вместо того чтобы писать целый класс с методами __enter__/__exit__, мы просто реализуем генератор с одним предложением yield, которое порождает значение, когда должен вернуть управление метод __enter__.

Если генератор снабжен декоратором @contextmanager, то yield разбивает тело функции на две части: все, что находится до yield, исполняется в начале блока with, когда интерпретатор вызывает метод __enter__; а все, что находится после yield, выполняется при вызове метода __exit__ в конце блока.

В примере 15.5 класс LookingGlass из примера 15.3 заменен генераторной функцией.

Пример 15.5. mirror_gen.py: реализация контекстного менеджера с помощью генератора

import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])
        sys.stdout.write = reverse_write
        yield 'JABBERWOCKY'
        sys.stdout.write = original_write

1 Применяем декоратор contextmanager.
2 Сохраняем исходный метод sys.stdout.write.
3 Определяем функцию reverse_write; original_write будет доступна в замыкании.
4 Заменяем sys.stdout.write функцией reverse_write.
5 Отдаем значение, которое будет связано с переменной в части as предложения with. В этой точке функция приостанавливается на время выполнения блока with.
6 Когда управление покидает блок with любым способом, выполнение функции возобновляется с места, следующего за yield; в данном случае мы восстанавливаем исходный метод sys.stdout.write.