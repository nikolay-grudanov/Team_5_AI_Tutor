---
source_image: page_313.png
page_number: 313
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.26
tokens: 11632
characters: 1554
timestamp: 2025-12-24T10:31:32.789075
finish_reason: stop
---

Чтение файла

Теперь добавим возможность чтения файла, указанного как аргумент командной строки filename. Во-первых, нам нужен пример файла для тестирования: лучший тип файла для проверки работы minigrep это файл с небольшим количеством текста в несколько строк с несколькими повторяющимися словами. В листинге 12-3 представлено стихотворение Эмили Дикинсон, которое будет хорошо работать! Создайте файл с именем poem.txt в корне вашего проекта и введите стихотворение "I’m nobody! Who are you?"

Файл: poem.txt

I'm nobody! Who are you?
Are you nobody, too?
Then there's a pair of us – don't tell!
They'd banish us, you know.

How dreary to be somebody!
How public, like a frog
To tell your name the livelong day
To an admiring bog!

Листинг 12-3: Стихотворение Эмили Дикинсон "I’m nobody! Who are you?"

Текст на месте, отредактируйте src/main.rs и добавьте код для чтения файла, как показано в листинге 12-4.

Файл: src/main.rs

use std::env;
use std::fs;

fn main() {
    // --snip--
    println!("In file {}", file_path);

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    println!("With text:\n{contents}");
}

Листинг 12-4: Чтение содержимого файла указанного во втором аргументе

Во-первых, мы добавляем ещё одно объявление use чтобы подключить соответствующую часть стандартной библиотеки: нам нужен std::fs для обработки файлов.

В main мы добавили новый оператор: функция fs::read_to_string принимает filename, открывает этот файл и возвращает содержимое файла как Result<String>.