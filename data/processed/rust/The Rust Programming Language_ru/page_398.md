---
source_image: page_398.png
page_number: 398
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 52.51
tokens: 11693
characters: 1505
timestamp: 2025-12-24T10:35:12.945360
finish_reason: stop
---

```rust
pub fn add_one(x: i32) -> i32 {
    x + 1
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        assert_eq!(3, add_one(2));
    }
}
```

Теперь запустите `cargo test` в каталоге верхнего уровня `add`. Запуск `cargo test` в рабочем пространстве, структурированном подобно этому, запустит тесты для всех крейтов в рабочем пространстве:

$ cargo test
Compiling add_one v0.1.0 (file:///projects/add/add_one)
Compiling adder v0.1.0 (file:///projects/add/adder)
Finished test [unoptimized + debuginfo] target(s) in 0.27s
Running target/debug/deps/add_one-f0253159197f7841

running 1 test
test tests::it_works ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

    Running target/debug/deps/adder-49979ff40686fa8e

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

Doc-tests add_one

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

Первая секция вывода показывает, что тест `it_works` в крейте `add_one` прошёл. Следующая секция показывает, что в крейте `adder` не было обнаружено ни одного теста, а последняя секция показывает, что в крейте `add_one` не было найдено ни одного теста документации.

Мы также можем запустить тесты для одного конкретного крейта в рабочем пространстве из каталог верхнего уровня с помощью флага `-p` и указанием имени крейта для которого мы хотим запустить тесты: