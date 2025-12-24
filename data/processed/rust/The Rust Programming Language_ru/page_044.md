---
source_image: page_044.png
page_number: 44
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.64
tokens: 11578
characters: 1514
timestamp: 2025-12-24T10:20:18.887043
finish_reason: stop
---

use rand::Rng;
use std::cmp::Ordering;
use std::io;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    loop {
        println!("Please input your guess.");

        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("You guessed: {guess}");

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }
}

Листинг 2-6: Полный код игры в угадывание

Итоги

На данный момент вы успешно создали игру в угадывание. Поздравляем!

Этот проект - практический способ познакомить вас со многими новыми концепциями Rust: let, match, функции, использование внешних пакетов и многое другое. В следующих нескольких главах вы изучите эти концепции более подробно. Глава 3 охватывает понятия, которые есть в большинстве языков программирования, такие как переменные, типы данных и функции, и показывает, как использовать их в Rust. В главе 4 рассматривается владение, особенность, которая отличает Rust от других языков. В главе 5 обсуждаются структуры и синтаксис методов, а в главе 6 объясняется, как работают перечисления.