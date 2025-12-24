---
source_image: page_587.png
page_number: 587
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.33
tokens: 7349
characters: 1428
timestamp: 2025-12-24T11:00:57.635365
finish_reason: stop
---

Rust, то, вероятно, видели предупреждения компилятора. Например, рассмотрим код:

src/main.rs
    fn do_something() {}

    fn main() {
        for i in 0..100 {
            do_something();
        }
    }

Здесь мы вызываем функцию do_something 100 раз, но никогда не используем переменную i в теле цикла for. Компилятор об этом предупреждает:

    $ cargo build
        Compiling myprogram v0.1.0 (file:///projects/myprogram)
    warning: unused variable: `i`
    --> src/main.rs:4:9
    |
    4 |     for i in 1..100 {
    |         ^ help: consider using `_i` instead
    |
    = note: #[warn(unused_variables)] on by default

    Finished dev [unoptimized + debuginfo] target(s) in 0.50s

Предупреждение рекомендует, чтобы мы использовали _i в качестве имени: подчеркивание указывает на то, что мы не намерены использовать эту переменную. Можно автоматически применить эту рекомендацию с помощью инструмента rustfix, выполнив команду cargo fix:

    $ cargo fix
        Checking myprogram v0.1.0 (file:///projects/myprogram)
        Fixing src/main.rs (1 fix)
        Finished dev [unoptimized + debuginfo] target(s) in 0.59s

Когда мы снова посмотрим на src/main.rs, мы увидим, что команда cargo fix изменила код:

src/main.rs
    fn do_something() {}

    fn main() {
        for _i in 0..100 {
            do_something();
        }
    }

Переменная цикла for теперь называется _i, и предупреждение больше не появляется.