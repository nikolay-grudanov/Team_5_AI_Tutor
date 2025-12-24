---
source_image: page_296.png
page_number: 296
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.99
tokens: 11447
characters: 794
timestamp: 2025-12-24T10:30:47.794323
finish_reason: stop
---

Код программы 11-11: Три теста с различными именами

Если вы выполните команду `cargo test` без уточняющих аргументов, все тесты выполняются параллельно:

$ cargo test
Compiling adder v0.1.0 (file:///projects/adder)
Finished test [unoptimized + debuginfo] target(s) in 0.62s
Running unittests src/lib.rs (target/debug/deps/adder-92948b65e88960b4)

running 3 tests
test tests::add_three_and_two ... ok
test tests::add_two_and_two ... ok
test tests::one_hundred ... ok

test result: ok. 3 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

Doc-tests adder

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

Запуск одного теста

Мы можем запустить один тест с помощью указания его имени в команде `cargo test`: