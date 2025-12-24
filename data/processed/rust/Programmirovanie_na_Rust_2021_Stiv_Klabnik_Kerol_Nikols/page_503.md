---
source_image: page_503.png
page_number: 503
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.63
tokens: 7344
characters: 1603
timestamp: 2025-12-24T10:58:56.121342
finish_reason: stop
---

В реализации outline_print мы хотим использовать функциональность типажа Display. Следовательно, нужно указать, что OutlinePrint будет работать только для типов, которые также реализуют Display и обеспечивают функциональность, необходимую типажу OutlinePrint. Мы можем сделать это в определении типажа, указав OutlinePrint: Display. Этот технический прием подобен добавлению типажа, привязанного к этому типажу. В листинге 19.22 показана реализация OutlinePrint.

Листинг 19.22. Реализация типажа OutlinePrint, которая требует функциональности из типажа Display

src/main.rs
use std::fmt;

trait OutlinePrint: fmt::Display {
    fn outline_print(&self) {
        let output = self.to_string();
        let len = output.len();
        println!("{}", "*".repeat(len + 4));
        println!("*{}*", " ".repeat(len + 2));
        println!("* {} *", output);
        println!("*{}*", " ".repeat(len + 2));
        println!("{}", "*".repeat(len + 4));
    }
}

Поскольку мы указали, что OutlinePrint требует типаж Display, можно использовать функцию to_string, которая автоматически выполняется для любого типа, реализующего типаж Display. Если бы мы попытались использовать to_string без добавления двоеточия и указания Display после имени типажа, то получили бы сообщение об ошибке, что метод с именем to_string не найден для типа &Self в текущей области видимости.

Давайте посмотрим, что происходит, когда мы пытаемся реализовать OutlinePrint в типе, который не реализует типаж Display. Примером служит структура Point:

src/main.rs
struct Point {
    x: i32,
    y: i32,
}

impl OutlinePrint for Point {}