---
source_image: page_457.png
page_number: 457
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.28
tokens: 11557
characters: 1387
timestamp: 2025-12-24T10:37:28.507226
finish_reason: stop
---

hi number 1 from the main thread!
hi number 2 from the main thread!
hi number 1 from the spawned thread!
hi number 3 from the main thread!
hi number 2 from the spawned thread!
hi number 4 from the main thread!
hi number 3 from the spawned thread!
hi number 4 from the spawned thread!
hi number 5 from the spawned thread!
hi number 6 from the spawned thread!
hi number 7 from the spawned thread!
hi number 8 from the spawned thread!
hi number 9 from the spawned thread!

Два потока продолжают чередоваться, но основной поток находится в ожидании из-за вызова `handle.join()` и не завершается до тех пор, пока не завершится запущенный поток.

Но давайте посмотрим, что произойдёт, если мы вместо этого переместим `handle.join()` перед циклом `for` в `main`, например так:

Файл: src/main.rs

```rust
use std::thread;
use std::time::Duration;

fn main() {
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {} from the spawned thread!", i);
            thread::sleep(Duration::from_millis(1));
        }
    });

    handle.join().unwrap();

    for i in 1..5 {
        println!("hi number {} from the main thread!", i);
        thread::sleep(Duration::from_millis(1));
    }
}
```

Основной поток будет ждать завершения порождённого потока, а затем запустит свой цикл `for`, поэтому выходные данные больше не будут чередоваться, как показано ниже: