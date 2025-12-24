---
source_image: page_290.png
page_number: 290
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 65.28
tokens: 11755
characters: 1848
timestamp: 2025-12-24T10:31:06.789232
finish_reason: stop
---

```rust
if value < 1 {
    panic!(
        "Guess value must be less than or equal to 100, got {}.",
        value
    );
} else if value > 100 {
    panic!(
        "Guess value must be greater than or equal to 1, got {}.",
        value
    );
}
```

На этот раз, когда мы выполним `should_panic` тест, он потерпит неудачу:

```
$ cargo test
Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
Finished test [unoptimized + debuginfo] target(s) in 0.66s
Running unittests src/lib.rs (target/debug/deps/guessing_game-57d70c3acb738f4d)

running 1 test
test tests::greater_than_100 - should panic ... FAILED

failures:

---- tests::greater_than_100 stdout ----
thread 'main' panicked at 'Guess value must be greater than or equal to 1, got 200.', src/lib.rs:13:13
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
note: panic did not contain expected string
    panic message: `"Guess value must be greater than or equal to 1, got 200."`,
expected substring: `"less than or equal to 100"`

failures:
    tests::greater_than_100

test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

error: test failed, to rerun pass '--lib'
```

Сообщение об ошибке указывает, что этот тест действительно вызвал панику, как мы и ожидали, но сообщение о панике не включено ожидаемую строку 'Guess value must be less than or equal to 100'. Сообщение о панике, которое мы получили в этом случае, было Guess value must be greater than or equal to 1, got 200. Теперь мы можем начать выяснение, где ошибка!

Использование `Result<T, E>` в тестах

Пока что мы написали тесты, которые паникуют, когда терпят неудачу. Мы также можем написать тесты которые используют `Result<T, E>`! Вот тест из листинга 11-1, переписанный с использованием `Result<T, E>` и возвращающий `Err` вместо паники: