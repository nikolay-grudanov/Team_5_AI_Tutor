---
source_image: page_578.png
page_number: 578
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.98
tokens: 11538
characters: 1339
timestamp: 2025-12-24T10:42:24.926582
finish_reason: stop
---

use hello_macro::HelloMacro;
use hello_macro_derive::HelloMacro;

#[derive(HelloMacro)]
struct Pancakes;

fn main() {
    Pancakes::hello_macro();
}

Листинг 19-30: Код, который сможет писать пользователь нашего крейта при использовании нашего процедурного макроса

Этот код напечатает Hello, Macro! My name is Pancakes!, когда мы закончим. Первый шаг - создать новый, библиотечный крейт так:

$ cargo new hello_macro --lib

Далее, мы определим типаж HelloMacro и ассоциированную с ним функцию:

Файл: src/lib.rs

pub trait HelloMacro {
    fn hello_macro();
}

У нас есть типаж и его функция. На этом этапе пользователь крейта может реализовать типаж для достижения желаемой функциональности, так:

use hello_macro::HelloMacro;

struct Pancakes;

impl HelloMacro for Pancakes {
    fn hello_macro() {
        println!("Hello, Macro! My name is Pancakes!");
    }
}

fn main() {
    Pancakes::hello_macro();
}

Тем не менее, ему придётся написать блок реализации для каждого типа, который он хотел использовать вместе с hello_macro; а мы хотим избавить их от необходимости делать эту работу.

Кроме того, мы пока не можем предоставить функцию hello_macro с реализацией по умолчанию, которая будет печатать имя типа, для которого реализован типаж: Rust не имеет возможностей рефлексии (reflection), поэтому он не может выполнить поиск имени