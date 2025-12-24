---
source_image: page_075.png
page_number: 75
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.82
tokens: 7437
characters: 1843
timestamp: 2025-12-24T10:47:33.723755
finish_reason: stop
---

Давайте начнем новый двоичный проект functions («функции») и продолжим изучать функции. Поместите пример another_function в файл src/main.rs и выполните его. На выходе вы должны увидеть следующий результат:

$ cargo run
    Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 1.50 secs
    Running `target/debug/functions`
Hello, World!
Еще одна функция.

Строки кода исполняются в том порядке, в котором они появляются в функции main. Сначала выводится сообщение «Hello, World!», а затем вызывается функция another_function и выводится ее сообщение.

Параметры функций

Функции также могут определяться вместе с параметрами, то есть специальными переменными, являющимися частью сигнатуры функции. Когда у функции есть параметры, вы можете предоставить ей конкретные значения для этих параметров. Технически конкретные значения называются аргументами, но в обычной беседе люди склонны использовать термины «параметр» и «аргумент» взаимозаменяемо, как для переменных в определении функции, так и для конкретных значений, передаваемых при вызове функции.

Следующая переписанная версия функции another_function показывает, как выглядят параметры:

src/main.rs
fn main() {
    another_function(5);
}

fn another_function(x: i32) {
    println!("Значение x равно {}", x);
}

Попробуйте выполнить эту программу. На выходе вы должны получить следующий результат:

$ cargo run
    Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 1.50 secs
    Running `target/debug/functions`
Значение x равно 5

Объявление функции another_function имеет один параметр с именем x. Тип x задан как i32. Когда 5 передается в функцию another_function, макрокоманда println! помещает 5 туда, где в форматной строке находилась пара фигурных скобок.