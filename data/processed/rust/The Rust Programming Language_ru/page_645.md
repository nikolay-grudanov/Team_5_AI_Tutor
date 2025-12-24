---
source_image: page_645.png
page_number: 645
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.73
tokens: 11597
characters: 1364
timestamp: 2025-12-24T10:45:15.845856
finish_reason: stop
---

$ rustup component add clippy

Для запуска проверок Clippy’s для проекта Cargo, введите следующее:

$ cargo clippy

Например, скажем что Вы хотите написать программу, в которой будет использоваться приближенная математическая константа, такая как число Пи, как в следующей программе:

Файл: src/main.rs

fn main() {
    let x = 3.1415;
    let r = 8.0;
    println!("the area of the circle is {}", x * r * r);
}

Запуск cargo clippy для этого проекта вызовет следующую ошибку:

error: approximate value of `f{32, 64}::consts::PI` found. Consider using it directly
 --> src/main.rs:2:13
  |
2 |     let x = 3.1415;
  |           ^^^^^^^
= note: #[deny(clippy::approx_constant)] on by default
= help: for further information visit https://rust-lang-nursery.github.io/rust-clippy/master/index.html#approx_constant

Эта ошибка сообщает вам, что в Rust уже определена более точная константа PI, и что ваша программа будет более корректной, если вы вместо неё будете использовать эту константу. Затем вы должны изменить свой код, чтобы использовать константу PI.

Следующий код не приводит к ошибкам или предупреждениям от Clippy:

Файл: src/main.rs

fn main() {
    let x = std::f64::consts::PI;
    let r = 8.0;
    println!("the area of the circle is {}", x * r * r);
}

Для большей информации о Clippy смотрите документацию.

Интеграция с IDE с помощью rust-analyzer