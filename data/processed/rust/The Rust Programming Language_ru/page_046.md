---
source_image: page_046.png
page_number: 46
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 52.81
tokens: 11723
characters: 1970
timestamp: 2025-12-24T10:20:42.615256
finish_reason: stop
---

Переменные и понятие изменяемости

Как упоминалось в разделе “Сохранение значений в переменных”, по умолчанию переменные являются неизменяемыми. Это одна из многих подсказок, которые Rust даёт вам для написания кода таким образом, чтобы использовать преимущества безопасности и простого параллелизма, которые предлагает Rust. Однако у вас есть возможность сделать ваши переменные изменяемыми. Давайте рассмотрим, как и почему Rust поощряет неизменность, и почему иногда вы можете отказаться от этого.

Когда переменная неизменяемая, то её значение нельзя менять, как только значение привязано к её имени. Приведём пример использования этого типа переменной. Для этого создадим новый проект variables в каталоге projects при помощи команды: cargo new variables.

Потом в созданной папке проекта variables откройте исходный файл src/main.rs и замените содержимое следующим кодом, который пока не будет компилироваться:

Файл: src/main.rs

```rust
fn main() {
    let x = 5;
    println!("The value of x is: {x}");
    x = 6;
    println!("The value of x is: {x}");
}
```

Сохраните код программы и выполните команду cargo run. В командной строке вы увидите сообщение об ошибке:

```
$ cargo run
Compiling variables v0.1.0 (file:///projects/variables)
error[E0384]: cannot assign twice to immutable variable `x`
 --> src/main.rs:4:5
  |
2 |     let x = 5;
  |         -
  |         |
  |         first assignment to `x`
  |         help: consider making this binding mutable: `mut x`
3 |     println!("The value of x is: {x}");
4 |     x = 6;
   |     ^^^^^ cannot assign twice to immutable variable

For more information about this error, try `rustc --explain E0384`.
error: could not compile `variables` due to previous error
```

Данный пример показывает, как компилятор помогает вам находить ошибки в ваших программах. Ошибки компилятора могут вызывать разочарование, но на самом деле они лишь означают, что ваша программа ещё не делает то, что вы от неё хотите. Они не