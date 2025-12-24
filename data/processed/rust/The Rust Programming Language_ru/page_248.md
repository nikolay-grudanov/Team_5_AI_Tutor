---
source_image: page_248.png
page_number: 248
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 55.93
tokens: 11793
characters: 2165
timestamp: 2025-12-24T10:29:08.169957
finish_reason: stop
---

В примере 10-14 показано, как указать строку по умолчанию для метода `summarize` из типажа `Summary` вместо определения только сигнатуры метода, как мы сделали в примере 10-12.

Файл: src/lib.rs

```rust
pub trait Summary {
    fn summarize(&self) -> String {
        String::from("(Read more...)")
    }
}
```

Листинг 10-14: Определение типажа `Summary` с реализацией метода `summarize` по умолчанию

Для использования реализации по умолчанию при создании сводки у экземпляров `NewsArticle` вместо определения пользовательской реализации, мы указываем пустой блок `impl` с `impl Summary for NewsArticle {}`.

Хотя мы больше не определяем метод `summarize` непосредственно в `NewsArticle`, мы предоставили реализацию по умолчанию и указали, что `NewsArticle` реализует типаж `Summary`. В результате мы всё ещё можем вызвать метод `summarize` у экземпляра `NewsArticle`, например так:

```rust
let article = NewsArticle {
    headline: String::from("Penguins win the Stanley Cup Championship!"),
    location: String::from("Pittsburgh, PA, USA"),
    author: String::from("Iceburgh"),
    content: String::from(
        "The Pittsburgh Penguins once again are the best \
         hockey team in the NHL.",
    ),
};

println!("New article available! {}", article.summarize());
```

Этот код печатает `New article available! (Read more...)`.

Создание реализации по умолчанию не требует от нас изменений чего-либо в реализации `Summary` для `Tweet` в листинге 10-13. Причина заключается в том, что синтаксис для переопределения реализации по умолчанию является таким же, как синтаксис для реализации метода типажа, который не имеет реализации по умолчанию.

Реализации по умолчанию могут вызывать другие методы в том же типаже, даже если эти другие методы не имеют реализации по умолчанию. Таким образом, типаж может предоставить много полезной функциональности и только требует от разработчиков указывать небольшую его часть. Например, мы могли бы определить типаж `Summary` имеющий метод `summarize_author`, реализация которого требуется, а затем определить метод `summarize` который имеет реализацию по умолчанию, которая внутри вызывает метод `summarize_author`: