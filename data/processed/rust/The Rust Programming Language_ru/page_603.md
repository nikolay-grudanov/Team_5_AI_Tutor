---
source_image: page_603.png
page_number: 603
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.28
tokens: 11561
characters: 1328
timestamp: 2025-12-24T10:43:40.168741
finish_reason: stop
---

Эта ошибка указывает, что далее нам нужно создать ассоциированную функцию с именем new для ThreadPool. Мы также знаем, что new должен иметь один параметр, который может принимать 4 в качестве аргумента и должен возвращать экземпляр ThreadPool. Давайте реализуем простейшую функцию new, которая будет иметь эти характеристики:

Файл: src/lib.rs

```rust
pub struct ThreadPool;

impl ThreadPool {
    pub fn new(size: usize) -> ThreadPool {
        ThreadPool
    }
}
```

Мы выбираем usize в качестве типа параметра size, потому что мы знаем, что отрицательное число потоков не имеет никакого смысла. Мы также знаем, что мы будем использовать число 4 в качестве количества элементов в коллекции потоков, для чего предназначен тип usize, как обсуждалось в разделе "Целочисленные типы" главы 3.

Давайте проверим код ещё раз:

```sh
$ cargo check
   Checking hello v0.1.0 (file:///projects/hello)
error[E0599]: no method named `execute` found for struct `ThreadPool` in the current scope
  --> src/main.rs:17:14
   |
17 |     pool.execute(|| {
   |         ^^^^^^^^ method not found in `ThreadPool`
```

Теперь мы получаем предупреждение и ошибку. Игнорируем предупреждение не надолго, ошибка происходит потому что у нас нет метода execute в структуре ThreadPool. Вспомните раздел "Создание подобного интерфейса для конечного числа