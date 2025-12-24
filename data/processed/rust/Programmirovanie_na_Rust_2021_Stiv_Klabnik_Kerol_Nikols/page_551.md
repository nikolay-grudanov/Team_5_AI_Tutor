---
source_image: page_551.png
page_number: 551
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.26
tokens: 7319
characters: 1467
timestamp: 2025-12-24T11:00:11.639261
finish_reason: stop
---

```rust
impl ThreadPool {
    // --пропуск--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
            workers.push(Worker::new(id));
        }

        ThreadPool {
            workers
        }
    }
    // --пропуск--
}

struct Worker {
    id: usize,
    thread: thread::JoinHandle<()>,
}

impl Worker {
    fn new(id: usize) -> Worker {
        let thread = thread::spawn(|| {});

        Worker {
            id,
            thread,
        }
    }
}
```

Мы поменяли имя поля в типе ThreadPool с threads на workers, потому что теперь оно содержит экземпляры структуры Worker вместо экземпляров типа JoinHandle<()>. Мы используем счетчик в цикле for в качестве аргумента для функции Worker::new и храним каждый новый Worker в векторе workers.

Внешнему коду (как наш сервер в src/bin/main.rs) не нужно знать детали реализации, касающиеся структуры Worker в ThreadPool, поэтому мы делаем структуру Worker и ее функцию new приватными. Функция Worker::new использует id, который мы ей даем, и сохраняет экземпляр типа JoinHandle<()>, созданный путем порождения нового потока исполнения с пустым замыканием.

Этот код будет компилироваться и хранить число экземпляров структуры Worker, указанное в качестве аргумента для функции ThreadPool::new. Но мы пока что не обрабатываем замыкание, которое получаем в методе execute. Давайте посмотрим, как это сделать.