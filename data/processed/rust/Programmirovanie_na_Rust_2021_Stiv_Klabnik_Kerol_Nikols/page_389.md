---
source_image: page_389.png
page_number: 389
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.77
tokens: 7517
characters: 2211
timestamp: 2025-12-24T10:56:02.097053
finish_reason: stop
---

```rust
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
```

Этот тестовый код определяет структуру MockMessenger ①, которая имеет поле sent_messages с вектором значений типа String ②, чтобы отслеживать сообщения, которые она должна отправлять. Мы также определяем связанную функцию new ③ для удобства в создании новых значений типа MockMessenger, которые начинают с пустого списка сообщений. Затем мы реализуем типаж Messenger для MockMessenger ④, благодаря чему можно передавать структуру MockMessenger структуре LimitTracker. В определении метода send ⑤ мы берем сообщение, переданное внутрь в качестве параметра, и сохраняем его в поле sent_messages списка отправленных сообщений, состоящего из структур MockMessenger.

В тесте мы проверяем, что происходит, когда LimitTracker поручает установить значение равным чему-то, что составляет более 75% от максимального значения ⑥. Сначала мы создаем новый экземпляр структуры MockMessenger, который будет начинаться с пустого списка сообщений. Затем мы создаем новый экземпляр структуры LimitTracker и даем ему ссылку на новый MockMessenger и максимальное значение 100. Мы вызываем метод set_value для LimitTracker со значением 80, что составляет более 75% от 100. Затем мы выполняем проверочное утверждение, что список сообщений, который отслеживается структурой MockMessenger, теперь должен содержать одно сообщение.

Однако с этим тестом есть одна проблема, как показано ниже¹:

error[E0596]: cannot borrow immutable field 'self.sent_messages' as mutable
 --> src/lib.rs:52:13
  |
51 |     fn send(&self, message: &str) {
  |         ---- use '&mut self' here to make mutable
52 |         self.sent_messages.push(String::from(message));
  |         ^^^^^^^^^^^^^^^^^^^^ cannot mutably borrow immutable field

¹ ошибка[E0596]: не получается заимствовать неизменяемое поле 'self.sent_messages' как изменяемое