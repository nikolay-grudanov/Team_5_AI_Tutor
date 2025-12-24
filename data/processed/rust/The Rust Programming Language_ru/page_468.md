---
source_image: page_468.png
page_number: 468
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.42
tokens: 11611
characters: 1500
timestamp: 2025-12-24T10:37:55.443705
finish_reason: stop
---

Ранее мы упоминали, что mpsc — это аббревиатура от множественного производителя, одного потребителя. Давайте используем mpsc в полной мере и расширим код в листинге 16.10, создав несколько потоков, которые отправляют значения одному и тому же получателю. Мы можем сделать это, клонировав передатчик, как показано в листинге 16.11:

Файл: src/main.rs

```rust
// --snip--

let (tx, rx) = mpsc::channel();

let tx1 = tx.clone();
thread::spawn(move || {
    let vals = vec![
        String::from("hi"),
        String::from("from"),
        String::from("the"),
        String::from("thread"),
    ];

    for val in vals {
        tx1.send(val).unwrap();
        thread::sleep(Duration::from_secs(1));
    }
});

thread::spawn(move || {
    let vals = vec![
        String::from("more"),
        String::from("messages"),
        String::from("for"),
        String::from("you"),
    ];

    for val in vals {
        tx.send(val).unwrap();
        thread::sleep(Duration::from_secs(1));
    }
});

for received in rx {
    println!("Got: {}", received);
}

// --snip--
```

Листинг 16-11: Отправка нескольких сообщений от нескольких производителей

На этот раз, прежде чем мы создадим первый порождённый поток, мы вызовем функцию clone на передатчике. В результате мы получим новый передатчик, который мы сможем передать первому порождённому потоку. Исходный передатчик мы передадим второму порождённому потоку. Это даст нам два потока, каждый из которых отправляет разные сообщения одному получателю.