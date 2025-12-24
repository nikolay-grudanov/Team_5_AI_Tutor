---
source_image: page_553.png
page_number: 553
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.41
tokens: 7285
characters: 1307
timestamp: 2025-12-24T11:00:12.002203
finish_reason: stop
---

// --пропуск--
pub fn new(size: usize) -> ThreadPool {
    assert!(size > 0);

    let (sender, receiver) = mpsc::channel();

    let mut workers = Vec::with_capacity(size);

    for id in 0..size {
        workers.push(Worker::new(id));
    }

    ThreadPool {
        workers,
        sender,
    }
}
// --пропуск--

В функции ThreadPool::new мы создаем новый канал ①, причем пул занимает отправляющий конец ②. Это код будет успешно компилироваться, правда, по-прежнему с предупреждениями.

Давайте попробуем передавать принимающий конец канала внутрь каждого работника тогда, когда пул потоков исполнения создает канал. Мы знаем, что хотим использовать принимающий конец в потоке, который работники порождают, поэтому мы будем ссылаться на параметр receiver в замыкании. Код в листинге 20.17 пока не компилируется полностью.

Листинг 20.17. Передача принимающего конца канала работникам
src/lib.rs

impl ThreadPool {
    // --пропуск--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let (sender, receiver) = mpsc::channel();

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
            workers.push(Worker::new(id, receiver)); ①
        }

        ThreadPool {
            workers,
            sender,
        }
    }
    // --пропуск--
}