---
source_image: page_063.png
page_number: 63
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 45.10
tokens: 11668
characters: 1609
timestamp: 2025-12-24T10:21:15.271090
finish_reason: stop
---

Листинг 3-1: Объявление функции `main`, содержащей один оператор

Определения функций также являются операторами. Весь предыдущий пример сам по себе является оператором.

Поэтому нельзя присвоить значение оператора `let` другой переменной, как это сделано в следующем коде. Вы получите ошибку:

Имя файла: src/main.rs

```rust
fn main() {
    let x = (let y = 6);
}
```

Если вы запустите эту программу, то ошибка будет выглядеть так:

```
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
error: expected expression, found statement (`let`)
 --> src/main.rs:2:14
  |
2 |     let x = (let y = 6);
  |                ^^^^^^^^
  = note: variable declaration using `let` is a statement

error[E0658]: `let` expressions in this position are unstable
 --> src/main.rs:2:14
  |
2 |     let x = (let y = 6);
  |                ^^^^^^^^
  = note: see issue #53667 <https://github.com/rust-lang/rust/issues/53667> for more information

warning: unnecessary parentheses around assigned value
 --> src/main.rs:2:13
  |
2 |     let x = (let y = 6);
  |                ^        ^
  = note: `#[warn(unused_parens)]` on by default
help: remove these parentheses
  |
2 -     let x = (let y = 6);
2 +     let x = let y = 6;
  |

For more information about this error, try `rustc --explain E0658`.
warning: `functions` (bin "functions") generated 1 warning
error: could not compile `functions` due to 2 previous errors; 1 warning emitted
```

Оператор `let y = 6` не возвращает значение, поэтому не с чем связать переменную `x`. Это отличается от поведения в других языках, таких как C и Ruby, где операция