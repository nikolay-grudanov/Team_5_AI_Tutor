---
source_image: page_358.png
page_number: 358
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.81
tokens: 7531
characters: 1969
timestamp: 2025-12-24T10:55:11.017081
finish_reason: stop
---

$ cargo build
    Updating registry `https://github.com/rust-lang/crates.io-index`
    Downloading rand v0.3.14
    -- пропуск --
    Compiling rand v0.3.14
    Compiling add-one v0.1.0 (file:///projects/add/add-one)
    Compiling adder v0.1.0 (file:///projects/add/adder)
    Finished dev [unoptimized + debuginfo] target(s) in 10.18 secs

Верхнеуровневый файл Cargo.lock теперь содержит информацию о зависимости add-one от rand. Однако, даже если упаковка rand используется где-то в рабочем пространстве, мы не можем применять ее в других упаковках рабочего пространства, если не добавим rand и в их файлы Cargo.toml тоже. Например, если мы разместим use rand; в файле adder/src/main.rs для упаковки adder, то получим ошибку¹:

$ cargo build
    Compiling adder v0.1.0 (file:///projects/add/adder)
error: use of unstable library feature 'rand': use `rand` from crates.io (see issue #27703)
    --> adder/src/main.rs:1:1
     |
1  | use rand;

Для ее устранения отредактируйте файл Cargo.toml для упаковки adder и укажите, что rand является зависимостью и для этой упаковки тоже. Построение упаковки adder добавит rand в список зависимостей для adder в файле Cargo.lock, но никакие дополнительные копии rand не будут скачиваться. Cargo обеспечил, чтобы каждая упаковка в рабочем пространстве, использующая упаковку rand, применяла одну и ту же версию. Использование одной и той же версии rand в рабочем пространстве экономит место, поскольку у нас не будет нескольких копий, и обеспечивает, чтобы упаковки в рабочем пространстве были совместимы друг с другом.

Добавление теста в рабочее пространство

В качестве еще одного улучшения давайте добавим тест функции add_one::add_one внутрь упаковки add_one:

add-one/src/lib.rs
pub fn add_one(x: i32) -> i32 {
    x + 1
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
_____________________
¹ ошибка: использование нестабильного библиотечного средства 'rand': используйте 'rand' из crates.io (см. вопрос #27703)