---
source_image: page_358.png
page_number: 358
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.41
tokens: 11577
characters: 1377
timestamp: 2025-12-24T10:33:23.676764
finish_reason: stop
---

$ cargo run
    Compiling rectangles v0.1.0 (file:///projects/rectangles)
    Finished dev [unoptimized + debuginfo] target(s) in 0.41s
    Running `target/debug/rectangles`
[
    Rectangle {
        width: 3,
        height: 5,
    },
    Rectangle {
        width: 7,
        height: 12,
    },
    Rectangle {
        width: 10,
        height: 1,
    },
]

Причина, по которой sort_by_key определена как принимающая замыкание FnMut, заключается в том, что она вызывает замыкание несколько раз: по одному разу для каждого элемента в срезе. Замыкание |r| r.width не захватывает, не изменяет и не перемещает ничего из своего окружения, поэтому оно удовлетворяет требованиям связанности признаков.

И наоборот, в листинге 13-8 показан пример замыкания, которое реализует только признак FnOnce, потому что оно перемещает значение из среды. Компилятор не позволит нам использовать это замыкание с sort_by_key:

Файл : src/main.rs

#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let mut list = [
        Rectangle { width: 10, height: 1 },
        Rectangle { width: 3, height: 5 },
        Rectangle { width: 7, height: 12 },
    ];

    let mut sort_operations = vec![];
    let value = String::from("by key called");

    list.sort_by_key(|r| {
        sort_operations.push(value);
        r.width
    });
    println!("{:#?}", list);
}