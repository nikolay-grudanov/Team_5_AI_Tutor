---
source_image: page_467.png
page_number: 467
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.06
tokens: 11584
characters: 1435
timestamp: 2025-12-24T10:37:54.898784
finish_reason: stop
---

use std::sync::mpsc;
use std::thread;
use std::time::Duration;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let vals = vec![
            String::from("hi"),
            String::from("from"),
            String::from("the"),
            String::from("thread"),
        ];

        for val in vals {
            tx.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
    });

    for received in rx {
        println!("Got: {}", received);
    }
}

Листинг 16-10: Отправка нескольких сообщений и пауза между ними

На этот раз порождённый поток имеет вектор строк, которые мы хотим отправить основному потоку. Мы перебираем их, отправляя каждую строку по отдельности и делаем паузу между ними, вызывая функцию thread::sleep со значением Duration равным 1 секунде.

В основном потоке мы больше не вызываем функцию recv явно: вместо этого мы используем rx как итератор. Для каждого полученного значения мы печатаем его. Когда канал будет закрыт, итерация закончится.

При выполнении кода в листинге 16-10 вы должны увидеть следующий вывод с паузой в 1 секунду между каждой строкой:

Got: hi
Got: from
Got: the
Got: thread

Поскольку у нас нет кода, который приостанавливает или задерживает цикл for в основном потоке, мы можем сказать, что основной поток ожидает получения значений из порождённого потока.

Создание нескольких отправителей путём клонирования передатчика