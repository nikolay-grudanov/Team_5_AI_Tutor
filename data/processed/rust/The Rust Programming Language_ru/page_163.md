---
source_image: page_163.png
page_number: 163
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.86
tokens: 11509
characters: 1027
timestamp: 2025-12-24T10:25:09.221590
finish_reason: stop
---

Rust даёт нам возможность открывать внутренние части кода дочерних модулей для внешних модулей-предков, используя ключевое слово `pub`, чтобы сделать элемент общедоступным.

Раскрываем приватные пути с помощью ключевого слова `pub`

Давайте вернёмся к ошибке в листинге 7-4, которая говорит, что модуль `hosting` является приватным. Мы хотим, чтобы функция `eat_at_restaurant` из родительского модуля имела доступ к функции `add_to_waitlist` в дочернем модуле, поэтому мы помечаем модуль `hosting` ключевым словом `pub`, как показано в листинге 7-5.

Файл: src/lib.rs

```rust
mod front_of_house {
    pub mod hosting {
        fn add_to_waitlist() {}
    }
}

pub fn eat_at_restaurant() {
    // Absolute path
    crate::front_of_house::hosting::add_to_waitlist();

    // Relative path
    front_of_house::hosting::add_to_waitlist();
}
```

Листинг 7-5. Объявление модуля `hosting` как `pub` для его использования из `eat_at_restaurant`

К сожалению, код в листинге 7-5 всё ещё приводит к ошибке, как показано в листинге 7-6.