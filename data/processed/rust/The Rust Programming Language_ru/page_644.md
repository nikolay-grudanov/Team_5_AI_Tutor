---
source_image: page_644.png
page_number: 644
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.18
tokens: 11639
characters: 1497
timestamp: 2025-12-24T10:45:16.253067
finish_reason: stop
---

Мы вызываем функцию do_something 100 раз, но никогда не используем переменную i в теле цикла for. Rust предупреждает нас об этом:

$ cargo build
    Compiling myprogram v0.1.0 (file:///projects/myprogram)
warning: unused variable: `i`
 --> src/main.rs:4:9
  |
4 |     for i in 0..100 {
  |         ^ help: consider using `_i` instead
  |
= note: #[warn(unused_variables)] on by default

Finished dev [unoptimized + debuginfo] target(s) in 0.50s

Предупреждение предлагает нам использовать _i как имя переменной: нижнее подчёркивание в начале идентификатора предполагает, что мы его не используем. Мы можем автоматически применить это предположение с помощью rustfix, запустив команду cargo fix:

$ cargo fix
    Checking myprogram v0.1.0 (file:///projects/myprogram)
      Fixing src/main.rs (1 fix)
    Finished dev [unoptimized + debuginfo] target(s) in 0.59s

Когда посмотрим в src/main.rs снова, мы увидим что cargo fix изменил наш код:

Файл: src/main.rs

fn do_something() {}

fn main() {
    for _i in 0..100 {
        do_something();
    }
}

Переменная цикла for теперь носит имя _i, и предупреждение больше не появляется.

Также Вы можете использовать команду cargo fix для перемещения вашего кода между различными редакциями Rust. Редакции будут рассмотрены в дополнении Д.

Больше проверок с Clippy

Инструмент Clippy является коллекцией проверок (lints) для анализа Вашего кода, поэтому Вы можете найти простые ошибки и улучшить ваш Rust код.

Для установки Clippy, введите следующее: