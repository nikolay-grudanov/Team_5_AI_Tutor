---
source_image: page_414.png
page_number: 414
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.95
tokens: 11615
characters: 1344
timestamp: 2025-12-24T10:35:42.146507
finish_reason: stop
---

Листинг 15-9. Попытка использовать `MyBox<T>` таким же образом, как мы использовали ссылки и `Box<T>`

Вот результат ошибки компиляции:

```
$ cargo run
Compiling deref-example v0.1.0 (file:///projects/deref-example)
error[E0614]: type `MyBox<{integer}>` cannot be dereferenced
 --> src/main.rs:14:19
  |
14 |     assert_eq!(5, *y);
  |                 ^^^

For more information about this error, try `rustc --explain E0614`.
error: could not compile `deref-example` due to previous error
```

Наш тип `MyBox<T>` не может быть разыменован, потому что мы не реализовали эту возможность. Чтобы включить разыменование с помощью оператора `*`, мы реализуем типаж `Deref`.

Трактование типа как ссылки реализуя типаж `Deref`

Как обсуждалось в разделе “Реализация трейта для типа” Главы 10, для реализации типажа нужно предоставить реализации требуемых методов типажа. Типаж `Deref`, предоставляемый стандартной библиотекой требует от нас реализации одного метода с именем `deref`, который заимствует `self` и возвращает ссылку на внутренние данные. Листинг 15-10 содержит реализацию `Deref` добавленную к определению `MyBox`:

Файл: src/main.rs

```rust
use std::ops::Deref;

impl<T> Deref for MyBox<T> {
    type Target = T;

    fn deref(&self) -> &Self::Target {
        &self.0
    }
}
```

Листинг 15-10: Реализация `Deref` для типа `MyBox<T>`