---
source_image: page_340.png
page_number: 340
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 54.17
tokens: 11672
characters: 1597
timestamp: 2025-12-24T10:32:54.333724
finish_reason: stop
---

Давайте посмотрим, проходит ли эта реализация тесты:

$ cargo test
Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished test [unoptimized + debuginfo] target(s) in 1.33s
    Running unittests src/lib.rs (target/debug/deps/minigrep-9cd200e5fac0fc94)

running 2 tests
test tests::case_insensitive ... ok
test tests::case_sensitive ... ok

test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

    Running unittests src/main.rs (target/debug/deps/minigrep-9cd200e5fac0fc94)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

Doc-tests minigrep

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

Отлично! Тесты прошли. Теперь давайте вызовем новую функцию search_case_insensitive из функции run. Во-первых, мы добавим параметр конфигурации в структуру Config для переключения между поиском с учётом регистра и без учёта регистра. Добавление этого поля приведёт к ошибкам компилятора, потому что мы ещё нигде не инициализируем это поле:

Файл: src/lib.rs

pub struct Config {
    pub query: String,
    pub file_path: String,
    pub ignore_case: bool,
}

Обратите внимание, что мы добавили поле case_sensitive, которое содержит логическое значение. Далее нам нужна функция run, чтобы проверить значение поля case_sensitive и использовать его, чтобы решить, вызывать ли функцию search или функцию search_case_insensitive, как показано в листинге 12-22. Обратите внимание, что код все ещё не компилируется.

Файл: src/lib.rs