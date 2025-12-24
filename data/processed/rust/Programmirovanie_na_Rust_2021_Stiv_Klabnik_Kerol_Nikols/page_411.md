---
source_image: page_411.png
page_number: 411
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.77
tokens: 7401
characters: 1720
timestamp: 2025-12-24T10:56:34.458697
finish_reason: stop
---

Замыкание использует переменную v, поэтому оно захватит v и сделает ее частью среды замыкания. Поскольку функция thread::spawn выполняет это замыкание в новом потоке исполнения, мы должны иметь возможность обращаться к переменной v внутри этого нового потока. Но когда мы компилируем этот пример, возникает следующая ошибка¹:

error[E0373]: closure may outlive the current function, but it borrows `v`,
which is owned by the current function
--> src/main.rs:6:32
6 |     let handle = thread::spawn(|| {
    |                        ^^^ may outlive borrowed value `v`
7 |         println!("Вот вектор: {:?}", v);
    |                        - `v` is borrowed here
help: to force the closure to take ownership of `v` (and any other referenced variables), use the `move` keyword
6 |     let handle = thread::spawn(move || {

Rust логически выводит то, как следует захватывать переменную v, а поскольку макрокоманде println! требуется только ссылка на v, замыкание пытается заимствовать v. Однако существует одна проблема: нельзя сказать, как долго будет работать порожденный поток, поэтому неизвестно, будет ли ссылка на v всегда действительно.

Листинг 16.4 содержит сценарий, в котором ссылка на переменную v, скорее всего, не будет действительно.

Листинг 16.4. Поток с замыканием, пытающийся захватить ссылку на переменную v из главного потока, который отбрасывает переменную v

src/main.rs
use std::thread;

fn main() {
    let v = vec![1, 2, 3];

    let handle = thread::spawn(|| {
        println!("Вот вектор: {:?}", v);
    });

    drop(v); // о нет!

    handle.join().unwrap();
}

¹ ошибка[E0373]: замыкание может пережить текущую функцию, но оно заимствует переменную `v`, которая принадлежит текущей функции