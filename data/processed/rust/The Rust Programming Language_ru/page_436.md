---
source_image: page_436.png
page_number: 436
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 52.52
tokens: 11747
characters: 2148
timestamp: 2025-12-24T10:36:52.441394
finish_reason: stop
---

мы принимаем сообщение для передачи в качестве параметра и сохраняем его в MockMessenger внутри списка sent_messages.

В этом тесте мы проверяем, что происходит, когда LimitTracker сказано установить value в значение, превышающее 75 процентов от значения max. Сначала мы создаём новый MockMessenger, который будет иметь пустой список сообщений. Затем мы создаём новый LimitTracker и передаём ему ссылку на новый MockMessenger и max значение равное 100. Мы вызываем метод set_value у LimitTracker со значением 80, что составляет более 75 процентов от 100. Затем мы с помощью утверждения проверяем, что MockMessenger должен содержать одно сообщение из списка внутренних сообщений.

Однако с этим тестом есть одна проблема, показанная ниже:

$ cargo test
Compiling limit-tracker v0.1.0 (file:///projects/limit-tracker)
error[E0596]: cannot borrow `self.sent_messages` as mutable, as it is behind a `&` reference
  --> src/lib.rs:58:13
   |
2  |     fn send(&self, msg: &str);
   |         ---- help: consider changing that to be a mutable reference:
   |         `&mut self`
...
58 |         self.sent_messages.push(String::from(message));
   |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ `self` is a `&` reference, so the data it refers to cannot be borrowed as mutable

For more information about this error, try `rustc --explain E0596`.
error: could not compile `limit-tracker` due to previous error
warning: build failed, waiting for other jobs to finish...

Мы не можем изменять MockMessenger для отслеживания сообщений, потому что метод send принимает неизменяемую ссылку на self. Мы также не можем принять предложение из текста ошибки, чтобы использовать &mut self, потому что тогда сигнатура send не будет соответствовать сигнатуре в определении типажа Messenger (не стесняйтесь попробовать и посмотреть, какое сообщение об ошибке получите вы).

Это ситуация, в которой внутренняя изменяемость может помочь! Мы сохраним sent_messages внутри типа RefCell<T>, а затем в методе send сообщение сможет изменить список sent_messages для хранения сообщений, которые мы видели. Листинг 15-22 показывает, как это выглядит:

Файл: src/lib.rs