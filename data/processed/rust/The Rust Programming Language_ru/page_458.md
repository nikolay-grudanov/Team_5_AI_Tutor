---
source_image: page_458.png
page_number: 458
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 56.25
tokens: 11729
characters: 1853
timestamp: 2025-12-24T10:37:47.450554
finish_reason: stop
---

hi number 1 from the spawned thread!
hi number 2 from the spawned thread!
hi number 3 from the spawned thread!
hi number 4 from the spawned thread!
hi number 5 from the spawned thread!
hi number 6 from the spawned thread!
hi number 7 from the spawned thread!
hi number 8 from the spawned thread!
hi number 9 from the spawned thread!
hi number 1 from the main thread!
hi number 2 from the main thread!
hi number 3 from the main thread!
hi number 4 from the main thread!

Небольшие детали, такие как место вызова join, могут повлиять на то, выполняются ли ваши потоки одновременно.

Использование move-замыканий в потоках

Мы будем часто использовать ключевое слово move с замыканиями, переданными в thread::spawn, потому что замыкание будет затем владеть значениями, взятыми из окружающего кода, а значит передаст владение этими значениями от одного потока к другому. В разделе «Захват окружения замыканиями» главы 13 мы обсуждали move (перемещение) в контексте замыканий. Теперь мы больше сосредоточимся на взаимодействии между move и thread::spawn.

Обратите внимание, что в листинге 16-1 замыкание, которое мы передаём в thread::spawn не принимает аргументов: мы не используем никаких данных из основного потока в коде порождённого потока. Чтобы использовать данные из основного потока в порождённом потоке, замыкание порождённого потока должно захватывать значения, которые ему необходимы. Листинг 16-3 показывает попытку создать вектор в главном потоке и использовать его в порождённом потоке. Тем не менее, это не будет работать, как вы увидите через мгновение.

Файл: src/main.rs

use std::thread;

fn main() {
    let v = vec![1, 2, 3];

    let handle = thread::spawn(|| {
        println!("Here's a vector: {:?}", v);
    });

    handle.join().unwrap();
}

Листинг 16-3: Попытка использовать вектор, созданный основным потоком, в другом потоке