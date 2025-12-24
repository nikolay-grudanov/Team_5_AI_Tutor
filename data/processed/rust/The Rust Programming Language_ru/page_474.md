---
source_image: page_474.png
page_number: 474
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.60
tokens: 11527
characters: 1095
timestamp: 2025-12-24T10:38:11.824731
finish_reason: stop
---

Листинг 16-14: Попытка использования `Rc<T>`, чтобы позволить нескольким потокам владеть `Mutex<T>`

Ещё раз, мы компилируем и получаем ... другие ошибки! Компилятор учит нас.

$ cargo run
Compiling shared-state v0.1.0 (file:///projects/shared-state)
error[E0277]: `Rc<Mutex<i32>>` cannot be sent between threads safely
 --> src/main.rs:11:22
  |
11 |         let handle = thread::spawn(move || {
  |         ^^^^^^^^^^^^^^^^^^^^
  |         |                        |
  |         `Rc<Mutex<i32>>` cannot be sent between threads safely
12 |             let mut num = counter.lock().unwrap();
13 |             *num += 1;
14 |         });
15 |         |_________-- within this `[closure@src/main.rs:11:36: 15:10]`
|                = help: within `[closure@src/main.rs:11:36: 15:10]`, the trait `Send` is not implemented for `Rc<Mutex<i32>>`
= note: required because it appears within the type `[closure@src/main.rs:11:36: 15:10]`
note: required by a bound in `spawn`

For more information about this error, try `rustc --explain E0277`.
error: could not compile `shared-state` due to previous error