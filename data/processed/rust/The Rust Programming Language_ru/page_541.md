---
source_image: page_541.png
page_number: 541
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.85
tokens: 11664
characters: 1707
timestamp: 2025-12-24T10:41:05.805317
finish_reason: stop
---

unsafe fn dangerous() {}

unsafe {
    dangerous();
}

Мы должны вызвать функцию dangerous в отдельном unsafe блоке. Если мы попробуем вызвать dangerous без unsafe блока, мы получим ошибку:

$ cargo run
Compiling unsafe-example v0.1.0 (file:///projects/unsafe-example)
error[E0133]: call to unsafe function is unsafe and requires unsafe function or block
 --> src/main.rs:4:5
  |
4 |     dangerous();
   |     ^^^^^^^^^^^^ call to unsafe function
   |
   = note: consult the function's documentation for information on how to avoid undefined behavior

For more information about this error, try `rustc --explain E0133`.
error: could not compile `unsafe-example` due to previous error

Вставив unsafe блок вокруг нашего вызова dangerous, мы утверждаем, что мы прочитали документацию к функции, мы понимаем как её использовать правильно и мы убедились, что выполняем контракт функции.

Тела небезопасных функций являются фактически unsafe блоками, поэтому для выполнения других небезопасных операций внутри небезопасной функции не нужно добавлять ещё один unsafe блок.

Создание безопасных абстракций вокруг небезопасного кода

Тот факт, что функция содержит небезопасный код, не означает, что мы должны пометить всю функцию как небезопасную. Фактически, упаковка небезопасного кода в безопасную функцию является обычной абстракцией. В качестве примера давайте изучим функцию из стандартной библиотеки split_at_mut, для которой требуется небезопасный код и исследуем, как мы могли бы её реализовать. Этот безопасный метод определён для изменяемых срезов: он берёт один срез и делит его на два, разделяя срез по индексу, указанному в качестве аргумента. В листинге 19.4 показано, как использовать split_at_mut.