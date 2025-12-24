---
source_image: page_069.png
page_number: 69
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 48.77
tokens: 11610
characters: 1543
timestamp: 2025-12-24T10:21:37.879151
finish_reason: stop
---

$ cargo run
Compiling branches v0.1.0 (file:///projects/branches)
Finished dev [unoptimized + debuginfo] target(s) in 0.31s
    Running `target/debug/branches`
condition was true

Попробуйте изменить значение number на значение, которое делает условие false и посмотрите, что произойдёт:

let number = 7;

Запустите программу снова и посмотрите на вывод:

$ cargo run
Compiling branches v0.1.0 (file:///projects/branches)
Finished dev [unoptimized + debuginfo] target(s) in 0.31s
    Running `target/debug/branches`
condition was false

Также стоит отметить, что условие в этом коде должно быть логического типа bool. Если условие не является bool, возникнет ошибка. Например, попробуйте запустить следующий код:

Имя файла: src/main.rs

fn main() {
    let number = 3;

    if number {
        println!("number was three");
    }
}

На этот раз условие if вычисляется в значение 3, и Rust бросает ошибку:

$ cargo run
Compiling branches v0.1.0 (file:///projects/branches)
error[E0308]: mismatched types
 --> src/main.rs:4:8
  |
4 |     if number {
  |     ^^^^^ expected `bool`, found integer

For more information about this error, try `rustc --explain E0308`.
error: could not compile `branches` due to previous error

Ошибка говорит, что Rust ожидал тип bool, но получил значение целочисленного типа. В отличии от других языков вроде Ruby и JavaScript, Rust не будет пытаться автоматически конвертировать нелогические типы в логические. Необходимо явно и всегда использовать if с логическим типом в качестве условия. Если нужно, чтобы блок