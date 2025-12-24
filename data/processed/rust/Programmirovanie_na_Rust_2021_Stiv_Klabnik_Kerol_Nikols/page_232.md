---
source_image: page_232.png
page_number: 232
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.36
tokens: 7487
characters: 1892
timestamp: 2025-12-24T10:51:52.608473
finish_reason: stop
---

На этот раз при компиляции кода мы получаем другой набор ошибок:

error[E0508]: cannot move out of type `[T]`, a non-copy slice
 --> src/main.rs:2:23
  |
2 |     let mut largest = list[0];
  |     ^^^^^^
  |     |
  |     cannot move out of here
  |     help: consider using a reference instead: `&list[0]`

error[E0507]: cannot move out of borrowed content
 --> src/main.rs:4:9
  |
4 |     for &item in list.iter() {
  |     ^-----
  |     ||
  |     |hint: to prevent move, use `ref item` or `ref mut item`
  |     cannot move out of borrowed content

Ключевой строчкой в этой ошибке является cannot move out of type [T], a non-copy slice. Работая с необобщенными версиями функции largest, мы пытались найти наибольшее значение только типов i32 или char. Как обсуждалось в разделе «Данные только из стека: Copy» (с. 99) такие типы, как i32 и char, которые имеют известный размер, хранятся в стеке, поэтому они реализуют типаж Copy. Но когда мы сделали функцию largest обобщенной, стало возможным, чтобы список параметров имел в ней типы, которые не реализуют типаж Copy. Как следствие, мы не сможем переместить значение из list[0] в переменную largest, что и приводит к этой ошибке.

Для того чтобы вызывать этот код только с теми типами, которые реализуют типаж Copy, мы можем добавить Copy в границы типажа для T! Листинг 10.15 показывает полный код обобщенной функции largest, которая будет компилироваться, пока типы значений в срезе, которые мы передаем внутрь функции, реализуют типажи PartialOrd и Copy, как это делают типы i32 и char.

Листинг 10.15. Рабочее определение функции largest, которая работает в любом обобщенном типе, реализующем типажи PartialOrd и Copy

src/main.rs

fn largest<T: PartialOrd + Copy>(list: &[T]) -> T {
    let mut largest = list[0];

    for &item in list.iter() {
        if item > largest {
            largest = item;
        }
    }

    largest
}