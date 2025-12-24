---
source_image: page_160.png
page_number: 160
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.30
tokens: 7408
characters: 1661
timestamp: 2025-12-24T10:49:50.639542
finish_reason: stop
---

не упаковки. Пути, введенные в область видимости с помощью use, проверяют конфиденциальность так же, как и любые другие пути.

Указание относительного пути с помощью use немного отличается. Вместо того, чтобы начинать с имени в текущей области видимости, мы должны начинать путь, переданный инструкции use, с ключевого слова self. В листинге 7.12 показано, как указать относительный путь для получения того же результата, что и в листинге 7.11.

Листинг 7.12. Введение модуля в область видимости с помощью use и относительный путь, начинающийся с self

src/lib.rs
```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use self::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
    hosting::add_to_waitlist();
    hosting::add_to_waitlist();
}
```

Обратите внимание, что такое использование self в будущем может не понадобиться. Оно представляет собой нестыковку в языке, над устранением которой работают разработчики Rust.

Создание идиоматических путей use

Глядя на листинг 7.11, можно задаться вопросом, почему мы указали use crate::front_of_house::hosting, а затем вызвали hosting::add_to_waitlist в функции eat_at_restaurant вместо указания пути use вплоть до функции add_to_waitlist для достижения того же результата, что и в листинге 7.13.

Листинг 7.13. Введение функции add_to_waitlist в область видимости с помощью use, которое не является идиоматическим

src/lib.rs
```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting::add_to_waitlist;

pub fn eat_at_restaurant() {
    add_to_waitlist();
}