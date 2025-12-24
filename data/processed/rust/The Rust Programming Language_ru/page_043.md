---
source_image: page_043.png
page_number: 43
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.88
tokens: 11409
characters: 747
timestamp: 2025-12-24T10:19:55.612068
finish_reason: stop
---

$ cargo run
    Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 4.45s
    Running `target/debug/guessing_game`
Guess the number!
The secret number is: 61
Please input your guess.
10
You guessed: 10
Too small!
Please input your guess.
99
You guessed: 99
Too big!
Please input your guess.
foo
Please input your guess.
61
You guessed: 61
You win!

Потрясающе! С помощью одной маленькой последней правки мы закончим игру в угадывание. Напомним, что программа все ещё печатает секретное число. Это хорошо подходило для тестирования, но это портит игру. Давайте удалим println!, который выводит секретное число. В Листинге 2-6 показан окончательный вариант кода.

Файл: src/main.rs