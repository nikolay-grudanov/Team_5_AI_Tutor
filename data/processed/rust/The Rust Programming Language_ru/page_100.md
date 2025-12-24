---
source_image: page_100.png
page_number: 100
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 56.46
tokens: 11689
characters: 1772
timestamp: 2025-12-24T10:22:59.876858
finish_reason: stop
---

Недействительные ссылки

В языках с указателями легко ошибочно создать висячий указатель — указатель, ссылающийся на место в памяти, которое могло быть передано кому-то другому после освобождения этой части памяти, сохраняя при этом указатель на неё. В Rust, напротив, компилятор гарантирует, что ссылки никогда не будут висячими: если у вас есть ссылка на какие-то данные, компилятор убедится, что данные не выйдут за пределы области видимости до того, как это сделает ссылка на них.

Давайте попробуем создать висячую ссылку, чтобы увидеть, как Rust предотвращает их появление с помощью ошибки во время компиляции:

Файл: src/main.rs

```rust
fn main() {
    let reference_to_nothing = dangle();
}

fn dangle() -> &String {
    let s = String::from("hello");

    &s
}
```

Здесь ошибка:

```
$ cargo run
   Compiling ownership v0.1.0 (file:///projects/ownership)
error[E0106]: missing lifetime specifier
 --> src/main.rs:5:16
  |
5 | fn dangle() -> &String {
  |                ^ expected named lifetime parameter
  |
  = help: this function's return type contains a borrowed value, but there is no value for it to be borrowed from
help: consider using the `'static` lifetime
  |
5 | fn dangle() -> &'static String {
  |           ~~~~~~~~~~
For more information about this error, try `rustc --explain E0106`.
error: could not compile `ownership` due to previous error
```

Это сообщение об ошибке относится к особенности языка, которую мы ещё не рассмотрели: времени жизни. Мы подробно обсудим времена жизни в главе 10. Но если вы не обращаете внимания на части, касающиеся времени жизни, сообщение будет содержать ключ к тому, почему этот код является проблемой:

this function's return type contains a borrowed value, but there is no value for it to be borrowed from