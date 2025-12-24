---
source_image: page_262.png
page_number: 262
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.13
tokens: 7311
characters: 1280
timestamp: 2025-12-24T10:52:35.395215
finish_reason: stop
---

Листинг 11.8 показывает тест, который проверяет, что условия возникновения ошибки функции Guess::new наступают тогда, когда мы этого ожидаем.

Листинг 11.8. Проверка того, что условие станет причиной для panic!

src/lib.rs

```rust
pub struct Guess {
    value: i32,
}

impl Guess {
    pub fn new(value: i32) -> Guess {
        if value < 1 || value > 100 {
            panic!("Значение догадки должно быть между 1 и 100, получено {}.", value);
        }
        Guess {
            value
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    #[should_panic]
    fn greater_than_100() {
        Guess::new(200);
    }
}
```

Мы помещаем атрибут #[should_panic] после атрибута #[test] и перед тестовой функцией, к которой он применяется. Давайте посмотрим на результат, когда этот тест срабатывает:

```
running 1 test
test tests::greater_than_100 ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
```

Выглядит неплохо! Теперь давайте введем в код ошибку, удалив условие, что функция new будет паниковать, если значение больше 100:

```rust
// --пропуск--

impl Guess {
    pub fn new(value: i32) -> Guess {
        if value < 1 {
            panic!("Значение догадки должно быть между 1 и 100, получено {}.", value);
```