---
source_image: page_607.png
page_number: 607
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.80
tokens: 11666
characters: 1760
timestamp: 2025-12-24T10:43:56.004841
finish_reason: stop
---

произойдёт. В нашем случае замыкания, которые мы передаём пулу потоков, будут обрабатывать соединение и ничего не будут возвращать, поэтому T будет единичным (unit) типом ().

Листинг 20-14 скомпилируется, но пока не создаёт потоков. Мы изменили объявление ThreadPool, чтобы оно содержало вектор экземпляров thread::JoinHandle<()>, инициализировали вектор с размером size, установили цикл for, который будет запускать некоторый код для создания потоков и вернули экземпляр ThreadPool содержащий потоки.

Файл: src/lib.rs

use std::thread;

pub struct ThreadPool {
    threads: Vec<thread::JoinHandle<()>>,
}

impl ThreadPool {
    // --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let mut threads = Vec::with_capacity(size);

        for _ in 0..size {
            // create some threads and store them in the vector
        }

        ThreadPool { threads }
    }
    // --snip--
}

Листинг 20-14: Создание вектора в ThreadPool для хранения потоков

Мы добавили std::thread в область видимости библиотечного крейта, потому что мы используем thread::JoinHandle в качестве типа элементов вектора в ThreadPool.

После получения корректного значения size, наш ThreadPool создаёт новый вектор, который может содержать size элементов. В этой книге мы ещё не использовали функцию with_capacity, которая выполняет ту же задачу что и Vec::new, но с важным отличием: она заранее выделяет указанную память в векторе. Поскольку мы знаем, что нам нужно хранить size элементов в векторе, выполнение этого выделения немного более эффективно, чем использование Vec::new, который изменяет размеры при вставке элементов.

Когда вы снова запустите cargo check, вы получите ещё несколько предупреждений, но все должно завершится успехом.