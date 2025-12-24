---
source_image: page_563.png
page_number: 563
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.40
tokens: 7437
characters: 1867
timestamp: 2025-12-24T11:00:38.770723
finish_reason: stop
---

Option<thread::JoinHandle<()>>, то можно вызвать метод take для Option, чтобы переместить значение из варианта Some и не трогать вариант None. Другими словами, работающий Worker будет иметь вариант Some в поле thread, а когда мы захотим очистить Worker, мы поменяем Some на None, чтобы у Worker не было потока, подлежащего выполнению.

Итак, мы знаем, что хотим обновить определение Worker следующим образом:

src/lib.rs
struct Worker {
    id: usize,
    thread: Option<thread::JoinHandle<()>>,
}

Теперь давайте доверимся компилятору — он найдет другие места, которые нужно изменить. Проверив этот код, мы получим две ошибки1:

error[E0599]: no method named `join` found for type `std::option::Option<std::thread::JoinHandle<()>>` in the current scope
  --> src/lib.rs:65:27
   |
65 |         worker.thread.join().unwrap();
   |                        ^^^^

error[E0308]: mismatched types
  --> src/lib.rs:89:13
   |
89 |             thread,
   |             ^^^^^^
   |             |
   |             expected enum `std::option::Option`, found struct `std::thread::JoinHandle`
   |             help: try using a variant of the expected type:
   |             `Some(thread)`
   |             = note: expected type `std::option::Option<std::thread::JoinHandle<()>>`
   |                         found type `std::thread::JoinHandle<_>`

Давайте обратимся ко второй ошибке, которая указывает на код в конце функции Worker::new. Нам нужно завернуть значение thread в Some при создании нового экземпляра типа Worker. Внесите следующие изменения, чтобы устранить эту ошибку:

src/lib.rs
impl Worker {
    fn new(id: usize, receiver: Arc<Mutex<mpsc::Receiver<Job>>>) -> Worker {

_____________________
1 ошибка[E0599]: не найден метод с именем `join` для типа `std::option::Option<std::thread::JoinHandle<()>>` в текущей области видимости
ошибка[E0308]: несовпадающие типы