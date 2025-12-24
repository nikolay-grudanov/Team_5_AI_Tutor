---
source_image: page_555.png
page_number: 555
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.00
tokens: 7308
characters: 1400
timestamp: 2025-12-24T11:00:14.665338
finish_reason: stop
---

Mutex обеспечит, чтобы только один работник получал задание от приемника за один раз. В листинге 20.18 показаны изменения, которые необходимо внести.

Листинг 20.18. Совместное использование принимающего конца канала работниками с использованием типов Arc и Mutex

src/lib.rs
```rust
use std::sync::Arc;
use std::sync::Mutex;

// --пропуск--

impl ThreadPool {
    // --пропуск--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let (sender, receiver) = mpsc::channel();

        let receiver = Arc::new(Mutex::new(receiver)); ①

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
            workers.push(Worker::new(id, Arc::clone(&receiver)②));
        }

        ThreadPool {
            workers,
            sender,
        }
    }
    // --пропуск--
}

impl Worker {
    fn new(id: usize, receiver: Arc<Mutex<mpsc::Receiver<Job>>>) -> Worker {
        // --пропуск--
    }
}
```

В функции ThreadPool::new мы помещаем принимающий конец канала в Arc и Mutex ①. Для каждого нового работника мы клонируем Arc, увеличивая число ссылок, чтобы работники могли совместно владеть принимающим концом ②.

С этими изменениями код компилируется! Мы почти у цели!

Реализация метода execute

Давайте, наконец, реализуем метод execute в типе ThreadPool. Мы также изменим тип Job со структуры на псевдоним типажного объекта, содержащего тип замыка-