---
source_image: page_552.png
page_number: 552
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 45.94
tokens: 11687
characters: 1511
timestamp: 2025-12-24T10:41:38.067529
finish_reason: stop
---

Rust не позволяет создавать собственные операторы или перегружать произвольные операторы. Но можно перегрузить перечисленные операции и соответствующие им типажи из `std::ops` путём реализации типажей, связанных с этими операторами. Например, в листинге 19-14 мы перегружаем оператор `+`, чтобы складывать два экземпляра `Point`. Мы делаем это реализуя типаж `Add` для структуры `Point`.

Файл: src/main.rs

```rust
use std::ops::Add;

#[derive(Debug, Copy, Clone, PartialEq)]
struct Point {
    x: i32,
    y: i32,
}

impl Add for Point {
    type Output = Point;

    fn add(self, other: Point) -> Point {
        Point {
            x: self.x + other.x,
            y: self.y + other.y,
        }
    }
}

fn main() {
    assert_eq!(
        Point { x: 1, y: 0 } + Point { x: 2, y: 3 },
        Point { x: 3, y: 3 }
    );
}
```

Листинг 19-14: Реализация типажа `Add` для перезагрузки оператора `+` у структуры `Point`

Метод `add` складывает значения `x` двух экземпляров `Point` и значения `y` у `Point` для создания нового экземпляра `Point`. Типаж `Add` имеет ассоциированный тип с именем `Output`, который определяет тип, возвращаемый из метода `add`.

Обобщённый тип по умолчанию в этом коде находится в типаже `Add`. Вот его определение:

```rust
trait Add<Rhs = Self> {
    type Output;
    fn add(self, rhs: Rhs) -> Self::Output;
}
```

Этот код должен выглядеть знакомым: типаж с одним методом и ассоциированным типом. Новый синтаксис это `RHS=Self`. Такой синтаксис называется *параметры типа по*