---
source_image: page_422.png
page_number: 422
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 60.43
tokens: 11737
characters: 2110
timestamp: 2025-12-24T10:36:26.342647
finish_reason: stop
---

Это сообщение об ошибке говорит, что мы не можем явно вызывать drop. В сообщении об ошибке используется термин деструктор (destructor), который является общим термином программирования для функции, которая очищает экземпляр. Деструктор аналогичен конструктору, который создаёт экземпляр. Функция drop в Rust является определённым деструктором.

Rust не позволяет обращаться к drop напрямую, потому что он все равно автоматически вызовет drop в конце main. Это вызвало бы ошибку double free, потому что в этом случае Rust попытался бы дважды очистить одно и то же значение.

Невозможно отключить автоматическую подстановку вызова drop, когда значение выходит из области видимости, и нельзя вызвать метод drop напрямую. Поэтому, если нам нужно принудительно избавиться от значения раньше времени, следует использовать функцию std::mem::drop.

Функция std::mem::drop отличается от метода drop трейта Drop. Мы вызываем её, передавая в качестве аргумента значение, которое хотим принудительно уничтожить. Функция находится в прелюдии, поэтому мы можем изменить main в листинге 15-15 так, чтобы вызвать функцию drop, как показано в листинге 15-16:

Файл: src/main.rs

```rust
fn main() {
    let c = CustomSmartPointer {
        data: String::from("some data"),
    };
    println!("CustomSmartPointer created.");
    drop(c);
    println!("CustomSmartPointer dropped before the end of main.");
}
```

Листинг 15-16: Вызов std::mem::drop для принудительного удаления значения до того, как оно выйдет из области видимости

Выполнение данного кода выведет следующий результат::

$ cargo run
Compiling drop-example v0.1.0 (file:///projects/drop-example)
Finished dev [unoptimized + debuginfo] target(s) in 0.73s
    Running `target/debug/drop-example`
CustomSmartPointer created.
Dropping CustomSmartPointer with data `some data`!
CustomSmartPointer dropped before the end of main.

Текст Dropping CustomSmartPointer with data some data!, напечатанный между CustomSmartPointer created. и текстом CustomSmartPointer dropped before the end of main., показывает, что код метода drop вызывается для удаления с в этой точке.