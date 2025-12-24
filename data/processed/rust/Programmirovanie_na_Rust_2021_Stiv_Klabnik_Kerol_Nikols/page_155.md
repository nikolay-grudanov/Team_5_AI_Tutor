---
source_image: page_155.png
page_number: 155
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.01
tokens: 7503
characters: 1849
timestamp: 2025-12-24T10:49:43.694560
finish_reason: stop
---

К сожалению, код в листинге 7.5 по-прежнему приводит к ошибке, как показано в листинге 7.6¹.

Листинг 7.6. Ошибки компилятора при построении кода в листинге 7.5

$ cargo build
    Compiling restaurant v0.1.0 (file:///projects/restaurant)
error[E0603]: function `add_to_waitlist` is private
  --> src/lib.rs:9:37
   |
9 |     crate::front_of_house::hosting::add_to_waitlist();
   |                                 ^^^^^^^^^^^^^^^^^^^^
error[E0603]: function `add_to_waitlist` is private
  --> src/lib.rs:12:30
   |
12 |     front_of_house::hosting::add_to_waitlist();
   |                                 ^^^^^^^^^^^^^^^

Что случилось? Добавление ключевого слова pub перед mod hosting делает модуль публичным. С этим изменением, в случае если мы можем обратиться к front_of_house, можно обратиться к модулю hosting. Но содержимое модуля hosting по-прежнему является конфиденциальным; делая модуль публичным, вы не делаете публичным его содержимое. Ключевое слово pub в модуле позволяет коду ссылаться на него только в его предковых модулях.

Ошибки в листинге 7.6 говорят о том, что функция add_to_waitlist является конфиденциальной. Правила конфиденциальности применяются к структурам, перечислениям, функциям и методам, а также модулям.

Давайте также сделаем функцию add_to_waitlist публичной, добавив ключевое слово pub перед ее определением, как в листинге 7.7.

Листинг 7.7. Добавление ключевого слова pub в mod hosting и fn add_to_waitlist позволяет вызывать функцию из eat_at_restaurant

src/lib.rs

mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

pub fn eat_at_restaurant() {
    // Абсолютный путь
    crate::front_of_house::hosting::add_to_waitlist();

    // Относительный путь
    front_of_house::hosting::add_to_waitlist();
}

¹ ошибка[E0603]: функция `add_to_waitlist` является конфиденциальной