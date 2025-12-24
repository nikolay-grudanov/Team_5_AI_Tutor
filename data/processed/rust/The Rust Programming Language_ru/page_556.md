---
source_image: page_556.png
page_number: 556
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 45.92
tokens: 11689
characters: 1716
timestamp: 2025-12-24T10:41:48.173057
finish_reason: stop
---

использовать в зависимости от типа self.

Однако ассоциированные функции являющиеся частью типажей не имеют self параметра. Когда два типа в одной области видимости реализуют такой типаж, Rust не может выяснить, какой тип вы имеете в виду если вы не используете полностью квалифицированный синтаксис (fully qualified). Например, типаж Animal в листинге 19-19 имеет: ассоциированную функцию baby_name, реализацию типажа Animal для структуры Dog и ассоциированную функцию baby_name, объявленную напрямую у структуры Dog.

Файл: src/main.rs

trait Animal {
    fn baby_name() -> String;
}

struct Dog;

impl Dog {
    fn baby_name() -> String {
        String::from("Spot")
    }
}

impl Animal for Dog {
    fn baby_name() -> String {
        String::from("puppy")
    }
}

fn main() {
    println!("A baby dog is called a {}", Dog::baby_name());
}

Листинг 19-19: Типаж с ассоциированной функцией и тип с ассоциированной функцией с тем же именем, которая тоже реализует типаж

Этот код для приюта для животных, который хочет назвать всех щенков именем Spot, что реализовано в ассоциированной функции baby_name, которая определена для Dog. Тип Dog также реализует типаж Animal, который описывает характеристики, которые есть у всех животных. Маленьких собак называют щенками, и это выражается в реализации Animal у Dog в функции baby_name ассоциированной с типажом Animal.

В main мы вызываем функцию Dog::baby_name, которая вызывает ассоциированную функцию определённую напрямую у Dog. Этот код печатает следующее:

$ cargo run
Compiling traits-example v0.1.0 (file:///projects/traits-example)
Finished dev [unoptimized + debuginfo] target(s) in 0.54s
Running `target/debug/traits-example`
A baby dog is called a Spot