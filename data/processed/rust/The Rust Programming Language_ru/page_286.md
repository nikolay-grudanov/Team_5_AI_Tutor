---
source_image: page_286.png
page_number: 286
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.90
tokens: 11531
characters: 1147
timestamp: 2025-12-24T10:30:28.842458
finish_reason: stop
---

Guess экземпляры будут содержать значения только от 1 до 100. Мы можем написать тест, который гарантирует, что попытка создать экземпляр Guess со значением вне этого диапазона вызывает панику.

Реализуем это с помощью другого атрибута тест функции #[should_panic]. Этот атрибут сообщает системе тестирования, что тест проходит, когда метод генерирует ошибку. Если ошибка не генерируется - тест считается не пройденным.

Листинг 11-8 показывает тест, который проверяет, что условия ошибки Guess::new произойдут, когда мы их ожидаем их.

Файл: src/lib.rs

```rust
pub struct Guess {
    value: i32,
}

impl Guess {
    pub fn new(value: i32) -> Guess {
        if value < 1 || value > 100 {
            panic!("Guess value must be between 1 and 100, got {}.", value);
        }
        Guess { value }
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

Листинг 11-8: Проверка того, что условие вызовет макрос panic!

Атрибут #[should_panic] следует после #[test] и до объявления текстовой функции.
Посмотрим на вывод результата, когда тест проходит: