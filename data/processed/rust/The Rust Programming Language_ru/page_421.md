---
source_image: page_421.png
page_number: 421
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 46.64
tokens: 11710
characters: 1878
timestamp: 2025-12-24T10:36:07.474791
finish_reason: stop
---

типичных случаях вы будете задавать код очистки, который должен выполнить ваш тип, а не печатать сообщение.

Раннее удаление значения с помощью std::mem::drop

К сожалению, отключение функции автоматического удаления с помощью drop является не простым. Отключение drop обычно не требуется; весь смысл типажа Drop том, чтобы о функции позаботились автоматически. Иногда, однако, вы можете захотеть очистить значение рано. Одним из примеров является использование интеллектуальных указателей, которые управляют блокировками: вы могли бы потребовать принудительный вызов метода drop который снимает блокировку, чтобы другой код в той же области видимости мог получить блокировку. Rust не позволяет вызвать метод типа Drop вручную; вместо этого вы должны вызвать функцию std::mem::drop предоставляемую стандартной библиотекой, если хотите принудительно удалить значение до конца области видимости.

Если попытаться вызвать метод drop типа Drop вручную, изменяя функцию main листинга 15-14 так, как показано в листинге 15-15, мы получим ошибку компилятора:

Файл: src/main.rs

```rust
fn main() {
    let c = CustomSmartPointer {
        data: String::from("some data"),
    };
    println!("CustomSmartPointer created.");
    c.drop();
    println!("CustomSmartPointer dropped before the end of main.");
}
```

Листинг 15-15: Попытка вызвать метод drop из трейта Drop вручную для досрочной очистки

Когда мы попытаемся скомпилировать этот код, мы получим ошибку:

$ cargo run
Compiling drop-example v0.1.0 (file:///projects/drop-example)
error[E0040]: explicit use of destructor method
 --> src/main.rs:16:7
  |
16 |     c.drop();
  |     ^^^^^^
  |     |
  |     explicit destructor calls not allowed
  help: consider using `drop` function: `drop(c)`

For more information about this error, try `rustc --explain E0040`.
error: could not compile `drop-example` due to previous error