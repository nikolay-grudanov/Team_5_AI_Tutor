---
source_image: page_101.png
page_number: 101
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.21
tokens: 11512
characters: 1170
timestamp: 2025-12-24T10:22:41.455294
finish_reason: stop
---

Давайте подробнее рассмотрим, что именно происходит на каждом этапе нашего кода dangle:

Файл: src/main.rs

```rust
fn dangle() -> &String { // dangle returns a reference to a String
    let s = String::from("hello"); // s is a new String
    &s // we return a reference to the String, s
} // Here, s goes out of scope, and is dropped. Its memory goes away.
   // Danger!
```

Поскольку s создаётся внутри dangle, когда код dangle будет завершён, s будет освобождена. Но мы попытались вернуть ссылку на неё. Это означает, что эта ссылка будет указывать на недопустимую String. Это неправильно! Rust не позволит нам сделать это.

Решением будет вернуть непосредственно String:

```rust
fn no_dangle() -> String {
    let s = String::from("hello");
    s
}
```

Это работает без проблем. Владение перемещено, и ничего не освобождено.

Правила работы с ссылками

Давайте повторим все, что мы обсудили про ссылки:

• В один момент времени, может существовать либо одна изменяемая ссылочная переменная, либо любое количество неизменяемых ссылочных переменных,
• Все ссылки должны быть действительными.

В следующей главе мы рассмотрим другой тип ссылочных переменных — срезы.