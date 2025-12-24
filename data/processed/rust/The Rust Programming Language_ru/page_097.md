---
source_image: page_097.png
page_number: 97
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 48.60
tokens: 11613
characters: 1501
timestamp: 2025-12-24T10:22:40.846783
finish_reason: stop
---

Сначала мы меняем s на mut. Затем мы создаём изменяемую ссылку с помощью &mut s, у которой вызываем change и обновляем сигнатуру функции, чтобы принять изменяемую ссылку с помощью some_string: &mut String. Это даёт понять, что change изменит значение, которое заимствует.

Изменяемые ссылки имеют одно большое ограничение: если у вас есть изменяемая ссылка на значение, у вас не может быть других ссылок на это значение. Код, который пытается создать две изменяемые ссылки на s, завершится ошибкой:

Файл: src/main.rs

```rust
let mut s = String::from("hello");

let r1 = &mut s;
let r2 = &mut s;

println!("{}, {}", r1, r2);
```

Описание ошибки:

```
$ cargo run
Compiling ownership v0.1.0 (file:///projects/ownership)
error[E0499]: cannot borrow `s` as mutable more than once at a time
 --> src/main.rs:5:14
  |
4 |     let r1 = &mut s;
  |         ------ first mutable borrow occurs here
5 |     let r2 = &mut s;
  |         ^^^^^^ second mutable borrow occurs here
6 | 
7 |     println!("{}, {}", r1, r2);
  |                     -- first borrow later used here

For more information about this error, try `rustc --explain E0499`.
error: could not compile `ownership` due to previous error
```

Эта ошибка говорит о том, что код недействителен, потому что мы не можем заимствовать s как изменяемые более одного раза в один момент. Первое изменяемое заимствование находится в r1 и должно длиться до тех пор, пока оно не будет использовано в println!, но между созданием этой изменяемой ссылки и её