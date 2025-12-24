---
source_image: page_449.png
page_number: 449
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.04
tokens: 7269
characters: 1298
timestamp: 2025-12-24T10:57:23.767376
finish_reason: stop
---

Мы оставим метод content в структуре Post как есть, возвращая пустой строковый срез. Теперь статья может быть в состоянии PendingReview, а также в состоянии Draft, но мы хотим, чтобы то же самое поведение было в состоянии PendingReview. Листинг 17.11 теперь работает вплоть до строки 5!

Добавление метода approve, который изменяет поведение метода content

Метод approve будет похож на метод request_review: он установит поле state равным значению, которое согласно текущему состоянию оно должно иметь, когда это состояние одобрено, как показано в листинге 17.16.

Листинг 17.16. Реализация методов approve в структуре Post и типаже Sate
src/lib.rs

impl Post {
    // --пропуск--
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
    // --пропуск--
    fn approve(self: Box<Self>) -> Box<dyn State> {
        1 self
    }
}

struct PendingReview {}

impl State for PendingReview {
    // --пропуск--
    fn approve(self: Box<Self>) -> Box<dyn State> {
        2 Box::new(Published {})
    }
}

struct Published {}

impl State for Published {