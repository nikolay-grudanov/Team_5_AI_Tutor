---
source_image: page_166.png
page_number: 166
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.70
tokens: 7459
characters: 1844
timestamp: 2025-12-24T10:50:05.027999
finish_reason: stop
---

Давайте начнем с кода в листинге 7.17 и переместим модуль front_of_house в его собственный файл src/front_of_house.rs, изменив файл корня упаковки таким образом, чтобы он содержал код, показанный в листинге 7.21. В этом случае файлом корня упаковки является src/lib.rs, но эта процедура также работает с двоичными упаковками, чьим файлом корня упаковки является src/main.rs.

Листинг 7.21. Объявление модуля front_of_house, тело которого будет находиться в src/front_of_house.rs

src/lib.rs
```rust
mod front_of_house;

pub use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
    hosting::add_to_waitlist();
    hosting::add_to_waitlist();
}
```

И src/front_of_house.rs получает определения из тела модуля front_of_house, как показано в листинге 7.22.

Листинг 7.22. Определения внутри модуля front_of_house в src/front_of_house.rs

src/front_of_house.rs
```rust
pub mod hosting {
    pub fn add_to_waitlist() {}
}
```

Использование точки с запятой после mod front_of_house вместо блока сообщает языку Rust о том, что нужно загрузить содержимое модуля из другого файла с тем же именем, что и модуль. В продолжение нашего примера, чтобы извлечь модуль hosting в его собственный файл, мы изменим src/front_of_house.rs так, чтобы он содержал только объявление модуля hosting:

src/front_of_house.rs
```rust
pub mod hosting;
```

Затем мы создаем каталог src/front_of_house и файл src/front_of_house/hosting.rs, содержащий определения, сделанные в модуле hosting:

src/front_of_house/hosting.rs
```rust
pub fn add_to_waitlist() {}
```

Дерево модулей остается тем же самым, а вызовы функций в eat_at_restaurant будут работать без каких-либо изменений, даже если определения располагаются в разных файлах. Этот технический прием позволяет перемещать модули в новые файлы по мере увеличения их размера.