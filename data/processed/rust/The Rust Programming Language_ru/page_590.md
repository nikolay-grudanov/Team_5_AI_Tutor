---
source_image: page_590.png
page_number: 590
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 54.48
tokens: 11804
characters: 2167
timestamp: 2025-12-24T10:43:19.819599
finish_reason: stop
---

use std::{
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
};

fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();

        handle_connection(stream);
    }
}

fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&mut stream);
    let http_request: Vec<_> = buf_reader
        .lines()
        .map(|result| result.unwrap())
        .take_while(|line| !line.is_empty())
        .collect();

    println!("Request: {:#?}", http_request);
}

Листинг 20-2: Чтение из потока TcpStream и печать данных

Мы добавляем std::io::prelude в область видимости, чтобы получить доступ к определённым свойствам, которые позволяют нам читать и писать в поток. В цикле for функции main вместо вывода сообщения о том, что мы установили соединение, мы теперь вызываем новую функцию handle_connection и передаём ей stream.

В функции handle_connection мы сделали параметр stream изменяемым. Причина в том, что экземпляр TcpStream отслеживает, какие данные он нам возвращает. Он может прочитать больше данных, чем мы запрашивали, и сохранить их для следующего раза, когда мы запросим данные. Следовательно, он должен быть mut поскольку его внутреннее состояние может измениться; Обычно мы думаем, что «чтение» не требует мутации, но в этом случае нам нужно ключевое слово mut.

Далее нам нужно фактически прочитать данные из потока. Мы делаем это в два этапа: во-первых, мы объявляем buffer в стеке для хранения считываемых данных. Мы сделали буфер размером 1024 байта, что достаточно для хранения данных базового запроса и достаточно для наших целей в этой главе. Если бы мы хотели обрабатывать запросы произвольного размера, управление буфером должно было бы быть более сложным; пока делаем проще. Мы передаём буфер в stream.read, который считывает байты из TcpStream и помещает их в буфер.

Во-вторых, мы конвертируем байты из буфера в строку и печатаем эту строку. Функция String::from_utf8_lossy принимает &[u8] и создаёт из неё String. Названия «lossy» (с потерями) в её имени указывает на поведение этой функции. Когда она видит