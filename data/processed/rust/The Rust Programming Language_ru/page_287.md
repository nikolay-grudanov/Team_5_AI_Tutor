---
source_image: page_287.png
page_number: 287
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 9.08
tokens: 11311
characters: 419
timestamp: 2025-12-24T10:30:01.658556
finish_reason: stop
---

Выглядит хорошо! Теперь давайте внесём ошибку в наш код, убрав условие о том, что функция `new` будет паниковать если значение больше 100:

```rust
// --snip--
impl Guess {
    pub fn new(value: i32) -> Guess {
        if value < 1 {
            panic!("Guess value must be between 1 and 100, got {}.", value);
        }

        Guess { value }
    }
}
```

Когда мы запустим тест в листинге 11-8, он потерпит неудачу: