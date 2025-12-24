---
source_image: page_279.png
page_number: 279
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.47
tokens: 11493
characters: 1008
timestamp: 2025-12-24T10:30:02.030886
finish_reason: stop
---

Поскольку правильный результат функции can_hold в этом случае false, то мы должны инвертировать этот результат, прежде чем передадим его в assert! макро. Как результат, наш тест пройдёт, если can_hold вернёт false:

$ cargo test
Compiling rectangle v0.1.0 (file:///projects/rectangle)
Finished test [unoptimized + debuginfo] target(s) in 0.66s
Running unittests src/lib.rs (target/debug/deps/rectangle-6584c4561e48942e)

running 2 tests
test tests::larger_can_hold_smaller ... ok
test tests::smaller_cannot_hold_larger ... ok

test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

Doc-tests rectangle

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

Два теста работают. Теперь проверим, как отреагируют тесты, если мы добавим ошибку в код. Давайте изменим реализацию метода can_hold заменив одно из логических выражений знак сравнения с "больше чем" на противоположный "меньше чем" при сравнении ширины: