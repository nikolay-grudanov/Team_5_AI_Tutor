---
source_image: page_447.png
page_number: 447
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.53
tokens: 7356
characters: 1534
timestamp: 2025-12-24T10:57:23.975058
finish_reason: stop
---

тинге 17.11. Пока что давайте реализуем метод content с простейшей вещью, которая будет выполнять это требование: всегда возвращать пустой строковый срез. Мы изменим это поведение позже, когда займемся реализацией возможности изменять состояние статьи, чтобы ее можно было публиковать. Пока что статьи могут быть только в черновом состоянии, поэтому содержимое статьи всегда должно быть пустым. В листинге 17.14 показана такая заполнительная реализация.

Листинг 17.14. Добавление заполнителя для метода content в структуру Post, которая всегда возвращает пустой строковый срез &str

src/lib.rs
```rust
impl Post {
    // --пропуск--
    pub fn content(&self) -> &str {
        ""
    }
}
```

После того как был добавлен метод content, в листинге 17.11 все работает, как и задумывалось, вплоть до строки в 3.

Запрос на проверку статьи изменяет ее состояние

Далее нам нужно добавить функциональность запроса на проверку статьи, который должен изменить ее состояние с Draft на PendingReview. Этот код показан в листинге 17.15.

Листинг 17.15. Реализация методов request_review в структуре Post и типаже State

src/lib.rs
```rust
impl Post {
    // --пропуск--
    pub fn request_review(&mut self) {
        if let Some(s) = self.state.take() {
            self.state = Some(s.request_review())
        }
    }
}

trait State {
    fn request_review(self: Box<Self>) -> Box<dyn State>;
}

struct Draft {}

impl State for Draft {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
        Box::new(PendingReview {})
    }
}
```