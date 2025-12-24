---
source_image: page_571.png
page_number: 571
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 56.23
tokens: 11758
characters: 1893
timestamp: 2025-12-24T10:42:34.370365
finish_reason: stop
---

использовать замыкания. Оба варианта компилируется в один и тот же код, поэтому используйте любой стиль, который вам понятнее.

Возврат замыканий

Замыкания представлены типажами, что означает невозможность напрямую вернуть замыкания. В большинстве случаев, когда вы возможно хотите вернуть типаж, вы вместо этого используете конкретный тип, который реализует типаж в качестве возвращаемого значения функции. Но вы не можете сделать этого с замыканиями, потому что у них нет конкретного типа, который можно вернуть; не разрешается использовать указатель функции `fn` в качестве возвращаемого типа, например.

Следующий код пытается напрямую вернуть замыкание, но он не компилируется:

```rust
fn returns_closure() -> dyn Fn(i32) -> i32 {
    |x| x + 1
}
```

Ошибку компилятора выглядит следующим образом:

```
$ cargo build
Compiling functions-example v0.1.0 (file:///projects/functions-example)
error[E0746]: return type cannot have an unboxed trait object
 --> src/lib.rs:1:25
  |
1 | fn returns_closure() -> dyn Fn(i32) -> i32 {
  | ^^^^^^^^^^^^^^^^^^^^^^^^ doesn't have a size known at compile-time
  = note: for information on `impl Trait`, see <https://doc.rust-lang.org/book/ch10-02-traits.html#returning-types-that-implement-traits>
help: use `impl Fn(i32) -> i32` as the return type, as all return paths are of type `[closure@src/lib.rs:2:5: 2:14]`, which implements `Fn(i32) -> i32`
  |
1 | fn returns_closure() -> impl Fn(i32) -> i32 {
  | ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
For more information about this error, try `rustc --explain E0746`.
error: could not compile `functions-example` due to previous error
```

Ошибка снова ссылается на типаж `Sized`! Rust не знает, сколько памяти нужно будет выделить для замыкания. Мы видели решение этой проблемы ранее. Мы можем использовать типаж-объект:

```rust
fn returns_closure() -> Box<dyn Fn(i32) -> i32> {
    Box::new(|x| x + 1)
}
```