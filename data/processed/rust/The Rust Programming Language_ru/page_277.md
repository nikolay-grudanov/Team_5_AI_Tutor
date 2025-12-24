---
source_image: page_277.png
page_number: 277
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.55
tokens: 11609
characters: 1467
timestamp: 2025-12-24T10:30:04.038009
finish_reason: stop
---

аварийным. Использование макроса assert! помогает проверить, что код функционирует как ожидалось.

В главе 5, листинга 5-15, мы использовали структуру Rectangle и метод can_hold, который повторён в листинге 11-5. Давайте поместим этот код в файл src/lib.rs и напишем несколько тестов для него используя assert! макрос.

Файл: src/lib.rs

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```

Листинг 11-5: Использование структуры Rectangle и её метода can_hold из главы 5

Метод can_hold возвращает логическое значение, что означает, что она является идеальным вариантом использования в макросе assert!. В листинге 11-6 мы пишем тест, который выполняет метод can_hold путём создания экземпляра Rectangle шириной 8 и высотой 7 и убеждаемся, что он может содержать другой экземпляр Rectangle имеющий ширину 5 и высоту 1.

Файл: src/lib.rs

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn larger_can_hold_smaller() {
        let larger = Rectangle {
            width: 8,
            height: 7,
        };
        let smaller = Rectangle {
            width: 5,
            height: 1,
        };

        assert!(larger.can_hold(&smaller));
    }
}
```

Листинг 11-6: Теста для метода can_hold, который проверяет что больший прямоугольник действительно может содержать меньший