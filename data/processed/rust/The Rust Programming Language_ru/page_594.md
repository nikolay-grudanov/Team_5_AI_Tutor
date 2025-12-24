---
source_image: page_594.png
page_number: 594
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.25
tokens: 11764
characters: 2006
timestamp: 2025-12-24T10:43:25.680295
finish_reason: stop
---

Это минимальный документ HTML5 с заголовком и некоторым текстом. Чтобы вернуть это с сервера при получении запроса, мы handle_connection как показано в листинге 20-5, чтобы прочитать файл HTML, добавить его в ответ в виде тела и отправить.

Файл: src/main.rs

```rust
use std::{
    fs,
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
};
// --snip--

fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&mut stream);
    let http_request: Vec<_> = buf_reader
        .lines()
        .map(|result| result.unwrap())
        .take_while(|line| !line.is_empty())
        .collect();

    let status_line = "HTTP/1.1 200 OK";
    let contents = fs::read_to_string("hello.html").unwrap();
    let length = contents.len();

    let response =
        format!("{status_line}\r\nContent-Length: {length}\r\n\r\n{contents}");

    stream.write_all(response.as_bytes()).unwrap();
}
```

Листинг 20-5. Отправка содержимого hello.html в качестве тела ответа

Мы добавили строку вверху, чтобы включить в область видимости модуль файловой системы стандартной библиотеки. Код для чтения содержимого файла в строку должен выглядеть знакомо; мы использовали его в главе 12, когда читали содержимое файла для нашего проекта ввода-вывода в листинге 12-4.

Далее мы используем format! чтобы добавить содержимое файла в качестве тела ответа об успешном завершении. Чтобы гарантировать действительный HTTP-ответ, мы добавляем заголовок Content-Length который имеет размер тела нашего ответа, в данном случае размер hello.html.

Запустите этот код командой cargo run и загрузите 127.0.0.1:7878 в браузере; вы должны увидеть выведенный HTML в браузере!

В настоящее время мы игнорируем данные запроса в buffer и просто безоговорочно отправляем обратно содержимое HTML-файла. Это означает, что если вы попытаетесь запросить 127.0.0.1:7878/something-else в своём браузере, вы все равно получите тот же ответ HTML. Наш сервер очень ограничен, и это не то, что делает большинство веб-