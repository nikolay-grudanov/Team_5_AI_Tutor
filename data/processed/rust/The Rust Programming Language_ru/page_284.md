---
source_image: page_284.png
page_number: 284
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 45.58
tokens: 11555
characters: 1271
timestamp: 2025-12-24T10:30:29.072009
finish_reason: stop
---

Требования к этой программе ещё не были согласованы и мы вполне уверены, что текст Hello в начале приветствия ещё изменится. Мы решили, что не хотим обновлять тест при изменении требований, поэтому вместо проверки на точное равенство со значением возвращённым из greeting, мы просто будем проверять, что вывод содержит текст из входного параметра.

Давайте внесём ошибку в этот код, изменяя greeting так, чтобы оно не включало name и увидим, как выглядит сбой этого теста:

```rust
pub fn greeting(name: &str) -> String {
    String::from("Hello!")
}
```

Запуск этого теста выводит следующее:

$ cargo test
Compiling greeter v0.1.0 (file:///projects/greeter)
Finished test [unoptimized + debuginfo] target(s) in 0.91s
Running unittests src/lib.rs (target/debug/deps/greeter-170b942eb5bf5e3a)

running 1 test
test tests::greeting_contains_name ... FAILED

failures:

---- tests::greeting_contains_name stdout ----
thread 'main' panicked at 'assertion failed: result.contains("\\"Carol\\")',
src/lib.rs:12:9
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

failures:
    tests::greeting_contains_name

test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

error: test failed, to rerun pass '--lib'