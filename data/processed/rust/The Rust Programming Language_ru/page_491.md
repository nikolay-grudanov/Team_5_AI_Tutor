---
source_image: page_491.png
page_number: 491
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.28
tokens: 11481
characters: 1143
timestamp: 2025-12-24T10:38:38.554683
finish_reason: stop
---

Листинг 17-8: Другой крейт, использующий gui и реализующий типаж Draw у структуры SelectBox

Пользователь нашей библиотеки теперь может написать свою функцию main для создания экземпляра Screen. К экземпляру Screen он может добавить SelectBox и Button, поместив каждый из них в Box<T>, чтобы он стал типаж-объектом. Затем он может вызвать метод run у экземпляра Screen, который вызовет draw для каждого из компонентов. Листинг 17-9 показывает эту реализацию:

Файл: src/main.rs

use gui::{Button, Screen};

fn main() {
    let screen = Screen {
        components: vec![
            Box::new(SelectBox {
                width: 75,
                height: 10,
                options: vec![
                    String::from("Yes"),
                    String::from("Maybe"),
                    String::from("No"),
                ],
            }),
            Box::new(Button {
                width: 50,
                height: 10,
                label: String::from("OK"),
            }),
        ],
    };

    screen.run();
}

Листинг 17-9: Использование типаж-объектов для хранения значений разных типов, реализующих один и тот же типаж