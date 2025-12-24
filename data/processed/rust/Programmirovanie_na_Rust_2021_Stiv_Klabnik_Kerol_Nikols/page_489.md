---
source_image: page_489.png
page_number: 489
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.29
tokens: 7454
characters: 1721
timestamp: 2025-12-24T10:58:34.769896
finish_reason: stop
---

утверждение означает, что, если мы передадим индекс, который больше индекса, в котором делится срез, то эта функция поднимет панику до попытки использовать этот индекс.

Затем мы возвращаем два изменяемых среза в кортеже: один от начала исходного среза до индекса mid, а другой от mid до конца среза.

Когда мы попытаемся скомпилировать код из листинга 19.5, возникнет ошибка¹:

error[E0499]: cannot borrow `*slice` as mutable more than once at a time
  --> 
6 |     (&mut slice[..mid],
   |      ---- first mutable borrow occurs here
7 |     &mut slice[mid..])
   |      ^^^^^ second mutable borrow occurs here
8 | }
   | - first borrow ends here

Контролер заимствования Rust не может понять, что мы заимствуем разные части среза. Он только знает, что мы заимствуем у одного и того же среза дважды. Заимствовать разные части среза в принципе нормально, потому что два среза не перекрываются, но язык Rust недостаточно умен, чтобы это знать. Когда нам известно, что с кодом все в порядке, а языку Rust — нет, самое время обратиться к небезопасному коду.

Листинг 19.6 показывает, как использовать блок unsafe, сырой указатель и несколько вызовов небезопасных функций, чтобы привести реализацию split_at_mut в рабочее состояние.

Листинг 19.6. Использование небезопасного кода в реализации функции split_at_mut
use std::slice;

fn split_at_mut(slice: &mut [i32], mid: usize) -> (&mut [i32], &mut [i32]) {
    let len = slice.len();
    let ptr = slice.as_mut_ptr();

    assert!(mid <= len);

    unsafe {
        (slice::from_raw_parts_mut(ptr, mid),
         slice::from_raw_parts_mut(ptr.offset(mid as isize), len - mid))
    }
}

¹ ошибка[E0499]: не получается позаимствовать `*slice` как изменяемый более одного раза