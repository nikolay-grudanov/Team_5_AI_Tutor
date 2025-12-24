---
source_image: page_320.png
page_number: 320
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.41
tokens: 11567
characters: 1283
timestamp: 2025-12-24T10:31:50.779219
finish_reason: stop
---

Листинг 12-7. Изменение имени с parse_config на Config::new

Мы обновили main где вызывали parse_config, чтобы вместо этого вызывалась Config::new. Мы изменили имя parse_config на new и перенесли его внутрь блока impl, который связывает функцию new с Config. Попробуйте снова скомпилировать код, чтобы убедиться, что он работает.

Исправление ошибок обработки

Теперь мы поработаем над исправлением обработки ошибок. Напомним, что попытки получить доступ к значениям в векторе args с индексом 1 или индексом 2 приведут к панике, если вектор содержит менее трёх элементов. Попробуйте запустить программу без каких-либо аргументов; это будет выглядеть так:

$ cargo run
Compiling minigrep v0.1.0 (file:///projects/minigrep)
Finished dev [unoptimized + debuginfo] target(s) in 0.0s
    Running `target/debug/minigrep`
thread 'main' panicked at 'index out of bounds: the len is 1 but the index is 1', src/main.rs:27:21
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

Строка index out of bounds: the len is 1 but the index is 1 является сообщением об ошибке предназначенной для программистов. Она не поможет нашим конечным пользователям понять, что случилось и что они должны сделать вместо этого. Давайте исправим это сейчас.

Улучшение сообщения об ошибке