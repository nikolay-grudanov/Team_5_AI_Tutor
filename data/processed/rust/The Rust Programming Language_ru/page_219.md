---
source_image: page_219.png
page_number: 219
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 46.51
tokens: 11701
characters: 1725
timestamp: 2025-12-24T10:27:47.851564
finish_reason: stop
---

В случае листинга 9-7 оператор ? в конце вызова File::open вернёт значение внутри Ok в переменную username_file. Если произойдёт ошибка, оператор ? выполнит ранний возврат значения Err вызывающему коду. То же самое относится к оператору ? в конце вызова read_to_string.

Оператор ? позволяет избавиться от большого количества шаблонного кода и упростить реализацию этой функции. Мы могли бы даже ещё больше сократить этот код, если бы использовали цепочку вызовов методов сразу после ?, как показано в листинге 9-8.

Файл: src/main.rs

use std::fs::File;
use std::io;
use std::io::Read;

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username = String::new();

    File::open("hello.txt")?.read_to_string(&mut username)?;

    Ok(username)
}

Листинг 9-8: Цепочка вызовов методов после оператора ?

Мы перенесли создание новой String в username в начало функции; эта часть не изменилась. Вместо создания переменной username_file мы соединили вызов read_to_string непосредственно с результатом File::open("hello.txt")?. У нас по-прежнему есть ? в конце вызова read_to_string, и мы по-прежнему возвращаем значение Ok, содержащее username, когда и File::open и read_to_string завершаются успешно, а не возвращают ошибки. Функциональность снова такая же, как в Листинге 9-6 и Листинге 9-7; это просто другой, более эргономичный способ её написания.

Продолжая рассматривать разные способы записи данной функции, листинг 9-9 демонстрирует способ сделать её ещё короче.

Файл: src/main.rs

use std::fs;
use std::io;

fn read_username_from_file() -> Result<String, io::Error> {
    fs::read_to_string("hello.txt")
}

Листинг 9-9: Использование fs::read_to_string вместо открытия и последующего чтения файла