---
source_image: page_303.png
page_number: 303
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 61.25
tokens: 11770
characters: 1918
timestamp: 2025-12-24T10:31:30.398940
finish_reason: stop
---

Листинг 11-13: Интеграционная тест функция из крейта adder

Каждый файл в каталоге tests представляет собой отдельный крейт, поэтому нам нужно подключить нашу библиотеку в область видимости каждого тестового крейта. По этой причине мы добавляем use adder в верхней части кода, что не нужно нам делать в модульных тестах.

Нам не нужно комментировать код в tests/integration_test.rs с помощью #[cfg(test)]. Cargo специальным образом обрабатывает каталог tests и компилирует файлы в этом каталоге только тогда, когда мы запускаем команду cargo test. Запустите cargo test сейчас:

$ cargo test
Compiling adder v0.1.0 (file:///projects/adder)
Finished test [unoptimized + debuginfo] target(s) in 1.31s
Running unittests src/lib.rs (target/debug/deps/adder-1082c4b063a8fbe6)

running 1 test
test tests::internal ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

    Running tests/integration_test.rs (target/debug/deps/integration_test-1082c4b063a8fbe6)

running 1 test
test it_adds_two ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

Doc-tests adder

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

Выходные данные представлены тремя разделами: модульные тесты, интеграционные тесты и тесты документации. Обратите внимание, что если какой-нибудь тест в одной из секций не пройдёт, последующие секции выполнятся не будут. Например, если модульный тест провалился, не будет выведено результатов интеграционных и документационных тестов, потому что эти тесты будут выполняться только в том случае, если все модульные тесты завершатся успешно.

Первый раздел для модульных тестов такой же, как мы видели: одна строка для каждого модульного теста (один с именем internal, который мы добавили в листинге 11-12), а затем сводная строка для модульных тестов.