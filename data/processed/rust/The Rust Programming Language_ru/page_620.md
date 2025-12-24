---
source_image: page_620.png
page_number: 620
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.89
tokens: 11366
characters: 674
timestamp: 2025-12-24T10:44:04.132445
finish_reason: stop
---

Давайте обратимся ко второй ошибке, которая указывает на код в конце `Worker::new`; нам нужно обернуть значение `thread` в вариант `Some` при создании нового `Worker`. Внесите следующие изменения, чтобы исправить эту ошибку:

Файл: src/lib.rs

```rust
impl Worker {
    fn new(id: usize, receiver: Arc<Mutex<mpsc::Receiver<Job>>>) -> Worker {
        // --snip--
        Worker {
            id,
            thread: Some(thread),
        }
    }
}
```

Первая ошибка находится в нашей реализации `Drop`. Ранее мы упоминали, что намеревались вызвать `take` для параметра `Option`, чтобы забрать `thread` из процесса `worker`. Следующие изменения делают это:

Файл: src/lib.rs