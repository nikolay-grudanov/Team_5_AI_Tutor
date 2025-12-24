---
source_image: page_424.png
page_number: 424
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.26
tokens: 7388
characters: 1631
timestamp: 2025-12-24T10:56:53.080198
finish_reason: stop
---

9 |     let handle = thread::spawn(move || {
|           ------ value moved (into closure) here
...
21 |     println!("Result: {}", *counter.lock().unwrap());
|           ^^^^^^^ value used here after move
|
= note: move occurs because `counter` has type `std::sync::Mutex<i32>`,
which does not implement the `Copy` trait

error: aborting due to 2 previous errors

В сообщении об ошибке говорится, что значение переменной counter перемещается в замыкание, а затем захватывается, когда мы вызываем lock. Мы этого хотели, но это запрещено!

Давайте выясним это, упростив программу. Вместо десяти потоков исполнения в цикле for давайте сделаем только два потока без цикла и посмотрим, что получится. Замените первый цикл for в листинге 16.13 следующим кодом.

let handle = thread::spawn(move || {
    let mut num = counter.lock().unwrap();

    *num += 1;
});
handles.push(handle);

let handle2 = thread::spawn(move || {
    let mut num2 = counter.lock().unwrap();

    *num2 += 1;
});
handles.push(handle2);

Мы делаем два потока и меняем имена переменных, используемых со вторым потоком, на handle2 и num2. Когда мы выполняем код в этот раз, компиляция дает следующее:

error[E0382]: capture of moved value: `counter`
 --> src/main.rs:16:24
  |
8 |     let handle = thread::spawn(move || {
|           ------ value moved (into closure) here
...
16 |     let mut num2 = counter.lock().unwrap();
|           ^^^^^^^ value captured here after move
|
= note: move occurs because `counter` has type `std::sync::Mutex<i32>`,
which does not implement the `Copy` trait

error[E0382]: use of moved value: `counter`
 --> src/main.rs:26:29
  |