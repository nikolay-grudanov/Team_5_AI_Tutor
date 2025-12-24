---
source_image: page_274.png
page_number: 274
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.78
tokens: 7462
characters: 1709
timestamp: 2025-12-24T10:52:51.089033
finish_reason: stop
---

Листинг 11.13. Интеграционный тест функции в упаковке adder

tests/integration_test.rs

use adder;

#[test]
fn it_adds_two() {
    assert_eq!(4, adder::add_two(2));
}

Мы добавили строку use adder в верхней части кода, которая не нужна в модульных тестах. Причина в том, что каждый тест в каталоге tests — это отдельная упаковка, поэтому нужно ввести библиотеку в область видимости каждой тестовой упаковки.

Не нужно аннотировать какой-либо код в tests/integration_test.rs с помощью #[cfg(test)]. Cargo обрабатывает каталог тестов особым образом и компилирует файлы в этом каталоге только при выполнении команды cargo test. Теперь выполните команду cargo test:

$ cargo test
Compiling adder v0.1.0 (file:///projects/adder)
Finished dev [unoptimized + debuginfo] target(s) in 0.31 secs
Running target/debug/deps/adder-abcabcabc

① running 1 test
test tests::internal ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out

② Running target/debug/deps/integration_test-ce99bcc2479f4607

running 1 test
③ test it_adds_two ... ok

④ test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out

Doc-tests adder

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out

Три раздела данных включают модульные тесты, интеграционный тест и документационные тесты. Первый раздел модульных тестов ① совпадает с тем, что мы уже видели: одна строка для каждого модульного теста (эта строка называется internal, мы добавили ее в листинге 11.12), а затем итоговая строка для модульных тестов.

Раздел интеграционных тестов начинается со строки Running target/debug/deps/integration_test-ce99bcc2479f4607 ② (хеш-код в конце вывода будет другим).