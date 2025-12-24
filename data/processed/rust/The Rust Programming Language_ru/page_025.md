---
source_image: page_025.png
page_number: 25
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.76
tokens: 11573
characters: 1399
timestamp: 2025-12-24T10:19:23.528996
finish_reason: stop
---

fn main() {
    println!("Hello, world!");
}

Теперь давайте скомпилируем программу "Hello, world!" и сразу на этом же этапе запустим её с помощью команды cargo run:

$ cargo run
Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
Finished dev [unoptimized + debuginfo] target(s) in 1.50s
    Running `target/debug/guessing_game`
Hello, world!

Команда run пригодится, когда необходимо ускоренно выполнить итерацию проекта, мы так собираемся сделать в этом проекте, быстро тестируя каждую итерацию, прежде чем перейти к следующей.

Снова откройте файл src/main.rs. Весь код вы будете писать в этом файле.

Обработка отгадки

Первая часть программы игры угадывания запрашивает ввод данных пользователем, обрабатывает их и проверяет, что вводимые данные имеют ожидаемую форму. Для начала мы позволим игроку ввести отгадку. Введите код из Листинга 2-1 в src/main.rs.

Файл: src/main.rs

use std::io;

fn main() {
    println!("Guess the number!");

    println!("Please input your guess.");

    let mut guess = String::new();

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

    println!("You guessed: {guess}");
}

Листинг 2-1: Код, который получает отгадку от пользователя и печатает её

Этот код содержит много информации, поэтому давайте рассмотрим его построчно.
Чтобы получить пользовательский ввод и затем вывести результат в качестве вывода,