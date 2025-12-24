---
source_image: page_302.png
page_number: 302
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.35
tokens: 7550
characters: 2165
timestamp: 2025-12-24T10:53:45.069965
finish_reason: stop
---

Чтобы вернуть каждую строку из функции search и напечатать ее, мы по-прежнему используем цикл for.

Теперь вся программа должна работать! Давайте испытаем ее сначала со словом, которое должно вернуть ровно одну строчку из стихотворения Эмили Дикинсон — frog («лягушка»):

    $ cargo run frog poem.txt
        Compiling minigrep v0.1.0 (file:///projects/minigrep)
        Finished dev [unoptimized + debuginfo] target(s) in 0.38 secs
        Running `target/debug/minigrep frog poem.txt`
    How public, like a frog

Круто! Теперь давайте попробуем слово, которое совпадет с несколькими строками текста, к примеру, body («тело»):

    $ cargo run body poem.txt
        Finished dev [unoptimized + debuginfo] target(s) in 0.0 secs
        Running `target/debug/minigrep body poem.txt`
    I'm nobody! Who are you?
    Are you nobody, too?
    How dreary to be somebody!

И наконец, давайте убедимся, что мы не получаем никаких строк, когда ищем слово, которого нет в стихотворении, к примеру, monomorphization («мономорфизация»):

    $ cargo run monomorphization poem.txt
        Finished dev [unoptimized + debuginfo] target(s) in 0.0 secs
        Running `target/debug/minigrep monomorphization poem.txt`

Превосходно! Мы создали свою мини-версию классического инструмента и многое узнали о том, как структурировать приложения. Мы также немного узнали о файловом вводе и выводе, жизненных циклах, тестировании и разборе командной строки.

В завершение этого проекта мы кратко продемонстрируем, как работать с переменными среды и как печатать в стандартный вывод ошибок — и то и другое полезно при написании программ командной строки.

Работа с переменными среды

Мы улучшим программу minigrep, добавив дополнительное средство — возможность поиска без учета регистра, которую пользователь активирует через переменную среды. Мы могли бы сделать это средство аргументом командной строки и требовать от пользователей, чтобы они вводили его всякий раз, когда хотят применить, но вместо этого воспользуемся переменной среды. Это позволит пользователям устанавливать переменную среды один раз, что сделает поиск нечувствительным к регистру в конкретном сеансе терминала.