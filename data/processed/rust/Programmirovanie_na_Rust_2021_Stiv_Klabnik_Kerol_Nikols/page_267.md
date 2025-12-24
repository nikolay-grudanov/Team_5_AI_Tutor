---
source_image: page_267.png
page_number: 267
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.06
tokens: 7383
characters: 1558
timestamp: 2025-12-24T10:52:43.267854
finish_reason: stop
---

Показ результатов функции

По умолчанию, если тест успешен, библиотека тестов перехватывает все, что выводится в стандартном выводе данных. Например, если мы вызовем макрокоманду println! в тесте, а тест выполнится успешно, то мы не увидим данные работы println! в терминале — появится только строчка, которая указывает, что тест успешен. Если тест не сработает, то мы увидим все, что было в стандартном выводе данных вместе с остальной частью сообщения об ошибке.

Например, листинг 11.10 содержит глупую функцию, которая выводит значение своего параметра и возвращает 10, а также успешный и неуспешный тесты.

Листинг 11.10. Тесты для функции, которая вызывает макрокоманду println!

src/lib.rs

```rust
fn prints_and_returns_10(a: i32) -> i32 {
    println!("Я получил значение {}", a);
    10
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn this_test_will_pass() {
        let value = prints_and_returns_10(4);
        assert_eq!(10, value);
    }

    #[test]
    fn this_test_will_fail() {
        let value = prints_and_returns_10(8);
        assert_eq!(5, value);
    }
}
```

Когда мы выполним эти тесты с помощью команды cargo test, то увидим данные ниже:

```
running 2 tests
test tests::this_test_will_pass ... ok
test tests::this_test_will_fail ... FAILED

failures:

---- tests::this_test_will_fail stdout ----
    ① Я получил значение 8
thread 'tests::this_test_will_fail' panicked at 'assertion failed: `(left == right)`
    left: `5`,
    right: `10`', src/lib.rs:19:8
note: Run with `RUST_BACKTRACE=1` for a backtrace.
```