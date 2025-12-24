---
source_image: page_461.png
page_number: 461
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 60.41
tokens: 11774
characters: 1978
timestamp: 2025-12-24T10:38:00.674132
finish_reason: stop
---

Листинг 16-5. Использование ключевого слова move, чтобы замыкание стало владельцем используемых им значений.

У нас может возникнуть соблазн попробовать то же самое, чтобы исправить код в листинге 16.4, где основной поток вызывал drop с помощью замыкания move. Однако это исправление не сработает, потому что то, что пытается сделать листинг 16.4, запрещено по другой причине. Если мы добавим move к замыканию, мы переместим v в окружение замыкания и больше не сможем вызывать для него drop в основном потоке. Вместо этого мы получим эту ошибку компилятора:

$ cargo run
Compiling threads v0.1.0 (file:///projects/threads)
error[E0382]: use of moved value: `v`
 --> src/main.rs:10:10
  |
4 |     let v = vec![1, 2, 3];
|         - move occurs because `v` has type `Vec<i32>`, which does not implement the `Copy` trait
5 |     let handle = thread::spawn(move || {
|                ------ value moved into closure here
7 |         println!("Here's a vector: {:?}", v);
|                        - variable moved due to use in closure
...
10 |     drop(v); // oh no!
|           ^ value used here after move

For more information about this error, try `rustc --explain E0382`.
error: could not compile `threads` due to previous error

Правила владения Rust снова нас спасли! Мы получили ошибку кода из листинга 16-3, потому что Rust был консервативен и заимствовал v только для потока, что означало, что основной поток теоретически может сделать недействительной ссылку на порождённый поток. Сообщив Rust о передаче владения v в порождаемый поток, мы гарантируем Rust, что основной поток больше не будет использовать v. Если мы изменим Листинг 16-4 таким же образом, то мы нарушаем правила владения при попытке использовать v в главном потоке. Ключевое слово move отменяет основное консервативное поведение Rust по заимствованию, что не позволяет нам нарушать правила владения.

Имея базовое понимание потоков и API потоков, давайте посмотрим, что мы можем делать с помощью потоков.