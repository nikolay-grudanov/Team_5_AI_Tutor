---
source_image: page_262.png
page_number: 262
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 53.34
tokens: 11793
characters: 2204
timestamp: 2025-12-24T10:29:38.008468
finish_reason: stop
---

В этом примере переменная `string1` действительно до конца внешней области, `string2` действует до конца внутренней области видимости и `result` ссылается на что-то, что является действительным до конца внутренней области видимости. Запустите этот код, и вы увидите что анализатор заимствований разрешает такой код; он скомпилирует и напечатает `The longest string is long string is long`.

Теперь, давайте попробуем пример, который показывает, что время жизни ссылки `result` должно быть меньшим временем жизни одного из двух аргументов. Мы переместим объявление переменной `result` за пределы внутренней области видимости, но оставим присвоение значения переменной `result` в области видимости `string2`. Затем мы переместим `println!`, который использует `result` за пределы внутренней области видимости, после того как внутренняя область видимости закончилась. Код в листинге 10-23 не скомпилируется.

Файл: src/main.rs

```rust
fn main() {
    let string1 = String::from("long string is long");
    let result;
    {
        let string2 = String::from("xyz");
        result = longest(string1.as_str(), string2.as_str());
    }
    println!("The longest string is {}", result);
}
```

Листинг 10-23: Попытка использования `result`, после того как `string2` вышла из области видимости

При попытке скомпилировать этот код, мы получим такую ошибку:

```
$ cargo run
   Compiling chapter10 v0.1.0 (file:///projects/chapter10)
error[E0597]: `string2` does not live long enough
 --> src/main.rs:6:44
  |
6 |         result = longest(string1.as_str(), string2.as_str());
  |                                  ^^^^^^^^^^^^^^^^^^^^ borrowed value does not live long enough
7 |     }
8 |     println!("The longest string is {}", result);
  |                ------ borrow later used here

For more information about this error, try `rustc --explain E0597`.
error: could not compile `chapter10` due to previous error
```

Эта ошибка говорит о том, что если мы хотим использовать `result` в `println!`, переменная `string2` должна бы быть действительно до конца внешней области видимости. Rust знает об этом, потому что мы аннотировали параметры функции и её возвращаемое значение одинаковым временем жизни `'a`.