---
source_image: page_280.png
page_number: 280
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 66.51
tokens: 11713
characters: 1872
timestamp: 2025-12-24T10:30:40.223484
finish_reason: stop
---

// --snip--
impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width < other.width && self.height > other.height
    }
}

Запуск тестов теперь производит следующее:

$ cargo test
Compiling rectangle v0.1.0 (file:///projects/rectangle)
Finished test [unoptimized + debuginfo] target(s) in 0.66s
Running unittests src/lib.rs (target/debug/deps/rectangle-6584c4561e48942e)

running 2 tests
test tests::larger_can_hold_smaller ... FAILED
test tests::smaller_cannot_hold_larger ... ok

failures:

---- tests::larger_can_hold_smaller stdout ----
thread 'main' panicked at 'assertion failed: larger.can_hold(&smaller)', src/lib.rs:28:9
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

failures:
    tests::larger_can_hold_smaller

test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

error: test failed, to rerun pass '--lib'

Наши тесты нашли ошибку! Так как в тесте larger.width равно 8 и smaller.width равно 5 сравнение ширины в методе can_hold возвращает результат false, поскольку число 8 не меньше чем 5.

Проверка на равенство с помощью макросов assert_eq! и assert_ne!

Общим способом проверки функциональности является использование сравнения результата тестируемого кода и ожидаемого значения, чтобы убедиться в их равенстве. Для этого можно использовать макрос assert!, передавая ему выражение с использованием оператора ==. Важно также знать, что кроме этого стандартная библиотека предлагает пару макросов assert_eq! и assert_ne!, чтобы сделать тестирование более удобным. Эти макросы сравнивают два аргумента на равенство или неравенство соответственно. Макросы также печатают два значения входных параметров, если тест завершился ошибкой, что позволяет легче увидеть почему тест ошибочен. Противоположно этому, макрос assert! может только отобразить, что он