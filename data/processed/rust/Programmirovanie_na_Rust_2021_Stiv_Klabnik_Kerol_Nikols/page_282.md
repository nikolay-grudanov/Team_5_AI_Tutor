---
source_image: page_282.png
page_number: 282
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.30
tokens: 7426
characters: 1745
timestamp: 2025-12-24T10:53:10.615004
finish_reason: stop
---

Running `target/debug/minigrep test sample.txt`
Searching for test
In file sample.txt

Отлично, программа работает! Значения необходимых аргументов сохраняются в правильных переменных. Позже мы добавим небольшую обработку ошибок, чтобы учесть потенциальные ошибочные ситуации, например, когда пользователь не предоставляет никаких аргументов. Пока что мы проигнорируем эту ситуацию и поработаем над добавлением способности читать файлы.

Чтение файла

Теперь мы добавим функциональность чтения файла, указываемого в аргументе командной строки filename. Сначала нам нужен образец файла для тестирования. Для проверки работы программы minigrep самый лучший файл — это тот, в котором мало текста на нескольких строках с несколькими повторяющимися словами. В листинге 12.3 представлено стихотворение Эмили Дикinson (Emily Dickinson), которое нам подходит. Создайте файл под названием poem.txt на корневом уровне проекта и введите стихотворение I’m Nobody! Who are you? («Я — никто! А ты кто такой?»).

Листинг 12.3. Стихотворение Эмили Дикinson — хороший пример для теста poem.txt

I'm nobody! Who are you?
Are you nobody, too?
Then there's a pair of us – don't tell!
They'd banish us, you know.

How dreary to be somebody!
How public, like a frog
To tell your name the livelong day
To an admiring bog!

Когда текст будет готов, отредактируйте src/main.rs и добавьте код для чтения файла, как показано в листинге 12.4.

Листинг 12.4. Чтение содержимого файла, указанного вторым аргументом src/main.rs

use std::env;
use std::fs;

fn main() {
    // --пропуск--
    println!("В файле {}", filename);

    let contents = fs::read_to_string(filename)
        .expect("Что-то пошло не так при чтении файла");

    println!("С текстом:\n{}", contents);
}