---
source_image: page_357.png
page_number: 357
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.76
tokens: 7561
characters: 2015
timestamp: 2025-12-24T10:55:13.530996
finish_reason: stop
---

Листинг 14.7. Использование библиотечной упаковки add-one из упаковки adder

adder/src/main.rs

use add_one;

fn main() {
    let num = 10;
    println!("Здравствуй, Мир! {} плюс один равно {}!", num, add_one::add_one(num));
}

Давайте построим рабочее пространство, выполнив команду cargo build в верхнем-уровневом каталоге add!

$ cargo build
    Compiling add-one v0.1.0 (file:///projects/add/add-one)
    Compiling adder v0.1.0 (file:///projects/add/adder)
    Finished dev [unoptimized + debuginfo] target(s) in 0.68 secs

Для того чтобы выполнить двоичную упаковку из каталога add, нужно указать имя пакета из рабочего пространства, который мы хотим использовать, включив аргумент -p и имя пакета в команду cargo run:

$ cargo run -p adder
    Finished dev [unoptimized + debuginfo] target(s) in 0.0 secs
    Running `target/debug/adder`
Здравствуй, Мир! 10 плюс один равно 11!

Эта команда выполняет код в adder/src/main.rs, который зависит от упаковки add-one.

Зависимость от внешней упаковки в рабочем пространстве

Обратите внимание, вместо того чтобы иметь файл Cargo.lock в каталоге каждой упаковки, рабочее пространство имеет только один файл Cargo.lock на верхнем уровне рабочего пространства. Этим обеспечивается, чтобы все упаковки использовали одну и ту же версию всех зависимостей. Если мы добавим упаковку rand в файлы adder/Cargo.toml и add-one/Cargo.toml, то Cargo сведет их к одной версии rand и запишет в один файл Cargo.lock. Если все упаковки в рабочем пространстве используют одинаковые зависимости, то это означает, что упаковки в рабочем пространстве всегда будут совместимы друг с другом. Давайте добавим упаковку rand в раздел [dependencies] файла add-one/Cargo.toml, чтобы иметь возможность использовать упаковку rand в упаковке add-one:

add-one/Cargo.toml

[dependencies]

rand = "0.3.14"

Теперь мы можем добавить use rand; в файл add-one/src/lib.rs, и построение всего рабочего пространства путем выполнения команды cargo build в каталоге add введет и скомпилирует упаковку rand: