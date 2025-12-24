---
source_image: page_213.png
page_number: 213
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 53.36
tokens: 11742
characters: 2072
timestamp: 2025-12-24T10:27:36.721433
finish_reason: stop
---

$ cargo run
Compiling error-handling v0.1.0 (file:///projects/error-handling)
Finished dev [unoptimized + debuginfo] target(s) in 0.73s
    Running `target/debug/error-handling`
thread 'main' panicked at 'Problem opening the file: Os { code: 2, kind: NotFound, message: "No such file or directory" }', src/main.rs:8:23
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

Как обычно, данное сообщение точно говорит, что пошло не так.

Обработка различных ошибок с помощью match

Код в листинге 9-4 будет вызывать panic! независимо от того, почему вызов File::open не удался. Однако мы хотим предпринять различные действия для разных причин сбоя. Если открытие File::open не удалось из-за отсутствия файла, мы хотим создать файл и вернуть его дескриптор. Если вызов File::open не удался по любой другой причине - например, потому что у нас не было прав на открытие файла, то все равно мы хотим вызвать panic! как у нас сделано в листинге 9-4. Для этого мы добавляем выражение внутреннего match, показанное в листинге 9-5.

Файл: src/main.rs

use std::fs::File;
use std::io::ErrorKind;

fn main() {
    let greeting_file_result = File::open("hello.txt");

    let greeting_file = match greeting_file_result {
        Ok(file) => file,
        Err(error) => match error.kind() {
            ErrorKind::NotFound => match File::create("hello.txt") {
                Ok(fc) => fc,
                Err(e) => panic!("Problem creating the file: {:?}", e),
            },
            other_error => {
                panic!("Problem opening the file: {:?}", other_error);
            }
        },
    };
}

Листинг 9-5: Обработка различных ошибок разными способами

Типом значения возвращаемого функцией File::open внутри Err варианта является io::Error, структура из стандартной библиотеки. Данная структура имеет метод kind, который можно вызвать для получения значения io::ErrorKind. Перечисление io::ErrorKind из стандартной библиотеки имеет варианты, представляющие различные типы ошибок, которые могут появиться при выполнении операций в io. Вариант,