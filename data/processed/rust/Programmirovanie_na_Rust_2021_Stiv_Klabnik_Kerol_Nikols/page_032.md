---
source_image: page_032.png
page_number: 32
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.88
tokens: 7342
characters: 1510
timestamp: 2025-12-24T10:46:30.727373
finish_reason: stop
---

Откройте терминал и введите следующие команды, чтобы создать каталог projects и каталог для проекта Hello, world! в каталоге проектов.

Для Linux, macOS и оболочки PowerShell в Windows введите следующее:

    $ mkdir ~/projects
    $ cd ~/projects
    $ mkdir hello_world
    $ cd hello_world

Для интерпретатора командной строки cmd в Windows введите:

    > mkdir "%USERPROFILE%\projects"
    > cd /d "%USERPROFILE%\projects"
    > mkdir hello_world
    > cd hello_world

Написание и выполнение программы Rust

Далее создайте новый исходный файл и назовите его main.rs. Файлы Rust всегда заканчиваются расширением .rs. Если в имени файла вы используете более одного слова, то используйте нижнее подчеркивание, чтобы их отделить. Например, используйте hello_world.rs вместо helloworld.rs.

Теперь откройте файл main.rs, который вы только что создали, и введите код листинга 1.1.

Листинг 1.1. Программа, которая выводит Hello, World!

main.rs

    fn main() {
        println!("Hello, World!");
    }

Сохраните файл и вернитесь в окно вашего терминала. В Linux или macOS введите следующие команды для компиляции и выполнения файла:

    $ rustc main.rs
    $ ./main
    Hello, World!

В Windows вместо команды ./main введите команду .\main.exe:

    > rustc main.rs
    > .\main.exe
    Hello, World!

Независимо от вашей операционной системы в терминале должен быть выведен строковый литерал Hello, World!. Если вы не видите этих данных, то обратитесь к разделу «Устранение неполадок» для получения справки.