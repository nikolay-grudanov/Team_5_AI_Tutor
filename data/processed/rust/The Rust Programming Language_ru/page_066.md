---
source_image: page_066.png
page_number: 66
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.70
tokens: 11552
characters: 1199
timestamp: 2025-12-24T10:21:19.053182
finish_reason: stop
---

ошибку.

Имя файла: src/main.rs

```rust
fn main() {
    let x = plus_one(5);

    println!("The value of x is: {x}");
}

fn plus_one(x: i32) -> i32 {
    x + 1;
}
```

Компиляция данного кода вызывает следующую ошибку:

```
$ cargo run
Compiling functions v0.1.0 (file:///projects/functions)
error[E0308]: mismatched types
 --> src/main.rs:7:24
  |
7 | fn plus_one(x: i32) -> i32 {
  | --------         ^^^ expected `i32`, found `()` 
  |         |
  |         implicitly returns `()` as its body has no tail or `return` expression
8 |     x + 1;
  |     - help: remove this semicolon

For more information about this error, try `rustc --explain E0308`.
error: could not compile `functions` due to previous error
```

Основное сообщение об ошибке "несовпадение типов" раскрывает ключевую проблему этого кода. Определение функции `plus_one` сообщает, что будет возвращено `i32`, но операторы не вычисляют значение, что и выражается единичным типом `()`. Следовательно, ничего не возвращается, что противоречит определению функции и приводит к ошибке. В этом выводе Rust выдаёт сообщение, которое, возможно, поможет исправить эту проблему: он предлагает удалить точку с запятой для устранения ошибки.