---
source_image: page_613.png
page_number: 613
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 58.66
tokens: 11631
characters: 1700
timestamp: 2025-12-24T10:44:24.465329
finish_reason: stop
---

является моделью несколько производителей (multiple producer), один потребитель (single consumer). Это означает, что мы не можем просто клонировать принимающую часть канала для исправления этого кода. Даже если бы мы это могли, это не техника которую мы хотели бы использовать; вместо этого мы хотим распределить задачи среди потоков, разделяя один receiver среди всех "работников".

Кроме того, удаление задачи из очереди канала включает изменение receiver, поэтому потокам необходим безопасный способ делиться и изменять receiver, в противном случае мы можем получить условия гонки (как описано в главе 16).

Вспомните умные указатели, которые обсуждались в главе 16: чтобы делиться владением между несколькими потоками и позволить потокам изменять значение, нам нужно использовать тип Arc<Mutex<T>>. Тип Arc позволит нескольким "работникам" владеть получателем (receiver), а Mutex гарантирует что только один "работник" получит задание (job) от получателя в один момент времени. Листинг 20-18 показывает изменения, которые мы должны сделать.

Файл: src/lib.rs

use std::{
    sync::{mpsc, Arc, Mutex},
    thread,
};
// --snip--

impl ThreadPool {
    // --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let (sender, receiver) = mpsc::channel();

        let receiver = Arc::new(Mutex::new(receiver));

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
            workers.push(Worker::new(id, Arc::clone(&receiver)));
        }

        ThreadPool { workers, sender }
    }
    // --snip--
}

// --snip--

impl Worker {
    fn new(id: usize, receiver: Arc<Mutex<mpsc::Receiver<Job>>> ) -> Worker {
        // --snip--
    }
}