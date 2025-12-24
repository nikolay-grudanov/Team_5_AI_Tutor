---
source_image: page_624.png
page_number: 624
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 62.95
tokens: 11769
characters: 2028
timestamp: 2025-12-24T10:44:57.527543
finish_reason: stop
---

Чтобы увидеть этот код в действии, давайте изменим main, чтобы принимать только два запроса, прежде чем корректно завершить работу сервера как показано в листинге 20-25.

Файл: src/bin/main.rs

```rust
{{#rustdoc_include ../listings/ch20-web-server/listing-20-25/src/bin/main.rs:here}}
```

Код 20-25. Выключение сервера после обслуживания двух запросов с помощью выхода из цикла

Вы бы не хотели, чтобы реальный веб-сервер отключался после обслуживания только двух запросов. Этот код всего лишь демонстрирует, что корректное завершение работы и освобождение ресурсов находятся в рабочем состоянии.

Метод take определён в типаже Iterator и ограничивает итерацию максимум первыми двумя элементами. ThreadPool выйдет из области видимости в конце main и будет запущена его реализация drop.

Запустите сервер с cargo run и сделайте три запроса. Третий запрос должен выдать ошибку и в терминале вы должны увидеть вывод, подобный следующему:

$ cargo run
Compiling hello v0.1.0 (file:///projects/hello)
Finished dev [unoptimized + debuginfo] target(s) in 1.0s
    Running `target/debug/main`
Worker 0 got a job; executing.
Worker 3 got a job; executing.
Shutting down.
Sending terminate message to all workers.
Shutting down all workers.
Shutting down worker 0
Worker 1 was told to terminate.
Worker 2 was told to terminate.
Worker 0 was told to terminate.
Worker 3 was told to terminate.
Shutting down worker 1
Shutting down worker 2
Shutting down worker 3

Вы возможно увидите другой порядок рабочих потоков и напечатанных сообщений. Мы можем увидеть, как этот код работает по сообщениям: "работники" номер 0 и 3 получили первые два запроса, затем на третьем запросе сервер прекратил принимать соединения. Когда ThreadPool выходит из области видимости в конце main, то срабатывает его реализация типажа Drop и пул сообщает всем рабочим потокам прекратить выполнение. Каждый рабочий поток распечатывает сообщение, когда видит сообщение о завершении, а затем пул потоков вызывает join, чтобы завершить работу каждого рабочего потока.