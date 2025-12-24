---
source_image: page_109.png
page_number: 109
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 62.14
tokens: 11713
characters: 1874
timestamp: 2025-12-24T10:23:24.246272
finish_reason: stop
---

Более опытные разработчики Rust написали бы сигнатуру из листинга 4-9, потому что она позволяет использовать одну функцию для значений обоих типов &String и &str.

```rust
fn first_word(s: &str) -> &str {
```

Листинг 4-9: Улучшение функции first_word с помощью среза строки для типа параметра s

Если у нас есть фрагмент строки, мы можем передать его напрямую. Если у нас есть String, мы можем передать часть String или ссылку на String. Эта гибкость использует преимущества разыменованного приведения, функции, которую мы рассмотрим в разделе «Неявные разыменованные приведения с функциями и методами». Главы 15. Определение функции, принимающей фрагмент строки вместо ссылки на String, делает наш API более общим и полезным без потери какой-либо функциональности:

Файл: src/main.rs

```rust
fn main() {
    let my_string = String::from("hello world");

    // `first_word` works on slices of `String`s, whether partial or whole
    let word = first_word(&my_string[0..6]);
    let word = first_word(&my_string[..]);
    // `first_word` also works on references to `String`s, which are equivalent
    // to whole slices of `String`s
    let word = first_word(&my_string);

    let my_string_literal = "hello world";

    // `first_word` works on slices of string literals, whether partial or whole
    let word = first_word(&my_string_literal[0..6]);
    let word = first_word(&my_string_literal[..]);

    // Because string literals *are* string slices already,
    // this works too, without the slice syntax!
    let word = first_word(my_string_literal);
}
```

Другие срезы

Как вы могли бы представить, строковые срезы относятся к строкам. Но также есть более общий тип среза. Рассмотрим массив:

```rust
let a = [1, 2, 3, 4, 5];
```

Подобно тому как мы хотели бы ссылаться на часть строки, мы можем захотеть ссылаться на часть массива. Мы можем делать это вот так: