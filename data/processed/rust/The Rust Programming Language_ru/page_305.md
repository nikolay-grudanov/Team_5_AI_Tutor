---
source_image: page_305.png
page_number: 305
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 46.55
tokens: 11699
characters: 1640
timestamp: 2025-12-24T10:31:19.334540
finish_reason: stop
---

Файл: tests/common.rs

```rust
pub fn setup() {
    // setup code specific to your library's tests would go here
}
```

Когда мы снова запустим тесты, мы увидим новый раздел в результатах тестов для файла common.rs, хотя этот файл не содержит никаких тестовых функций, более того, мы даже не вызывали функцию setup откуда либо:

$ cargo test
Compiling adder v0.1.0 (file:///projects/adder)
Finished test [unoptimized + debuginfo] target(s) in 0.89s
Running unittests src/lib.rs (target/debug/deps/adder-92948b65e88960b4)

running 1 test
test tests::internal ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

    Running tests/common.rs (target/debug/deps/common-92948b65e88960b4)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

    Running tests/integration_test.rs (target/debug/deps/integration_test-92948b65e88960b4)

running 1 test
test it_adds_two ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

Doc-tests adder

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

Упоминание файла common и появление в результатах выполнения тестов сообщения типа running 0 tests - это не то, чего мы хотели. Мы только хотели выделить некоторый общий код, который будет использоваться другими файлами интеграционных тестов.

Чтобы модуль common больше не появлялся в результатах выполнения тестов, вместо файла tests/common.rs мы создадим файл tests/common/mod.rs. Директория проекта теперь выглядит следующим образом: