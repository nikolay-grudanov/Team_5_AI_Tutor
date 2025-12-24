---
source_image: page_147.png
page_number: 147
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.41
tokens: 11747
characters: 1939
timestamp: 2025-12-24T10:24:45.965999
finish_reason: stop
---

Оно совпадает! Для данной ветки шаблон (None) не подразумевает наличие какого-то значения к которому можно было бы что-то добавить, поэтому программа останавливается и возвращает значение которое находится справа от => - т.е. None. Так как шаблон первой ветки совпал, то никакие другие шаблоны веток не сравниваются.

Комбинирование match и перечислений полезно во многих ситуациях. Вы часто будете видеть подобную комбинацию в коде на Rust: сделать сопоставление значений перечисления используя match, привязать переменную к данным внутри значения, выполнить код на основе привязанных данных. Сначала это может показаться немного сложным, но как только вы привыкнете, то захотите чтобы такая возможность была бы во всех языках. Это неизменно любимый пользователями приём.

Match объемлет все варианты значения

Есть ещё один аспект match, который мы должны обсудить: шаблоны должны покрывать все возможные варианты. Рассмотрим эту версию нашей функции plus_one, которая содержит ошибку и не компилируется:

```rust
fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
        Some(i) => Some(i + 1),
    }
}
```

Мы не обработали вариант None, поэтому этот код вызовет дефект в программе. К счастью, Rust знает и умеет ловить такой случай. Если мы попытаемся скомпилировать такой код, мы получим ошибку компиляции:

```
$ cargo run
Compiling enums v0.1.0 (file:///projects/enums)
error[E0004]: non-exhaustive patterns: `None` not covered
 --> src/main.rs:3:15
  |
3 |     match x {
  |         ^ pattern `None` not covered
note: `Option<i32>` defined here
 = note: the matched value is of type `Option<i32>`
help: ensure that all possible cases are being handled by adding a match arm with a wildcard pattern or an explicit pattern as shown
|
4  ~      Some(i) => Some(i + 1),
5  ~      None => todo!(),
|
For more information about this error, try `rustc --explain E0004`.
error: could not compile `enums` due to previous error
```