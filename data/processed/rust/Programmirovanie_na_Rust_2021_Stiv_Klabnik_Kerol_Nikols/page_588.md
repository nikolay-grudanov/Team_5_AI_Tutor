---
source_image: page_588.png
page_number: 588
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.69
tokens: 7394
characters: 1578
timestamp: 2025-12-24T11:00:59.479237
finish_reason: stop
---

Вы также можете использовать команду cargo fix для транзита кода между разными редакциями Rust. Редакции рассматриваются в приложении Д далее.

Статический анализ кода с помощью Clippy

Инструмент Clippy представляет собой коллекцию проверок для анализа кода, благодаря которому вы можете фиксировать распространенные ошибки и улучшать код Rust.

Для того чтобы инсталлировать Clippy, введите следующее:

    $ rustup component add clippy

Для запуска проверок Clippy в любом проекте Cargo введите:

    $ cargo clippy

Например, вы пишете программу, которая использует аппроксимацию математической константы π, как в этой программе:

src/main.rs
    fn main() {
        let x = 3.1415;
        let r = 8.0;
        println!("площадь окружности равна {}", x * r * r);
    }

Выполнение команды cargo clippy в этом проекте приведет к ошибке¹:

error: approximate value of `f{32, 64}::consts::PI` found. Consider using it directly
 --> src/main.rs:2:13
  |
2 |     let x = 3.1415;
  |     ^^^^^^
  |
  = note: #[deny(clippy::approx_constant)] on by default
  = help: for further information visit https://rust-lang-nursery.github.io/rust-clippy/master/index.html#approx_constant

Благодаря ошибке понятно, что в языке Rust эта константа определена точнее, и программа могла бы быть правильнее, если бы вы использовали константу. Затем вы изменяете код так, чтобы в нем использовалась константа PI. Следующий код не приводит ни к ошибкам, ни к предупреждениям со стороны Clippy:

¹ ошибка: найдено приближенное значение `f{32, 64}::consts::PI`. Подумайте о его прямом использовании