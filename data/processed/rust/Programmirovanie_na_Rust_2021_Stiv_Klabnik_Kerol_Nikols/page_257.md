---
source_image: page_257.png
page_number: 257
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.90
tokens: 7461
characters: 1928
timestamp: 2025-12-24T10:52:31.207002
finish_reason: stop
---

running 2 tests
test tests::smaller_cannot_hold_larger ... ok
test tests::larger_can_hold_smaller ... ok

test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out

Оба теста успешно! Теперь давайте посмотрим, что происходит с результатами тестирования, когда мы вводим в код ошибку. Давайте изменим реализацию метода can_hold, заменив знак «больше» на «меньше», когда он сравнивает длины:

// --пропуск--
impl Rectangle {
    pub fn can_hold(&self, other: &Rectangle) -> bool {
        self.length < other.length && self.width > other.width
    }
}

В результате выполнения тестов теперь мы получаем данные, как показано ниже:

running 2 tests
test tests::smaller_cannot_hold_larger ... ok
test tests::larger_can_hold_smaller ... FAILED

failures:

---- tests::larger_can_hold_smaller stdout ----
    thread 'tests::larger_can_hold_smaller' panicked at 'assertion failed:
larger.can_hold(&smaller)', src/lib.rs:22:8
note: Run with `RUST_BACKTRACE=1` for a backtrace.

failures:
    tests::larger_can_hold_smaller

test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out

Тесты зафиксировали ошибку! Так как larger.length равно 8, а smaller.length равно 5, сравнение длин в can_hold теперь возвращает false: 8 не меньше 5.

Проверка равенства с помощью макрокоманд assert_eq! и assert_ne!

Широко распространенный способ тестирования функциональности — сравнение результата тестируемого кода со значением, которое он должен вернуть, чтобы проверить, что они равны. Вы можете сделать это с помощью макрокоманды assert!, передав ей выражения с оператором ==. Однако этот тест встречается настолько часто, что стандартная библиотека предоставляет пару макрокоманд — assert_eq! и assert_ne!, — делая выполнение его удобнее. Эти макрокоманды сравнивают два аргумента на предмет равенства или неравенства соответственно. Они также напечатают эти два значения, если утверждение не сработает, что