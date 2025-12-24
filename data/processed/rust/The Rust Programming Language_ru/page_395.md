---
source_image: page_395.png
page_number: 395
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.51
tokens: 11581
characters: 1224
timestamp: 2025-12-24T10:34:48.188011
finish_reason: stop
---

В файле add_one/src/lib.rs добавим функцию add_one:

Файл: add_one/src/lib.rs

```rust
pub fn add_one(x: i32) -> i32 {
    x + 1
}
```

Теперь мы можем сделать так, чтобы пакет adder с нашим исполняемым файлом зависел от пакета add_one, содержащего нашу библиотеку. Сначала нам нужно добавить зависимость пути от add_one в adder/Cargo.toml.

Файл: adder/Cargo.toml

```toml
[dependencies]
add_one = { path = "../add_one" }
```

Cargo не исходит из того, что крейты в рабочем пространстве могут зависеть друг от друга, поэтому нам необходимо явно указать отношения зависимости.

Далее, давайте используем функцию add_one (из крейта add_one) в крейте adder. Откройте файл adder/src/main.rs и добавьте строку use в верхней части, чтобы ввести в область видимости новый библиотечный крейт add_one. Затем измените функцию main для вызова функции add_one, как показано в листинге 14-7.

Файл: adder/src/main.rs

```rust
use add_one;

fn main() {
    let num = 10;
    println!("Hello, world! {num} plus one is {}!", add_one::add_one(num));
}
```

Листинг 14-7: Использование функционала библиотечного крейта add-one в крейте adder

Давайте соберём рабочее пространство, запустив команду cargo build в каталоге верхнего уровня add!