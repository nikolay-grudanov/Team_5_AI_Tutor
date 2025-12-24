---
source_image: page_500.png
page_number: 500
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.24
tokens: 11476
characters: 1125
timestamp: 2025-12-24T10:39:10.885486
finish_reason: stop
---

Добывление approve для изменения поведения content

Метод approve ("одобрить") будет аналогичен методу request_review: он будет устанавливать у state значение, которое должна иметь запись при её одобрении, как показано в листинге 17-16:

Файл: src/lib.rs

```rust
impl Post {
    // --snip--
    pub fn approve(&mut self) {
        if let Some(s) = self.state.take() {
            self.state = Some(s.approve())
        }
    }
}

trait State {
    fn request_review(self: Box<Self>) -> Box<dyn State>;
    fn approve(self: Box<Self>) -> Box<dyn State>;
}

struct Draft {}

impl State for Draft {
    // --snip--
    fn approve(self: Box<Self>) -> Box<dyn State> {
        self
    }
}

struct PendingReview {}

impl State for PendingReview {
    // --snip--
    fn approve(self: Box<Self>) -> Box<dyn State> {
        Box::new(Published {})
    }
}

struct Published {}

impl State for Published {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
        self
    }

    fn approve(self: Box<Self>) -> Box<dyn State> {
        self
    }
}
```

Листинг 17-16. Реализация метода approve для типа Post и типажа State