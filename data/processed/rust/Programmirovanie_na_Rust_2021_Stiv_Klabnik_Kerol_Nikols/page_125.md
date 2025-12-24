---
source_image: page_125.png
page_number: 125
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.65
tokens: 7513
characters: 1994
timestamp: 2025-12-24T10:49:02.839578
finish_reason: stop
---

= help: the trait `std::fmt::Display` is not implemented for `Rectangle`
= note: in format strings you may be able to use `{:?}` (or {:#?} for prettyprint) instead

Давайте попробуем! Вызов макрокоманды println! теперь будет выглядеть как println!("rect1 равен {:?}", rect1);. Размещение спецификатора :? внутри фигурных скобок говорит макрокоманде println! о том, что мы хотим использовать выходной формат под названием Debug. Типаж Debug дает возможность печатать структуру в полезном для разработчиков виде, благодаря которому видно ее значение во время отладки кода.

Выполните код с этим изменением. Проклятие! Все равно есть ошибка:

error[E0277]: `Rectangle` doesn't implement `std::fmt::Debug`

И снова компилятор дает нам полезное примечание¹:

= help: the trait `std::fmt::Debug` is not implemented for `Rectangle`
= note: add `#[derive(Debug)]` or manually implement `std::fmt::Debug`

Язык Rust включает в себя функциональность печати отладочной информации, но мы должны согласиться с тем, чтобы сделать эту функциональность доступной для структуры. Для этого нужно добавить аннотацию #[derive (Debug)] непосредственно перед определением структуры, как показано в листинге 5.12.

Листинг 5.12. Добавление аннотации для генерирования типажа Debug и печати экземпляра структуры Rectangle с использованием отладочного форматирования src/main.rs

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle { width: 30, height: 50 };

    println!("rect1 равен {:?}", rect1);
}
```

Теперь, выполнив эту программу, мы не получим никаких ошибок и увидим следующий результат:

rect1 равен Rectangle { width: 30, height: 50 }

Здорово! Этот результат не самый красивый, но он показывает значения всех полей для этого экземпляра, что определенно поможет во время отладки. Когда есть

¹ справка: типаж `std::fmt::Debug` не реализован для `Rectangle`
¹ примечание: добавьте `#[derive(Debug)]` либо реализуйте `std::fmt::Debug` вручную