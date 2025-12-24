---
source_image: page_356.png
page_number: 356
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.77
tokens: 7362
characters: 1337
timestamp: 2025-12-24T10:54:58.808559
finish_reason: stop
---

Cargo.toml
    [workspace]
    members = [
        "adder",
        "add-one",
    ]

Затем сгенерируйте новую библиотечную упаковку с именем add-one:

    $ cargo new add-one --lib
        Created library `add-one` project

Теперь в каталоге add должны быть эти каталоги и файлы:

├── Cargo.lock
├── Cargo.toml
├── add-one
│   ├── Cargo.toml
│   └── src
│       └── lib.rs
├── adder
│   ├── Cargo.toml
│   └── src
│       └── main.rs
└── target

В файл add-one/src/lib.rs давайте добавим функцию add_one:

add-one/src/lib.rs
    pub fn add_one(x: i32) -> i32 {
        x + 1
    }

Теперь, когда в рабочем пространстве есть библиотечная упаковка, двоичная упаковка adder может зависеть от библиотечной упаковки add-one. Сначала нужно добавить в adder/Cargo.toml зависимость от пути add-one.

adder/Cargo.toml
    [dependencies]
    add-one = { path = "../add-one" }

Использование Cargo не подразумевает, что упаковки в рабочем пространстве будут зависеть друг от друга, поэтому нам нужно четко определить отношения зависимости между упаковками.

Далее давайте применим функцию add_one из упаковки add-one в упаковке adder. Откройте файл adder/src/main.rs и добавьте вверху строку use, чтобы ввести новую библиотечную упаковку add-one в область видимости. Затем измените функцию main, чтобы вызвать функцию add_one, как в листинге 14.7.