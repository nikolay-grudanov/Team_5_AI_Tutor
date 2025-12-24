---
source_image: page_435.png
page_number: 435
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 45.48
tokens: 11670
characters: 1871
timestamp: 2025-12-24T10:36:41.120794
finish_reason: stop
---

Нам нужен мок объект, который вместо отправки электронного письма или текстового сообщения будет отслеживать сообщения, которые были ему поручены для отправки через send. Мы можем создать новый экземпляр мок объекта, создать LimitTracker с использованием мок объект для него, вызвать метод set_value у экземпляра LimitTracker, а затем проверить, что мок объект имеет ожидаемое сообщение. В листинге 15-21 показана попытка реализовать мок объект, чтобы сделать именно то что хотим, но анализатор заимствований не разрешит такой код:

Файл: src/lib.rs

```rust
#[cfg(test)]
mod tests {
    use super::*;

    struct MockMessenger {
        sent_messages: Vec<String>,
    }

    impl MockMessenger {
        fn new() -> MockMessenger {
            MockMessenger {
                sent_messages: vec![],
            }
        }
    }

    impl Messenger for MockMessenger {
        fn send(&self, message: &str) {
            self.sent_messages.push(String::from(message));
        }
    }

    #[test]
    fn it_sends_an_over_75_percent_warning_message() {
        let mock_messenger = MockMessenger::new();
        let mut limit_tracker = LimitTracker::new(&mock_messenger, 100);

        limit_tracker.set_value(80);

        assert_eq!(mock_messenger.sent_messages.len(), 1);
    }
}
```

Листинг 15-21: Попытка реализовать MockMessenger, которая не была принята механизмом проверки заимствований

Этот тестовый код определяет структуру MockMessenger, в которой есть поле sent_messages со значениями типа Vec из String для отслеживания сообщений, которые поручены структуре для отправки. Мы также определяем ассоциированную функцию new, чтобы было удобно создавать новые экземпляры MockMessenger, которые создаются с пустым списком сообщений. Затем мы реализуем типаж Messenger для типа MockMessenger, чтобы передать MockMessenger в LimitTracker. В сигнатуре метода send