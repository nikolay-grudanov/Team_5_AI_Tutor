---
source_image: page_612.png
page_number: 612
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.72
tokens: 11464
characters: 975
timestamp: 2025-12-24T10:44:00.471388
finish_reason: stop
---

Листинг 20-17: Передача принимающей части канала "работнику"

Мы внесли несколько небольших и простых изменений: мы передаём принимающую часть канала в Worker::new, а затем используем его внутри замыкания.

При попытке проверить код, мы получаем ошибку:

$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0382]: use of moved value: `receiver`
 --> src/lib.rs:26:42
21 |     let (sender, receiver) = mpsc::channel();
22 |         ---------- move occurs because `receiver` has type `std::sync::mpsc::Receiver<Job>`, which does not implement the `Copy` trait
...
26 |     workers.push(Worker::new(id, receiver));
        ^^^^^^^^ value moved here, in previous iteration of loop

For more information about this error, try `rustc --explain E0382`.
error: could not compile `hello` due to previous error

Код пытается передать receiver в несколько экземпляров Worker. Это не будет работать, как вы помните из главы 16: реализация канала предоставляемая Rust,