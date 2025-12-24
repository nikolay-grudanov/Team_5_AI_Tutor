---
source_image: page_035.png
page_number: 35
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.17
tokens: 11596
characters: 1437
timestamp: 2025-12-24T10:19:55.528128
finish_reason: stop
---

Во второй новой строке печатается секретный номер. Полезно, пока разрабатывается программа, иметь возможность тестировать её, но в финальной версии мы это удалим. Конечно это не похоже на игру, если программа печатает ответ сразу после запуска!

Попробуйте запустить программу несколько раз:

$ cargo run
    Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 2.53s
        Running `target/debug/guessing_game`
Guess the number!
The secret number is: 7
Please input your guess.
4
You guessed: 4

$ cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.02s
        Running `target/debug/guessing_game`
Guess the number!
The secret number is: 83
Please input your guess.
5
You guessed: 5

Вы должны получить разные случайные числа, и все они должны быть числами от 1 до 100. Отличная работа!

Сравнение догадки с секретным числом

Теперь, когда у нас есть пользовательский ввод и случайное число, мы можем их сравнить. Этот шаг показан в Листинге 2-4. Обратите внимание, что этот код ещё не удастся скомпилировать.

Имя файла: src/main.rs

use rand::Rng;
use std::cmp::Ordering;
use std::io;

fn main() {
    // --snip--

    println!("You guessed: {guess}");

    match guess.cmp(&secret_number) {
        Ordering::Less => println!("Too small!"),
        Ordering::Greater => println!("Too big!"),
        Ordering::Equal => println!("You win!"),
    }
}