---
source_image: page_545.png
page_number: 545
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.48
tokens: 7509
characters: 1964
timestamp: 2025-12-24T11:00:06.863284
finish_reason: stop
---

src/lib.rs

pub struct ThreadPool;

impl ThreadPool {
    pub fn new(size: usize) -> ThreadPool {
        ThreadPool
    }
}

Мы выбрали тип usize в качестве типа параметра size, поскольку знаем, что отрицательное число потоков исполнения не имеет смысла. Мы также знаем, что будем использовать 4 как число элементов в коллекции потоков исполнения, для чего и предназначен тип usize, как описано в разделе «Целочисленные типы» (с. 67).

Давайте проверим код еще раз¹:

$ cargo check
    Compiling hello v0.1.0 (file:///projects/hello)
warning: unused variable: `size`
  --> src/lib.rs:4:16
   |
4 |     pub fn new(size: usize) -> ThreadPool {
   |           ^^^^
= note: #[warn(unused_variables)] on by default
= note: to avoid this warning, consider using `_size` instead

error[E0599]: no method named `execute` found for type `hello::ThreadPool` in the current scope
  --> src/bin/main.rs:18:14
   |
18 |         pool.execute(|| {
   |                ^^^^^^^

Теперь мы получаем предупреждение и ошибку. На мгновение проигнорируем предупреждение. Ошибка возникает, потому что у нас нет метода execute в структуре ThreadPool. Вспомните раздел «Создание похожего интерфейса для конечного числа потоков исполнения» (с. 543), там мы приняли решение, что пул потоков исполнения должен иметь интерфейс, подобный функции thread::spawn. В дополнение к этому мы реализуем функцию execute, которая принимает заданное замыкание и передает его для выполнения простаивающему потоку в пуле.

Мы определим метод execute для структуры ThreadPool, который будет принимать замыкание в качестве параметра. Вспомним раздел «Хранение замыканий с использованием обобщенных параметров и типажей Fn» (с. 319): мы можем принимать замыкания как параметры с тремя разными типажами — Fn, FnMut и FnOnce. Нужно решить, какой вид замыкания использовать здесь. Мы знаем, что в итоге

¹ ошибка[E0599]: не найден метод с именем `execute` для типа 'hello::ThreadPool` в текущей области видимости