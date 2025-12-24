---
source_image: page_050.png
page_number: 50
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.60
tokens: 11558
characters: 1399
timestamp: 2025-12-24T10:20:39.279560
finish_reason: stop
---

изменить тип значения, но снова использовать предыдущее имя. К примеру, наша программа спрашивает пользователя, сколько пробелов он хочет разместить между некоторым текстом, запрашивая символы пробела, но мы на самом деле хотим сохранить данный ввод как число:

```rust
let spaces = "   ";
let spaces = spaces.len();
```

Первая переменная `spaces` — является строковым типом, а вторая переменная `spaces` — числовым типом. Таким образом, затенение избавляет нас от необходимости придумывать разные имена, такие как `spaces_str` и `spaces_num`; вместо этого мы можем повторно использовать более простое имя `spaces`. Однако, если мы попытаемся использовать для этого `mut`, как здесь показано, то мы получим ошибку времени компиляции:

```rust
let mut spaces = "   ";
spaces = spaces.len();
```

Ошибка говорит, что не разрешается менять тип переменной:

```
$ cargo run
Compiling variables v0.1.0 (file:///projects/variables)
error[E0308]: mismatched types
 --> src/main.rs:3:14
  |
2 | let mut spaces = "   ";
  |         ---- expected due to this value
3 | spaces = spaces.len();
  | ^^^^^^^^^^^^^^^ expected `&str`, found `usize`

For more information about this error, try `rustc --explain E0308`.
error: could not compile `variables` due to previous error
```

Теперь, когда вы имеете представление о работе с переменными, посмотрим на большее количество типов данных, которые они могут иметь.