---
source_image: page_543.png
page_number: 543
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 52.29
tokens: 11800
characters: 2135
timestamp: 2025-12-24T10:41:19.436828
finish_reason: stop
---

$ cargo run
Compiling unsafe-example v0.1.0 (file:///projects/unsafe-example)
error[E0499]: cannot borrow `*values` as mutable more than once at a time
--> src/main.rs:6:31
|
1 | fn split_at_mut(values: &mut [i32], mid: usize) -> (&mut [i32], &mut [i32]) {
|                - let's call the lifetime of this reference ``'1``
...
6 |     (&mut values[..mid], &mut values[mid..])
|______________________________^^^^^^^_______
|        |                           |
|        |                           second mutable borrow occurs here
|        first mutable borrow occurs here
|    returning this value requires that `*values` is borrowed for ``'1`

For more information about this error, try `rustc --explain E0499`.
error: could not compile `unsafe-example` due to previous error

Анализатор заимствований Rust не может понять, что мы заимствуем различные части среза, он понимает лишь, что мы хотим осуществить заимствование частей одного среза дважды. Заимствование различных частей среза в принципе нормально, потому что они не перекрываются, но Rust недостаточно умён, чтобы это понять. Когда мы знаем, что код верный, но Rust этого не понимает, значит пришло время прибегнуть к небезопасному коду.

Листинг 19-6 демонстрирует, как можно использовать unsafe блок, сырой указатель и вызовы небезопасных функций чтобы split_at_mut заработала:

use std::slice;

fn split_at_mut(values: &mut [i32], mid: usize) -> (&mut [i32], &mut [i32]) {
    let len = values.len();
    let ptr = values.as_mut_ptr();

    assert!(mid <= len);

    unsafe {
        (
            slice::from_raw_parts_mut(ptr, mid),
            slice::from_raw_parts_mut(ptr.add(mid), len - mid),
        )
    }
}

Листинг 19-6. Использование небезопасного кода в реализации функции split_at_mut

Напомним, из раздела "Тип срез" главы 4, что срезы состоят из указателя на некоторые данные и длины. Мы используем метод len для получения длины среза и метод as_mut_ptr для доступа к сырому указателю среза. Поскольку у нас есть изменяемый срез на значения типа i32, функция as_mut_ptr возвращает сырой указатель типа *mut i32, который мы сохранили в переменной ptr.