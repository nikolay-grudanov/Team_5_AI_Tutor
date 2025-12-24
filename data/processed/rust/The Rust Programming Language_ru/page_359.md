---
source_image: page_359.png
page_number: 359
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 58.76
tokens: 11776
characters: 2046
timestamp: 2025-12-24T10:33:47.515756
finish_reason: stop
---

Листинг 13-8: Попытка использовать замыкание FnOnce с sort_by_key

Это надуманный, запутанный способ (который не работает) попытаться подсчитать количество вызовов sort_by_key при сортировке list. Этот код пытается выполнить подсчёт, перемещая value - String из окружения замыкания - в вектор sort_operations. Замыкание захватывает value, затем перемещает value из замыкания, передавая право собственности на value вектору sort_operations. Это замыкание можно вызвать один раз; попытка вызвать его второй раз не сработает, потому что value уже не будет находиться в той среде, из которой его можно будет снова поместить в sort_operations! Поэтому это замыкание реализует только FnOnce. Когда мы пытаемся скомпилировать этот код, мы получаем ошибку, что value не может быть перемещено из замыкания, потому что замыкание должно реализовать FnMut:

$ cargo run
Compiling rectangles v0.1.0 (file:///projects/rectangles)
error[E0507]: cannot move out of `value`, a captured variable in an `FnMut` closure
 --> src/main.rs:18:30
  |
15 |     let value = String::from("by key called");
  |         ----- captured outer variable
16 |
17 |     list.sort_by_key(|r| {
18 |         sort_operations.push(value);
  |         ^^^^^ move occurs because `value` has type `String`, which does not implement the `Copy` trait
19 |         r.width
20 |     });
  |____- captured by this `FnMut` closure

For more information about this error, try `rustc --explain E0507`.
error: could not compile `rectangles` due to previous error

Ошибка указывает на строку в теле замыкания, которая перемещает value из окружения. Чтобы исправить это, нужно изменить тело замыкания так, чтобы оно не перемещало значения из окружения. Для подсчёта количества вызовов sort_by_key более простым способом является хранение счётчика в окружении и увеличение его значения в теле закрытия. Замыкание в листинге 13-9 работает с sort_by_key, поскольку оно фиксирует только изменяемую ссылку на счётчик num_sort_operations и поэтому может быть вызвано более одного раза:

Файл : src/main.rs