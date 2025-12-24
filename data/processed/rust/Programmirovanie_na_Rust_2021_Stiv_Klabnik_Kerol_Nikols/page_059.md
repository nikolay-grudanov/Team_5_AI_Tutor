---
source_image: page_059.png
page_number: 59
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.81
tokens: 7379
characters: 1399
timestamp: 2025-12-24T10:47:04.974578
finish_reason: stop
---

Теперь в программе все должно работать как следует. Давайте испытаем ее:

$ cargo run
    Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 1.50 secs
    Running `target/debug/guessing_game`
Угадайте число!
Секретное число равно 61
Пожалуйста, введите свою догадку.
10
Вы загадали: 10
Слишком малое число!
Пожалуйста, введите свою догадку.
99
Вы загадали: 99
Слишком большое число!
Пожалуйста, введите свою догадку.
foo
Пожалуйста, введите свою догадку.
61
Вы загадали: 61
Вы выиграли!

Потрясающе! Благодаря одной крошечной финальной доработке мы завершим игру-угадайку! Напомним, что программа по-прежнему выводит секретное число. Это пригодилось для тестирования, но портит игру. Давайте удалим макрокоманду println!, которая выводит секретное число. В листинге 2.6 показан окончательный код.

Листинг 2.6. Полный код игры-угадайки

src/main.rs

use std::io;
use std::cmp::Ordering;
use rand::Rng;

fn main() {
    println!("Угадайте число!");

    let secret_number = rand::thread_rng().gen_range(1, 101);

    loop {
        println!("Пожалуйста, введите свою догадку.");

        let mut guess = String::new();

        io::stdin().read_line(&mut guess)
            .expect("Не получилось прочитать строку");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,