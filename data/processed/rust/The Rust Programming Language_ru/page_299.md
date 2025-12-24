---
source_image: page_299.png
page_number: 299
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.18
tokens: 11439
characters: 809
timestamp: 2025-12-24T10:30:47.938156
finish_reason: stop
---

$ cargo test -- --ignored
  Compiling adder v0.1.0 (file:///projects/adder)
  Finished test [unoptimized + debuginfo] target(s) in 0.61s
  Running unittests src/lib.rs (target/debug/deps/adder-92948b65e88960b4)

running 1 test
test expensive_test ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 1 filtered out;
finished in 0.00s

Doc-tests adder

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

Управляя тем, какие тесты запускать, вы можете быть уверены, что результаты вашего cargo test будут быстрыми. Вы можете фильтровать тесты по имени при запуске. Вы также можете указать какие тесты должны быть проигнорированы при помощи ignored, а также отдельно запускать проигнорированные тесты при помощи cargo test -- --ignored.