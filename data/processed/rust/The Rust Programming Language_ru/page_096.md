---
source_image: page_096.png
page_number: 96
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 49.26
tokens: 11648
characters: 1561
timestamp: 2025-12-24T10:22:41.454734
finish_reason: stop
---

Мы называем процесс создания ссылки заимствованием. Как и в реальной жизни, если человек чем-то владеет, вы можете это у него позаимствовать. Когда вы закончите, вы должны вернуть это законному владельцу.

Так что же произойдёт, если мы попытаемся изменить что-то, что мы заимствуем? Попробуйте запустить код из листинга 4-6. Спойлер: это не сработает!

Файл: src/main.rs

```rust
fn main() {
    let s = String::from("hello");

    change(&s);
}

fn change(some_string: &String) {
    some_string.push_str(", world");
}
```

Листинг 4-6: попытка модификации заимствованной переменной

Вот ошибка:

```
$ cargo run
Compiling ownership v0.1.0 (file:///projects/ownership)
error[E0596]: cannot borrow `*some_string` as mutable, as it is behind a `&` reference
 --> src/main.rs:8:5
  |
7 | fn change(some_string: &String) {
  |                -------- help: consider changing this to be a mutable reference: `&mut String`
8 |     some_string.push_str(", world");
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ `some_string` is a `&` reference, so the data it refers to cannot be borrowed as mutable

For more information about this error, try `rustc --explain E0596`.
error: could not compile `ownership` due to previous error
```

Как переменные неизменяемы по умолчанию, так и ссылки. Нам не разрешено изменять то, на что у нас есть ссылка.

Изменяемые ссылочные переменные

Мы можем исправить код из листинга 4-6, чтобы позволить себе изменять заимствованное значение, с помощью нескольких небольших настроек, которые используют изменяемую ссылку:

Файл: src/main.rs