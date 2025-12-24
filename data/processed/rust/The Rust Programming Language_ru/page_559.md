---
source_image: page_559.png
page_number: 559
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.78
tokens: 11520
characters: 1248
timestamp: 2025-12-24T10:41:47.767647
finish_reason: stop
---

Файл: src/main.rs

```rust
use std::fmt;

trait OutlinePrint: fmt::Display {
    fn outline_print(&self) {
        let output = self.to_string();
        let len = output.len();
        println!("{}", "*".repeat(len + 4));
        println!("*{}*", " ".repeat(len + 2));
        println!("* {} *", output);
        println!("*{}*", " ".repeat(len + 2));
        println!("{}", "*".repeat(len + 4));
    }
}
```

Листинг 19-22: Реализация типажа OutlinePrint которая требует функциональности типажа Display

Поскольку мы указали, что типаж OutlinePrint требует типажа Display, мы можем использовать функцию to_string, которая автоматически реализована для любого типа реализующего Display. Если бы мы попытались использовать to_string не добавляя двоеточие и не указывая типаж Display после имени типажа, мы получили бы сообщение о том, что метод с именем to_string не был найден у типа &Self в текущей области видимости.

Давайте посмотрим что происходит, если мы пытаемся реализовать типаж OutlinePrint для типа, который не реализует Display, например структура Point:

Файл: src/main.rs

```rust
struct Point {
    x: i32,
    y: i32,
}

impl OutlinePrint for Point {}
```

Мы получаем сообщение о том, что требуется реализация Display, но её нет: