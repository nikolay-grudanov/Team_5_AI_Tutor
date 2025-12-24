---
source_image: page_412.png
page_number: 412
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.91
tokens: 11714
characters: 1706
timestamp: 2025-12-24T10:35:44.162657
finish_reason: stop
---

ссылке к значению, на которое она указывает (таким образом, происходит разыменование), для того чтобы компилятор при сравнении мог использовать фактическое значение. Как только мы разыменуем y, мы получим доступ к целочисленному значению, на которое указывает y, которое и будем сравнивать с 5.

Если бы мы попытались написать assert_eq!(5, y);, то получили ошибку компиляции:

$ cargo run
   Compiling deref-example v0.1.0 (file:///projects/deref-example)
error[E0277]: can't compare `{integer}` with `&{integer}`
 --> src/main.rs:6:5
  |
6 |     assert_eq!(5, y);
  |     ^^^^^^^^^^^^^^^^ no implementation for `{integer} == &{integer}`
  |
  = help: the trait `PartialEq<&{integer}>` is not implemented for `{integer}`
  = help: the following other types implement trait `PartialEq<Rhs>`:
    f32
    f64
    i128
    i16
    i32
    i64
    i8
    isize
    and 6 others
  = note: this error originates in the macro `assert_eq` (in Nightly builds, run with -Z macro-backtrace for more info)

For more information about this error, try `rustc --explain E0277`.
error: could not compile `deref-example` due to previous error

Сравнение числа и ссылки на число не допускается, потому что они различных типов. Мы должны использовать оператор разыменования, чтобы перейти по ссылке на значение, на которое она указывает.

Использование Box<T> как ссылку

Мы можем переписать код в листинге 15-6, чтобы использовать Box<T> вместо ссылки; оператор разыменования, используемый для Box<T> в листинге 15-7, работает так же, как оператор разыменования, используемый для ссылки в листинге 15-6:

Файл: src/main.rs

fn main() {
    let x = 5;
    let y = Box::new(x);

    assert_eq!(5, x);
    assert_eq!(5, *y);
}