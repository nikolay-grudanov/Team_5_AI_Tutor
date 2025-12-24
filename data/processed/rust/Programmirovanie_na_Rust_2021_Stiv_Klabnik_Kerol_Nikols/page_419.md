---
source_image: page_419.png
page_number: 419
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.13
tokens: 7290
characters: 1345
timestamp: 2025-12-24T10:56:36.619915
finish_reason: stop
---

Листинг 16.11. Отправка нескольких сообщений от нескольких производителей
src/main.rs

// --пропуск--

let (tx, rx) = mpsc::channel();

let tx1 = mpsc::Sender::clone(&tx);
thread::spawn(move || {
    let vals = vec![
        String::from("привет"),
        String::from("из"),
        String::from("потока"),
        String::from("исполнения"),
    ];

    for val in vals {
        tx1.send(val).unwrap();
        thread::sleep(Duration::from_secs(1));
    }
});

thread::spawn(move || {
    let vals = vec![
        String::from("еще"),
        String::from("сообщения"),
        String::from("для"),
        String::from("вас"),
    ];

    for val in vals {
        tx.send(val).unwrap();
        thread::sleep(Duration::from_secs(1));
    }
});

for received in rx {
    println!("Получено: {}", received);
}

// --пропуск--

На этот раз, прежде чем мы создадим первый порожденный поток, мы вызываем clone на отправляющем конце канала. Это дает новый отправляющий дескриптор, который мы можем передать первому порожденному потоку исполнения. Мы передаем исходный отправляющий конец канала второму порожденному потоку исполнения. Это дает нам два потока, каждый из которых отправляет разные сообщения в принимающий конец канала.

Когда вы выполните этот код, данные должны выглядеть примерно так:

Получено: привет
Получено: еще
Получено: от