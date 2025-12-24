---
source_image: page_269.png
page_number: 269
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.65
tokens: 7350
characters: 1323
timestamp: 2025-12-24T10:52:43.507280
finish_reason: stop
---

В качестве демонстрации того, как выполнять подмножество тестов, мы создадим три теста для функции add_two, как показано в листинге 11.11, и выберем, какие из них нужно выполнить.

Листинг 11.11. Три теста с тремя разными именами

src/lib.rs
```rust
pub fn add_two(a: i32) -> i32 {
    a + 2
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn add_two_and_two() {
        assert_eq!(4, add_two(2));
    }

    #[test]
    fn add_three_and_two() {
        assert_eq!(5, add_two(3));
    }

    #[test]
    fn one_hundred() {
        assert_eq!(102, add_two(100));
    }
}
```

Если мы выполним тесты без передачи каких-либо аргументов, как мы видели ранее, то все тесты будут выполняться параллельно:

```
running 3 tests
test tests::add_two_and_two ... ok
test tests::add_three_and_two ... ok
test tests::one_hundred ... ok

test result: ok. 3 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
```

Выполнение одиночных тестов

Мы можем передать имя любой тестовой функции в команду cargo test для выполнения только этого теста:

```
$ cargo test one_hundred
    Finished dev [unoptimized + debuginfo] target(s) in 0.0 secs
    Running target/debug/deps/adder-06a75b4a1f2515e9

running 1 test
test tests::one_hundred ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 2 filtered out
```