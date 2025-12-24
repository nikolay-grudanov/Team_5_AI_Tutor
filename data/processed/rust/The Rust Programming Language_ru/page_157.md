---
source_image: page_157.png
page_number: 157
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 48.53
tokens: 11654
characters: 1557
timestamp: 2025-12-24T10:25:15.118578
finish_reason: stop
---

• **Скрытие или общедоступность**: Код в модуле по умолчанию скрыт от родительского модуля. Чтобы сделать модуль общедоступным, объявите его как `pub mod` вместо `mod`. Чтобы сделать элементы общедоступного модуля тоже общедоступными, используйте `pub` перед их объявлением.
• **Ключевое слово use**: Внутри области видимости использование ключевого слова `use` создаёт псевдонимы для элементов, чтобы уменьшить повторение длинных путей. В любой области видимости, в которой может обращаться к `crate::garden::vegetables::Asparagus`, вы можете создать псевдоним `use crate::garden::vegetables::Asparagus;` и после этого вам нужно просто писать `Asparagus`, чтобы использовать этот тип в этой области видимости.

Мы создали бинарный крейт `backyard`, который иллюстрирует эти правила. Директория крейта, также названная как `backyard`, содержит следующие файлы и директории:

backyard
├── Cargo.lock
├── Cargo.toml
└── src
    ├── garden
    │   └── vegetables.rs
    ├── garden.rs
    └── main.rs

Файл корневого модуля крейта в нашем случае `src/main.rs`, и его содержимое:

Файл: src/main.rs

```rust
use crate::garden::vegetables::Asparagus;

pub mod garden;

fn main() {
    let plant = Asparagus {};
    println!("I'm growing {:?}!", plant);
}
```

Строка `pub mod garden;` говорит компилятору о подключении кода, найденном в `src/garden.rs`:

Файл: src/garden.rs

```rust
pub mod vegetables;
```

А здесь `pub mod vegetables;` указывает на подключаемый код в `src/garden/vegetables.rs`.

Этот код:

```rust
#[derive(Debug)]
pub struct Asparagus {}
```