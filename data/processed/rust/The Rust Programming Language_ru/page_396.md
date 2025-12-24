---
source_image: page_396.png
page_number: 396
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.43
tokens: 11651
characters: 1531
timestamp: 2025-12-24T10:35:03.256359
finish_reason: stop
---

$ cargo build
Compiling add_one v0.1.0 (file:///projects/add/add_one)
Compiling adder v0.1.0 (file:///projects/add/adder)
Finished dev [unoptimized + debuginfo] target(s) in 0.68s

Чтобы запустить бинарный крейт из каталога add, нам нужно указать какой пакет из рабочей области мы хотим использовать с помощью аргумента -p и названия пакета в команде cargo run:

$ cargo run -p adder
Finished dev [unoptimized + debuginfo] target(s) in 0.0s
    Running `target/debug/adder`
Hello, world! 10 plus one is 11!

Запуск кода из adder/src/main.rs, который зависит от add_one.

Зависимость от внешних крейтов в рабочем пространстве

Обратите внимание, что рабочая область имеет один единственный файл Cargo.lock на верхнем уровне, а не содержит Cargo.lock в каталоге каждого крейта. Это гарантирует, что все крейты используют одну и ту же версию всех зависимостей. Если мы добавим пакет rand в файлы adder/Cargo.toml и add_one/Cargo.toml, Cargo сведёт их оба к одной версии rand и запишет её в один Cargo.lock. Если заставить все крейты в рабочей области использовать одни и те же зависимости, то это будет означать, что крейты всегда будут совместимы друг с другом. Давайте добавим крейт rand в раздел [dependencies] в файле add_one/Cargo.toml, чтобы мы могли использовать крейт rand в крейте add_one:

Файл: add_one/Cargo.toml

[dependencies]
rand = "0.8.3"

Теперь мы можем добавить use rand; в файл add_one/src/lib.rs и сделать сборку рабочего пространства, запустив cargo build в каталоге add, что загрузит и скомпилирует rand крейт: