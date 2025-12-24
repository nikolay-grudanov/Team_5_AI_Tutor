---
source_image: page_281.png
page_number: 281
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 55.64
tokens: 11668
characters: 1430
timestamp: 2025-12-24T10:30:29.715138
finish_reason: stop
---

вычислил значение `false` для выражения `==`, но не значения, которые привели к результату `false`.

В листинге 11-7, мы напишем функцию `add_two`, которая прибавляет к входному параметру `2` и возвращает значение. Затем, протестируем эту функцию с помощью макроса `assert_eq!`:

Файл: src/lib.rs

```rust
pub fn add_two(a: i32) -> i32 {
    a + 2
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_adds_two() {
        assert_eq!(4, add_two(2));
    }
}
```

Листинг 11-7: Тестирование функции `add_two` с помощью макроса `assert_eq!`

Проверим, что тесты проходят!

$ cargo test
Compiling adder v0.1.0 (file:///projects/adder)
Finished test [unoptimized + debuginfo] target(s) in 0.58s
Running unittests src/lib.rs (target/debug/deps/adder-92948b65e88960b4)

running 1 test
test tests::it_adds_two ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

Doc-tests adder

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

Первый аргумент, который мы передаём в макрос `assert_eq!` число `4` чей результат вызова равен `add_two(2)`. Строка для этого теста - `test tests::it_adds_two ... ok`, а текст `ok` означает, что наш тест пройден!

Давайте введём ошибку в код, чтобы увидеть, как она выглядит, когда тест, который использует `assert_eq!` завершается ошибкой. Измените реализацию функции `add_two`,