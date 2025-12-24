---
source_image: page_498.png
page_number: 498
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.34
tokens: 11478
characters: 1098
timestamp: 2025-12-24T10:38:57.082204
finish_reason: stop
---

Листинг 17-14. Добавление реализации-заглушки для метода content в Post, которая всегда возвращает пустой фрагмент строки.

С добавленным таким образом методом content всё в листинге 17-11 работает, как задумано, вплоть до строки 7.

Запрос на проверку записи меняет её состояние

Далее нам нужно добавить функциональность для запроса проверки записи, который должен изменить её состояние с Draft на PendingReview. Листинг 17-15 показывает такой код:

Файл: src/lib.rs

```rust
impl Post {
    // --snip--
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

struct PendingReview {}

impl State for PendingReview {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
        self
    }
}
```

Листинг 17-15. Реализация методов request_review в структуре Post и типаже State