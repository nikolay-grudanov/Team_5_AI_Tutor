---
source_image: page_057.png
page_number: 57
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.03
tokens: 7390
characters: 1572
timestamp: 2025-12-24T10:47:04.985067
finish_reason: stop
---

Finished dev [unoptimized + debuginfo] target(s) in 1.50 secs
    Running `target/debug/guessing_game`
Угадайте число!
Секретное число равно 59
Пожалуйста, введите свою догадку.
45
Вы загадали: 45
Слишком малое число!
Пожалуйста, введите свою догадку.
60
Вы загадали: 60
Слишком большое число!
Пожалуйста, введите свою догадку.
59
Вы загадали: 59
Вы выиграли!
Пожалуйста, введите свою догадку.
выйти
thread 'main' panicked at 'Please type a number!: ParseIntError { kind: InvalidDigit }', src/libcore/result.rs:785
note: Run with `RUST_BACKTRACE=1` for a backtrace.

Набрав quit, вы фактически выходите из игры, но так же произойдет и при вводе любых других нечисловых данных. Мягко говоря, неразумно. Мы хотим, чтобы игра автоматически останавливалась, когда игрок угадывает правильное число.

Выход из игры после правильно угаданного числа

Давайте запрограммируем игру так, чтобы она завершалась, когда пользователь выигрывает, добавив для этого инструкцию break:

src/main.rs
    // --пропуск--
        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Слишком малое число!"),
            Ordering::Greater => println!("Слишком большое число!"),
            Ordering::Equal => {
                println!("Вы выиграли!");
                break;
            }
        }
    }

Добавление строки кода с инструкцией break после сообщения Вы выиграли! побуждает программу выйти из цикла, когда пользователь правильно угадывает секретное число. Выход из цикла также означает выход из программы, потому что цикл является последней частью функции main.