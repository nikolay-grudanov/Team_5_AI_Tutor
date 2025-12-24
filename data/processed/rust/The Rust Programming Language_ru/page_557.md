---
source_image: page_557.png
page_number: 557
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 55.70
tokens: 11778
characters: 2047
timestamp: 2025-12-24T10:42:00.888340
finish_reason: stop
---

Этот вывод является не тем, что мы хотели получить. Мы хотим вызвать функцию baby_name, которая является частью типажа Animal реализованного у Dog, так чтобы код печатал A baby dog is called a puppy. Техника указания имени типажа использованная в листинге 19-18 здесь не помогает; если мы изменим main код как в листинге 19-20, мы получим ошибку компиляции.

Файл: src/main.rs

```rust
fn main() {
    println!("A baby dog is called a {}", Animal::baby_name());
}
```

Листинг 19-20. Попытка вызвать функцию baby_name из типажа Animal, но Rust не знает какую реализацию использовать

Так как Animal::baby_name является ассоциированной функцией не имеющей self параметра в сигнатуре, а не методом, то Rust не может понять, какую реализацию Animal::baby_name мы хотим вызвать. Мы получим эту ошибку компилятора:

```
$ cargo run
   Compiling traits-example v0.1.0 (file:///projects/traits-example)
error[E0283]: type annotations needed
 --> src/main.rs:20:43
  |
20 |     println!("A baby dog is called a {}", Animal::baby_name());
  |                                  ^^^^^^^^^^^^^^^^^^^ cannot infer type
  = note: cannot satisfy `_: Animal`

For more information about this error, try `rustc --explain E0283`.
error: could not compile `traits-example` due to previous error
```

Чтобы устранить неоднозначность и сказать Rust, что мы хотим использовать реализацию Animal для Dog, нужно использовать полный синтаксис. Листинг 19-21 демонстрирует, как использовать полный синтаксис.

Файл: src/main.rs

```rust
fn main() {
    println!("A baby dog is called a {}", <Dog as Animal>::baby_name());
}
```

Листинг 19-21: Использование полностью квалифицированного синтаксиса для указания, что мы мы хотим вызвать функцию baby_name у типажа Animal реализованную в Dog

Мы указываем аннотацию типа в угловых скобках, которая указывает на то что мы хотим вызвать метод baby_name из типажа Animal реализованный в Dog, также указывая что мы хотим рассматривать тип Dog в качестве Animal для вызова этой функции. Этот код теперь напечатает то, что мы хотим: