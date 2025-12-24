---
source_image: page_123.png
page_number: 123
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.28
tokens: 11638
characters: 1502
timestamp: 2025-12-24T10:23:39.225910
finish_reason: stop
---

Снова компилятор даёт нам полезное замечание:

= help: the trait `Debug` is not implemented for `Rectangle`
= note: add `#[derive(Debug)]` to `Rectangle` or manually `impl Debug for Rectangle`

Rust реализует функциональность для печати отладочной информации, но не включает (не выводит) её по умолчанию. Мы должны явно включить эту функциональность для нашей структуры. Чтобы это сделать, добавляем внешний атрибут #[derive(Debug)] сразу перед определением структуры, как показано в листинге 5-12.

Файл: src/main.rs

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!("rect1 is {:?}", rect1);
}
```

Листинг 5-12: добавление атрибута для вывода типажа Debug и печати экземпляра Rectangle с отладочным форматированием

Теперь при запуске программы мы не получим ошибок и увидим следующий вывод:

$ cargo run
Compiling rectangles v0.1.0 (file:///projects/rectangles)
Finished dev [unoptimized + debuginfo] target(s) in 0.48s
    Running `target/debug/rectangles`
rect1 is Rectangle { width: 30, height: 50 }

Отлично! Это не самый красивый вывод, но он показывает значения всех полей экземпляра, которые определённо помогут при отладке. Когда у нас более крупные структуры, то полезно иметь более простой для чтения вывод; в таких случаях можно использовать код {:#?} вместо {:?} в строке макроса println!. В этом примере использование стиля {:#?} приведёт к такому выводу: