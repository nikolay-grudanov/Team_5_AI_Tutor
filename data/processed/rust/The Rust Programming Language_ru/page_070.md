---
source_image: page_070.png
page_number: 70
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 48.22
tokens: 11609
characters: 1543
timestamp: 2025-12-24T10:21:37.959185
finish_reason: stop
---

кода if запускался только, когда число не равно 0, то, например, мы можем изменить выражение if на следующее:

Имя файла: src/main.rs

fn main() {
    let number = 3;

    if number != 0 {
        println!("number was something other than zero");
    }
}

Будет напечатана следующая строка number was something other than zero.

Обработка нескольких условий с помощью else if

Можно использовать несколько условий, комбинируя if и else в выражении else if.
Например:

Имя файла: src/main.rs

fn main() {
    let number = 6;

    if number % 4 == 0 {
        println!("number is divisible by 4");
    } else if number % 3 == 0 {
        println!("number is divisible by 3");
    } else if number % 2 == 0 {
        println!("number is divisible by 2");
    } else {
        println!("number is not divisible by 4, 3, or 2");
    }
}

У этой программы есть четыре возможных пути выполнения. После её запуска вы должны увидеть следующий результат:

$ cargo run
Compiling branches v0.1.0 (file:///projects/branches)
Finished dev [unoptimized + debuginfo] target(s) in 0.31s
    Running `target/debug/branches`
number is divisible by 3

Во время выполнения этой программы по очереди проверяется каждое выражение if и выполняется первое тело, для которого условие истинно. Заметьте, что хотя 6 делится на 2, мы не видим ни вывода number is divisible by 2, ни текста number is not divisible by 4, 3, or 2 из блока else. Так происходит потому, что Rust выполняет блок только для первого истинного условия, а обнаружив его, даже не проверяет остальные.