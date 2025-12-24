---
source_image: page_543.png
page_number: 543
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.22
tokens: 7506
characters: 1939
timestamp: 2025-12-24T11:00:03.036893
finish_reason: stop
---

Создание похожего интерфейса для конечного числа потоков исполнения

Мы хотим, чтобы пул потоков исполнения работал похожим, привычным образом, когда переключение с потоков исполнения на пул не требует крупных изменений в коде, использующем API. В листинге 20.12 показан гипотетический интерфейс для структуры ThreadPool, которую мы хотим использовать вместо функции thread::spawn.

Листинг 20.12. Идеальный интерфейс структуры ThreadPool
src/main.rs

fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();
    let pool = ThreadPool::new(4);
    for stream in listener.incoming() {
        let stream = stream.unwrap();
        pool.execute(|| {
            handle_connection(stream);
        });
    }
}

Мы используем функцию ThreadPool::new для создания нового пула потоков исполнения с конфигурируемым числом потоков, в данном случае четырьмя ①. Затем, в цикле for, метод pool.execute имеет интерфейс, похожий на othread::spawn тем, что он берет замыкание, которое пул должен выполнять для каждого потока ②. Мы должны реализовать метод pool.execute так, чтобы он брал замыкание и передавал его потоку из пула для выполнения. Этот код пока не компилируется, но мы постараемся, чтобы компилятор направил нас в нужную сторону.

Построение структуры ThreadPool с использованием разработки на основе компилятора

Внесите изменения в листинг 20.12 для src/main.rs, а затем давайте использовать ошибки компилятора из cargo check, которые будут направлять разработку. Вот первая полученная ошибка¹:

$ cargo check
Compiling hello v0.1.0 (file:///projects/hello)
error[E0433]: failed to resolve. Use of undeclared type or module `ThreadPool`
 --> src\main.rs:10:16
  |
10 |     let pool = ThreadPool::new(4);
  |     ^^^^^^^^^^^^^^^^ Use of undeclared type or module `ThreadPool`
error: aborting due to previous error

¹ ошибка[E0433]: не получилось урегулировать. Использование необъявленного типа или модуля `ThreadPool`