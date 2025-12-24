---
source_image: page_326.png
page_number: 326
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.44
tokens: 11397
characters: 758
timestamp: 2025-12-24T10:31:50.450349
finish_reason: stop
---

Rust говорит, что наш код проигнорировал Result значение и значение Result может указывать на то, что произошла ошибка. Но мы не проверяем, была ли ошибка и компилятор напоминает нам, что мы, вероятно, хотели здесь выполнить некоторый код обработки ошибок! Давайте исправим эту проблему сейчас.

Обработка ошибок, возвращённых из run в main

Мы будем проверять и обрабатывать ошибки используя методику, аналогичную той, которую мы использовали для Config::new в листинге 12-10, но с небольшой разницей:

Файл: src/main.rs

fn main() {
    // --snip--

    println!("Searching for {}", config.query);
    println!("In file {}", config.file_path);

    if let Err(e) = run(config) {
        println!("Application error: {e}");
        process::exit(1);
    }
}