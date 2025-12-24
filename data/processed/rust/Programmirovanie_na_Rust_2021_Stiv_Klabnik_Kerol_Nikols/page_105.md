---
source_image: page_105.png
page_number: 105
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.31
tokens: 7360
characters: 1504
timestamp: 2025-12-24T10:48:18.665303
finish_reason: stop
---

src/main.rs

fn main() {
    let mut s = String::from("hello");

    change(&mut s);
}

fn change(some_string: &mut String) {
    some_string.push_str(", world");
}

Сначала нам пришлось внести изменение в s, добавив ключевое слово mut. Затем мы создали изменяемую ссылку с помощью &mut s и приняли ее с помощью some_string: &mut String.

Но изменяемые ссылки имеют одно существенное ограничение: у вас может быть только одна изменяемая ссылка на отдельный фрагмент данных в отдельной области видимости. Приведенный ниже код не сработает:

src/main.rs

let mut s = String::from("hello");

let r1 = &mut s;
let r2 = &mut s;

println!("{}, {}", r1, r2);

Вот ошибка¹:

error[E0499]: cannot borrow `s` as mutable more than once at a time
 --> src/main.rs:5:14
  |
4 |     let r1 = &mut s;
   |         ------ first mutable borrow occurs here
5 |     let r2 = &mut s;
   |         ^^^^^^ second mutable borrow occurs here
6 | 
7 |     println!("{}, {}", r1, r2);
   |                        -- first borrow later used here

Указанное ограничение допускает изменение, но это можно строго контролировать. С этим с трудом справляются новые растягиваемые, потому что большинство языков позволяют осуществлять изменение, когда вам захочется.

Преимущество этого ограничения в том, что Rust предотвращает гонку данных во время компиляции. Гонка данных похожа на гоночную ситуацию и случается при следующих обстоятельствах:

¹ ошибка[E0499]: не получается заимствовать переменную `s` как изменяемую более чем за раз