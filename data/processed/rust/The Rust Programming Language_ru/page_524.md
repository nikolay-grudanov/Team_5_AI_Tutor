---
source_image: page_524.png
page_number: 524
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 55.00
tokens: 11727
characters: 1760
timestamp: 2025-12-24T10:40:36.682658
finish_reason: stop
---

В этом примере значение r совпадает по второй ветке, так как x содержит значение 0, поэтому этот код будет печатать On the y axis at 7.

Помните, что выражение match перестаёт проверять следующие ветви, как только оно находит первый совпадающий шаблон, поэтому, даже если Point { x: 0, y: 0} находится на оси x и оси y, этот код будет печатать только On the x axis at 0.

Деструктуризация перечислений

Мы уже деструктурировали перечисления в книге (см., например, листинг 6-5 главы 6), но не обсуждали явно, что шаблон для деструктуризации перечисления должен соответствовать способу объявления данных, хранящихся в перечислении. Например, в листинге 18-15 мы используем перечисление Message из листинга 6-2 и пишем match с шаблонами, которые будут деструктурировать каждое внутреннее значение.

Файл: src/main.rs

enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

fn main() {
    let msg = Message::ChangeColor(0, 160, 255);

    match msg {
        Message::Quit => {
            println!("The Quit variant has no data to destructure.")
        }
        Message::Move { x, y } => {
            println!(
                "Move in the x direction {} and in the y direction {}",
                x, y
            );
        }
        Message::Write(text) => println!("Text message: {}", text),
        Message::ChangeColor(r, g, b) => println!(
            "Change the color to red {}, green {}, and blue {}",
            r, g, b
        ),
    }
}

Листинг 18-15: Деструктуризация вариантов перечисления, содержащих разные виды значений

Этот код напечатает Change the color to red 0, green 160, and blue 255. Попробуйте изменить значение переменной msg, чтобы увидеть выполнение кода в других ветках.