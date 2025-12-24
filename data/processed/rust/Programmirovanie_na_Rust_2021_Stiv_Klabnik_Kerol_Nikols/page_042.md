---
source_image: page_042.png
page_number: 42
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.29
tokens: 7346
characters: 1407
timestamp: 2025-12-24T10:46:37.324556
finish_reason: stop
---

version = "0.1.0"
authors = ["Ваше имя <you@example.com>"]
edition = "2018"

[dependencies]

Если сведения об авторе, полученные из вашей среды, неверны, то исправьте их в файле и сохраните его снова.

Как вы увидели в главе 1, команда cargo new генерирует программу «Hello, World!». Проверьте файл src/main.rs:

src/main.rs
fn main() {
    println!("Hello, World!");
}

Теперь давайте скомпилируем эту программу «Hello, World!» и выполним ее, используя команду cargo run:

$ cargo run
Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
Finished dev [unoptimized + debuginfo] target(s) in 1.50 secs
    Running `target/debug/guessing_game`
Hello, World!

Команда run бывает очень кстати, когда требуются быстрые итерации по проекту, как в этой игре, где нужно будет оперативно тестировать каждую итерацию перед переходом к следующей.

Снова откройте файл src/main.rs. Вы будете писать весь код в этот файл.

Обработка загаданного числа

В первой части программы игры на угадывание пользователю нужно будет ввести данные, программа обработает эти данные и проверит, что они в корректной форме. Вначале мы даем игроку ввести загаданное число. Наберите код из листинга 2.1 в файл src/main.rs.

Листинг 2.1. Код, который получает от пользователя загаданное число и выводит его
src/main.rs
use std::io;

fn main() {
    println!("Угадайте число!");
    println!("Пожалуйста, введите свою догадку.");