---
source_image: page_341.png
page_number: 341
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.56
tokens: 11504
characters: 1177
timestamp: 2025-12-24T10:32:44.192978
finish_reason: stop
---

Листинг 12-22. Вызов либо search, либо search_case_insensitive на основе значения в config.case_sensitive

Наконец, нам нужно проверить переменную среды. Функции для работы с переменными среды находятся в модуле env стандартной библиотеки, поэтому мы хотим подключить этот модуль в область видимости с помощью строки use std::env; в верхней части src/lib.rs. Затем мы будем использовать функцию var из модуля env для проверки переменной среды с именем CASE_INSENSITIVE, как показано в листинге 12-23.

Файл: src/lib.rs

use std::env;
// --snip--

impl Config {
    pub fn build(args: &[String]) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("not enough arguments");
        }

        let query = args[1].clone();
        let file_path = args[2].clone();

        let ignore_case = env::var("IGNORE_CASE").is_ok();

        Ok(Config {
            query,
            file_path,
            ignore_case,
        })
    }
}

Листинг 12-23. Проверка переменной среды с именем CASE_INSENSITIVE

Здесь мы создаём новую переменную case_sensitive. Чтобы установить её значение, мы вызываем функцию env::var и передаём ей имя переменной окружения