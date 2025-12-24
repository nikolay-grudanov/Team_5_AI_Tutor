---
source_image: page_611.png
page_number: 611
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.31
tokens: 11481
characters: 1069
timestamp: 2025-12-24T10:44:03.503799
finish_reason: stop
---

use std::{sync::mpsc, thread};

pub struct ThreadPool {
    workers: Vec<Worker>,
    sender: mpsc::Sender<Job>,
}

struct Job;

impl ThreadPool {
    // --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let (sender, receiver) = mpsc::channel();

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
            workers.push(Worker::new(id));
        }

        ThreadPool { workers, sender }
    }
    // --snip--
}

Листинг 20-16: Модификация ThreadPool для хранения отправляющей части канала, который отправляет экземпляры Job

В ThreadPool::new мы создаём наш новый канал и пул содержащий отправляющую сторону. Код успешно скомпилируется все ещё с предупреждениями.

Давайте попробуем передавать принимающую сторону канала каждому "работнику" (структуре woker), когда пул потоков создаёт канал. Мы знаем, что хотим использовать получающую часть канала в потоке порождаемым "работником", поэтому мы будем ссылаться на параметр receiver в замыкании. Код 20-17 пока не компилируется.

Файл: src/lib.rs