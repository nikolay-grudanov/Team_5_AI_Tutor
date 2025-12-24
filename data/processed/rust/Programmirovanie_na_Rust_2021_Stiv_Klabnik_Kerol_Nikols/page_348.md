---
source_image: page_348.png
page_number: 348
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.16
tokens: 7313
characters: 1237
timestamp: 2025-12-24T10:54:48.222660
finish_reason: stop
---

```rust
Purple,
    }
}
pub mod utils {
    use crate::kinds::*;

    /// Комбинирует два первичных цвета в одинаковых объемах для создания вторичного цвета.
    pub fn mix(c1: PrimaryColor, c2: PrimaryColor) -> SecondaryColor {
        // --пропуск--
    }
}

На рис. 14.3 приведена первая страница документации, сгенерированная командой cargo doc, по этой упаковке

![Первая страница документации по упаковке art, на которой перечислены модули kinds и utils](../images/ch14_03.png)

Рис. 14.3. Первая страница документации по упаковке art, на которой перечислены модули kinds и utils

Обратите внимание, что типы PrimaryColor и SecondaryColor не перечислены на первой странице, как и функция mix, и чтобы их увидеть, мы должны нажать kinds и utils.

Еще одной упаковке, зависящей от этой библиотеки, потребовались бы инструкции use, вводящие в область видимости элементы из art, уточняющие структуру модуля, которая в настоящее время определена. В листинге 14.4 показан пример упаковки, в которой используются элементы PrimaryColor и mix из упаковки art.

Листинг 14.4. Упаковка, использующая элементы упаковки art с экспортированной внутренней структурой
src/main.rs
use art::kinds::PrimaryColor;
use art::utils::mix;

fn main() {
```