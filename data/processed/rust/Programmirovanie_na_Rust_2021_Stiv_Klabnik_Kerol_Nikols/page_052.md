---
source_image: page_052.png
page_number: 52
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.34
tokens: 7374
characters: 1515
timestamp: 2025-12-24T10:47:00.606901
finish_reason: stop
---

Попробуйте выполнить программу несколько раз:

    $ cargo run
        Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
        Finished dev [unoptimized + debuginfo] target(s) in 1.50 secs
        Running `target/debug/guessing_game`
    Угадайте число!
    Секретное число равно 7
    Пожалуйста, введите свою догадку.
    4
    Вы загадали: 4
    $ cargo run
        Running `target/debug/guessing_game`
    Угадайте число!
    Секретное число равно 83
    Пожалуйста, введите свою догадку.
    5
    Вы загадали: 5

Вы должны получить разные случайные числа, и все они должны быть от 1 до 100. Отлично!

Сравнение загаданного числа с секретным числом

Теперь, когда у нас есть данные, введенные пользователем, и случайное число, мы можем их сравнить. Этот шаг показан в листинге 2.4. Обратите внимание, что этот код пока что не компилируется, и позже мы объясним почему.

Листинг 2.4. Обработка возможных результатов сравнения двух чисел
src/main.rs

    use std::io;
    use std::cmp::Ordering;
    use rand::Rng;

    fn main() {
        // --пропуск--
        println!("Вы загадали: {}", guess);
        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Слишком малое число!"),
            Ordering::Greater => println!("Слишком большое число!"),
            Ordering::Equal => println!("Вы выиграли!"),
        }
    }

Здесь первый новый фрагмент — это еще одна инструкция use ①, вводящая тип с именем std::cmp::Ordering в область видимости из стандартной библиотеки.