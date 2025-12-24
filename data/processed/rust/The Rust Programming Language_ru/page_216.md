---
source_image: page_216.png
page_number: 216
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.10
tokens: 11634
characters: 1658
timestamp: 2025-12-24T10:27:36.158382
finish_reason: stop
---

используемое сообщение.
Вот как это выглядит:

thread 'main' panicked at 'hello.txt should be included in this project: Os { code: 2, kind: NotFound, message: "No such file or directory" }',
src/main.rs:5:10

В рабочем коде, большинство выбирает expect в угоду unwrap и добавляет описание, почему операция должна закончиться успешно. Но даже если предположение оказалось неверным, информации для отладки будет больше.

Проброс ошибок

Когда вы пишете функцию, реализация которой вызывает что-то, что может завершиться ошибкой, вместо обработки ошибки в этой функции, вы можете вернуть ошибку в вызывающий код, чтобы он мог решить, что с ней делать. Такой приём известен как распространение ошибки (propagating the error). Благодаря нему мы даём больше контроля вызывающему коду, где может быть больше информации или логики, которая диктует, как ошибка должна обрабатываться, чем было бы в месте появления этой ошибки.

Например, код программы 9-6 читает имя пользователя из файла. Если файл не существует или не может быть прочтён, то функция возвращает ошибку в код, который вызвал данную функцию.

Файл: src/main.rs

use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let username_file_result = File::open("hello.txt");

    let mut username_file = match username_file_result {
        Ok(file) => file,
        Err(e) => return Err(e),
    };

    let mut username = String::new();

    match username_file.read_to_string(&mut username) {
        Ok(_) => Ok(username),
        Err(e) => Err(e),
    }
}

Листинг 9-6: Функция, которая возвращает ошибки в вызывающий код, используя оператор match