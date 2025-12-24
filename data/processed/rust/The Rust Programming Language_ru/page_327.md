---
source_image: page_327.png
page_number: 327
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.47
tokens: 11664
characters: 1663
timestamp: 2025-12-24T10:32:17.945273
finish_reason: stop
---

Мы используем if let вместо unwrap_or_else чтобы проверить, возвращает ли run значение Err и вызывается process::exit(1), если это так. Функция run не возвращает значение, которое мы хотим развернуть методом unwrap, таким же образом как Config::new возвращает экземпляр Config. Так как run возвращает () в случае успеха и мы заботимся только об обнаружении ошибки, то нам не нужно вызывать unwrap_or_else, чтобы вернуть развёрнутое значение, потому что оно будет только ().

Тело функций if let и unwrap_or_else одинаковы в обоих случаях: мы печатаем ошибку и выводим.

Разделение кода на библиотечный крейт

Наш проект minigrep пока выглядит хорошо! Теперь мы разделим файл src/main.rs и поместим некоторый код в файл src/lib.rs, чтобы мы могли его тестировать и чтобы в файле src/main.rs было меньше количество функциональных обязанностей.

Давайте перенесём весь код не относящийся к функции main из файла src/main.rs в новый файл src/lib.rs:

• Определение функции run.
• Соответствующие инструкции use.
• Определение структуры Config.
• Определение функции Config::new.

Содержимое src/lib.rs должно иметь сигнатуры, показанные в листинге 12-13 (мы опустили тела функций для краткости). Обратите внимание, что код не будет компилироваться пока мы не изменим src/main.rs в листинге 12-14.

Файл: src/lib.rs

use std::error::Error;
use std::fs;

pub struct Config {
    pub query: String,
    pub file_path: String,
}

impl Config {
    pub fn build(args: &[String]) -> Result<Config, &'static str> {
        // --snip--
    }
}

pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    // --snip--
}

Листинг 12-13. Перемещение Config и run в src/lib.rs