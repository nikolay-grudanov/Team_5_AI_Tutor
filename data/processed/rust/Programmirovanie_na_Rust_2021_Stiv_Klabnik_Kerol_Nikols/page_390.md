---
source_image: page_390.png
page_number: 390
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.79
tokens: 7423
characters: 1824
timestamp: 2025-12-24T10:55:56.788085
finish_reason: stop
---

Мы не можем модифицировать MockMessenger, чтобы отслеживать сообщения, потому что метод send берет неизменяемую ссылку на self. Мы также не можем принять рекомендацию из текста ошибки использовать &mut self, потому что тогда сигнатура метода send не будет совпадать с сигнатурой в определении типажа Messenger (попробуйте это сделать и посмотрите, какое сообщение об ошибке вы получите).

Это именно та ситуация, в которой помогает внутренняя изменяемость! Мы сохраним поле sent_messages внутри умного указателя RefCell<T>. Затем сообщение из метода send сможет модифицировать поле sent_messages, чтобы сохранить сообщения, которые мы видели. Листинг 15.22 показывает, как это выглядит.

Листинг 15.22. Использование умного указателя RefCell<T> для изменения внутреннего значения, тогда как внешнее значение считается неизменяемым

src/lib.rs

```rust
#[cfg(test)]
mod tests {
    use super::*;
    use std::cell::RefCell;

    struct MockMessenger {
        sent_messages: RefCell<Vec<String>>, // 1
    }

    impl MockMessenger {
        fn new() -> MockMessenger {
            MockMessenger { sent_messages: RefCell::new(vec![]) } // 2
        }
    }

    impl Messenger for MockMessenger {
        fn send(&self, message: &str) {
            self.sent_messages.borrow_mut().push(String::from(message)); // 3
        }
    }

    #[test]
    fn it_sends_an_over_75_percent_warning_message() {
        // --пропуск--
        assert_eq!(mock_messenger.sent_messages.borrow().len(), 1); // 4
    }
}
```

Поле sent_messages теперь имеет тип RefCell<Vec<String>> 1 вместо Vec<String>. В функции new мы создаем новый экземпляр RefCell<Vec<String>> вокруг пустого вектора 2.

Для реализации метода send первый параметр по-прежнему является неизменяемым заимствованием self, которое совпадает с определением типажа. Мы вызыва-