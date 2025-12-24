---
source_image: page_425.png
page_number: 425
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.67
tokens: 7497
characters: 1980
timestamp: 2025-12-24T10:57:01.141607
finish_reason: stop
---

8 |     let handle = thread::spawn(move || {
|         ------ value moved (into closure) here
...
26 |     println!("Result: {}", *counter.lock().unwrap());
|         ^^^^^^^ value used here after move
|
= note: move occurs because `counter` has type `std::sync::Mutex<i32>`,
which does not implement the `Copy` trait

error: aborting due to 2 previous errors

Ага! Первое сообщение об ошибке говорит, что переменная counter перемещается внутрь замыкания для потока, связанного с переменной handle. Это перемещение мешает захватить переменную counter, когда мы пытаемся вызвать для нее метод lock и сохранить результат в переменной num2 во втором потоке! Поэтому Rust говорит нам о том, что мы не можем переместить владение переменной counter в несколько потоков. Раньше это было трудно увидеть, потому что наши потоки были в цикле, а Rust не может указывать на разные потоки в разных итерациях цикла. Давайте исправим ошибку компилятора с помощью метода множественного владения.

Множественное владение с несколькими нитями исполнения

В главе 15 мы передавали значение нескольким владельцам, используя умный указатель Rc<T>, чтобы создать значение с числом посчитанных ссылок. Давайте сделаем то же самое здесь и посмотрим, что произойдет. В листинге 16.14 мы обернем Mutex<T> в умный указатель Rc<T> и клонируем Rc<T> перед перемещением владения в поток. Теперь, когда мы увидели ошибки, мы также вернемся к циклу for и оставим ключевое слово move с замыканием.

Листинг 16.14. Попытка использовать умный указатель Rc<T>, чтобы разрешить нескольким потокам владеть умным указателем Mutex<T>

src/main.rs
use std::rc::Rc;
use std::sync::Mutex;
use std::thread;

fn main() {
    let counter = Rc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Rc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();

            *num += 1;
        });
        handles.push(handle);
    }